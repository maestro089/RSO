from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from .models import comments,article,user_profile


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'name': "username", 'class': "input username", 'value': "Логин", 'onfocus': "this.value=''"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'password'}
))


class comment_form(forms.ModelForm):
    class Meta():
        model = comments
        fields = ('message',)
        message = forms.CharField(
                                  widget=forms.Textarea(attrs={'placeholder':'Комментарий','width':100,'height':50, 'class': 'text_form'}))


class create_article(forms.ModelForm):
    class Meta():
        model = article
        fields = ('title','content','photo')

        title = forms.CharField(label="Название статьи", min_length=2, max_length=100,
                                widget=forms.TextInput(attrs={'class': 'class'}))
        content = forms.CharField(label='Текст статьи',
                                  widget=forms.Textarea(attrs={'rows': 5, 'cols': 20, 'class': 'text_form'}))
        photo = forms.FileField(label='Загрузите фото',
                                widget=forms.FileInput(attrs={'class':'class'}))


class update_profile(forms.ModelForm):
    class Meta():
        model = user_profile
        fields = ('about', 'photo')

        about = forms.CharField(label='Информация о вас',
                                  widget=forms.Textarea(attrs={'rows': 5, 'cols': 20, 'class': 'text_form'}))
        photo = forms.FileField(label='Загрузите фото',
                                widget=forms.FileInput(attrs={'class':'class'}))

