from django.urls import path
from .views import NotifyCustomerView

app_name = 'orders'

urlpatterns = [
    path('notify/<str:model_name>/<str:version>/<int:customer_id>/', NotifyCustomerView.as_view(), name='notify_customer'),
]