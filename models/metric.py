from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Float

from . import Base


class Metric(Base):
    __tablename__ = 'metrics'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    value = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
