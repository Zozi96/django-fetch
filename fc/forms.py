from django import forms

from .models import FootballClub


class FootballClubForm(forms.ModelForm):
    class Meta:
        model = FootballClub
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'foundation_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }
