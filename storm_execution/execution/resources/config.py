# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-execution is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

import marshmallow as ma

from storm_commons.resources.config import BaseResourceConfig
from storm_execution.execution.resources.args import ExecutionTaskSearchRequestArgsSchema


class ExecutionTaskManagementResourceConfig(BaseResourceConfig):
    """Execution task management resource config."""

    # Blueprint configuration.
    blueprint_name = "storm_execution_execution_tasks_management"

    # Request/Response configuration.
    request_view_args = {"job_id": ma.fields.Str()}
    request_search_args = ExecutionTaskSearchRequestArgsSchema

    # Routes configuration.
    url_prefix = "/projects/<project_id>/executions"
    routes = {
        # Services operations
        "list-service": "/services",
        # Execution Task operations
        "list-item": "",
        "create-item": "",
        "read-item": "/<job_id>",
        "delete-item": "/<job_id>",
        "update-item": "/<job_id>",
        # Execution Task actions
        "start-task-action": "/<job_id>/actions/start",
    }
