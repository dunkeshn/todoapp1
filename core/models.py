from django.contrib.auth.models import AbstractUser
from django.db import models
from core.managers import UserManager


# Модель для задач
class Tasks(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')  # Название задачи
    description = models.TextField(blank=True, verbose_name='Описание')  # Описание задачи
    priority = models.CharField(max_length=50, choices=[
        ('COMMON', 'Обычный'),
        ('LOW', 'Низкий'),
        ('MEDIUM', 'Средний'),
        ('HIGH', 'Высокий')
    ], verbose_name='Приоритет', default='COMMON')  # Приоритет задачи
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  # Дата создания задачи
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')  # Дата последнего изменения задачи
    deadline = models.DateTimeField(null=True, blank=True, verbose_name='Сделать до')  # Крайний срок выполнения задачи
    completed = models.BooleanField(default=False, verbose_name='Выполнено')  # Флаг завершения задачи
    duration = models.IntegerField(null=True, blank=True, verbose_name='Время выполнения')  # Продолжительность выполнения задачи
    owners = models.ManyToManyField('User', related_name='tasks', verbose_name='Пользователь')  # Связь с пользователями, назначенными на задачу

    objects = models.Manager()  # Менеджер по умолчанию

    def __str__(self):
        return self.title  # Возвращает название задачи как строковое представление объекта

    class Meta:
        verbose_name = 'Задача'  # Название модели в единственном числе
        verbose_name_plural = 'Задачи'  # Название модели во множественном числе
        ordering = ['updated_at']  # Сортировка задач по дате последнего изменения


# Расширенная модель пользователя
class User(AbstractUser):
    name = models.CharField(max_length=100, verbose_name='Имя')  # Имя пользователя
    last_name = models.CharField(max_length=100, blank=True, verbose_name='Фамилия')  # Фамилия пользователя
    nickname = models.CharField(max_length=100, unique=True, verbose_name='Никнейм')  # Уникальный никнейм пользователя
    email = models.CharField(max_length=100, unique=True, verbose_name='Почта')  # Уникальный адрес электронной почты пользователя
    about = models.TextField(blank=True, verbose_name='О себе')  # О себе пользователя
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')  # Дата рождения пользователя
    picture = models.ImageField(upload_to='pictures', null=True, blank=True, default='pictures/default.jpg', verbose_name='Фото')  # Фотография пользователя
    friends = models.ManyToManyField('self', blank=True, verbose_name='Друзья', symmetrical=False)  # Друзья пользователя
    is_active = models.BooleanField(default=True)  # Флаг активности пользователя
    is_staff = models.BooleanField(default=False)  # Флаг сотрудника (доступ к админке)
    is_superuser = models.BooleanField(default=False)  # Флаг суперпользователя
    date_joined = models.DateTimeField(auto_now_add=True)  # Дата регистрации пользователя
    username = None

    objects = UserManager()  # Менеджер объектов пользователей

    USERNAME_FIELD = 'email'  # Поле, используемое для входа в систему
    REQUIRED_FIELDS = ['nickname']  # Обязательные поля при создании пользователя

    def __str__(self):
        return self.email  # Возвращает адрес электронной почты пользователя как строковое представление объекта

    class Meta:
        verbose_name = 'Пользователь'  # Название модели в единственном числе
        verbose_name_plural = 'Пользователи'  # Название модели во множественном числе
        ordering = ['email']  # Сортировка пользователей по адресу электронной почты
