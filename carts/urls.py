from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import CartCreateView, CartView, CartUpdateView

urlpatterns = [
    path("cart/<int:pk>/", CartCreateView.as_view()),
    path("cart/<int:pk>/item/", CartUpdateView.as_view()),
    path("cart/", CartView.as_view()),
]
