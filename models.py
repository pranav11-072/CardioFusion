from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, default='Default Patient')
    vitals = db.relationship('Vitals', backref='patient', lazy=True)


class Vitals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # FIX 5: datetime.datetime.utcnow is deprecated in Python 3.12+
    # Use timezone-aware datetime instead.
    timestamp = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    hr = db.Column(db.Float, nullable=True)
    mode = db.Column(db.String(10), nullable=True)
    lrl = db.Column(db.Integer, nullable=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
