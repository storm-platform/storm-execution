# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.


from flask import g
from pydash import py_

from flask_resources import (
    Resource,
    resource_requestctx,
    response_handler,
    route,
)

from .parsers import request_data, request_read_args, request_view_args


class ExecutionJobResource(Resource):
    """Execution Job resource."""

    def __init__(self, config, service):
        """Constructor."""
        super(ExecutionJobResource, self).__init__(config)
        self.service = service

    def create_url_rules(self):
        """Create the URL rules for the record resource."""
        routes = self.config.routes
        return [
            route("GET", routes["read-item"], self.read),
            route("POST", routes["create-item"], self.create),
            # route("GET", routes["list"], self.search),
            # route("DELETE", routes["item"], self.delete),
        ]

    def _dump(self, records):
        """Dump records to JSON."""
        values = (
            py_.chain([records])
            .flatten()
            .map(
                lambda record: self.service.schema.dump(
                    record, context={"identity": g.identity}
                )
            )
            .value()
        )

        return py_.head(values) if type(records) != list else values

    @request_data
    @response_handler()
    def create(self):
        """Create an item."""
        item = self.service.create(
            g.identity,
            resource_requestctx.data or {},
        )

        return self._dump(item), 201

    @request_read_args
    @request_view_args
    @response_handler()
    def read(self):
        """Read an item."""
        item = self.service.read(
            g.identity,
            resource_requestctx.view_args["job_id"],
        )
        return self._dump(item), 200

    # @request_search_args
    # @response_handler(many=True)
    # def search(self):
    #     """Perform a search over the items."""
    #     identity = g.identity
    #     hits = self.service.search(
    #         identity=identity,
    #         params=resource_requestctx.args,
    #         es_preference=es_preference(),
    #     )
    #     return hits.to_dict(), 200
    #

    # @request_headers
    # @request_view_args
    # def delete(self):
    #     """Delete an item."""
    #     self.service.delete(
    #         resource_requestctx.view_args["pid_value"],
    #         g.identity,
    #         revision_id=resource_requestctx.headers.get("if_match"),
    #     )
    #     return "", 204
