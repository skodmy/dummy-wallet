from django.db import models
from django.conf import settings


class Currency(models.Model):
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'currencies'


class Account(models.Model):
    balance = models.FloatField(default=0.0)
    currency = models.ForeignKey(Currency, models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)

    def __str__(self):
        return "{}: {:.2f} {}".format(self.user.username, self.balance, self.currency.code)
