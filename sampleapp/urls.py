from django.urls import path
from .import views


urlpatterns =[
    path('', views.police, name='police'),
    path('signup', views.form, name='signup'),
    path('login',views.login, name='login'),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('schedule',views.schedule,name='schedule'),
    path('complaint',views.complaint,name='complaint'),
    path('logout',views.logout,name='logout'),
    
]

