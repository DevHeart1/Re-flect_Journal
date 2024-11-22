from django.shortcuts import render

def index (request):
    return render (request, 'journal_entries/index.html')

def add(request):
    return render (request, 'journal_entries/add.html')
