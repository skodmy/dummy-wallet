from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes, api_view

from .serializers import AccountSerializer
from .models import Account
from .contextmanagers import transaction


TRANSACT_STATUS_CODE2DETAIL = {
    200: "successfully completed",
    409: "declined multiple",
    412: "insufficient funds",
    500: "operational error",
}


@api_view(['GET'])
def get_accounts(request, user_id, currency_id=None):
    accounts = Account.objects.filter(user_id=user_id)
    if currency_id:
        accounts = accounts.filter(currency_id=currency_id)
    return JsonResponse(AccountSerializer(accounts, many=True).data, safe=False)


@api_view(['PATCH'])
@parser_classes((JSONParser, ))
def transact(request, user_id, account_id):
    account = Account.objects.get(id=account_id, user_id=user_id)
    transaction_id = request.data['transaction_id']
    value = float(request.data['value'])
    if account.active_transaction_id != transaction_id:
        if value < 0 and account.balance < abs(value):
            status_code = 412
        else:
            with transaction(account, transaction_id):
                account.balance += value
            if account.active_transaction_id == 0:
                status_code = 200
            else:
                status_code = 500
    else:
        status_code = 409
    return JsonResponse({'detail': TRANSACT_STATUS_CODE2DETAIL[status_code]}, status=status_code)
