from orders.models import Order
from django.core.mail import send_mail

def notify_customers(instance):
    try:
        order = Order.objects.get(robot_serial=instance.serial, status=Order.Status.WAITING)
        customer = order.customer
        send_mail(
            'Робот в наличии',
            f'Добрый день!\n\n'
            f'Недавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}.\n'
            f'Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.',
            None,
            [customer.email],
            fail_silently=False,
        )
        order.status = Order.Status.READY
        order.save()
        print(f"Письмо успешно отправлено клиенту: {customer.email}")
    except Order.DoesNotExist:
        print("Нет подходящих заказов.")
    except Exception as e:
        print(f"Ошибка при отправке письма клиенту {customer.email}: {e}")
