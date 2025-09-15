import pytest
from app import create_app, db
from app.models import PregnancyRecord

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # DB זמני לכל בדיקה
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_add_and_get_record(client):
    # שלח POST להוספת רשומה
    response = client.post("/records", json={
        "patient_name": "Dana",
        "week": 15,
        "notes": "Feeling good"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['patient_name'] == "Dana"
    assert data['week'] == 15

    # בדוק שהרשומה נשמרה גם ב־GET
    response = client.get("/records")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['patient_name'] == "Dana"
