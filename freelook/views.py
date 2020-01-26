import requests
from django.shortcuts import render
from django.urls import reverse


def get_freelook_data(request):
    data = {
        "SAD": 5400000,
        "EMRPERCENT": 0.75,
        "YEARS": 365.25,
        "DAYS": 13,
        "FLCRATE": 0.004434
    }
    response = requests.post("http://localhost:8000" + reverse('freelook'), data=data)
    return render(request, "freelook.html", context=response.json())
