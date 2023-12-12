def test_get_schedules(client):
    response = client.get('/schedules')
    assert response.status_code == 200

def test_get_schedule_by_id(client):
    response = client.get('/schedules/2')
    assert response.status_code == 200

def test_get_schedule_not_found(client):
    response = client.get('/schedules/-1')
    assert response.status_code == 404

def test_get_available_appointment(client):
    response = client.get('/available-appointment/lunes')
    assert response.status_code == 200