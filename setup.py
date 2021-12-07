# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Job schedule and management module for reproduce scientific research in the Storm Platform."""

import os
from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

tests_require = []

invenio_db_version = ">=1.0.9,<2.0.0"

extras_require = {
    "docs": [
        "Sphinx>=3,<4",
    ],
    "tests": tests_require,
    # Databases
    "mysql": [
        f"invenio-db[mysql,versioning]{invenio_db_version}",
    ],
    "postgresql": [
        f"invenio-db[postgresql,versioning]{invenio_db_version}",
    ],
    "sqlite": [
        f"invenio-db[versioning]{invenio_db_version}",
    ],
}

extras_require["all"] = [req for _, reqs in extras_require.items() for req in reqs]

setup_requires = []

install_requires = [
    # Invenio dependencies
    "invenio-records-resources>=0.17.0,<0.18",
    # Storm dependencies
    "storm-commons @ git+https://github.com/storm-platform/storm-commons",
    "storm-pipeline @ git+https://github.com/storm-platform/storm-pipeline",
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("storm_job", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="storm-job",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords=["Storm Platform", "Execution jobs", "Invenio module"],
    license="MIT",
    author="Felipe Menino Carlos",
    author_email="felipe.carlos@inpe.br",
    url="https://github.com/storm-platform/storm-job",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "invenio_base.apps": [
            "storm_job = storm_job:StormJob",
            "storm_job_marshmallow = flask_marshmallow:Marshmallow",
        ],
        "invenio_base.api_apps": ["storm_job = storm_job:StormJob"],
        "invenio_base.api_blueprints": [
            "storm_job_api = storm_job.views:create_job_management_blueprint_api"
        ],
        "invenio_db.models": ["storm_job = storm_job.job.models.model"],
        # 'invenio_access.actions': [],
        # 'invenio_admin.actions': [],
        # 'invenio_assets.bundles': [],
        # 'invenio_base.api_apps': [],
        # 'invenio_base.api_blueprints': [],
        # 'invenio_base.blueprints': [],
        # 'invenio_celery.tasks': [],
        # 'invenio_db.models': [],
        # 'invenio_pidstore.minters': [],
        # 'invenio_records.jsonresolver': [],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 1 - Planning",
    ],
)
