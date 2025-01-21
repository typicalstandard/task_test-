from django.urls import path

from .views import CreateRobotAPIView

app_name = 'robots'
from .views import ExportRobotsView

app_name = 'robots'

urlpatterns = [
    path('create_robot/', CreateRobotAPIView.as_view(), name='create_robot'),
    path('export_robots/', ExportRobotsView.as_view(), name='export_robots'),
]
