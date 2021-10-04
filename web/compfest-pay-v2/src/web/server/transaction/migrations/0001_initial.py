# Generated by Django 3.2.4 on 2021-07-18 17:02

from django.db import migrations, models
import django.db.models.deletion
import transaction.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=1, validators=[transaction.models.money_positive])),
                ('msg', models.TextField()),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_recipient', to='accmanager.accountmodel')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_sender', to='accmanager.accountmodel')),
            ],
        ),
    ]
