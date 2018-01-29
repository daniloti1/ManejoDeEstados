from django.shortcuts import render


def index(request):
    return render(request, "camposOcultos/index.html")

def controlador1(request):
    usuario=request.POST.get('user_name')
    contrasenia=request.POST.get('user_password')
    return render(request, 'camposOcultos/secundaria.html', {'usuario':usuario, 'contrasenia':contrasenia})

def controlador2(request):
    usuario=request.POST.get('user_name')
    contrasenia=request.POST.get('user_password')
    valor1=request.POST.get('user_valor1')
    valor2=request.POST.get('user_valor2')
    resultado=int(valor1) + int(valor2) 
    return render(request, 'camposOcultos/final.html', {'usuario':usuario, 'contrasenia':contrasenia, 'valor1':valor1, 'valor2':valor2, 'resultado':resultado})
