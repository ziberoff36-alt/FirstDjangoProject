from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Game, Platform
from .forms import GameForm

class GameListView(ListView):
    model = Game
    template_name = 'games/game_list.html'
    context_object_name = 'games'
    def get_queryset(self):
        return Game.objects.select_related('platform').all()

class PlatformListView(ListView):
    model = Platform
    template_name = 'games/platform_list.html'
    context_object_name = 'platforms'

class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game_detail.html'
    context_object_name = 'game'
    def get_queryset(self):
        return Game.objects.select_related('platform').all()

class GamesByPlatformListView(ListView):
    model = Game
    template_name = 'games/games_by_platform.html'
    context_object_name = 'games'
    def get_queryset(self):
        self.platform = get_object_or_404(Platform, pk=self.kwargs['pk'])
        return Game.objects.filter(platform=self.platform)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['platform'] = self.platform
        return context

class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'games/game_form.html'
    success_url = reverse_lazy('game_list')
