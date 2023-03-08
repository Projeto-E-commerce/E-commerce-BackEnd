from django.urls import path
from . import views


urlpatterns = [
    path("orders/", views.OrderViewl.as_view()),
]
