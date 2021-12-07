# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from storm_project import current_project
from storm_pipeline.pipeline.records.api import ResearchPipeline


class ServiceComponentBase:
    """Base execution job service component."""

    def __init__(self, service, *args, **kwargs):
        """Initialize the base service component."""
        self.service = service

    def create(self, identity, **kwargs):
        """Create handler."""
        pass

    def read(self, identity, **kwargs):
        """Read handler."""
        pass

    def update(self, identity, **kwargs):
        """Update handler."""
        pass

    def delete(self, identity, **kwargs):
        """Delete handler."""
        pass

    def search(self, identity, search, params, **kwargs):
        """Search handler."""
        return search


class ProjectComponent(ServiceComponentBase):
    """Service component which set the project context in the record."""

    def create(self, identity, data=None, record=None, **kwargs):
        """Create handler."""
        record.project_id = current_project._obj.id


class PipelineComponent(ServiceComponentBase):
    """Service component which set the pipeline context in the record."""

    def create(self, identity, data=None, record=None, **kwargs):
        """Create handler."""
        record.pipeline_id = ResearchPipeline.pid.resolve(data.get("pipeline_id")).id


class UserComponent(ServiceComponentBase):
    """Service component which set the user context in the record."""

    def create(self, identity, data=None, record=None, **kwargs):
        """Create handler."""
        record.user_id = identity.id


__all__ = ("ProjectComponent", "PipelineComponent", "UserComponent")
