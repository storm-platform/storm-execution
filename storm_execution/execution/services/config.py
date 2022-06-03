# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-execution is free software; you can redistribute it and/or modify it under
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

from storm_execution.execution.models.api import ExecutionTask
from storm_execution.execution.schema import ExecutionTaskSchema
from storm_execution.execution.services.components import (
    WorkflowComponent,
    ProjectComponent,
    ExecutionTaskComponent,
)
from storm_execution.execution.services.security.permissions import (
    ExecutionTaskRecordPermissionPolicy,
)


class ExecutionTaskManagementServiceConfig:
    """Execution Task management service configuration."""

    result_item_cls = BaseItemResult
    result_list_cls = BaseListResult

    #
    # Common configurations
    #
    permission_policy_cls = ExecutionTaskRecordPermissionPolicy

    #
    # Record configuration
    #
    record_cls = ExecutionTask

    schema = ExecutionTaskSchema

    #
    # Components configuration
    #
    components = [
        ProjectComponent,
        WorkflowComponent,
        UserComponent,
        SoftDeleteComponent,
        RecordServiceComponent,
        ExecutionTaskComponent,
    ]

    links_item = {
        "self": ProjectContextLink("{+api}/projects/{project_id}/executions/{id}")
    }
    links_action = {
        "start": ProjectContextLink(
            "{+api}/projects/{project_id}/executions/{id}/actions/start",
        ),
        "cancel": ProjectContextLink(
            "{+api}/projects/{project_id}/executions/{id}/actions/cancel",
        ),
    }

    links_search = project_context_pagination_links(
        "{+api}/projects/{project_id}/executions{?args*}"
    )

    # Search configuration
    search = BaseSearchOptions


__all__ = "ExecutionTaskManagementServiceConfig"
