from django.urls import path, include

from .views import get_accounts, transact

balance_urlpatterns = [
    path('', get_accounts, name='accounts-get-all'),
    path('currency/<int:currency_id>/', get_accounts, name='accounts-get-by-currency'),
    path('transact/target/<int:account_id>/', transact, name='accounts-transact'),
]

urlpatterns = [
    path('REST/user/<int:user_id>/', include([
        path('accounts/', include(balance_urlpatterns))
    ])),
]
