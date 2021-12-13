# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from storm_commons.security import BaseRecordPermissionPolicy


class JobRecordPermissionPolicy(BaseRecordPermissionPolicy):
    """Permissions for the Execution Job records."""

    can_execute = BaseRecordPermissionPolicy.can_use


__all__ = "JobRecordPermissionPolicy"
