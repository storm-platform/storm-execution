# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

import marshmallow as ma

from flask_resources import (
    JSONDeserializer,
    JSONSerializer,
    RequestBodyParser,
    ResourceConfig,
    ResponseHandler,
)


class JobResourceConfigBase(ResourceConfig):
    """Base configuration class for job resources."""

    # Request parsing
    request_read_args = {}
    request_view_args = {"job_id": ma.fields.Str()}
    request_body_parsers = {"application/json": RequestBodyParser(JSONDeserializer())}
    default_content_type = "application/json"

    # Response handling
    response_handlers = {"application/json": ResponseHandler(JSONSerializer())}
    default_accept_mimetype = "application/json"


class JobManagementResourceConfig(JobResourceConfigBase):
    """Job management resource config."""

    # Blueprint configuration
    blueprint_name = "storm_job_jobs_management"
    url_prefix = "/projects/<project_id>/jobs"
    routes = {
        # Base operations
        "create-item": "",
        "read-item": "/<job_id>",
        # Execution operations
        "list-executor-item": "/executors",
    }
