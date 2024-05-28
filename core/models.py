from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    priority = models.CharField(max_length=50,
                                choices=[('COMMON', 'Обычный'), ('LOW', 'Низкий'), ('MEDIUM', 'Средний'), ('HIGH', 'Высокий')],
                                verbose_name='Приоритет',
                                default='COMMON')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    deadline = models.DateTimeField(null=True, blank=True, verbose_name='Сделать до')
    completed = models.BooleanField(default=False, verbose_name='Выполнено')
    duration = models.IntegerField(null=True, blank=True, verbose_name='Время выполнения')
    owners = models.ManyToManyField('User', related_name='tasks', verbose_name='Пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['updated_at']


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, blank=True, verbose_name='Фамилия')
    nickname = models.CharField(max_length=100, unique=True, verbose_name='Никнейм')
    email = models.CharField(max_length=100, unique=True, verbose_name='Почта')
    about = models.TextField(blank=True, verbose_name='О себе')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    picture = models.ImageField(upload_to='pictures', null=True, blank=True, verbose_name='Фото')
    friends = models.ManyToManyField('self', blank=True, verbose_name='Друзья', symmetrical=False)



    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email']


