from django.http import JsonResponse, HttpResponse
from django.views import View
from customers.models import Customer
from .services.robot_service import check_robot_availability, create_order

class NotifyCustomerView(View):
    def get(self, request, model_name, version, customer_id):
        try:
            customer = Customer.objects.get(pk=customer_id)

            response, status = check_robot_availability(model_name, version)
            if status == 200:
                return HttpResponse(response["message"], status=status)

            create_order(customer, model_name, version)
            return HttpResponse("Недостаточное количество роботов в наличии", status=404)
        except Customer.DoesNotExist:
            return HttpResponse("Клиент не найден", status=404)
        except Exception as e:
            return HttpResponse(str(e), status=500)
