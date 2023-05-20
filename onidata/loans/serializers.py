from _decimal import Decimal
from django.db.models import Sum
from rest_framework import serializers

from .models import Loan, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

    def validate(self, data):
        validated_data = super().validate(data)

        # get loan from payment
        loan = validated_data["loan"]

        if validated_data["payment_amount"] > loan.nominal_value:
            raise serializers.ValidationError(
                "The payment amount cannot be greater than the nominal value of the loan."
            )
        elif validated_data["payment_amount"] > loan.get_balance_due():
            raise serializers.ValidationError(
                "The payment amount cannot be greater than the balance due of the loan."
            )

        return validated_data


class LoanSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)
    balance_due = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = "__all__"

    def get_balance_due(self, obj):
        total_payments = obj.payments.aggregate(sum_payments=Sum("payment_amount"))[
            "sum_payments"
        ]
        nomimal_value = obj.nominal_value
        interest_rate = obj.interest_rate

        if not total_payments:
            total_payments = Decimal("0")

        balance_due = nomimal_value - total_payments
        balance_due += balance_due * (interest_rate / 100)
        return balance_due
