from django.urls import path
from . import views

urlpatterns = [
    path('', views.GameListView.as_view(), name='game_list'),
    path('add/', views.GameCreateView.as_view(), name='game_create'),
    path('<int:pk>/delete/', views.GameDeleteView.as_view(), name='game_delete'),
    path('<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),
    path('platform/', views.PlatformListView.as_view(), name='platform_list'),
    path('platform/<int:pk>/', views.GamesByPlatformListView.as_view(), name='games_by_platform'),
]
