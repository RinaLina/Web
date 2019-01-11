from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import model_to_dict
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from core.forms import RegisterForm, UpdateProfileForm, BookCreateForm
from core.models import Book, User


class RegistrationForm(View):
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        return render(request, 'registration/signup.html', {'form': form})

    def get(self, request):
        form = RegisterForm()
        return render(request, 'registration/signup.html', {'form': form})


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = "book_list"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form_create'] = BookCreateForm()
        return data

    def get_queryset(self):
        return self.model.objects.order_by('-id')


class BookListApi(LoginRequiredMixin, ListView):
    model = Book
    def get(self, request):
        return



class BookCreateView(CreateView):
    fields = ['title', 'author', 'publisher', 'year', 'pages', 'image']
    model = Book

    def form_valid(self, form):
        book = form.save()
        return render(self.request, 'book.html', {'book': book})


class BookView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Book

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        book = get_object_or_404(Book, pk=self.get_object().pk)
        data['users_list'] = book.user_set.all()
        return data


class OrderBookView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = request.user
        book = get_object_or_404(Book, pk=pk)
        user.books.add(book)
        return render(request, 'order_user.html', {'user': user})


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        form = UpdateProfileForm(initial=model_to_dict(user, fields=['about_me', 'favorite_author']))
        return render(request, 'update_profile.html', {'user': user, 'form': form})

    def post(self, request):
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('/profile/')


class ProfileView(DetailView):
    template_name = 'profile.html'
    model = User


class IndexRedirectView(View):
    def get(self, request):
        return redirect('/login/')


class BookListPageView(ListView):
    model = Book
    template_name = 'page.html'
    context_object_name = "book_list"
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.order_by('-id')