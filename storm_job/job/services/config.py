# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from storm_commons.services.components import (
    UserComponent,
    SoftDeleteComponent,
    RecordServiceComponent,
)

from storm_commons.services.pagination.options import BaseSearchOptions
from storm_commons.services.results import BaseItemResult, BaseListResult
from storm_project.project.services.links import (
    ProjectContextLink,
    project_context_pagination_links,
)

from storm_job.job.models.api import ExecutionJob
from storm_job.job.schema import ExecutionJobSchema
from storm_job.job.services.components import (
    PipelineComponent,
    ProjectComponent,
    ExecutionJobComponent,
)
from storm_job.job.services.security.permissions import (
    JobExecutionRecordPermissionPolicy,
)


class JobManagementServiceConfig:
    """Job management service configuration."""

    result_item_cls = BaseItemResult
    result_list_cls = BaseListResult

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
        SoftDeleteComponent,
        RecordServiceComponent,
        ExecutionJobComponent,
    ]

    links_item = {"self": ProjectContextLink("{+api}/projects/{project_id}/jobs/{id}")}
    links_search = project_context_pagination_links(
        "{+api}/projects/{project_id}/jobs{?args*}"
    )

    # Search configuration
    search = BaseSearchOptions


__all__ = "JobManagementServiceConfig"
