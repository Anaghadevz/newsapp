from django.shortcuts import render
import requests
API_KEY = '6da724d3a7e44e0292b481f3bef46dd8'


# Create your views here.


def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    # elif country and category:
    #     url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={API_KEY}"
    #     response = requests.get(url)
    #     data = response.json()
    #     articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']



    context = {
        'articles' : articles
    }

    return render(request, 'news_api/home.html', context)



