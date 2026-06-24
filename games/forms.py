from django import forms
from .models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'year', 'rating', 'platform']

        labels = {
            'name': 'Название игры',
            'year': 'Год выпуска',
            'rating': 'Рейтинг (от 0 до 10)',
            'platform': 'Платформа',
        }

        help_texts = {
            'year': 'Например: 2024',
            'rating': 'Можно вводить дробные числа, например: 8.5',
            'platform': 'Выберите платформу из списка (необязательно)',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Введите название игры...',
            }),
            'year': forms.NumberInput(attrs={
                'min': 1950,
                'max': 2026,
                'placeholder': 'гггг'
            }),
            'rating': forms.NumberInput(attrs={
                'min': 0,
                'max': 10,
                'step': 0.1,
                'placeholder': '0.0'
            }),
        }
