from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from core import views

urlpatterns = [
    path('', Welcome.as_view(), name='home'),
    path('tasks/', Tasks.as_view(), name='tasks'),
    path('calendar/', Calendar.as_view(), name='calendar'),
    path('pomodoro/', Pomodoro.as_view(), name='pomodoro'),
    path('search/', Search.as_view(), name='search')
    # path('category/<int:pk>/', CategoryDetail.as_view(), name='category'),
]
