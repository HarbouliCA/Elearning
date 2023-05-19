from extensions import db
from sqlalchemy.orm import relationship

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    purchases = relationship('Purchase', backref='course', lazy=True)
    sessions = relationship('Session', backref='course', lazy=True)
