from django.urls import path
from onidata.loans.views import (
    LoanDetailAPIView,
    LoanListCreateAPIView,
    PaymentDetailAPIView,
    PaymentListCreateAPIView,
)

urlpatterns = [
    path("loans/", LoanListCreateAPIView.as_view(), name="loan-list-create"),
    path("loans/<int:pk>/", LoanDetailAPIView.as_view(), name="loan-detail"),
    path("payments/", PaymentListCreateAPIView.as_view(), name="payment-list-create"),
    path("payments/<int:pk>/", PaymentDetailAPIView.as_view(), name="payment-detail"),
]
