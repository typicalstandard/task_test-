from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Robot
from orders.models import Order

@receiver(post_save, sender=Robot)
def notify_customers(sender, instance, **kwargs):
    if instance.pk is None:
        return

    orders = Order.objects.filter(robot_serial=instance.serial, status=Order.Status.WAITING)
    customer = orders.customer
    try:
        send_mail(
            'Робот в наличии',
            f'Добрый день!\n\n'
            f'Недавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}.\n'
            f'Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.',
            None,
            [customer.email],
            fail_silently=False,
        )
        orders.status = Order.Status.READY
        orders.save()
        print(f"Письмо успешно отправлено клиенту: {customer.email}")
    except Exception as e:
        print(f"Ошибка при отправке письма клиенту {customer.email}: {e}")
