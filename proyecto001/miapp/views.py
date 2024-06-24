from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layout= """
<h1> Proyecto Web (LP3 2024) | Flor Cerdán </h1>
<hr/>
<ul>
    <li>
        <a href="/index"> Inicio</a>
    </li>
    <li>
        <a href="/saludo"> Mensaje de Saludo</a>
    </li>
    <li>
        <a href="/rango"> Mostrar Números [a,b]</a>
    </li>
    <li>
        <a href="/rango2/40/30"> Mostrar Números [40,30]</a>
    </li>
</ul>
<hr/>
"""
def saludo(request):
    return render(request, 'saludo.html')

def index(request):
    return render(request, 'index.html')

def rango(request):
    a=10
    b=20
    resultado = f"""
    <h2>Numeros de [{a},{b}]</h2>
    resultado: <br>
    <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
    resultado += "</ul>"
    return HttpResponse(layout + resultado)

def rango2(request,a,b):
    if a>b:
        return redirect('rango2',a=b,b=a)
    
    resultado = f"""
    <h2>Numeros de [{a},{b}]</h2>
    resultado: <br>
    <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
    resultado += "</ul>"
    return HttpResponse(layout + resultado)
