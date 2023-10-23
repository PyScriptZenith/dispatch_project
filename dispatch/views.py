import datetime
import random
from random import choice
from django.core.cache import cache

from django.contrib.auth.mixins import LoginRequiredMixin


from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView


from blog.models import Blog
from dispatch.forms import DispatchForm, MessageForm, ClientForm
from dispatch.models import Dispatch, Message, Logs, Client


from config import settings





class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'dispatch/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        # Формируем данные для отображения на главной странице

        # Количество рассылок

        context_data['count_dispatches'] = Dispatch.objects.all().count()

        # Количество запущенных рассылок

        context_data['count_active_dispatches'] = \
            Dispatch.objects.filter(status='запущена').count()

        # Количество уникальных клиентов

        context_data['count_user'] = Client.objects.all().count()

        # 3 статьи из блога

        context_data['blogposts'] = Blog.objects.all()[:3]

        # Низкоуровневое кэширование 3-х статей из блога

        if settings.CACHE_ENABLED:
            key = 'object_list'
            object_list = cache.get(key)
            if object_list is None:
                object_list = Blog.objects.all()[:3]
                cache.set(key, object_list)
        else:
            object_list = Blog.objects.all()[:3]

        context_data['object_list'] = object_list

        return context_data



class DispatchListView(LoginRequiredMixin, ListView):
    model = Dispatch
    context_object_name = 'dispatches'

    # Фильтруем рассылки по пользователю

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs


class DispatchDetailView(LoginRequiredMixin, DetailView):
    model = Dispatch


class DispatchCreateView(LoginRequiredMixin, CreateView):
    model = Dispatch
    form_class = DispatchForm
    success_url = reverse_lazy('dispatch:dispatch_list')



class DispatchUpdateView(LoginRequiredMixin, UpdateView):
    model = Dispatch
    form_class = DispatchForm
    success_url = reverse_lazy('dispatch:dispatch_list')



class DispatchDeleteView(LoginRequiredMixin, DeleteView):
    model = Dispatch
    context_object_name = 'dispatch'
    success_url = reverse_lazy('dispatch:dispatch_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    context_object_name = 'messages'


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('dispatch:message_list')

    def form_valid(self, form):
        self.object = form.save()

        return super().form_valid(form)




class MessageDetailView(LoginRequiredMixin,DetailView):
    model = Message


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('dispatch:message_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    context_object_name = 'message'

    success_url = reverse_lazy('dispatch:message_list')


class LogsListView(LoginRequiredMixin, ListView):
    model = Logs
    context_object_name = 'logs'




class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    context_object_name = 'clients'

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('dispatch:client_list')



class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm

    success_url = reverse_lazy('dispatch:client_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    context_object_name = 'client'

    success_url = reverse_lazy('dispatch:client_list')

