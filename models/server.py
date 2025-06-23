from sqlalchemy import Column, Integer, String

from . import Base


class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True)
    domain = Column(String(256), nullable=False)
    port = Column(Integer, nullable=False)
    web_path = Column(String(256), nullable=False)
    sub_port = Column(Integer, nullable=False)
    sub_web_path = Column(String(256), nullable=False)
