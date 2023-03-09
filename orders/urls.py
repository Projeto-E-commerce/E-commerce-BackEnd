from django.urls import path
from . import views


urlpatterns = [
    path("orders/", views.OrderViewl.as_view()),
    path("orders/client/", views.OrderListClientView.as_view()),
    path("orders/salesman/", views.OrderListSalesmanView.as_view()),
    path("orders/salesman/<int:pk>/", views.OrderEditView.as_view()),
]
