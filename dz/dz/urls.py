from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from core.views import RegistrationForm, BookListView, BookView, OrderBookView, UserProfileView, \
    ProfileView, IndexRedirectView, BookListPageView, BookCreateView
from dz import settings

login_forbidden = user_passes_test(lambda u: u.is_anonymous, '/books/', redirect_field_name=None)

urlpatterns = [
    path('', IndexRedirectView.as_view()),
    path('admin/', admin.site.urls),
    path('books/', BookListView.as_view(), name='home'),
    path('books/<int:pk>/', BookView.as_view(), name='book_detail'),
    path('books/<int:pk>/order/', OrderBookView.as_view(), name='book_order'),
    path('books/page/', BookListPageView.as_view(), name='book_page'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('profile/', UserProfileView.as_view(), name='update_profile'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('login/', login_forbidden(LoginView.as_view()), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationForm.as_view(), name='signup')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
