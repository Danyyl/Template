from django.urls import path

from app.views import index, accept_view

urlpatterns = [
    path('index/', index),
    path('accept/', accept_view),
]