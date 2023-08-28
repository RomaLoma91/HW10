from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Author, Quote
from .forms import AuthorForm, QuoteForm


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_author')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_quote')
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})

def author_quote_list(request):
    authors = Author.objects.all()
    quotes = Quote.objects.all()
    return render(request, 'author_quote_list.html', {'authors': authors, 'quotes': quotes})



