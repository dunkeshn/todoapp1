from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from core.models import Tasks


# Форма для регистрации пользователей
class SignupForm(UserCreationForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = User  # Указываем модель, с которой связана форма
        fields = ['name', 'last_name', 'email', 'nickname', 'picture', 'password1', 'password2']  # Поля, которые будут отображены в форме


# Форма для авторизации пользователей
class LoginForm(forms.Form):
    username = forms.CharField(label='Электронная почта')  # Поле для ввода электронной почты
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')  # Поле для ввода пароля


# Форма для создания и редактирования задач
class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks  # Указываем модель, с которой связана форма
        fields = ['title', 'description', 'priority', 'deadline', 'duration']  # Поля, которые будут отображены в форме
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Виджет для ввода даты и времени
        }


class ChangeProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'nickname', 'email', 'about', 'date_of_birth', 'picture']
