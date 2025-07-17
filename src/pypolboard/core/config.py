# PyPolBoard
# Copyright (C) 2025 Andrea Minasi
# Licensed under the GNU AGPL v3.0
# See LICENSE file for details

import os
from pathlib import Path
from dotenv import load_dotenv

# Find the project root directory (the one containing pyproject.toml)
# by navigating up from the current file's location.
# __file__ -> .../src/pypolboard/core/config.py
# .parent -> .../src/pypolboard/core
# .parent -> .../src/pypolboard
# .parent -> .../src
# .parent -> Project_Root/
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
ENV_PATH = PROJECT_ROOT / ".env"

# Explicitly check if the .env file exists at the expected path.
if not ENV_PATH.exists():
    raise FileNotFoundError(f".env file not found at the expected path: {ENV_PATH}")

# Load environment variables from the explicit .env file path.
load_dotenv(dotenv_path=ENV_PATH)

# Retrieve environment variables.
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Validation: ensure all required variables have been loaded.
# If any are None, the application will stop immediately with a clear error.
required_vars = {
    "DB_USER": db_user,
    "DB_PASS": db_pass,
    "DB_HOST": db_host,
    "DB_PORT": db_port,
    "DB_NAME": db_name,
}

missing_vars = [key for key, value in required_vars.items() if value is None]
if missing_vars:
    raise ValueError(f"Missing environment variables: {', '.join(missing_vars)}. Check {ENV_PATH}.")

# Build the database connection string only after validating all variables.
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"