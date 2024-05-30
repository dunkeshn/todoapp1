from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView

from .forms import LoginForm, SignupForm, TaskForm, ChangeProfileForm
from .models import Tasks, User


# Представление для приветственной страницы
class Welcome(TemplateView):
    template_name = 'core/welcome.html'  # Шаблон для отображения

    @method_decorator(login_required)  # Декоратор для обеспечения доступа только авторизованным пользователям
    def dispatch(self, request, *args, **kwargs):
        return super(Welcome, self).dispatch(request, *args, **kwargs)


# Представление для списка задач
class TaskListView(ListView):
    template_name = 'core/tasks.html'  # Шаблон для отображения
    model = Tasks
    context_object_name = 'tasks'  # Имя переменной контекста

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['tasks'] = user.tasks.filter(completed=False)  # Получение незавершенных задач текущего пользователя
        return context


# Функция для создания новой задачи
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            task.owners.add(request.user)
            return redirect('tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})


# Функция для пометки задачи как выполненной
def task_completed(request, pk):
    task = Tasks.objects.get(pk=pk)
    task.completed = True
    task.save()
    return redirect('tasks')


# Представление для календаря
class Calendar(TemplateView):
    template_name = 'core/calendar.html'  # Шаблон для отображения


# Представление для техники помидора
class Pomodoro(TemplateView):
    template_name = 'core/pomodoro.html'  # Шаблон для отображения

# Функция для регистрации нового пользователя
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration.html', {'form': form})


# Функция для входа пользователя
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'signin.html', {'form': form})


# Функция для выхода пользователя
def user_logout(request):
    logout(request)
    return redirect('login')


# Функция для отображения профиля пользователя
def user_profile(request):
    return render(request, 'profile.html')


def edit_profile(request):
    if request.method == 'POST':
        form = ChangeProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful form submission
    else:
        form = ChangeProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


def user_list(request):
    friend_ids = request.user.friends.values_list('id', flat=True)
    print(1 in friend_ids)
    users = User.objects.exclude(id=request.user.id).exclude(id__in=friend_ids)
    return render(request, 'user_list.html', {'users': users})


def add_friend(request, user_id):
    user = User.objects.get(id=user_id)
    request.user.friends.add(user)
    return redirect('profile')


def search(request):
    q = request.GET.get('q')
    tasks = request.user.tasks.filter(completed=False)
    print(tasks)
    tasks = tasks.filter(Q(title__icontains=q) | Q(description__icontains=q)) if q else tasks
    return render(request, 'core/tasksearch.html', context={'tasks': tasks})


def add_owner(request, task_id, user_id):
    task = Tasks.objects.get(id=task_id)
    user = User.objects.get(id=user_id)
    task.owners.add(user)
    return redirect('tasks')
