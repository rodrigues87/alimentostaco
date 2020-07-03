from django.shortcuts import render, redirect
from dietas.models import Dieta
from dietas.forms import DietaForm


def list_minhas_dietas(request):
    if request.user.is_authenticated:
        dietas = Dieta.objects.filter(usuario=request.user)
        return render(request, 'dietas/dietas_minha_lista.html', {'dietas': dietas})
    return redirect('/dietas/solicitar')


def list_dietas(request):
    if request.user.is_authenticated:
        dietas = Dieta.objects.all()
        return render(request, 'dietas/dietas_lista.html', {'dietas': dietas})
    return redirect('/dietas/solicitar')


def create_dieta(request):
    form = DietaForm(request.POST or None)
    form.usuario = request.user
    if form.is_valid():
        form.save()
        return redirect('list_dietas')
    return render(request, 'dietas/dieta-form.html', {'form': form})


def update_dieta(request, id):
    dieta = Dieta.objects.get(id=id)
    form = DietaForm(request.POST or None, instance=dieta)
    if form.is_valid():
        form.save()
        return redirect('list_dietas')
    return render(request, 'site/dietas/dieta-form.html', {'form': form, 'dieta': dieta})


def delete_dieta(request, id):
    dieta = Dieta.objects.get(id=id)

    if request.method == "POST":
        print("delete dieta post")
        dieta.delete()
        return redirect('list_dietas')

    return render(request, 'site/dietas/confirm-dieta-delete.html', {'dieta': dieta})


def add_alimento_dieta(request):
    pass
