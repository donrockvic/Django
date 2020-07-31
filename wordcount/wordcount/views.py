from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['text']
    wordlist = fulltext.split()
    words = {}
    for item in wordlist:
        if item in words:
            words[item]+=1
        else:
            words[item]=1
    dict1 = sorted(words.items(),key= operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'text':fulltext, 'count':len(wordlist), 'words':dict1})
