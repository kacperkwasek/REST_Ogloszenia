from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Ogloszenie

def dodaj_ogloszenie(request):
    if request.method == 'POST':
        tytul = request.POST.get('tytul')
        tresc = request.POST.get('tresc')
        if tytul and tresc:
            Ogloszenie.objects.create(tytul=tytul, tresc=tresc)
            return render(request, 'ogloszenia/dodaj_ogloszenie_success.html')
    return render(request, 'ogloszenia/dodaj_ogloszenie.html')

def wyswietl_ogloszenia(request):
    ogloszenia = Ogloszenie.objects.all()
    return render(request, 'ogloszenia/wyswietl_ogloszenia.html', {'ogloszenia': ogloszenia})

def edytuj_ogloszenie(request, ogloszenie_id):
    ogloszenie = get_object_or_404(Ogloszenie, pk=ogloszenie_id)
    if request.method == 'POST':
        tytul = request.POST.get('tytul')
        tresc = request.POST.get('tresc')
        ogloszenie.tytul = tytul
        ogloszenie.tresc = tresc
        ogloszenie.save()
        return redirect('wyswietl_ogloszenia')
    return render(request, 'ogloszenia/edytuj_ogloszenie.html', {'ogloszenie': ogloszenie})

def strona_glowna(request):
    return redirect('wyswietl_ogloszenia')
