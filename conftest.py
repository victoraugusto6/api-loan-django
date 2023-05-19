import pytest
from django.contrib.auth.models import User
from model_bakery import baker
from onidata.loans.models import Loan
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    user = baker.make(User)
    Token.objects.create(user=user)
    return user


@pytest.fixture
def loan(user):
    return baker.make(Loan, client=user)
