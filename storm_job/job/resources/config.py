# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

import marshmallow as ma

from storm_commons.resources.config import ResourceConfigBase


class JobManagementResourceConfig(ResourceConfigBase):
    """Job management resource config."""

    # Blueprint configuration.
    blueprint_name = "storm_job_jobs_management"

    # Request/Response configuration.
    request_view_args = {"job_id": ma.fields.Str()}

    # Routes configuration.
    url_prefix = "/projects/<project_id>/jobs"
    routes = {
        # Services operations
        "list-service": "/services",
        # Job operations
        "create-item": "",
        "read-item": "/<job_id>",
        "delete-item": "/<deposit_id>",
        "update-item": "/<deposit_id>",
        # Job actions
        "start-item": "/<job_id>/actions/start",
    }
