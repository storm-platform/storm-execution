# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-execution is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Storm Execution module for schedule and manage execution tasks in the Storm Platform."""

import storm_execution.config as config
from storm_commons.plugins.packages import PluginManager, plugin_factory

from storm_execution.execution.services.service import ExecutionTaskManagementService
from storm_execution.execution.resources.resource import ExecutionTaskManagementResource
from storm_execution.execution.services.config import ExecutionTaskManagementServiceConfig
from storm_execution.execution.resources.config import ExecutionTaskManagementResourceConfig


class StormExecution(object):
    """storm-execution extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)

        self.init_plugins(app)
        self.init_services(app)
        self.init_resources(app)

        app.extensions["storm-execution"] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith("STORM_EXECUTION_"):
                app.config.setdefault(k, getattr(config, k))

    def init_plugins(self, app):
        """Initialize the avaliable service plugins for the deposit operations."""
        available_plugin_services = plugin_factory(app, "storm_execution.plugins")

        self.plugin_manager = PluginManager(available_plugin_services)

    def init_services(self, app):
        """Initialize the execution runner services."""
        self.execution_task_management_service = ExecutionTaskManagementService(
            self.plugin_manager, ExecutionTaskManagementServiceConfig
        )

    def init_resources(self, app):
        """Initialize the execution runner resources."""
        self.execution_task_management_resource = ExecutionTaskManagementResource(
            ExecutionTaskManagementResourceConfig,
            self.execution_task_management_service,
        )


__all__ = "StormExecution"
