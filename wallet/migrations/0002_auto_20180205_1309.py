# Generated by Django 2.0.2 on 2018-02-05 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name_plural': 'currencies'},
        ),
        migrations.AddField(
            model_name='account',
            name='client_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
