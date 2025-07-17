# PyPolBoard
# Copyright (C) 2025 Andrea Minasi
# Licensed under the GNU AGPL v3.0
# See LICENSE file for details

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import centralized configuration
from .config import DATABASE_URL

# Create the engine
engine = create_engine(DATABASE_URL, echo=False, future=True)

# Create the factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
