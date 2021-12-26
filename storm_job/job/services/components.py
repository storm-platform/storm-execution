# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from invenio_records_resources.services.records.components import ServiceComponent

from storm_job.job.models.model import ExecutionJobStatus

from storm_project import current_project
from storm_pipeline.proxies import current_pipeline_service


class PipelineComponent(ServiceComponent):
    """Service component which set the pipeline context in the record."""

    def create(self, identity, data=None, record=None, **kwargs):
        """Create handler."""
        record.pipeline_id = current_pipeline_service.read(
            data.get("pipeline_id"), identity
        )._obj.id


class ProjectComponent(ServiceComponent):
    """Service component which set the project context in the record."""

    def create(self, identity, data=None, record=None, **kwargs):
        """Create handler."""
        record.project_id = current_project._obj.model.id


class ExecutionJobComponent(ServiceComponent):
    """Service component which set the execution job status in the record."""

    def start_execution_job(self, identity, record=None, **kwargs):
        """Start Execution Job handler."""
        record.status = ExecutionJobStatus.QUEUED

    def update(self, identity, data=None, record=None, **kwargs):
        """Update handler."""

        # defining the update strategies
        strategies = {
            "pipeline_id": lambda record, data: current_pipeline_service.read(
                data.get("pipeline_id"), identity
            )._obj.id,
            "service": lambda record, data: data.get("service"),
        }

        for key in data.keys():
            if key in strategies:  # to avoid errors
                # using the strategy
                value = strategies.get(key)(record, data)

                # setting the returned value
                setattr(record, key, value)


__all__ = (
    "ExecutionJobComponent",
    "PipelineComponent",
    "ProjectComponent",
)
