

def test_it_should_return_error_on_invalid_username(client):

    response = client.auth_register(
        username="#$!@",
        email="test02@email.com",
        password="aabb01cc"
    )

    assert response.status_code == 400, "Server should return a 400 error code on invalid username"



def test_it_should_return_error_on_invalid_password(client):

    response = client.auth_register(
        username="test01",
        email="test02@email.com",
        password="@@*&$^!@*&$^"
    )

    assert response.status_code == 400, "Server should return a 400 error code on invalid password"



def test_it_should_return_error_on_invalid_email(client):

    response = client.auth_register(
        username="test01",
        email="invalid.com",
        password="aabbcc01"
    )

    assert response.status_code == 400, "Server should return a 400 error code on invalid email"



def test_it_should_return_error_on_already_existing_user(client):

    client.auth_register(
        username="test01",
        email="test01@email.com",
        password="aabbcc01"
    )

    response = client.auth_register(
        username="test01",
        email="test01@email.com",
        password="aabbcc01"
    )

    assert response.status_code == 400, "Server should return a 400 error code on invalid email"