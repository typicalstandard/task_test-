from robots.models import Robot
from ..models import Order

def check_robot_availability(model_name, version):
    robots_count = Robot.objects.filter(model=model_name, version=version).count()
    min_required_robots = 1

    if robots_count >= min_required_robots:
        return {"message": "Роботов достаточно в наличии."}, 200
    else:
        return {"message": "Недостаточное количество роботов в наличии."}, 404


def create_order(customer, model_name, version):
    order = Order.objects.create(
        robot_serial=f"{model_name}-{version}",
        customer=customer,
        status=Order.Status.WAITING,
    )
    return order