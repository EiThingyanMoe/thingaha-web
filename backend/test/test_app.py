import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

from app import create_app


@pytest.fixture()
def init_app():
    create_app()


def test_sample(init_app):
    assert init_app == None


