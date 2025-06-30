from app.schemas import UserResponse
from .database import client, session
import pytest

# def test_root(client):
#     res = client.get("/")
#     assert res.json().get("message") == "Hi I'm fastapi"
#     assert res.status_code == 200


def test_create_user(client):
    res = client.post(
        "/users",
        json={
            "email": "ignismeow@gmail.com",
            "username": "ignismeow",
            "password": "password",
        },
    )

    new_user = UserResponse(**res.json())
    print(res.json())
    assert new_user.email == "ignismeow@gmail.com"
    assert res.status_code == 201


@pytest.fixture()
def test_user(client):
    user_data = {
        "email": "ignismeow@gmail.com",
        "username": "ignismeow",
        "password": "ignismeow123",
    }

    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user


def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user["username"] , "password": test_user["password"]})
    print(res.json())

    assert res.status_code == 200
