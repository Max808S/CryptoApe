from sqlalchemy import Column, Integer, DateTime, String
from db.base import Base


class CryptoApe_DB(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    entry_time = Column(DateTime, nullable=False)