from django .forms import forms
from . import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'year', 'rating', 'platform']