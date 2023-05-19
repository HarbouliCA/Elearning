from extensions import db
from sqlalchemy.orm import relationship

class Session(db.Model):
    __tablename__ = 'session'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    recording_url = db.Column(db.String(500))
    enrollments = relationship('Enrollment', backref='session', lazy=True)
