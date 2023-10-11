from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from dispatch.models import Dispatch


class DispatchListView(ListView):
    model = Dispatch
    context_object_name = 'dispatches'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # dispatches = Dispatch.objects.all()
        # context['dispatches'] = dispatches

        return context


