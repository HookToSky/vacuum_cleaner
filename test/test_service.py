
import json
import pytest

from src.api import service
from src.api.model import Path, Result
from test_data.small_vars import *


def test_clean_path_with_correct_path():
    response = service.move_accross_the_path(Path(**correct_json_path))
    assert response == Result(**result_default_json)


def test_clean_path_fails_with_incorrect_path():
    with pytest.raises(Exception):
        service.move_accross_the_path(Path(**incorrect_json_path))


def test_clean_path_with_visited_vertex():
    response = service.move_accross_the_path(Path(**correct_duplicate_json_path))
    assert response == Result(**result_duplicate_vertex_json)


def test_heavy_json_path():
    heavy_path = json.loads(open("./test/test_data/robotcleanerpathheavy.json", "r").read())
    response = service.move_accross_the_path(Path(**heavy_path))
    assert response == Result(**result_heavy_json)

    