# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-runner is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

import marshmallow as ma

from marshmallow_utils.fields import SanitizedUnicode
from storm_commons.plugins.validators import marshmallow_validate_plugin_service


class ExecutionTaskSchema(ma.Schema):
    """Execution Task schema."""

    class Meta:
        unknown = ma.EXCLUDE

    # Execution task
    id = ma.fields.UUID(dump_only=True)
    status = ma.fields.Function(lambda obj: obj.status.value, dump_only=True)

    service = SanitizedUnicode(
        validate=lambda obj: marshmallow_validate_plugin_service("storm-runner")(obj),
        required=True,
    )

    # Project
    project_id = ma.fields.Function(
        lambda obj: obj.project.data.get("id"), dump_only=True
    )

    # Workflow
    workflow_id = ma.fields.Function(
        lambda obj: obj.workflow.data.get("id"),
        lambda obj: obj,
        required=True,
    )


__all__ = "ExecutionTaskSchema"
