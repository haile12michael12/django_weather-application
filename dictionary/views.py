
import requests
from django.shortcuts import render
from .forms import WordForm

def search_word(request):
    form = WordForm()
    context = {'form': form}

    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            try:
                response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
                if response.status_code == 200:
                    word_data = response.json()[0]
                    context['word_data'] = word_data
                else:
                    context['error'] = 'Word not found'
            except Exception as e:
                context['error'] = 'An error occurred while fetching the definition'
    
    return render(request, 'dictionary/search.html', context)
