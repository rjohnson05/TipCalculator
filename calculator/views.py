from django.shortcuts import render

from calculator.models import TipForm


def index(request):
    form = TipForm()
    return render(request, "calculator/index.html", {"form": form})


def results(request):
    form = TipForm(request.POST)
    if form.is_valid():
        tip_amount = '{:,.2f}'.format(form.cleaned_data["billing_amount"] * (form.cleaned_data["tip_amount"] / 100))
    else:
        tip_amount = "N/A"
    return render(request, "calculator/results.html", {"tip_amount": tip_amount})
