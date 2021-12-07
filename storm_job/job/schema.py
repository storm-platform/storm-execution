# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from flask_marshmallow import Marshmallow
from storm_commons.request import current_access_token


# FIXME: The library does not provide a proxy
#        for easy access to the extension =(
ma = Marshmallow()


class ExecutionJobSchema(ma.Schema):
    """Execution Job schema."""

    class Meta:
        # Fields to expose
        fields = (
            "id",
            "status",
            "pipeline_id",
            "links",
        )

    # Job
    id = ma.UUID(dump_only=True)
    status = ma.Function(lambda obj: obj.status.value, dump_only=True)

    # Project
    project_id = ma.Function(lambda obj: obj.project.data.get("id"), dump_only=True)

    # Pipeline
    pipeline_id = ma.Function(
        lambda obj: obj.pipeline.data.get("id"),
        lambda obj: obj,
        required=True,
    )

    links = ma.Hyperlinks(
        {
            "self": ma.AbsoluteURLFor(
                "storm_job_jobs_management.read",
                values=dict(
                    job_id="<id>",
                    _scheme="https",
                    project_id="<project.data.id>",
                    access_token=current_access_token,
                ),
            )
        }
    )


class JobExecutorMetadataSchema(ma.Schema):
    """Job executor metadata schema."""

    title = ma.String(required=True)
    description = ma.String(required=True)
    supported_descriptors = ma.List(cls_or_instance=ma.String())


class JobExecutorSchema(ma.Schema):
    """Job executor schema."""

    id = ma.String(required=True)
    metadata = ma.Nested(JobExecutorMetadataSchema)


__all__ = "ExecutionJobSchema"
