from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import bs4

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):

    word = request.GET['word']

    res = requests.get('https://www.dictionary.com/browse/'+word)

    if res:
        soup = bs4.BeautifulSoup(res.text, 'lxml')

        meaning = soup.find_all('div', {'value': '1'})
        meaning1 = meaning[0].getText()
    else:
        word = 'Sorry, '+ word + ' Is Not Found In Our Database'
        meaning = ''
        meaning1 = ''

    

    results = {
        'word' : word,
        'meaning' : meaning1,
    }


    return render(request, 'word.html', { 'results': results})