from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, verify_email, UserListView,  \
    block_user, unblock_user

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('verify_email/<str:uidb64>/<str:token>/', verify_email, name='verify_email'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('<int:pk>/block_user', block_user, name='block_user'),
    path('<int:pk>/unblock_user', unblock_user, name='unblock_user'),


]
