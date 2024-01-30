from django import forms


class TipForm(forms.Form):
    billing_amount = forms.IntegerField(min_value=0, label="Billing Amount")
    tip_amount = forms.IntegerField(min_value=0, max_value=100, label="Tipping Amount (%)")