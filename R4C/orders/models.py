from django.db import models
from customers.models import Customer


class Order(models.Model):
    class Status(models.IntegerChoices):
        WAITING = 0, 'Waiting'
        READY = 1, 'Ready'

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    robot_serial = models.CharField(max_length=5, blank=False, null=False)
    status = models.IntegerField(choices=Status.choices, default=Status.READY)

