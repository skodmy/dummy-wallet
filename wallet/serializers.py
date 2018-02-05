from django.apps import apps
from django.conf import settings

from rest_framework import serializers

from .models import Currency, Account


USER_MODEL = apps.get_model(settings.AUTH_USER_MODEL)
USER_MODEL_SERIALIZABLE_FIELDS = (
    'id',
    'username',
    'first_name',
    'last_name',
    'email',
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = tuple(
            field_name for field_name in USER_MODEL_SERIALIZABLE_FIELDS if hasattr(USER_MODEL, field_name)
        )


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'code')


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    currency = CurrencySerializer()

    class Meta:
        model = Account
        fields = ('id', 'user', 'balance', 'currency', 'active_transaction_id')
