from pydantic import BaseModel, Field, field_validator, model_validator

class LoginIn(BaseModel):
    owner_document: str = Field(min_length=11, max_length=14)
    password: str = Field(min_length=8, max_length=128)

    @field_validator("owner_document", "password")
    @classmethod
    def strip_strings(cls, value: str) -> str:
        return value.strip()

class CredentialsUpdate(BaseModel):
    current_password: str = Field(min_length=8, max_length=128)
    new_password: str = Field(min_length=8, max_length=128)
    confirm_new_password: str = Field(min_length=8, max_length=128)

    @field_validator("current_password", "new_password", "confirm_new_password")
    @classmethod
    def strip_strings(cls, value: str) -> str:
        return value.strip()

    @model_validator(mode="after")
    def validate_confirmation(self):
        if self.new_password != self.confirm_new_password:
            raise ValueError("Password confirmation does not match")
        return self
