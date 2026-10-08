from django.shortcuts import render , get_object_or_404
from .models import  Kit
def home(request): 
    kit = Kit.objects.all()
    return render(request, 'home.html', {"kit":kit})


def navigation(request):
    return render(request, "navigation.html")


def footer(request):
    return render(request, "footer.html")

def sotuvchi_bolish(request):
    return render(request, "sotuvchi_bolish.html")


def sotuvchi_login(request):
    return render(request, "sotuvchi_login.html")


def sotuvchi_register(request):
    return render(request, "sotuvchi_register.html")



def topshirish_punkitini_ochish(request):
    return render(request, "topshirish_punkitini_ochish.html")
def savol_javob(request):
    return render(request, "savol_javob.html")
def salom(request):
    return render(request, "salom.html") 

def savdo(request): 
    return render(request, "savdo.html") 
def splash(request):
    return render(request, "splash.html")

def detail(request,tovar_id):
    kit = get_object_or_404(Kit, id=tovar_id)
    context = {
        'kit':kit
    }
    return render(request, "detail.html" , context)