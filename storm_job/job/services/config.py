# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.


from ..models.api import ExecutionJob
from ..schema import ExecutionJobSchema

from .permissions import ExecutionJobRecordPermissionPolicy
from .components import ProjectComponent, PipelineComponent, UserComponent


from storm_commons.plugins import load_service_plugins


class ExecutionJobServiceConfig:

    #
    # Common configurations
    #
    permission_policy_cls = ExecutionJobRecordPermissionPolicy

    #
    # Record configuration
    #
    record_cls = ExecutionJob

    schema = ExecutionJobSchema

    #
    # Components configuration
    #
    components = [ProjectComponent, PipelineComponent, UserComponent]

    #
    # Plugins configuration
    #
    plugins = load_service_plugins("storm_job.plugins")


__all__ = "ExecutionJobServiceConfig"
