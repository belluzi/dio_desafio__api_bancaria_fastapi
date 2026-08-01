class UserError(Exception):
    """Base para exceções relacionadas ao usuário."""


class InvalidUsernameError(UserError):
    def __init__(self):
        super().__init__("Username deve possuir pelo menos 4 caracteres.")


class SamePasswordError(UserError):
    def __init__(self):
        super().__init__("A nova senha deve ser diferente da atual.")
