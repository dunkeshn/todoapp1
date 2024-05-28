from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView, RedirectView, FormView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import models, forms, filters
from django.utils.timezone import now

class Welcome(TemplateView):
    template_name = 'core/welcome.html'
    model = models.User

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

class Tasks(ListView):
    template_name = 'core/tasks.html'
    model = models.Tasks
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['tasks'] = models.Tasks.objects.all()
        return context

class Calendar(TemplateView):
    template_name = 'core/calendar.html'
    model = models.User

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

class Pomodoro(TemplateView):
    template_name = 'core/pomodoro.html'
    model = models.User

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

class Search(TemplateView):
    template_name = 'core/tasksearch.html'
    model = models.User

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context
