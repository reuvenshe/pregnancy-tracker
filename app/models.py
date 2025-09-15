from . import db

class PregnancyRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100))
    week = db.Column(db.Integer)
    notes = db.Column(db.String(200))

    def __repr__(self):
        return f'<PregnancyRecord {self.patient_name} week {self.week}>'
