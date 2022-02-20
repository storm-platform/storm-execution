# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-execution is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.


def create_execution_task_management_blueprint_api(app):
    """Create execution task management API blueprint."""
    ext = app.extensions["storm-execution"]

    return ext.execution_task_management_resource.as_blueprint()


__all__ = "create_execution_task_management_blueprint_api"
