from django.shortcuts import render, redirect
from . models import JournalEntry
from . forms import JournalEntryForm

def index (request):
    entries = JournalEntry.objects.order_by('-created_at')

    context = {'entries': entries}
    return render (request, 'journal_entries/index.html', context)

def add(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, request.FILES)  # Add request.FILES here
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('home')
    else:
        form = JournalEntryForm()
    
    return render(request, 'journal_entries/add.html', {'form': form})