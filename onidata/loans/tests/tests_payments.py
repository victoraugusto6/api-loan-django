from _decimal import Decimal
from model_bakery import baker
from onidata.loans.models import Loan, Payment
from rest_framework import status
from rest_framework.exceptions import ErrorDetail


def test_user_post_payment(api_client, user, loan):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    payload = {
        "payment_date": "2023-05-19",
        "payment_amount": "200.00",
        "loan": loan.pk,
    }

    response = api_client.post("/payments/", payload, "json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Payment.objects.exists()


def test_user_view_payments(api_client, user, payment):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    response = api_client.get("/payments/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["results"] != []


def test_user_retrieve_payment(api_client, user, payment):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    response = api_client.get(f"/payments/{payment.pk}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data


def test_user_no_permission_retrieve_payment(api_client, user):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    payment = baker.make(Payment)
    response = api_client.get(f"/payments/{payment.pk}/")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == {
        "detail": ErrorDetail(string="Not found.", code="not_found")
    }


def test_user_post_validate_payment_gt_loan(api_client, user):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    loan = baker.make(Loan, nominal_value=Decimal("500.00"))
    payload = {
        "payment_date": "2023-05-19",
        "payment_amount": "1000.00",
        "loan": loan.pk,
    }

    response = api_client.post("/payments/", payload, "json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {
        "non_field_errors": [
            ErrorDetail(
                string="The payment amount cannot be greater than the nominal value of the loan.",
                code="invalid",
            )
        ]
    }


def test_user_post_validate_payment_gt_loan_payments(api_client, user):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    loan = baker.make(
        Loan, nominal_value=Decimal("500.00"), interest_rate=Decimal("5.00")
    )
    baker.make(Payment, loan=loan, payment_amount=Decimal(400.00))

    payload = {
        "payment_date": "2023-05-19",
        "payment_amount": "150.00",
        "loan": loan.pk,
    }

    response = api_client.post("/payments/", payload, "json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {
        "non_field_errors": [
            ErrorDetail(
                string="The payment amount cannot be greater than the balance due of the loan.",
                code="invalid",
            )
        ]
    }
