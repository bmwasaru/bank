import json

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from django.contrib.auth.models import User


class Event(models.Model):

    """Event table that stores all model changes"""
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    time_created = models.DateTimeField()
    content_object = GenericForeignKey('content_type', 'object_id')
    body = JSONField()


class Account(models.Model):

    """Bank Account"""
    balance = models.DecimalField(max_digits=100, decimal_places=6)
    owner = models.ForeignKey(User, related_name='account')

    def make_deposit(self, amount):
        """Deposit money into bank account"""
        Event.objects.create(
            content_object=self,
            time_created=timezone.now(),
            body=json.dumps({
                'type': 'make_deposit',
                'amount': amount
            }))
        self.balance += amount
        self.save()

    def make_withdrawal(self, amount):
        """Withdraw money from the bank"""
        Event.objects.create(
            content_object=self,
            time_created=timezone.now(),
            body=json.dumps({
                'type': 'made_withdrawal',
                'amount': amount
            }))

    @classmethod
    def create_account(cls, owner):
        account = cls.objects.create(owner=owner, balance=0)
        Event.objects.create(
            content_object=account,
            time_created=timezone.now(),
            body=json.dumps({
                'type': 'created_account',
                'id': account.id,
                'owner_id': owner.id
            }))
        return account
