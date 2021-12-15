# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from storm_job.job.models.model import ExecutionJobStatus
from storm_pipeline.pipeline.records.api import ResearchPipeline

from storm_project import current_project

from invenio_records_resources.services.records.components import ServiceComponent
from invenio_records_resources.services.base.components import BaseServiceComponent


class PipelineComponent(ServiceComponent):
    """Service component which set the pipeline context in the record."""

    def create(self, identity, data=None, record=None, **kwargs):
        """Create handler."""
        record.pipeline_id = ResearchPipeline.pid.resolve(data.get("pipeline_id")).id


class ExecutionJobStatusComponent(BaseServiceComponent):
    """Service component which set the execution job status in the record."""

    def start_execution_job(self, identity, record=None, **kwargs):
        """Start Execution Job handler."""
        record.status = ExecutionJobStatus.STARTING


class ProjectComponent(BaseServiceComponent):
    """Service component which set the project context in the record."""

    def create(self, identity, data=None, record=None, **kwargs):
        """Create handler."""
        record.project_id = current_project._obj.model.id
