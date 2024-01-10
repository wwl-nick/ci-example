from django.shortcuts import render


def index(request):
    text = 'Hello World!!'
    return render(request, 'index.html', {'text': text})
