# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from invenio_records_permissions.generators import SystemProcess
from invenio_records_permissions.policies.records import RecordPermissionPolicy
from storm_project.project.services.security.generators import ProjectRecordUser

from storm_job.job.services.security.generators import JobRecordOwner


class JobExecutionRecordPermissionPolicy(RecordPermissionPolicy):
    """Permissions for the records related to job execution."""

    #
    # High-level permissions
    #

    # Content creators and managers
    can_manage = [JobRecordOwner(), SystemProcess()]

    # General users
    can_use = can_manage + [ProjectRecordUser()]

    #
    # Low-level permissions
    #
    can_read = can_use
    can_search = can_use
    can_create = can_use

    can_update = can_manage
    can_delete = can_manage

    can_execute = can_manage


__all__ = "JobExecutionRecordPermissionPolicy"
