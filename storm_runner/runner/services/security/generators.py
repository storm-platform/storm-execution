# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-runner is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from storm_project.project.records.systemfields.access import ProjectAgent
from storm_project.project.services.security.generators import (
    ProjectRecordAgent,
)


class ExecutionTaskRecordOwner(ProjectRecordAgent):
    """Generator to define if the user is a collaborator of the
    project associated to the defined execution task."""

    def _select_record_agent(self, record, **kwargs):

        # using the associated project informations to define the
        # job record collaborators.
        user_agent = ProjectAgent(dict(user=record.user.id))
        project_agent = ProjectAgent(dict(project=record.project.id))

        return [project_agent], [user_agent]
