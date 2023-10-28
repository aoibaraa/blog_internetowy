from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Dla wszystkich użytkowników
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('author/<int:author_id>/', views.author_posts, name='author_posts'),

    # Dla zarejestrowanych użytkowników
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('post/<int:pk>/add_comment/', views.add_comment, name='add_comment'),

    # Dla redaktorów
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('my_posts/', views.my_posts, name='my_posts'),

    # Dla admina
    path('admin/', views.admin_panel, name='admin_panel'),
]