from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from user.forms import * #form_type_pari, form_autre_pari

from pari.models import *
from user.models import *

def compte(request,):
    if request.method == 'GET':
        return redirect('/user/' + str(request.user.id))

type_match = '0'

@csrf_exempt
def profile(request, user_id):
    form = form_type_pari()
    form_pari = form_autre_pari()
    paris = []
    invite_paris = []


    global type

    user = request.user


    if request.method == 'GET':
        if request.GET :
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

    autre_paris = user.autre_paris.all()
    if len(autre_paris) != 0:
        paris.append(autre_paris)
    matchs = user.matchs.all()
    if len(matchs) != 0:
        paris.append(matchs)
    combats = user.combats.all()
    if len(combats) != 0:
        paris.append(combats)

    #Invite
    inAutres = user.inAutres.all()
    if len(inAutres) != 0:
        invite_paris.append(inAutres)
    inMatchs = user.inMatchs.all()
    if len(inMatchs) != 0:
        invite_paris.append(inMatchs)
    inCombats = user.inCombats.all()
    if len(inCombats) != 0:
        invite_paris.append(inCombats)

    len_paris = len(paris)
    len_invite_paris = len(invite_paris)

    context = {
        'form': form,
        'form_pari': form_pari,
        'id': user.id,
        'paris': paris,
        'invites': invite_paris,
        'len_paris': len_paris,
        'len_invite_paris': len_invite_paris,
        # 'autre_paris': autre_paris,
        # 'matchs': matchs,
        # 'combats': combats,
    }

    return render(request, 'profile.html', context)

def valide(request, type):
    user = request.user

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
@csrf_exempt
def invite(request, pari_type, user_id, pari_id):
    pari = ''

    email = request.POST['email']
    invit = User.objects.get(email = email)
    if pari_type == 'MATCH':
        pari = Match.objects.get(id = pari_id)
        invit.inMatchs.add(pari)
    elif pari_type == 'COMBAT':
        pari = Combat.objects.get(id = pari_id)
        invit.inCombats.add(pari)
    else:
        pari = AutrePari.objects.get(id = pari_id)
        invit.inAutres.add(pari)

    invit.save()

    profile(request, user_id)
    return redirect('/user/' + user_id)

@csrf_exempt
def accepter(request, pari_type, pari_id):
    pari = ''
    user = request.user
    user_id = user.id

    if pari_type == 'MATCH':
        pari = Match.objects.get(id = pari_id)
        user.matchs.add(pari)
        user.inMatchs.remove(pari)
    elif pari_type == 'COMBAT':
        pari = Combat.objects.get(id = pari_id)
        user.combats.add(pari)
        user.inCombats.remove(pari)
    else:
        pari = AutrePari.objects.get(id = pari_id)
        user.autre_paris.add(pari)
        user.inAutres.remove(pari)

    user.save()

    profile(request, user_id)
    return redirect('/user/' + str(user_id))

@csrf_exempt
def refuser(request, pari_type, pari_id):
    pari = ''
    user = request.user
    user_id = user.id

    if pari_type == 'MATCH':
        pari = Match.objects.get(id = pari_id)
        user.inMatchs.remove(pari)
    elif pari_type == 'COMBAT':
        pari = Combat.objects.get(id = pari_id)
        user.inCombats.remove(pari)
    else:
        pari = AutrePari.objects.get(id = pari_id)
        user.inAutres.remove(pari)

    user.save()

    profile(request, user_id)
    return redirect('/user/' + str(user_id))
