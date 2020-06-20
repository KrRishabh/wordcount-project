from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def eggs(request):
    return HttpResponse("Eggs are great!")


def aboutpage(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    counting = len(wordlist)
    worddict = {}

    for word in wordlist:

        if word in worddict:
            worddict[word] += 1

        else:
            worddict[word]=1



    return render(request,'count.html',{'fulltext':fulltext, 'counting':counting, 'worddict' : worddict.items()})
