# Generated by Django 4.2.1 on 2023-05-19 00:25

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loans", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="interest_rate",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=5,
                validators=[django.core.validators.MinValueValidator(Decimal("0.01"))],
            ),
        ),
        migrations.AlterField(
            model_name="loan",
            name="nominal_value",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(Decimal("0.01"))],
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_amount",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=5,
                validators=[django.core.validators.MinValueValidator(Decimal("0.01"))],
            ),
        ),
    ]
