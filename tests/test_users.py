from http import HTTPStatus

def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'string',        
        }
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1
    }