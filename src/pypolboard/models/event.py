# PyPolBoard
# Copyright (C) 2025 Andrea Minasi
# Licensed under the GNU AGPL v3.0
# See LICENSE file for details

from sqlalchemy import Column, Integer, String, Text, DateTime
from src.pypolboard.models.base import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)
    location = Column(String(100), nullable=True)
    event_type = Column(String(50), nullable=False)
    created_by = Column(String(100), nullable=False)
    expected_participants = Column(Integer, nullable=True)
    attached_files = Column(Text, nullable=True)  # JSON-serialized list
