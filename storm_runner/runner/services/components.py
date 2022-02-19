# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-runner is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from invenio_records_resources.services.records.components import ServiceComponent

from storm_runner.runner.models.model import ExecutionTaskStatus

from storm_project import current_project
from storm_workflow.proxies import current_workflow_service


class WorkflowComponent(ServiceComponent):
    """Service component which set the workflow context in the record."""

    def create(self, identity, data=None, record=None, **kwargs):
        """Create handler."""
        record.workflow_id = current_workflow_service.read(
            data.get("workflow_id"), identity
        )._obj.id


class ProjectComponent(ServiceComponent):
    """Service component which set the project context in the record."""

    def create(self, identity, data=None, record=None, **kwargs):
        """Create handler."""
        record.project_id = current_project._obj.model.id


class ExecutionTaskComponent(ServiceComponent):
    """Service component which set the execution task status in the record."""

    def start_execution_task(self, identity, record=None, **kwargs):
        """Start Execution Task handler."""
        record.status = ExecutionTaskStatus.QUEUED

    def update(self, identity, data=None, record=None, **kwargs):
        """Update handler."""

        # defining the update strategies
        strategies = {
            "workflow_id": lambda record, data: current_workflow_service.read(
                data.get("workflow_id"), identity
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
    "ExecutionTaskComponent",
    "WorkflowComponent",
    "ProjectComponent",
)
