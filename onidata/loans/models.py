from uuid import uuid4

from _decimal import Decimal
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Sum


class Loan(models.Model):
    identifier = models.UUIDField(default=uuid4)
    nominal_value = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
    interest_rate = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
    ip_address = models.GenericIPAddressField()
    request_date = models.DateField()
    bank = models.CharField(max_length=60)
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.client} - {self.ip_address}"

    def get_balance_due(self):
        total_payments = self.payments.aggregate(sum_payments=Sum("payment_amount"))[
            "sum_payments"
        ]
        nomimal_value = self.nominal_value
        interest_rate = self.interest_rate

        if not total_payments:
            total_payments = Decimal("0")

        balance_due = nomimal_value - total_payments
        balance_due += balance_due * (interest_rate / 100)
        return balance_due


class Payment(models.Model):
    identifier = models.UUIDField(default=uuid4)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name="payments")
    payment_date = models.DateField()
    payment_amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
