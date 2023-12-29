from fastapi.testclient import TestClient
from test_data.small_vars import correct_json_path, incorrect_json_path
from main import app

client = TestClient(app)


def test_clean_given_correct_path():
    response = client.post("/tibber-developer-test/enter-path/", json=correct_json_path)
    assert response.status_code == 200


def test_clean_given_wrong_path():
    response = client.post("/tibber-developer-test/enter-path/", json=incorrect_json_path)
    assert response.status_code == 422


def test_clean_given_empty_path():
    response = client.post("/tibber-developer-test/enter-path/", json=None)
    assert response.status_code == 422