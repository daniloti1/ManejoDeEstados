from django.shortcuts import render


def index(request):
    return render(request, "sessions/index.html")

def controlador1(request):
    usuario=request.POST.get('user_name')
    contrasenia=request.POST.get('user_password')    
    request.session['usuario']=usuario
    request.session['contrasenia']=contrasenia
    response=render(request, 'sessions/secundaria.html')
    return response

def controlador2(request):
    usuario=request.session.get('usuario')
    contrasenia=request.session.get('contrasenia')
    valor1=request.POST.get('user_valor1')
    valor2=request.POST.get('user_valor2')
    resultado=int(valor1) + int(valor2) 
    response=render(request, 'sessions/final.html', {'usuario':usuario, 'contrasenia':contrasenia, 'valor1':valor1, 'valor2':valor2, 'resultado':resultado})
    return response
