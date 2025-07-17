# PyPolBoard
# Copyright (C) 2025 Andrea Minasi
# Licensed under the GNU AGPL v3.0
# See LICENSE file for details

from sqlalchemy import Column, Integer, String
from .base import Base

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)