# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from invenio_db import db

from storm_commons.plugins.rest.service import PluginService
from storm_commons.services.links import ActionLinksTemplate


class JobManagementService(PluginService):
    """Job service."""

    @property
    def links_item_tpl(self):
        """Item links template."""
        return ActionLinksTemplate(self.config.links_item, self.config.links_action)

    def start_execution_job(self, identity, id_, data):
        """Start a job execution."""
        record = self.record_cls.get_record(id=id_)
        self.require_permission(identity, "execute", record=record)

        # Selecting the service
        job_execution_plugin_service = self._plugin_manager.service(record.service)

        # Run components
        for component in self.components:
            if hasattr(component, "start_execution_job"):
                component.start_execution_job(identity, record=record, data=data)

        # Saving the data
        db.session.commit()

        # Running!
        job_execution_plugin_service.service.delay(id_, data)

        return self.result_item(
            self,
            identity,
            record,
            links_tpl=self.links_item_tpl,
            schema=self.schema,
        )


__all__ = "JobManagementService"
