from extensions import db
from sqlalchemy.orm import relationship

class Purchase(db.Model):
    __tablename__ = 'purchase'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    purchase_time = db.Column(db.DateTime, nullable=False)
    teacher_score = db.Column(db.Float, nullable=False)
    student_score = db.Column(db.Float, nullable=False)