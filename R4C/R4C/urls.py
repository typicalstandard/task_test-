from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots/', include('robots.urls', namespace='robots')),
    path('orders/', include('orders.urls', namespace='orders')),
]
