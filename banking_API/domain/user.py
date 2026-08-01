from dataclasses import dataclass
from datetime import datetime
from .exceptions.user import SamePasswordError, InvalidUsernameError

@dataclass
class User:
    id: int | None
    account_id: int
    username: str
    email: str
    password_hash: str
    created_at: datetime | None
    updated_at: datetime | None
    last_login_at: datetime | None
    password_changed_at: datetime | None

    def register_login(self, login_at: datetime, updated_at: datetime) -> None:

        self.last_login_at = login_at
        self.updated_at = updated_at


    def change_password(self, new_password_hash: str, changed_at: datetime) -> None:

        if self.password_hash == new_password_hash:
            raise SamePasswordError()

        self.password_hash = new_password_hash
        self.password_changed_at = changed_at
        self.updated_at = changed_at


    def change_email(self, email: str, updated_at: datetime) -> None:

        if not email.strip():
            raise InvalidEmailError()
        
        self.email = email
        self.updated_at = updated_at


    def change_username(self, username: str, updated_at: datetime) -> None:

        username = username.strip()

        if len(username) < 4:
            raise InvalidUsernameError()
    
        self.username = username
        self.updated_at = updated_at
