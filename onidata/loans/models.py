from _decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models


class Loan(models.Model):
    nominal_value = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
    interest_rate = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
    ip_address = models.GenericIPAddressField()
    request_date = models.DateField()
    bank = models.CharField(max_length=60)
    client = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.client} - {self.ip_address}"


class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name="payments")
    payment_date = models.DateField()
    payment_amount = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
