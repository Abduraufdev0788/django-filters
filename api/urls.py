from django.urls import path
from .views import add_user_view

urlpatterns = [
    path("list/", add_user_view, name='list')
]
