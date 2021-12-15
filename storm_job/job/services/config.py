# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from storm_commons.services.components import (
    UserComponent,
    RecordServiceTypeComponent,
)

from storm_job.job.models.api import ExecutionJob
from storm_job.job.schema import ExecutionJobSchema
from storm_job.job.services.components import (
    PipelineComponent,
    ExecutionJobStatusComponent,
    ProjectComponent,
)

from storm_job.job.services.security.permissions import (
    JobExecutionRecordPermissionPolicy,
)


class JobManagementServiceConfig:
    """Job management service configuration."""

    #
    # Common configurations
    #
    permission_policy_cls = JobExecutionRecordPermissionPolicy

    #
    # Record configuration
    #
    record_cls = ExecutionJob

    schema = ExecutionJobSchema

    #
    # Components configuration
    #
    components = [
        ProjectComponent,
        PipelineComponent,
        UserComponent,
        ExecutionJobStatusComponent,
        RecordServiceTypeComponent,
    ]


__all__ = "JobManagementServiceConfig"
