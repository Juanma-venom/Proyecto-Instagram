import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_all_members(client):
    """Test getting all family members"""
    response = client.get('/members')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 3
    assert any(member['first_name'] == 'John' for member in data)
    assert any(member['first_name'] == 'Jane' for member in data)
    assert any(member['first_name'] == 'Jimmy' for member in data)

def test_get_member_by_id(client):
    """Test getting a specific member by ID"""
    response = client.get('/members/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['first_name'] == 'John'
    assert data['age'] == 33
    assert data['lucky_numbers'] == [7, 13, 22]

def test_get_nonexistent_member(client):
    """Test getting a member that doesn't exist"""
    response = client.get('/members/999')
    assert response.status_code == 404

def test_add_member(client):
    """Test adding a new member"""
    new_member = {
        'first_name': 'Jack',
        'age': 25,
        'lucky_numbers': [5, 9]
    }
    response = client.post('/members', 
                          data=json.dumps(new_member),
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['first_name'] == 'Jack'
    assert data['age'] == 25
    assert data['last_name'] == 'Jackson'
    assert 'id' in data

def test_delete_member(client):
    """Test deleting a member"""
    response = client.delete('/members/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['done'] == True
    
    # Verify member is deleted
    response = client.get('/members/1')
    assert response.status_code == 404

def test_delete_nonexistent_member(client):
    """Test deleting a member that doesn't exist"""
    response = client.delete('/members/999')
    assert response.status_code == 404