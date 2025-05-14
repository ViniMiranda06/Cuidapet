import json
import os

# --- DADOS GLOBAIS ---
usuarios = []
usuario_logado = None
ARQUIVO_USUARIOS = 'usuarios.json'

# --- ARTES ASCII (mantidas exatamente como no original) ---
PATA = '''
­
         %%%%     %%%%%%        
        %%%%%%%  %%%%%%%%       
        %%%%%%%  %%%%%%%%       
       %%%%%%%%%%%%%%%%%%       
        %%%%%%%%%%%%%%%%%       
 %%%%%%  %%%%%%  %%%%%%%   %%%% 
%%%%%%%%% %%%     %%%%% %%%%%%%%
%%%%%%%%%%              %%%%%%%%
 %%%%%%%%% %%%%%%%%%%  %%%%%%%%%
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
   %%%%%%%%%%%%%%%%%%%%%%%%%%%  
        %%%%%%%%%%%%%%%%%%      
       %%%%%%%%%%%%%%%%%%%%     
      %%%%%%%%%%%%%%%%%%%%%     
      %%%%%%%%%%%%%%%%%%%%%%    
      %%%%%%%%%%%%%%%%%%%%%%    
        %%%%%%%    %%%%%%%%     
­
'''.strip().split('\n')

NOME_PATAS = '''
­                         
    @@@@@@@@@@@@@@@@         @@@@@@       @@@@@@@@@@@@@@@@@@            @@@@@@              @@@@@@@@@@           
     @@@@@@@@@@@@@@@     @@@@@@@@@@       @@@@@@@@@@@@@@@@@@        @@@@@@@@@@            @@@@@@@@@@@@@            
     @@@@@@@@@@@@@@@     @@@@@@@@@@        @@@@@@@@@@@@@@@@@        @@@@@@@@@@            @@@@@@@@@@@@             
      @@@@@   @@@@@@      @@@@@@@@@@       @@@@@@@@@@@@@@@@@@       @@@@@@@@@@@          @@@@@@@@@              
      @@@@@  @@@@@@@      @@@@@@@@@@       @@@   @@@@@@ @@@@         @@@@@@@@@@          @@@@@@@              
      @@@@@@@@@@@@        @@@@@@@@@@             @@@@@@              @@@@@@@@@@          @@@@@@@@@@@@@@            
       @@@@@@@@@@         @@@@  @@@@@@@          @@@@@@              @@@@ @@@@@@@@       @@@@@@@@@@@@@@            
       @@@@@@@@           @@@@ @@@@@@@@           @@@@@@             @@@@ @@@@@@@@              @@@@@@@@            
        @@@@@@            @@@@@@@@@@@             @@@@@@             @@@@@@@@@@@                    @@@@@@@           
        @@@@@             @@@@@@@@@@@@            @@@@@@@            @@@@@@@@@@@@                 @@@@@@@           
        @@@@@            @@@@@@@@@@@@@@           @@@@@@@           @@@@@@@@@@@@@@          @@@@@@@@@@@@           
        @@@@@@          @@@@@@@  @@@@@@@           @@@@@@          @@@@@@@  @@@@@@@           @@@@@@@@@            
        @@@@@@          @@@@@@    @@@@@            @@@@@@@         @@@@@@    @@@@@             @@@@@@@                                                                                      
­
'''.strip().split('\n')

# --- FUNÇÕES PRINCIPAIS ---
def carregar_usuarios():
    global usuarios
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r') as f:
            usuarios = json.load(f)

def salvar_usuarios():
    with open(ARQUIVO_USUARIOS, 'w') as f:
        json.dump(usuarios, f, indent=2)

def email_existe(email):
    return any(u['email'] == email for u in usuarios)

