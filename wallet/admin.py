from django.contrib import admin

from .models import Currency, Account


admin.site.register((Currency, Account))
