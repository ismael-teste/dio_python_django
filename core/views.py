from django.shortcuts import render, HttpResponse


def hello(request, num1, num2):
    soma = num1 + num2
    return HttpResponse(f'<h1>Hello World!{soma} </h1>')
