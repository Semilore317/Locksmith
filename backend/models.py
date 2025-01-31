import uuid
from dataclasses import dataclass, field
import time
from backend.encryption import encrypt, decrypt


@dataclass
class LoginItem:
    name: str
    username: str
    password: str
    timestamp: str = field(default_factory=lambda: time.time())
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    is_in_bin: bool = False

    def __post_init__(self):
        # Ensure existing IDs are not overwritten
        if not self.id:
            self.id = str(uuid.uuid4())

        # Encrypt password only if it's not already encrypted
        if not self.password.startswith("gAAAAA"):  # Fernet encryption prefix
            self.password = encrypt(self.password)

    def get_raw_data(self):
        return {
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "timestamp": self.timestamp,
            "id": self.id,
            "is_in_bin": self.is_in_bin,
        }

    def get_decrypted_data(self):
        data = self.get_raw_data()
        data["password"] = decrypt(self.password)
        return data


@dataclass
class SecureNoteItem:
    name: str
    note: str
    timestamp: str = field(default_factory=lambda: time.time())
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    is_in_bin: bool = False

    def __post_init__(self):
        # Ensure existing IDs are not overwritten
        if not self.id:
            self.id = str(uuid.uuid4())

        # Encrypt note only if it's not already encrypted
        if not self.note.startswith("gAAAAA"):  # Fernet encryption prefix
            self.note = encrypt(self.note)

    def get_raw_data(self):
        return {
            "name": self.name,
            "note": self.note,
            "timestamp": self.timestamp,
            "id": self.id,
            "is_in_bin": self.is_in_bin,
        }

    def get_decrypted_data(self):
        data = self.get_raw_data()
        data["note"] = decrypt(self.note)
        return data
