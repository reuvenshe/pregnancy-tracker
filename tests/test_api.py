import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # DB זמני
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_index(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b"<h1 class=\"mb-4\">Pregnancy Tracker</h1>" in res.data

def test_add_record_and_get(client):
    # הוספת רשומה חדשה
    res = client.post('/load_data')  # יטען מה-CSV
    assert res.status_code == 200

    res = client.get('/records')
    assert res.status_code == 200
    data = res.get_json()
    assert len(data) > 0
    assert "patient_name" in data[0]
