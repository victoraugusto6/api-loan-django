from _decimal import Decimal
from model_bakery import baker
from onidata.loans.models import Loan, Payment
from rest_framework import status
from rest_framework.exceptions import ErrorDetail


def test_user_post_loan(api_client, user):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    payload = {
        "payments": [],
        "nominal_value": "1000.00",
        "interest_rate": "10.00",
        "request_date": "2023-05-19",
        "bank": "Bank Test",
        "client": user.pk,
    }

    response = api_client.post("/loans/", payload, "json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Loan.objects.exists()


def test_user_post_loan_use_ip(api_client, user):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    payload = {
        "payments": [],
        "nominal_value": "1000.00",
        "interest_rate": "10.00",
        "request_date": "2023-05-19",
        "bank": "Bank Test",
        "client": user.pk,
    }

    response = api_client.post("/loans/", payload, "json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["ip_address"] == "127.0.0.1"


def test_user_view_loans(api_client, user, loan):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    response = api_client.get("/loans/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["results"] != []


def test_user_retrieve_loan(api_client, user, loan):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    response = api_client.get(f"/loans/{loan.pk}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data


def test_user_no_permission_retrieve_loan(api_client, user):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    loan = baker.make(Loan)
    response = api_client.get(f"/loans/{loan.pk}/")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == {
        "detail": ErrorDetail(string="Not found.", code="not_found")
    }


def test_user_retrieve_loan_get_balance_due(api_client, user):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    loan = baker.make(
        Loan,
        nominal_value=Decimal("100.00"),
        interest_rate=Decimal("5.00"),
        client=user,
    )

    baker.make(Payment, payment_amount=Decimal("10.00"), loan=loan)
    baker.make(Payment, payment_amount=Decimal("10.00"), loan=loan)

    response = api_client.get(f"/loans/{loan.pk}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["balance_due"] == Decimal("84.00")
