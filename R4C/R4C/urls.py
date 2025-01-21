from django.contrib import admin
from django.urls import path, include
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls', namespace='orders')),
    path('robots/', include('robots.urls', namespace='robots'))
]
