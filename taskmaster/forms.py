from django import forms
from django.contrib.admin.widgets import AdminTimeWidget, AdminDateWidget

from .models import Task, Message, User


# Login form
class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=40)
    password = forms.CharField(label='Пароль', max_length=40, widget=forms.PasswordInput())
    next = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control text-center'


# Task form
class TaskForm(forms.ModelForm):
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        label='Файлы', required=False)

    field_order = ['performer','to_complete']

    class Meta:
        model = Task
        fields = (
            'performer', 'importance', 'title', 'to_complete',
            'text', 'comment'
            )

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['to_complete'].input_formats = ["%a %b %d %Y %H:%M:%S"]


# Message form
class MessageForm(forms.ModelForm):
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        label='Файлы', required=False)

    class Meta:
        model = Message
        fields = ('recipient', 'title', 'text')

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['rows'] = 5


# User form
class UserForm(forms.ModelForm):
    #password = forms.CharField(max_length=50, widget=forms.PasswordInput(), label="Пароль")

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'third_name',
            'username', 'password', 'email', 'position', 'avatar'
        )



