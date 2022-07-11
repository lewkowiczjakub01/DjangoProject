from django.http import HttpResponse
from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect)
from .models import *
from .forms import *

def index(request):
    liga = Liga.objects.order_by('-id')
    context = {'liga' : liga}
    return render(request, 'league/index.html', context)

def leagues(request, liga_id):
    liga = Liga.objects.get(pk=liga_id)
    klub = Klub.objects.order_by('-id')
    context = {
        'liga' : liga,
        'klub' : klub,
        'liga_id' : liga_id,
    }
    return render(request, 'league/league.html', context)

def clubs(request, klub_id):
    klub = Klub.objects.get(pk=klub_id)
    pilkarz = Pilkarz.objects.order_by('-id')
    stadion = Stadion.objects.order_by('-id')
    trener = Trener.objects.order_by('-id')
    context = {
        'pilkarz' : pilkarz,
        'klub' : klub,
        'klub_id' : klub_id,
        'stadion' : stadion,
        'trener' : trener,
    }
    return render(request, 'league/klub.html', context)

def players(request, pilkarz_id):
    pilkarz = Pilkarz.objects.get(pk=pilkarz_id)
    klub = Klub.objects.order_by('-id')
    context = {
        'pilkarz' : pilkarz,
        'klub' : klub,
        'pilkarz_id' : pilkarz_id,
    }
    return render(request, 'league/pilkarz.html', context)

def stadions(request, stadion_id):
    stadion = Stadion.objects.get(pk=stadion_id)
    klub = Klub.objects.order_by('-id')
    context = {
        'stadion' : stadion,
        'klub' : klub,
        'stadion_id' : stadion_id,
    }
    return render(request, 'league/stadion.html', context)

def coach(request, trener_id):
    trener = Trener.objects.get(pk=trener_id)
    klub = Klub.objects.order_by('-id')
    context = {
        'trener' : trener,
        'klub' : klub,
        'trener_id' : trener_id,
    }
    return render(request, 'league/trener.html', context)

def mecze(request):
    mecze = Mecz.objects.order_by('-id')
    context = {
        'mecze' : mecze,
    }
    return render(request, 'league/mecze.html', context)

def mecz(request, mecz_id):
    mecz = Mecz.objects.get(pk=mecz_id)
    stadion = Stadion.objects.order_by('-id')
    context = {
        'mecz' : mecz,
        'stadion': stadion,
    }
    return render(request, 'league/mecz.html', context)

def dodajPilkarza(request):
    context ={}
    form = addPlayer(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']=form
    return render(request, "league/dodajPilkarza.html", context)

def dodajKlub(request):
    context ={}
    form = addClub(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']=form
    return render(request, "league/dodajKlub.html", context)

def edytujPilkarza(request, pilkarz_id):
    context ={}
    obj = get_object_or_404(Pilkarz, id=pilkarz_id)
    form = addPlayer(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()


    context["form"] = form
    return render(request, "league/edytujPilkarza.html", context)

def edytujKlub(request, klub_id):
    context ={}
    obj = get_object_or_404(Klub, id=klub_id)
    form = addClub(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()


    context["form"] = form
    return render(request, "league/edytujKlub.html", context)

def usunPilkarza(request, pilkarz_id):
    context ={}
    obj = get_object_or_404(Pilkarz, id=pilkarz_id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/league/")

    return render(request, "league/usunPilkarza.html", context)


def usunKlub(request, klub_id):
    context ={}
    obj = get_object_or_404(Klub, id=klub_id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/league/")
    return render(request, "league/usunKlub.html", context)