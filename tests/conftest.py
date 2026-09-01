import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

# Snapshot of the initial in-memory activities data, used to reset state between tests
_INITIAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the shared in-memory activities dict before each test."""
    activities.clear()
    activities.update(copy.deepcopy(_INITIAL_ACTIVITIES))
    yield


@pytest.fixture
def client():
    return TestClient(app)
