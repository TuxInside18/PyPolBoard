# alembic/env.py
# PyPolBoard
# Copyright (C) 2025 Andrea Minasi
# Licensed under the GNU AGPL v3.0
# See LICENSE file for details

import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# --- Project-specific configuration ---

# Add the 'src' directory to the Python path to make the application package importable.
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))

# Import the application's declarative base and configuration.
from pypolboard.core.config import DATABASE_URL
from pypolboard.models.base import Base

# Import the 'models' package. Its __init__.py ensures that all model classes
# are registered with the Base's metadata before it is used.
# This is crucial for 'autogenerate' to detect the models.
from pypolboard import models

# --- End of project-specific configuration ---

config = context.config

# Set the database URL from the application's configuration,
# overriding the value in alembic.ini.
if DATABASE_URL:
    config.set_main_option('sqlalchemy.url', DATABASE_URL)
else:
    raise ValueError("DATABASE_URL is not configured. Check your .env file and config module.")

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set the target metadata for Alembic's 'autogenerate' support.
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well. By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
