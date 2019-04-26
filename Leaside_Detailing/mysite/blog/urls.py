from django.urls import path
from . import views

#template tagging
app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^about/$', views.about, name='about'),
    path(r'^contact/$', views.contact, name='contact'),
    path(r'^events/$', views.events, name='events'),
    path(r'^user_login/', views.user_login, name='user_login'),
    path(r'^register/', views.register, name='register'),
    path(r'^services/$', views.services, name='services'),
    path(r'^single/$', views.single, name='single'),
]
