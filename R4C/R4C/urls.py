from django.contrib import admin
from django.urls import path

from R4C.robots.views import ExportRobotsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('export_robots/', ExportRobotsView.as_view(), name='export_robots'),  # Новый маршрут
]
