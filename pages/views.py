from django.shortcuts import render, get_object_or_404
from .models import Track

def index(request):
    tracks = Track.objects.all()
    context = {
        'welcome_title': 'Добро пожаловать в BeatBattle',
        'welcome_text': 'Твой слух — твоё оружие. Готов к битве?',
        'tracks': tracks
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def track_detail(request, pk):
    track = get_object_or_404(Track, pk=pk)
    context = {
        'track': track
    }
    return render(request, 'track_detail.html', context)