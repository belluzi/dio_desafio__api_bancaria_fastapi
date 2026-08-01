class AccountError(Exception):
    pass


class InactiveAccountError(AccountError):
    def __init__(self):
        super().__init__("Conta inativa.")


class InsufficientFundsError(AccountError):
    def __init__(self):
        super().__init__("Saldo insuficiente.")