def criar_usuario(nome, email, senha):
    if email_existe(email):
        print("\nE-mail já cadastrado. Redirecionando para login...")
        return None
    
    novo_usuario = {
        'id': max((u['id'] for u in usuarios), default=0) + 1,
        'nome': nome,
        'email': email,
        'senha': senha
    }
    
    usuarios.append(novo_usuario)
    salvar_usuarios()
    print(f"\nUsuário '{nome}' criado com sucesso!")
    return novo_usuario

def login(email, senha):
    global usuario_logado
    usuario = next((u for u in usuarios if u['email'] == email and u['senha'] == senha), None)
    
    if usuario:
        usuario_logado = usuario
        print(f"\nBem-vindo(a), {usuario['nome']}!")
        return True
    
    print("\nE-mail ou senha incorretos.")
    return False

def ver_perfil():
    if not usuario_logado:
        print("\nNenhum usuário logado.")
        return
    
    print("\n=== SEU PERFIL ===")
    print(f"ID: {usuario_logado['id']}")
    print(f"Nome: {usuario_logado['nome']}")
    print(f"E-mail: {usuario_logado['email']}")

def atualizar_perfil():
    if not usuario_logado:
        print("\nVocê precisa estar logado.")
        return
    
    novo_nome = input("\nNovo nome (deixe em branco para manter): ").strip()
    nova_senha = input("Nova senha (deixe em branco para manter): ").strip()
    
    if novo_nome:
        usuario_logado['nome'] = novo_nome
    if nova_senha:
        usuario_logado['senha'] = nova_senha
    
    salvar_usuarios()
    print("\nPerfil atualizado com sucesso!")

def deletar_conta():
    global usuarios, usuario_logado
    if not usuario_logado:
        print("\nNenhum usuário logado.")
        return
    
    confirm = input("\nTem certeza? (s/n): ").lower()
    if confirm == 's':
        usuarios = [u for u in usuarios if u['id'] != usuario_logado['id']]
        salvar_usuarios()
        print(f"\nConta de {usuario_logado['nome']} excluída.")
        usuario_logado = None
        return True
    return False

# --- INTERFACE ---
def mostrar_tela_inicial():
    for arte in (PATA, NOME_PATAS):
        for linha in arte:
            print(linha.center(100))
    print("\nBem-vindo ao P.A.T.A.S (Plataforma de Apoio ao Tratamento e Adoção Solidária)")

def tela_inicial():
    while True:
        mostrar_tela_inicial()
        print("\nO que deseja fazer?")
        print("[1] - Cadastrar Usuário\n[2] - Login")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            nome = input('\nDigite seu nome: ')
            if not nome.replace(' ', '').isalpha():
                print('\nDigite apenas letras e espaços')
                continue
            
            email = input("Digite seu e-mail: ")
            
            if email_existe(email):
                print("\nEste e-mail já está cadastrado. Vamos direcionar você para o login.")
                if login(input("E-mail: "), input("Senha: ")):
                    menu()
                continue
            
            senha = input("Digite sua senha: ")
            usuario = criar_usuario(nome, email, senha)
            
            if usuario:
                global usuario_logado
                usuario_logado = usuario
                print(f"\nCadastro realizado! Bem-vindo(a), {nome}!")
                menu()
        
        elif opcao == "2":
            if login(input("\nE-mail: "), input("Senha: ")):
                menu()
        
        else:
            print("\nOpção inválida! Por favor, Selecione uma opção válida.")
            input("Pressione Enter para continuar...")

def menu():
    while usuario_logado:
        print("\n=== MENU ===")
        print("1. Ver perfil")
        print("2. Atualizar perfil")
        print("3. Excluir conta")
        print("4. Sair")
        
        opcao = input("\nOpção: ")
        
        if opcao == '1':
            ver_perfil()
        elif opcao == '2':
            atualizar_perfil()
        elif opcao == '3':
            if deletar_conta():
                break
        elif opcao == '4':
            break

# --- EXECUÇÃO ---
if __name__ == "__main__":
    carregar_usuarios()
    tela_inicial()