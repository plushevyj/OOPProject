import pytest

from ..bumbo.api import API


@pytest.fixture
def api():
    return API()
