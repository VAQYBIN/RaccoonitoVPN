from datetime import datetime
from sqlalchemy import BigInteger, Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from . import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String(64), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    subscriptions = relationship('Subscription', back_populates='user')
    referrals = relationship('Referral', back_populates='user', foreign_keys='Referral.user_id')
    referred = relationship('Referral', back_populates='referred_user', foreign_keys='Referral.referred_user_id')
    transactions = relationship('Transaction', back_populates='user')
    logs = relationship('Log', back_populates='user')
