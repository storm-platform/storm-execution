# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-runner is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from flask import g

from flask_resources import (
    Resource,
    resource_requestctx,
    response_handler,
    route,
)

from storm_commons.resources.parsers import (
    request_data,
    request_read_args,
    request_view_args,
    request_search_args,
)

from invenio_records_resources.resources.errors import ErrorHandlersMixin


class ExecutionTaskManagementResource(ErrorHandlersMixin, Resource):
    """Execution Task management resource."""

    def __init__(self, config, service):
        super(ExecutionTaskManagementResource, self).__init__(config)
        self.service = service

    def create_url_rules(self):
        """Create the URL rules for the record resource."""
        routes = self.config.routes
        return [
            # Execution task operations
            route("GET", routes["read-item"], self.read),
            route("GET", routes["list-item"], self.search),
            route("POST", routes["create-item"], self.create),
            route("PUT", routes["update-item"], self.update),
            route("DELETE", routes["delete-item"], self.delete),
            # Execution task actions
            route("POST", routes["start-task-action"], self.start_execution_task),
            # Services operations
            route("GET", routes["list-service"], self.list_plugin_services),
        ]

    @request_data
    @response_handler()
    def create(self):
        """Create an item."""
        item = self.service.create(
            g.identity,
            resource_requestctx.data or {},
        )
        return item.to_dict(), 201

    @request_read_args
    @request_view_args
    @response_handler()
    def read(self):
        """Read an item."""
        item = self.service.read(
            g.identity,
            resource_requestctx.view_args["job_id"],
        )
        return item.to_dict(), 200

    @request_data
    @request_view_args
    @response_handler()
    def update(self):
        """Update an item."""
        item = self.service.update(
            g.identity,
            resource_requestctx.view_args["job_id"],
            resource_requestctx.data or {},
        )
        return item.to_dict(), 200

    @request_view_args
    def delete(self):
        """Delete an item."""
        self.service.delete(g.identity, resource_requestctx.view_args["job_id"])
        return "", 204

    @request_search_args
    @response_handler(many=True)
    def search(self):
        """Perform a search over the items."""
        items = self.service.search(g.identity, resource_requestctx.args)
        return items.to_dict(), 200

    @response_handler(many=True)
    def list_plugin_services(self):
        """List the available executors."""
        return self.service.list_plugin_services(), 200

    @request_data
    @request_view_args
    @response_handler()
    def start_execution_task(self):
        """Execute a task."""
        item = self.service.start_execution_task(
            g.identity,
            resource_requestctx.view_args["job_id"],
            resource_requestctx.data or {},
        )

        return item.to_dict(), 202


__all__ = "ExecutionTaskManagementResource"
