from django.shortcuts import render
from django.http import HttpResponse

from .models import Host, Tickethost

# Create your views here.
def index(request):
    return HttpResponse("Hello World.")

def gerador(request, Host, Tickethost):
    response = "Teste Gerador"
    return HttpResponse("Teste Gerador")

def listaservidores(request):
    response = "Lista Servidores"
    return render(request, "index.html", context)
