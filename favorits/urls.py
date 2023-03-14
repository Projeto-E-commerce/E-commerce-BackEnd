from django.urls import path
from .views import FavoriteListView, FavoriteListGetView

urlpatterns = [
    path("favorits/<int:pk>/", FavoriteListView.as_view()),
    path("favorits/", FavoriteListGetView.as_view()),
]
