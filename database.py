# PyPolBoard
# Copyright (C) 2025 Andrea Minasi
# Licensed under the GNU AGPL v3.0
# See LICENSE file for details

from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load local variables inside the .env file
load_dotenv()

USERNAME = os.environ['DB_USER']
PASSWORD = os.environ['DB_PASS']
HOST = os.environ['DB_HOST']
PORT = os.environ['DB_PORT']
DBNAME = os.environ['DB_NAME']

# Replace USERNAME, PASSWORD, HOST, PORT, and DBNAME with your credentials
engine = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}')