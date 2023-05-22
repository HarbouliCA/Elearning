from extensions import db
from sqlalchemy.orm import relationship
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), nullable=False) # Teacher or Student
    score = db.Column(db.Integer, default=0)
    courses_taught = relationship('Course', backref='teacher', lazy=True)
    enrollments = relationship('Enrollment', backref='user', lazy=True)
    rewardpoints = relationship('RewardPoint', backref='user', lazy=True)
    purchases = db.relationship('Purchase', backref='user', lazy='dynamic')
