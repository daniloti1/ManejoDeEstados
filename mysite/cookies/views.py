from django.shortcuts import render


def index(request):
    return render(request, "cookies/index.html")

def controlador1(request):    
    usuario=request.POST.get('user_name')
    contrasenia=request.POST.get('user_password')
    response=render(request, 'cookies/secundaria.html')
    response.set_cookie('usuario', usuario)
    response.set_cookie('contrasenia', contrasenia)
    return response

def controlador2(request):
    usuario=request.COOKIES.get('usuario')
    contrasenia=request.COOKIES.get('contrasenia')
    valor1=request.POST.get('user_valor1')
    valor2=request.POST.get('user_valor2')
    resultado=int(valor1) + int(valor2) 
    response=render(request, 'cookies/final.html', {'usuario':usuario, 'contrasenia':contrasenia, 'valor1':valor1, 'valor2':valor2, 'resultado':resultado})
    return response
