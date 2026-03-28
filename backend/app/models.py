from sqlalchemy import Column, String, JSON
from .database import Base

class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    password = Column(String)

class DashboardLayout(Base):
    __tablename__ = "dashboard_layouts"

    user_id = Column(String, primary_key=True, index=True)
    layout = Column(JSON)