from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from alimentostacoaz.models import Alimento
from atividades.models import Atividade
from dietas.models import Dieta
from dietas.forms import DietaForm
from recomendado.models import Recomendado
from tmb.models import TMB


def list_minhas_dietas(request):
    if request.user.is_authenticated:
        atividades = Atividade.objects.all()

        print(atividades)
        dietas = Dieta.objects.filter(usuario=request.user)
        return render(request, 'dietas/dietas_minha_lista.html', {'dietas': dietas, 'atividades': atividades})
    return redirect('/dietas/solicitar')


def list_dietas(request):
    if request.user.is_authenticated:
        dietas = Dieta.objects.all()
        return render(request, 'dietas/dietas_lista.html', {'dietas': dietas})
    return redirect('/dietas/solicitar')


def create_dieta(request):
    dieta = Dieta.objects.create(nome="Minha Dieta2", usuario=request.user)

    form = DietaForm(request.POST or None)
    form.usuario = request.user
    alimentos = Alimento.objects.all()
    if form.is_valid():
        form.save()
        return redirect('list_dietas')
    return render(request, 'dietas/dieta-form.html', {'form': form, 'dieta': dieta, 'alimentos': alimentos})


def update_dieta(request, id):
    alimentos = Alimento.objects.all()
    recomendacoes = Recomendado.objects.all()

    dieta = Dieta.objects.get(id=id)
    alimentos_dieta = dieta.alimentos.all()
    form = DietaForm(request.POST or None, instance=dieta)
    if form.is_valid():
        form.save()
        return redirect('list_dietas')
    return render(request, 'dietas/dieta-form.html', {'form': form, 'dieta': dieta, 'alimentos': alimentos,
                                                      'recomendacoes': recomendacoes,'alimentos_dieta':alimentos_dieta})


def delete_dieta(request, id):
    dieta = Dieta.objects.get(id=id)

    if request.method == "POST":
        print("delete dieta post")
        dieta.delete()
        return redirect('list_minhas_dietas')

    return render(request, 'dietas/confirm-dieta-delete.html', {'dieta': dieta})


def add_alimento_dieta(request, id_alimento, id_dieta):
    print('entrou na funcao')

    alimento = Alimento.objects.get(id=id_alimento)
    dieta = Dieta.objects.get(id=id_dieta)

    dieta.alimentos.add(alimento)

    dieta.save()

    return HttpResponse("foi")


def remove_alimento_dieta(request, id_alimento, id_dieta):
    print('entrou na funcao')

    alimento = Alimento.objects.get(id=id_alimento)
    dieta = Dieta.objects.get(id=id_dieta)

    dieta.alimentos.remove(alimento)

    dieta.save()

    return HttpResponse("foi")


@csrf_protect
def submit_dieta(request):
    if request.POST:
        sexo = request.POST.get('sexo')
        idade = request.POST.get('idade')
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')

        atividade = request.POST.get('atividade')
        atividade_encontrada = Atividade.objects.get(nome=atividade)

        tmb = TMB.objects.create(sexo=sexo, idade=int(idade), peso=int(peso), altura=int(altura), atividade=atividade_encontrada)
        tmb.save()

        nome = request.POST.get('nomeDieta')
        observacao = request.POST.get('observacao')
        user = request.user
        dieta = Dieta.objects.create(nome=nome, observacao=observacao, usuario=user, TMB=tmb)
        dieta.save()

    return redirect('/dietas/update/' + str(dieta.id))
