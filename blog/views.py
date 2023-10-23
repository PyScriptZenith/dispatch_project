from django.contrib.auth.mixins import LoginRequiredMixin


from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


from blog.forms import BlogForm
from blog.models import Blog


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = 'blogs'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog




class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')



class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    context_object_name = 'blog'
    success_url = reverse_lazy('blog:blog_list')
