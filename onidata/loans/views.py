from ipware import get_client_ip
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
        client_ip, is_routable = get_client_ip(self.request)
        serializer.save(ip_address=client_ip)


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
