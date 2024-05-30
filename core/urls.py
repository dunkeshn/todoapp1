from django.urls import path
from .views import *  # Импорт всех представлений из текущего приложения
from core import views  # Импорт представлений из приложения core

# URL-шаблоны для маршрутизации запросов к представлениям
urlpatterns = [
    path('', Welcome.as_view(), name='home'),  # Главная страница
    path('tasks/', TaskListView.as_view(), name='tasks'),  # Список задач
    path('tasks/<int:pk>/complete', views.task_completed, name='task-completed'),  # Пометить задачу как выполненную
    path('tasks/create', views.create_task, name='create-task'),  # Создать новую задачу
    path('calendar/', Calendar.as_view(), name='calendar'),  # Календарь
    path('pomodoro/', Pomodoro.as_view(), name='pomodoro'),  # Техника помидора
    path('search/', views.search, name='search'),  # Поиск
    path('login/', views.user_login, name='login'),  # Страница входа в систему
    path('signup/', views.user_signup, name='signup'),  # Страница регистрации нового пользователя
    path('logout/', views.user_logout, name='logout'),  # Выход из системы
    path('profile/', views.user_profile, name='profile'),  # Профиль пользователя
    path('profile/edit/', views.edit_profile, name='profile-edit'),  # Редактирование профиля
    path('users/', views.user_list, name='users'),  # Список пользоват
    path('add-friend/<int:user_id>/', views.add_friend, name='add-friend'),  # Добавить друга
    path('tasks/<int:task_id>/add-owner/<int:user_id>/', views.add_owner, name='add-owner'),  # Добавить владельца
]
