from django.urls import path

from .views import CreateRobotAPIView,ExportRobotsView

app_name = 'robots'

urlpatterns = [
    path('export_robots/', ExportRobotsView.as_view(), name='export_robots'),
]
