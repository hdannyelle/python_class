from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    news_api_request = requests.get('http://newsapi.org/v2/everything?'
                                    'q="Black Lives Matter"&'
                                    'to=2021-12-2&'
                                    'sortBy=relevancy&'
                                    'apiKey=2adab610c29b44e8bdfdcdcd8a428df3')
    api = json.loads(news_api_request.content)
    return render(request, 'home.html', {'api': api})
