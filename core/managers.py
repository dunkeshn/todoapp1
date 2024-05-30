from django.contrib.auth.base_user import BaseUserManager


# Менеджер для управления созданием пользователей
class UserManager(BaseUserManager):

    def create_user(self, email, nickname, password=None, **extra_fields):
        """
        Создаёт и возвращает обычного пользователя с электронной почтой, никнеймом и паролем.
        """
        if not email:
            raise ValueError('Поле Email должно быть установлено')  # Проверка, что поле email заполнено
        if not nickname:
            raise ValueError('Поле Nickname должно быть установлено')  # Проверка, что поле nickname заполнено

        email = self.normalize_email(email)  # Нормализация email, можно вводить любой регистр
        user = self.model(email=email, nickname=nickname, **extra_fields)  # Создание экземпляра пользователя
        user.set_password(password)  # Установка пароля
        user.save(using=self._db)  # Сохранение пользователя в базе данных
        return user

    def create_superuser(self, email, nickname, password=None, **extra_fields):
        """
        Создаёт и возвращает суперпользователя с электронной почтой, никнеймом и паролем.
        """
        extra_fields.setdefault('is_staff', True)  # Установка флага is_staff в True
        extra_fields.setdefault('is_superuser', True)  # Установка флага is_superuser в True

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')  # Проверка is_staff флага
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')  # Проверка is_superuser флага

        return self.create_user(email, nickname, password,
                                **extra_fields)  # Создание суперпользователя с переданными параметрами
