import pytest
from src.app import app


@pytest.fixture
def client():
    with app.test_client as client:
        yield client


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status":"ok"}


def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200

    users = response.get_json()

    assert isinstance(users, list)
    assert len(users) == 2
    assert users[0]["name"] == "Alice"
    assert users[1]["name"] == "Bob"