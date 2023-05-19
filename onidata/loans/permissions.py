from onidata.loans.models import Loan, Payment
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Loan):
            return True if request.user.is_superuser else obj.client == request.user

        elif isinstance(obj, Payment):
            return (
                True if request.user.is_superuser else obj.loan.client == request.user
            )
