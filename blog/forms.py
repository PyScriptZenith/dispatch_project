from django import forms

from blog.models import Blog
from dispatch.forms import StyleMixin


class BlogForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content',)
