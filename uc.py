import json
import os
from time import sleep

#TODAS AS FUNÇÕES DOCUMENTADAS

def carregar_dados(arquivo):
    """Carrega o arquivo json dos usuários"""
    try:
        with open(arquivo, 'r') as arquivo:
            #Tenta abrir o arquivo em modo 'r'(leitura)
            dados = json.load(arquivo)
            #Insere as informações do arquivo json em "dados"
            return dados
    except FileNotFoundError:
        #Se o arquivo não for encontrado, ele retornará o arquivo com uma lista em branco no nome informado na variável "arquivo"
        return []

def salvar_dados(arquivo, dados):
    """Salva as informações no arquivo json dos usuários"""
    with open(arquivo, 'w') as arquivo:
        #Abre o arquivo json em modo 'w'(write)
        json.dump(dados, arquivo, indent=4)
        #json é a biblioteca importada,   .dump() é a função que vai jogar da primeira variável, dentro do "arquivo" de usuarios.json, indent=4 é apenas para deixar mais organizado na hora da escrita do arquivo

def cadastrar_usuario():
    """Cadastra um novo usuário a partir dos dados:
    Nome:
    Email:
    Senha:"""
    print("--- Cadastro de Usuário ---")
    usuarios = carregar_dados('usuarios.json')
    #Esse é o primeiro momento em que o arquivo .json é criado, no caso ele irá carregar um dicionários dentro de uma lista "usuarios.json", e caso não exista ele criará.

#Cadastra o nome do usuário
    while True:
        nome = input(str("Digite seu nome e sobrenome: "))
        if nome == '':
            print('Nome não pode estar vazio. Tente novamente.')    
        elif nome.replace(' ', '').isalpha() == False:
            print('Nome deve conter apenas letras. Tente novamente.')
        else:
            break
#Cadastra o Email do usuário
    while True:
        email = input("Digite seu e-mail: ").strip().lower() 
        
        email_existe = False
        for usuario_existente in usuarios:
            if usuario_existente['email'] == email:
                email_existe = True
                break
        if email_existe:
            print("O email já está cadastrado, peço que tente executar o login.")
            return 
        
        if not ('@gmail.com' in email or \
                '@hotmail.com' in email or \
                '@yahoo.com' in email or \
                '@outlook.com' in email or \
                '@ufrpe.br' in email or \
                'ufpe' in email):
            print("Formato de e-mail inválido ou domínio não permitido.")
            continue 
        else:
            break 
#Cadastra a senha
    while True:
        senha = input("Digite sua senha (mínimo 8 caracteres): ").strip()
        if len(senha) < 8:
            print("A senha deve ter no mínimo 8 caracteres.")
            continue 
        confirmar_senha = input("Confirme sua senha: ").strip()
        if senha != confirmar_senha:
            print("As senhas não coincidem. Por favor, tente novamente.")
            continue 
        else:
            break 

#Cadastra o id do usuário
    novo_id = len(usuarios)
#Cria uma lista com as informações do usuário
    novo_usuario = {
        'id': novo_id,
        'nome': nome,
        'email': email,
        'senha': senha
    }
#Adiciona o usuário que foi cadastrado no "usuários json."
    usuarios.append(novo_usuario)
    salvar_dados('usuarios.json', usuarios) # Salva a lista atualizada
    print("Usuário cadastrado com sucesso!")
    print('\n')

def fazer_login():
    """Comando para fazer login do usuário.
    Informações requisitadas:
    email:
    senha:
    
    As informações devem estar presentes no id de algum usuário do "Usuários.json" """

    print("--- Login de Usuário ---")
    #Carrega os dados dos usuários presentes no "usuários.json" para validar as informações.
    usuarios = carregar_dados('usuarios.json')

    email_digitado = input("Digite seu e-mail: ")
    senha_digitada = input("Digite sua senha: ")

#Verifica se o email digitado e a senha correspondem a algum usuário existente
    for usuario in usuarios:
        if usuario['email'] == email_digitado and usuario['senha'] == senha_digitada:
            print(f"---Login bem-sucedido---")
            return usuario # Retorna o dicionário do usuário que as informações correspondem
        print('\n')
    print("E-mail ou senha incorretos.")
    print('\n')
    sleep(1)
    return None # Retorna nada se o login falhar