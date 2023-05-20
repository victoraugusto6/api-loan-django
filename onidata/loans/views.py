from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..auth import BearerToken
from .models import Loan, Payment
from .serializers import LoanSerializer, PaymentSerializer


class LoanListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LoanSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerToken,)

    def get_queryset(self):
        return Loan.objects.filter(client=self.request.user)

    def perform_create(self, serializer):
        user_ip_address = self.request.META.get("HTTP_X_FORWARDED_FOR")
        if user_ip_address:
            ip = user_ip_address.split(",")[0]
        else:
            ip = self.request.META.get("REMOTE_ADDR")
        serializer.save(ip_address=ip)


class LoanDetailAPIView(generics.RetrieveAPIView):
    serializer_class = LoanSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerToken,)

    def get_queryset(self):
        return Loan.objects.filter(client=self.request.user)


class PaymentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerToken,)

    def get_queryset(self):
        return Payment.objects.filter(loan__client=self.request.user)

    def perform_create(self, serializer):
        serializer.save()


class PaymentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerToken,)

    def get_queryset(self):
        return Payment.objects.filter(loan__client=self.request.user)
