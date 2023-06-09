from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return

def mostrar_correo(request):
    correo = "alu.18131214@correo.itlalaguna.edu.mx"
    mensaje = f"La confirmacion del pedido se enviara a: {correo}"
    return render(request, 'product_detail.html', {'mensaje': mensaje})