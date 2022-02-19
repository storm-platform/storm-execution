# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-runner is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

import enum

from sqlalchemy import Enum
from sqlalchemy_utils.types import UUIDType

from invenio_db import db
from invenio_accounts.models import User as InvenioUser

from storm_project.project.records.models import ResearchProjectMetadata
from storm_workflow.workflow.records.models import ResearchWorkflowMetadata

from storm_commons.records.model import BaseRecordModel


class ExecutionTaskStatus(enum.Enum):
    """Execution Task status."""

    # General
    CREATED = "created"
    FAILED = "failed"
    QUEUED = "queued"
    FINISHED = "finished"

    RUNNING = "running"


class ExecutionTaskModel(db.Model, BaseRecordModel):
    """Execution Task database model."""

    __tablename__ = "runner_execution_tasks"

    #
    # Execution Task
    #
    service = db.Column(db.String)

    status = db.Column(Enum(ExecutionTaskStatus), default=ExecutionTaskStatus.CREATED)

    #
    # Execution Task User owner
    #
    user_id = db.Column(db.Integer, db.ForeignKey(InvenioUser.id))
    user = db.relationship(InvenioUser)

    #
    # Associated project
    #
    project_id = db.Column(UUIDType, db.ForeignKey(ResearchProjectMetadata.id))
    project = db.relationship(ResearchProjectMetadata)

    #
    # Related pipeline
    #
    workflow_id = db.Column(UUIDType, db.ForeignKey(ResearchWorkflowMetadata.id))
    workflow = db.relationship(ResearchWorkflowMetadata)


__all__ = (
    "ExecutionTaskModel",
    "ExecutionTaskStatus",
)
