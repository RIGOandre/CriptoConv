from flask import Blueprint, render_template, request, redirect, url_for

usuarios_route = Blueprint('usuarios', __name__)

# Simulação de usuários para testes
USUARIOS = [
    {"id": 1, "nome": "andré", "email": "andre@gmail.com"}
]

# Rota para a página de login e cadastro
@usuarios_route.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']
        # Lógica de autenticação
        for usuario in USUARIOS:
            if usuario['nome'] == nome:  # Simulação simples de autenticação
                return redirect(url_for('usuarios.conversor'))  # Redireciona para a página do conversor após login
        return "Usuário não encontrado!"  # Simples mensagem de erro
    return render_template('login.html')

@usuarios_route.route('/cadastro', methods=['POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']
        # Lógica de cadastro
        novo_usuario = {"id": len(USUARIOS) + 1, "nome": nome, "email": f"{nome}@gmail.com"}
        USUARIOS.append(novo_usuario)
        return redirect(url_for('usuarios.conversor'))  # Redireciona para a página do conversor após cadastro
    return render_template('login.html')  # Retorna ao login em caso de erro

# Rota para a página do conversor
@usuarios_route.route('/conversor')
def conversor():
    return render_template('conversor.html')

@usuarios_route.route('/mercado')
def mercado():
    return render_template('mercado.html')

@usuarios_route.route('/carteira')  
def carteira():
    return render_template('carteira.html')