from django.shortcuts import render

from calculator.models import TipForm

"""
Contains the views for the calculator app, rendering the HTML templates the user sees.

Author: Ryan Johnson
"""


def index(request):
    """
    Displays the home page (index.html), including the form collecting tip data.
    """
    form = TipForm()
    return render(request, "calculator/index.html", {"form": form})


def results(request):
    """
    Displays the results page (results.html), stating the calculated tipping dollar amount.
    """
    form = TipForm(request.POST)
    if form.is_valid():
        tip_amount = '{:,.2f}'.format(form.cleaned_data["billing_amount"] * (form.cleaned_data["tip_amount"] / 100))
    else:
        tip_amount = "N/A"
    return render(request, "calculator/results.html", {"tip_amount": tip_amount})
