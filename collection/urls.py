from django.urls import path
from .views import CollectionListCreateView


urlpatterns = [
    path("", CollectionListCreateView.as_view()),
]