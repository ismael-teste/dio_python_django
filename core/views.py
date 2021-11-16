from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Evento


def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuario ou senha invalido")

    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    ctx = {"eventos": eventos}
    return render(request, 'agenda.html', ctx)


@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')


@login_required(login_url='/login/')
def submit_evento(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        data_evento = request.POST.get("data_evento")
        descricacao = request.POST.get("descricacao")
        usuario = request.user
        Evento.objects.create(
            titulo=titulo,
            data_evento=data_evento,
            descricacao=descricacao,
            usuario=usuario,
        )
    return redirect('/')
