from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('track/<int:pk>/', views.track_detail, name='track_detail'),
    path('contact/', views.contact_view, name='contact'),
]