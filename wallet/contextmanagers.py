from contextlib import contextmanager

from django.db import Error

from .models import Account


@contextmanager
def transaction(account: Account, transaction_id: int):
    try:
        account.active_transaction_id = transaction_id
        account.save()
        yield account
    except Error:
        account.active_transaction_id = -1
    else:
        account.active_transaction_id = 0
    finally:
        account.save()
