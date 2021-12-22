# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

import marshmallow as ma

from storm_commons.resources.config import BaseResourceConfig
from storm_job.job.resources.args import JobSearchRequestArgsSchema


class JobManagementResourceConfig(BaseResourceConfig):
    """Job management resource config."""

    # Blueprint configuration.
    blueprint_name = "storm_job_jobs_management"

    # Request/Response configuration.
    request_view_args = {"job_id": ma.fields.Str()}
    request_search_args = JobSearchRequestArgsSchema

    # Routes configuration.
    url_prefix = "/projects/<project_id>/jobs"
    routes = {
        # Services operations
        "list-service": "/services",
        # Job operations
        "list-item": "",
        "create-item": "",
        "read-item": "/<job_id>",
        "delete-item": "/<job_id>",
        "update-item": "/<job_id>",
        # Job actions
        "start-job-action": "/<job_id>/actions/start",
    }
