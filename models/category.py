from extensions import db
from sqlalchemy.orm import relationship

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    courses = relationship('Course', backref='category', lazy=True)
