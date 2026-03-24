from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),           # protected homepage
    path('login/', views.login_page, name='login'),   # login page
    path('signup/', views.signup_view, name='signup'),# register page
    path('logout/', views.logout_view, name='logout'),# logout action
]
