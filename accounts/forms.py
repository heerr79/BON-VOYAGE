# myapp/forms.py
from django import forms

class ItineraryForm(forms.Form):
    destination = forms.CharField(label="Destination", max_length=100)
    number_of_days = forms.IntegerField(label="Number of Days", min_value=1)
    budget = forms.DecimalField(label="Budget", max_digits=10, decimal_places=2)
