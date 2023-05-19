from django.contrib import admin
from onidata.loans.models import Loan, Payment


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "ip_address",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("loan",)
