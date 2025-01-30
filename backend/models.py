import uuid
from dataclasses import dataclass, field
import time
from backend.encryption import encrypt, decrypt

@dataclass
class LoginItem:
    name: str
    username: str
    _password: str  # Encrypted password (stored as _password)
    timestamp: str = field(default_factory=lambda: time.time())
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    is_in_bin: bool = False

    def __post_init__(self):
        # Ensure existing IDs are not overwritten
        if not self.id:
            self.id = str(uuid.uuid4())

        # Encrypt password only if it's not already encrypted
        if not self._password.startswith("gAAAAA"):  # Fernet encryption prefix
            self._password = encrypt(self._password)

    @property
    def password(self):
        return decrypt(self._password)

@dataclass
class SecureNoteItem:
    name: str
    _note: str  # Encrypted note (stored as _note)
    timestamp: str = field(default_factory=lambda: time.time())
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    is_in_bin: bool = False

    def __post_init__(self):
        # Ensure existing IDs are not overwritten
        if not self.id:
            self.id = str(uuid.uuid4())

        # Encrypt note only if it's not already encrypted
        if not self._note.startswith("gAAAAA"):  # Fernet encryption prefix
            self._note = encrypt(self._note)

    @property
    def note(self):
        return decrypt(self._note)