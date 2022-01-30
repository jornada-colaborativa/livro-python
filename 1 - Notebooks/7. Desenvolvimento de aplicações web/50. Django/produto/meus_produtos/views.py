from django.shortcuts import render, redirect, get_object_or_404
from meus_produtos.models import Produto
from .forms import cadastroForm


def lista_produtos(request):
    query_set_produtos = Produto.objects.all()
    return render(
        request, 'listagem_produtos.html',
        {'produto': query_set_produtos}
    )

def cadastra_produtos(request):
    if request.method == "POST":
        formulario = cadastroForm(request.POST)
        if formulario.is_valid():
            objeto = formulario.save()
            objeto.save()
            formulario = cadastroForm()
    else:
        formulario = cadastroForm(request.POST)
    return render(request, 'cadastra_produtos.html',{'formulario': formulario})
	
def editar_produtos(request, id):
    produto_para_editar = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        formulario = cadastroForm(request.POST, instance=produto_para_editar)
        if formulario.is_valid():
            objeto = formulario.save()
            objeto.save()
            formulario = cadastroForm()
            return redirect('listagem')
    else:
        formulario = cadastroForm(instance=produto_para_editar)
    return render(request, 'cadastra_produtos.html', {'formulario': formulario})

def excluir_produtos(request, id):
    produto_para_excluir = get_object_or_404(Produto, id=id)
    produto_para_excluir.delete()
    return redirect('listagem')