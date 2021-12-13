# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from flask_marshmallow import Marshmallow
from storm_commons.request import current_access_token

from marshmallow_utils.fields import SanitizedUnicode
from storm_commons.schema.validators import marshmallow_not_blank_field

ma = Marshmallow()


class ExecutionJobSchema(ma.Schema):
    """Execution Job schema."""

    class Meta:
        # Fields to expose
        fields = (
            "id",
            "status",
            "service",
            "pipeline_id",
            "links",
        )

    # Job
    id = ma.UUID(dump_only=True)
    status = ma.Function(lambda obj: obj.status.value, dump_only=True)

    service = SanitizedUnicode(validate=marshmallow_not_blank_field(), required=True)

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


__all__ = "JobExecutorMetadataSchema"
