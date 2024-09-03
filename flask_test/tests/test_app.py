def test_index(client):
    # ʹ��client��ģ������

    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'message': 'Hello, World!'}


def test_greet(client):
    response = client.get('/greet/skx')
    assert response.status_code == 200
    assert response.json == {'message': f'Hello, skx!'}


def test_echo(client):
    response = client.post('/echo', json={'message': 'Hello, World!'})
    assert response.status_code == 200
    assert response.json == {'message': 'Hello, World!'}
