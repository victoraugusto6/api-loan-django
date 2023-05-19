from model_bakery import baker
from onidata.loans.models import Payment
from rest_framework import status


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


def test_user_permission_retrieve_payment(api_client, user, payment):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    response = api_client.get(f"/payments/{payment.pk}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data


def test_user_no_permission_retrieve_payment(api_client, user):
    payment = baker.make(Payment)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user.auth_token.key}")

    response = api_client.get(f"/payments/{payment.pk}/")

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == {
        "detail": "You do not have permission to perform this action."
    }
