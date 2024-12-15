from django.urls import path

from robots import CreateRobotAPIView

urlpatterns = [
    path('create_robot/', CreateRobotAPIView.as_view(), name='create_robot'),
]
