def test_get_services(client):
    response = client.get('/services')
    assert response.status_code == 200

def test_get_service_by_id(client):
    response = client.get('/services/1')
    assert response.status_code == 200

def test_get_service_not_found(client):
    response = client.get('/services/-1')
    assert response.status_code == 404

def test_create_service(client):
    service_data = {'name': 'New Service', 'description': 'New Description'}
    response = client.post('/services', json=service_data)
    assert response.status_code == 200

def test_update_service(client):
    service_data = {'name': 'Updated Service', 'description': 'Updated Description'}
    response = client.put('/services/1', json=service_data)
    assert response.status_code == 200
