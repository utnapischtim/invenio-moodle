# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2023 Graz University of Technology.
#
# invenio-moodle is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""

from collections.abc import Callable

import pytest
from flask import Flask

from invenio_moodle import InvenioMoodle


@pytest.fixture(scope="module")
def create_app(instance_path: str) -> Callable:
    """Application factory fixture."""

    def factory(**config: dict) -> Flask:
        app = Flask("testapp", instance_path=instance_path)
        app.config.update(**config)
        InvenioMoodle(app)
        return app

    return factory
