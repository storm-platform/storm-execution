# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

import enum
import uuid

from sqlalchemy import Enum
from sqlalchemy_utils.types import UUIDType

from invenio_db import db
from invenio_records.models import Timestamp
from invenio_accounts.models import User as InvenioUser

from storm_project.project.records.models import ResearchProjectMetadata
from storm_pipeline.pipeline.records.models import ResearchPipelineMetadata


class ExecutionJobStatus(enum.Enum):
    """Execution Job status."""

    # General
    SUCCESS = "success"
    FAILURE = "failure"
    PENDING = "pending"

    # Internal executors
    RUNNING = "running"

    # External executors
    SENT = "SENT"
    SENDING = "SENDING"


class ExecutionJobModel(db.Model, Timestamp):
    """Execution Job database model."""

    __tablename__ = "job_execution_job"

    id = db.Column(
        UUIDType,
        primary_key=True,
        default=uuid.uuid4,
    )

    #
    # Execution Job status
    #
    status = db.Column(Enum(ExecutionJobStatus), default=ExecutionJobStatus.PENDING)

    #
    # Execution Job User owner
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
    pipeline_id = db.Column(UUIDType, db.ForeignKey(ResearchPipelineMetadata.id))
    pipeline = db.relationship(ResearchPipelineMetadata)


__all__ = ("ExecutionJobModel", "ExecutionJobStatus")
