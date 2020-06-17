from django.shortcuts import render, redirect
from .forms import calendar
from django.contrib import messages

# Create your views here.


def booking(request):
    if request.method == "POST":
        form = calendar(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre rendez-vous a bien été enregistré merci de votre confiance !')
            return render(request, 'reservation.html')
        else:
            for field, error in form.errors.items():
                print(field, error)
                messages.success(request, "L'heure que vous avez choisi n'est pas disponible !")

    else:
        form = calendar()
    return render(request, 'reservation.html', {"form": form})