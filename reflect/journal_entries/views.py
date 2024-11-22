from django.shortcuts import render
from . models import JournalEntry

def index (request):
    entries = JournalEntry.objects.order_by('-created_at')

    context = {'entries': entries}
    return render (request, 'journal_entries/index.html', context)

def add(request):
    return render (request, 'journal_entries/add.html')
