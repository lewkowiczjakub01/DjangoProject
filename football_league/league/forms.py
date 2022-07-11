from django import forms
from .models import *

class addPlayer(forms.ModelForm):
    class Meta:
        model = Pilkarz

        fields = [
            "imie",
            "nazwisko",
            "data_urodzenia",
            "poprzedni_klub",
            "numer_koszulki",
            "klub",
        ]

class addClub(forms.ModelForm):
    class Meta:
        model = Klub

        fields = [
            "nazwa",
            "zalozyciel",
            "prezes",
            "data_zalozenia",
            "liga",
        ]