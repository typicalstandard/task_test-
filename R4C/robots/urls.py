from django.urls import path

from robots import CreateRobotAPIView,ExportRobotsView

urlpatterns = [
    path('create_robot/', CreateRobotAPIView.as_view(), name='create_robot'),
    path('export_robots/', ExportRobotsView.as_view(), name='export_robots'),
]
