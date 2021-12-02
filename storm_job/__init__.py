# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Job schedule and management module for reproduce scientific research in the Storm Platform."""

from .ext import StormJob
from .version import __version__

__all__ = ('__version__', 'StormJob')
