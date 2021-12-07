# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.


def create_execution_job_blueprint_api(app):
    """Create execution job API blueprint."""
    ext = app.extensions["storm-job"]

    return ext.execution_job_resource.as_blueprint()


__all__ = "create_execution_job_blueprint_api"
