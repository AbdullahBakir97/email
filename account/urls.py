from django.urls import path
from .views import register, signup,
PasswordChangeView,
PasswordResetDoneView,
PasswordResetView,
LoginView,
LogoutView,
SignupView,


urlpatterns = [
    path('register/', register, name='register'),
    path('password/change/',PasswordChangeView.as_view(), name='password_change'),
    path('password/reset/',PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done/',PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('signup/',SignupView.as_view(), name='signup_view'),
    
]