# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-execution is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from marshmallow import fields
from storm_commons.resources.args import BaseSearchRequestArgsSchema


class ExecutionTaskSearchRequestArgsSchema(BaseSearchRequestArgsSchema):
    """Request URL query string arguments."""

    status = fields.String()

    service = fields.String()
    workflow_id = fields.String()
