from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Robot
from orders.services.notification_services import notify_customers
from .services.robot_services import set_robot_serial


@receiver(post_save, sender=Robot)
def handle_robot_save(sender, instance, created, **kwargs):
    if created:
        set_robot_serial(instance)
    notify_customers(instance)
