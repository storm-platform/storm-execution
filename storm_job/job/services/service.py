# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from pydash import py_

from invenio_db import db
from invenio_records_resources.services.base import Service
from invenio_records_resources.services import ServiceSchemaWrapper

from storm_job.job.schema import JobExecutorSchema


class JobManagementService(Service):
    def __iter__(self, config):
        super(JobManagementService, self).__init__(config)

    @property
    def record_cls(self):
        """Factory for creating a record class."""
        return self.config.record_cls

    @property
    def schema(self):
        """Returns the data schema instance."""
        return ServiceSchemaWrapper(self, schema=self.config.schema)

    @property
    def plugins(self):
        """Return the available execution plugins."""
        return self.config.plugins

    def create(self, identity, data):
        """Create a execution job.

        Args:
            identity (flask_principal.Identity): Identity of user creating the record.

            data (dict): Input data according to the data schema.
        Returns:
            storm_job.job.models.api.ExecutionJobBase: Execution Job object.
        """
        return self._create(self.record_cls, identity, data)

    def _create(self, record_cls, identity, data):
        """Create a execution job.

        Args:
            record_cls (storm_job.job.models.api.ExecutionJobBase): Model Class to represent the execution job.

            identity (flask_principal.Identity): Identity of user creating the record.

            data (dict): Input data according to the data schema.

        Returns:
            storm_job.job.models.api.ExecutionJobBase: Execution Job object.
        """
        self.require_permission(identity, "create")

        # Validate input data
        data, errors = self.schema.load(
            data, context={"identity": identity}, raise_errors=True
        )

        # It's the components who saves the actual data in the record.
        record = record_cls.create()

        # Run components
        for component in self.components:
            if hasattr(component, "create"):
                component.create(identity, record=record, data=data)

        # Saving the data
        db.session.commit()

        return record

    def read(self, identity, id_):
        """Retrieve a record."""
        # Resolve and require permission
        record = self.record_cls.get_record(id=id_)
        self.require_permission(identity, "read", record=record)

        # Run components
        for component in self.components:
            if hasattr(component, "read"):
                component.read(identity, record=record)

        return record

    def list_available_executors(self):
        """Return the metadata of the available executors."""
        available_executors = []
        if self.plugins:
            available_executors = JobExecutorSchema(many=True).dump(
                py_.chain(self.plugins).map(lambda x: py_.omit(x, "service")).value()
            )

        return available_executors

    def execute_job(self, identity, id_, data):
        """Start a job execution."""
        record = self.read(identity, id_)
        self.require_permission(identity, "execute", record=record)

        # Selecting an executor
        executor_id = py_.get(data, "executor_id", None)
        selected_executor = py_.filter_(self.plugins, lambda x: x["id"] == executor_id)

        if selected_executor:
            task = py_.get(selected_executor, "0.service")(
                py_.get(record.pipeline.data, "id"), **{**data, "type": "serial"}
            )

        return record


__all__ = "JobManagementService"
