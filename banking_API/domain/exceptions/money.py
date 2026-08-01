class MoneyError(Exception):
    """Base para exceções relacionadas ao dinheiro."""


class NegativeMoneyError(MoneyError):
    def __init__(self):
        super().__init__("Valor de dinheiro negativo.")


class InvalidMoneyScaleError(MoneyError):
    def __init__(self):
        super().__init__("Escala de dinheiro inválida.")


class InvalidMoneyValueError(MoneyError):
    def __init__(self):
        super().__init__("Valor de dinheiro inválido.")


class NonPositiveMoneyError(MoneyError):
    def __init__(self):
        super().__init__("O valor deve ser positivo.")
