from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..auth import BearerToken
from .models import Loan, Payment
from .permissions import IsOwner
from .serializers import LoanSerializer, PaymentSerializer


class LoanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    authentication_classes = (BearerToken,)

    def perform_create(self, serializer):
        serializer.save()


class LoanDetailAPIView(generics.RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    authentication_classes = (BearerToken,)


class PaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    authentication_classes = (BearerToken,)

    def perform_create(self, serializer):
        serializer.save()


class PaymentDetailAPIView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    authentication_classes = (BearerToken,)
