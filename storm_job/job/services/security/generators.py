# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.


from storm_project.project.records.api import ResearchProject
from storm_project.project.services.security.generators.context import (
    BaseStoredProjectContextGenerator,
)


class ProjectJobCreator(BaseStoredProjectContextGenerator):
    """Generator to define a user as execution job colaborator based on
    the records information."""

    #
    # Project API class
    #
    project_api_cls = ResearchProject