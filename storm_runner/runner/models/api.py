# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-runner is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from invenio_records.systemfields import SystemFieldsMixin, ModelField

from storm_runner.runner.models.model import ExecutionTaskModel
from storm_commons.records.api import BaseRecordModelAPI


class ExecutionTask(BaseRecordModelAPI, SystemFieldsMixin):
    """Execution Task High-level API"""

    model_cls = ExecutionTaskModel
    """SQLAlchemy model class defining which table stores the records."""

    #
    # Creator
    #
    user = ModelField()
    user_id = ModelField()

    #
    # Associated project
    #
    project = ModelField()
    project_id = ModelField()

    #
    # Used workflow
    #
    workflow = ModelField()
    workflow_id = ModelField()

    # General status
    status = ModelField()
    service = ModelField()

    is_deleted = ModelField()


__all__ = "ExecutionTask"
