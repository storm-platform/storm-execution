# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-runner is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

import marshmallow as ma

from storm_commons.resources.config import BaseResourceConfig
from storm_runner.runner.resources.args import ExecutionTaskSearchRequestArgsSchema


class ExecutionTaskManagementResourceConfig(BaseResourceConfig):
    """Execution task management resource config."""

    # Blueprint configuration.
    blueprint_name = "storm_runner_execution_tasks_management"

    # Request/Response configuration.
    request_view_args = {"execution_id": ma.fields.Str()}
    request_search_args = ExecutionTaskSearchRequestArgsSchema

    # Routes configuration.
    url_prefix = "/projects/<project_id>/executions"
    routes = {
        # Services operations
        "list-service": "/services",
        # Execution Task operations
        "list-item": "",
        "create-item": "",
        "read-item": "/<execution_id>",
        "delete-item": "/<execution_id>",
        "update-item": "/<execution_id>",
        # Execution Task actions
        "start-task-action": "/<execution_id>/actions/start",
    }
