from django import forms


"""
This class is used to collect and store the necessary data for tip calculations.
"""
class TipForm(forms.Form):
    billing_amount = forms.IntegerField(min_value=0, label="Billing Amount")
    tip_amount = forms.IntegerField(min_value=0, max_value=100, label="Tipping Amount (%)")