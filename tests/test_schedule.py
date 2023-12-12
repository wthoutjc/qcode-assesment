def test_get_schedules(client):
    response = client.get('/schedules')
    assert response.status_code == 200

def test_get_schedule_by_id(client):
    response = client.get('/schedules/2')
    assert response.status_code == 200

def test_get_schedule_not_found(client):
    response = client.get('/schedules/-1')
    assert response.status_code == 404

def test_create_schedule(client):
    schedule_data = {'day': 'lunes', 'id_service': 2, 'start_time': '09:15:00', 'duration': 60}
    response = client.post('/schedules', json=schedule_data)
    assert response.status_code == 200
    assert response['message'] == 'Schedule created successfully'

def test_update_schedule(client):
    schedule_data = {'day': 'martes', 'start_time': '10:00:00', 'duration': 90}
    response = client.put('/schedules/1', json=schedule_data)
    assert response.status_code == 200
    assert response['message'] == 'Schedule updated successfully'

def test_delete_schedule(client):
    response = client.delete('/schedules/1')
    assert response.status_code == 200
    assert response['message'] == 'Schedule deleted successfully'

def test_get_available_appointment(client):
    response = client.get('/available_appointments/lunes')
    assert response.status_code == 200
    assert 'available_appointments' in response