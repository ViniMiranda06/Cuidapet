import uc
import menus
import ac
from time import sleep

def ver_perfil(usuario_logado): #Considera como parâmetro o dicionário do usuário logado
    """
    Exibe o nome e e-mail do usuário logado."""

    print("\n--- Seus dados ---")
    print(f"Nome: {usuario_logado.get('nome', 'Não informado')}") # Imprime o nome do usuário logado
    print(f"E-mail: {usuario_logado.get('email', 'Não informado')}") # Imprime o e-mail do usuário logado
    sleep(2)
    print("-" * 20)
    input("Pressione ENTER para voltar ao menu.")

def atualizar_perfil(usuario_logado):
    print('\n--- Atualizar Perfil ---')
    
    arquivo_usuario = uc.carregar_dados('usuarios.json')
    
    print(f"\nNome atual: {usuario_logado['nome']}")
    while True:
        novo_nome = input(str("Digite o novo nome (ou ENTER para manter): ")).strip()
        if not novo_nome:
            break
        elif not novo_nome.replace(' ', '').isalpha():
            print('Nome deve conter apenas letras. Tente novamente.')
        else:
            usuario_logado['nome'] = novo_nome
            break
    
    print(f"\nE-mail atual: {usuario_logado['email']}")
    while True:
        novo_email = input(str("Digite o novo e-mail (ou ENTER para manter): ")).strip().lower()
        if not novo_email:
            break
        
        email_existe = False
        for usuario_id in arquivo_usuario:
            if usuario_id['email'] == novo_email and usuario_id['id'] != usuario_logado['id']:
                email_existe = True
                break
        
        if email_existe:
            print('Este e-mail já está em uso por outro usuário. Por favor, digite outro e-mail.')
            continue
        
        if not ('@gmail.com' in novo_email or \
                '@hotmail.com' in novo_email or \
                '@yahoo.com' in novo_email or \
                '@outlook.com' in novo_email or \
                '@ufrpe.br' in novo_email or \
                'ufpe' in novo_email):
            print('Formato de e-mail inválido ou domínio não permitido. Por favor, digite um e-mail válido (ex: @gmail.com, @ufrpe.br, etc.).')
            continue
        else:
            usuario_logado['email'] = novo_email
            break

    print('\n--- Atualizar Senha ---')
    print('Deixe em branco para manter a senha atual.')
    while True:
        nova_senha = input(str("Digite a nova senha (mínimo 8 caracteres): ")).strip()
        if not nova_senha:
            break
        
        if len(nova_senha) < 8:
            print('A senha deve ter no mínimo 8 caracteres.')
            continue
        
        confirmar_nova_senha = input(str("Confirme a nova senha: ")).strip()
        if nova_senha != confirmar_nova_senha:
            print('As senhas não coincidem. Por favor, tente novamente.')
            continue
        
        usuario_logado['senha'] = nova_senha
        break

    novo_arquivo_usuarios = []
    for usuarios in arquivo_usuario:
        if usuarios['id'] != usuario_logado['id']:
            novo_arquivo_usuarios.append(usuarios)
    
    novo_arquivo_usuarios.append(usuario_logado)
        
    uc.salvar_dados('usuarios.json', novo_arquivo_usuarios)
    
    print('\nPerfil atualizado com sucesso!')
    sleep(2)
    
    return usuario_logado