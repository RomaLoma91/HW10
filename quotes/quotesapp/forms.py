from django import forms
from .models import Author, Quote
from django.shortcuts import redirect, render


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'biography']  
        

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['author', 'text'] 

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:quote_list')  # Замініть 'quotes:quote_list' на відповідний URL-шлях до списку цитат
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form}) 
