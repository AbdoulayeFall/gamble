from django.shortcuts import render, redirect

from user.forms import * #form_type_pari, form_autre_pari

from pari.models import *
from user.models import *

def compte(request,):
    if request.method == 'GET':
        return redirect('/user/' + str(request.user.id))

type_match = '0'

def profile(request, user_id):
    form = form_type_pari()
    form_pari = form_autre_pari()
    global type

    if request.method == 'GET':
        form = form_type_pari(request.GET)
        if form.is_valid():
            type = form.cleaned_data['type']
            # type_match = type
            if type == '2': #Position Match
                form_pari = form_match()
            elif type == '3': #Position Match
                form_pari = form_combat()
            else:
                form_pari = form_autre_pari()
    else:
        valide(request, type)
    return render(request, 'profile.html', {'form': form, 'form_pari': form_pari, 'id': user_id, })

def valide(request, type):
    user = request.user
    print(type)
    if type == '1':
        form = form_autre_pari(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            date = form.cleaned_data['date']

            print('AutrePari')

            p = AutrePari(jour = date, description = description, name = name)
            p.save()
            user.autre_paris.add(p)
            user.save()

    elif type == '2':
        form = form_match(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            equipe1 = form.cleaned_data['equipe1']
            equipe2 = form.cleaned_data['equipe2']
            date = form.cleaned_data['date']

            p = Match(jour = date, name =name, equipe1 = equipe1, equipe2 = equipe2)
            p.save()
            user.matchs.add(p)
            user.save()
    else :
        form = form_combat(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            joueur1 = form.cleaned_data['joueur1']
            joueur2 = form.cleaned_data['joueur2']
            date = form.cleaned_data['date']

            p = Combat(jour = date, name =name, joueur1 = joueur1, joueur2 = joueur2)
            p.save()
            user.combats.add(p)
            user.save()
