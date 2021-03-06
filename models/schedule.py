from app import db
from datetime import datetime

class Schedule(db.Model):
    __tablename__= "schedules"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    working_hours = db.Column(db.Integer(), default=0, nullable=False)
    breaks = db.Column(db.Integer(), default=0, nullable=False)
    break_activities = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.now(), nullable=False)
