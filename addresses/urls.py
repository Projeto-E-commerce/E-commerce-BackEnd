from django.urls import path
from . import views

urlpatterns = [
    path("address/", views.AddressView.as_view()),
    path("address/<int:pk>/", views.AddressDetailView.as_view()),
]
