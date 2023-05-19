def test_loan_str(loan):
    assert str(loan) == f"{loan.client} - {loan.ip_address}"
