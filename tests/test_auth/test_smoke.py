

def test_it_should_register_user(client):

    response = client.auth_register(
        username="test01",
        email="test01@gmail.com",
        password="aa01bbcc"
    )
    data = response.json()

    assert (
        response.status_code == 201, 
        "Unsuccesful response code was received from server"
    )
    assert "id" in data, "id of user was not provided"








