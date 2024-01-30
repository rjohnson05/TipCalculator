from django import forms


class TipForm(forms.Form):
    billing_amount = forms.IntegerField(min_value=0)
    tip_amount = forms.IntegerField(min_value=0, max_value=100)