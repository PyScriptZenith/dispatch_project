from django import forms

from dispatch.models import Dispatch, Message, Client


class StyleMixin:
    """
    Класс для единой стилистики форм
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DispatchForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Dispatch
        fields = ('start_time', 'end_time', 'frequency', 'status', 'client')


class MessageForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'message', 'dispatch',)

class ClientForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email',)
