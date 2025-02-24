from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

class PlateSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(15), nullable=False)
    plate_numbers = db.Column(JSON, nullable=False)  # Lista de números de placa (JSON)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return f'Schedule {self.number}, start:{self.start_time}, end_time: {self.end_time}'
