from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Pessoa

from .forms import PessoaForm

def testeview(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'temp1/index.html', {'pessoas': pessoas})


def testeadd(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        pessoa = form.save()
        pessoa.save()
        return redirect('/')
    else:
        form = PessoaForm()
        return render(request, 'temp1/add.html', {'form': form})


# Create your views here.
