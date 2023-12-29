import pytest

from datetime import datetime
from unittest.mock import MagicMock

from src.api import service


@pytest.fixture(scope='session', autouse=True)
def get_timestamp():
    service.get_timestamp = MagicMock()
    service.get_timestamp.return_value=datetime(2023, 1, 1, 1, 1)

@pytest.fixture(scope='session', autouse=True)
def get_duration():
    service.get_duration = MagicMock()
    service.get_duration.return_value=0.0008148193359375e-05