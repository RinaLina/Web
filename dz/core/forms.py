from django.forms import Form, ModelForm
from django.contrib.auth.forms import UserCreationForm

from core.models import User, Book


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", )


class UpdateProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ("favorite_author", "about_me", "image")


class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'year', 'pages', 'image']