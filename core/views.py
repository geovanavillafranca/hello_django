from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, num1, num2):
    return HttpResponse('<h1>A soma de {} e {} é {}</h1>'.format(num1, num2, (num1 + num2)))


def multiplicacao(request, num1, num2):
    return HttpResponse(f'<h1>A multiplicacao de {num1} e {num2} é {(num1 * num2)}</h1>')


def subtracao(request, num1, num2):
    return HttpResponse(f'<h1>A subtracao de {num1} e {num2} é {(num1 - num2)}</h1>')


def divisao(request, num1, num2):
    return HttpResponse(f'<h1>A divisao de {num1} e {num2} é {num1 // num2}</h1>')
