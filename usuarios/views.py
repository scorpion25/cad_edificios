from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

def cadastro(request):
    """
    Exibe o formulário de cadastro para novos usuários (GET) ou processa o
    envio do formulário para criar um novo usuário (POST).
    """
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User.objects.filter(username=username).exists():
            return render(request, 'cadastro.html', {'error_username': 'Usuário já cadastrado!'})

        if User.objects.filter(email=email).exists():
            return render(request, 'cadastro.html', {'error_email': 'Este email já está cadastrado!'})

        user = User.objects.create_user(username=username, email=email, password=senha)
        # Redireciona para a página de login após o cadastro bem-sucedido
        return redirect('login')

def user_login(request):
    """
    Exibe o formulário de login (GET) ou processa a autenticação do usuário (POST).
    Se a autenticação for bem-sucedida, redireciona para a página de pesquisa para usuários normais
    e para /sadm/ para superusuários.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                return redirect('/sadm/')  # Redireciona superusuários para /sadm/
            else:
                return redirect('pesquisa')  # Redireciona usuários normais para a pesquisa
        else:
            return render(request, 'login.html', {'error': 'Nome de usuário ou senha inválidos'})
    return render(request, 'login.html')
