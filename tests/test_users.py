from app.schemas import UserResponse
from jose import jwt 
from app.config import settings
from app import schemas

# def test_root(client):
#     res = client.get("/")
#     assert res.json().get("message") == "Hi I'm fastapi"
#     assert res.status_code == 200


def test_create_user(client):
    res = client.post(
        "/users/",
        json={
            "email": "ignismeow@gmail.com",
            "username": "ignismeow",
            "password": "ignismeow123",
        },
    )

    new_user = UserResponse(**res.json())
    print(new_user.email)
    assert new_user.email == "ignismeow@gmail.com"
    assert res.status_code == 403


def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user["username"] , "password": test_user["password"]})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    print(res.json())

    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


def test_incorrect_login(test_user, client):
    res = client.post("/login", data={ "username": test_user["username"], "password": "wrongPassword"})

    assert res.status_code == 403
    assert res.json().get('detail') == "Invalid Credentials"