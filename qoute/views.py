import requests
from django.shortcuts import render


def qoute(request):
    # Fetch a random quote from the API
    response = requests.get("https://api.quotable.io/random")
    quote_data = response.json()

    context = {
        "quote": quote_data.get("content", ""),
        "author": quote_data.get("author", ""),
    }

    return render(request, "qoute.html", context)
