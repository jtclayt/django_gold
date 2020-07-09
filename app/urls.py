from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('process_gold/<str:location>', views.process_gold),
    path('reset', views.reset)
]
