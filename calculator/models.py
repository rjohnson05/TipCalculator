from django import forms


"""
This class contains the Tip From, which collects and stores the necessary data for tip calculations.

Author: Ryan Johnson
"""
class TipForm(forms.Form):
    billing_amount = forms.IntegerField(min_value=0, label="Billing Amount")
    tip_amount = forms.IntegerField(min_value=0, max_value=100, label="Tipping Amount (%)")