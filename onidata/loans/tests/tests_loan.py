from model_bakery import baker
from onidata.loans.models import Loan
from rest_framework import status


def test_user_post_loan(api_client, user):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    payload = {
        "payments": [],
        "nominal_value": "1000.00",
        "interest_rate": "10.00",
        "ip_address": "70.153.196.199",
        "request_date": "2023-05-19",
        "bank": "Bank Test",
        "client": user.pk,
    }

    response = api_client.post("/loans/", payload, "json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Loan.objects.exists()


def test_user_view_loans(api_client, user, loan):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    response = api_client.get("/loans/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["results"] != []


def test_user_permission_retrieve_loan(api_client, user, loan):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    response = api_client.get(f"/loans/{loan.pk}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data


def test_user_no_permission_retrieve_loan(api_client, user):
    loan = baker.make(Loan)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    response = api_client.get(f"/loans/{loan.pk}/")

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == {
        "detail": "You do not have permission to perform this action."
    }
