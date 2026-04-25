from django.contrib import admin
from django.urls import path
from pages.views import index, about, track_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('track/<int:pk>/', track_detail, name='track_detail'),
]