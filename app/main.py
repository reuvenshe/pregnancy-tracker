from flask import Blueprint, request, jsonify, render_template
from . import db
from .models import PregnancyRecord
import pandas as pd

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

# Load CSV data into SQLite
@main_bp.route('/load_data', methods=['POST'])
def load_data():
    df = pd.read_csv('data/pregnancy_data.csv')
    for _, row in df.iterrows():
        record = PregnancyRecord(
            patient_name=row['patient_name'],
            week=int(row['week']),
            notes=row.get('notes', '')
        )
        db.session.add(record)
    db.session.commit()
    return jsonify({"message": "Data loaded successfully!"})

# Get all records
@main_bp.route('/records', methods=['GET'])
def get_records():
    records = PregnancyRecord.query.all()
    output = []
    for r in records:
        output.append({
            'id': r.id,
            'patient_name': r.patient_name,
            'week': r.week,
            'notes': r.notes
        })
    return jsonify(output)

# POST חדש להוספת רשומה
@main_bp.route('/records', methods=['POST'])
def add_record():
    data = request.get_json()
    record = PregnancyRecord(
        patient_name=data["patient_name"],
        week=int(data["week"]),
        notes=data.get("notes", "")
    )
    db.session.add(record)
    db.session.commit()
    return jsonify({
        'id': record.id,
        'patient_name': record.patient_name,
        'week': record.week,
        'notes': record.notes
    }), 201
