from django.urls import path
from . import views


urlpatterns = [
    path("coupons/", views.CuoponViewl.as_view()),
    path("coupons/<int:pk>/", views.CouponDetailView.as_view()),
]
