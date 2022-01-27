from django.shortcuts import render


# Create your views here.
import requests


def home(request):
    return render(request, 'home.html')


def book(request):

    isbnfromform = request.GET.get("ISBN")

    urlfirsthalf = "https://openlibrary.org/api/books?bibkeys=ISBN:"
    urlSecondhalf = "&jscmd=details&format=json"
    url = urlfirsthalf + isbnfromform + urlSecondhalf

    JsonBook = requests.get(url, params=request.GET)
    JsonBook = JsonBook.json()

    isbnforreq = "ISBN:" + isbnfromform

    details = JsonBook[isbnforreq]['details']
    title = details['title']
    auhtor = details['publishers']
    imageLink = JsonBook[isbnforreq]['thumbnail_url']
    return render(request, 'book.html', {'title': title, 'author': auhtor, 'imageLink': imageLink})


"""



    https: // openlibrary.org/api/books?bibkeys = ISBN: 1931498717 & jscmd = details & format = json
    url = 'https://openlibrary.org/api/books?bibkeys=ISBN:'
    ISBN = request.GET.get('ISBN')
    urlRemaining = "&jscmd=details&format=json"

    r = requests.get(url)
    books = r.json()
    books_list = {'books': books['results']}
"""
