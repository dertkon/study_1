from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def pay(self, amount):
        self.balance -= amount


class PayPalPaymentProcessor(PaymentProcessor):
    def pay(self, amount):
        super().pay(amount)


class CreditCardPaymentProcessor(PaymentProcessor):
    def pay(self, amount):
        super().pay(amount)


class CryptoPaymentProcessor(PaymentProcessor):
    def pay(self, amount):
        super().pay(amount)

Т