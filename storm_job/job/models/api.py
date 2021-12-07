# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from invenio_db import db
from invenio_records.systemfields import SystemFieldsMixin, ModelField

from .model import ExecutionJobModel


class ExecutionJobBase:
    """Base class for Execution Job APIs."""

    model_cls = ExecutionJobModel
    """SQLAlchemy model class defining which table stores the records."""

    def __init__(self, model=None):
        self.model = model

    @property
    def id(self):
        """Get model identifier."""
        return self.model.id if self.model else None

    @property
    def created(self):
        """Get creation timestamp."""
        return self.model.created if self.model else None

    @property
    def updated(self):
        """Get last updated timestamp."""
        return self.model.updated if self.model else None

    @classmethod
    def create(cls, **kwargs):
        """Create a new execution job instance."""

        with db.session.begin_nested():
            # defining the model and the object
            execution_job = cls(cls.model_cls(**kwargs))

            # saving!
            db.session.add(execution_job.model)
        return execution_job

    @classmethod
    def get_record(cls, id_):
        """Get record by id.

        Args:
            id_ (str): Record id.

        Returns:
            ExecutionJobBase: The `ExecutionJobBase` instance.
        """
        with db.session.no_autoflush:
            query = cls.model_cls.query.filter_by(id=id_)

            obj = query.one()
            return cls(model=obj)


class ExecutionJob(ExecutionJobBase, SystemFieldsMixin):
    """Execution model API"""

    #
    # Creator
    #
    user = ModelField()
    user_id = ModelField()

    #
    # Associated project
    #
    project = ModelField()
    project_id = ModelField()

    #
    # Used pipeline
    #
    pipeline = ModelField()
    pipeline_id = ModelField()

    # General status
    status = ModelField()


__all__ = ("ExecutionJobBase", "ExecutionJob")
