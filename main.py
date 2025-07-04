# PyPolBoard
# Copyright (C) 2025 Andrea Minasi
# Licensed under the GNU AGPL v3.0
# See LICENSE file for details


from typing import List
from datetime import datetime


class Events:
    def __init__(self,
                 id: int,
                 title: str,
                 description: str,
                 date_start: datetime,
                 date_end: datetime,
                 location: str,
                 event_type: str,
                 created_by: str,
                 expected_participants: int,
                 attached_files: List[str] = None
                 ):
        self.id = id
        self.title = title
        self.description = description
        self.date_start = date_start
        self.date_end = date_end
        self.location = location
        self.event_type = event_type
        self.created_by = created_by
        self.expected_participants = expected_participants
        self.attached_files = attached_files if attached_files is not None else []
