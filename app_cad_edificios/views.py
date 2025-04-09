from django.shortcuts import render, redirect
from .models import Edificio
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from .models import Mensagem


def never_cache_view(view_func):
    return never_cache(view_func)


@login_required
@never_cache
def fazer_logout(request):
    logout(request)
    return redirect('/auth/login/')

@login_required
@never_cache
def minha_view(request):
    context = {
        'user': request.user,  # Passa o objeto usuário para o template
    }
    return render(request, 'base.html', context)

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def sadm(request):
    return render(request, 'edificios/sadm.html')

@login_required
@never_cache
def home(request):
    return render(request, 'edificios/home.html')

@login_required
@never_cache
def pesquisa(request):
    resultados = []
    if request.method == 'POST':
        termo_busca = request.POST.get('search')
        resultados = Edificio.objects.filter(nome__icontains=termo_busca)
        print(resultados) #imprime os resultados no terminal
    return render(request, 'edificios/pesquisa.html', {'resultados': resultados})

@login_required
@never_cache
def edificios(request):
    if request.method == 'POST':
        # salvar os dados da tela para o banco de dados
        novo_edificio = Edificio()
        novo_edificio.nome = request.POST.get('nome')
        novo_edificio.tipo = request.POST.get('tipo')
        novo_edificio.saturado = request.POST.get('saturado')
        novo_edificio.fac = request.POST.get('fac')
        novo_edificio.save()

        # Redireciona para a página de pesquisa após o cadastro
        return redirect('pesquisa')

    # exibir a lista de edifícios (para requisições GET)
    edificios_list = Edificio.objects.all()
    context = {
        'edificios': edificios_list
    }
    return render(request, 'edificios/edificios.html', context)

def apagar_edificio(request, id_edificio):
    """
    View para apagar um edifício.
    """
    edificio = get_object_or_404(Edificio, id_edificio=id_edificio)  # Use o nome correto do seu campo ID

    if request.method == 'POST':
        edificio.delete()
        return redirect('listar_edificios')  # Redirecione para a página de listagem (ajuste o nome)
    else:
        # Se quiser uma confirmação em outra página (opcional)
        context = {'edificio': edificio}
        return render(request, 'edificios/confirmar_apagar.html', context)

# Certifique-se de ter uma view para listar os edifícios, por exemplo:
def listar_edificios(request):
    edificios = Edificio.objects.all()
    return render(request, 'edificios/lista_edificios.html', {'edificios': edificios})

@login_required
def chat_usuario(request):
    if request.method == 'POST':
        texto = request.POST.get('mensagem')
        if texto:
            Mensagem.objects.create(usuario=request.user, texto=texto)
            return redirect('chat_usuario')
    return render(request, 'chat/chat_usuario.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def chat_admin(request):
    mensagens = Mensagem.objects.all().order_by('-data_envio')
    return render(request, 'chat/chat_admin.html', {'mensagens': mensagens})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def excluir_mensagem(request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, id=mensagem_id)
    mensagem.delete()
    return redirect('chat_admin')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def chat_admin(request):
    mensagens = Mensagem.objects.all().order_by('-data_envio')
    return render(request, 'chat/chat_admin.html', {'mensagens': mensagens})
