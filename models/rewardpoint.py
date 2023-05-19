from extensions import db
from sqlalchemy.orm import relationship

class RewardPoint(db.Model):
    __tablename__ = 'rewardpoint'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    points = db.Column(db.Integer, nullable=False)
    reward_time = db.Column(db.DateTime, nullable=False)
