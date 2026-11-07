from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def activities_state():
    original_activities = deepcopy(activities)
    yield activities
    activities.clear()
    activities.update(original_activities)


@pytest.fixture
def client(activities_state):
    return TestClient(app)