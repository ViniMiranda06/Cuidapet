#importando 
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
    """
    Permite que o usuário logado atualize seu nome, e-mail e senha.

    Valida se o novo nome contém apenas letras, verifica se o novo e-mail está disponível
    e possui domínio permitido, e garante que a nova senha tenha no mínimo 8 caracteres.
    Se nenhum campo for alterado, os dados permanecem os mesmos.

    Atualiza o arquivo 'usuarios.json' com as novas informações.

    Parâmetros:
        usuario_logado (dict): Dicionário contendo os dados do usuário atualmente logado.

    Retorna:
        dict: Dicionário atualizado do usuário.
    """
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

def deletar_conta(usuario_logado):
    """
    Exclui permanentemente a conta do usuário logado após confirmação da senha e consentimento.

    Requer que a senha atual seja informada corretamente. Em seguida, solicita confirmação
    do usuário para excluir a conta. Caso confirmado, remove o usuário do arquivo 'usuarios.json'.

    Parâmetros:
        usuario_logado (dict): Dicionário contendo os dados do usuário atualmente logado.

    Retorna:
        bool: True se a conta foi excluída com sucesso, False caso contrário.
    """
    print('\n--- Excluir Conta ---')
    
    senha = input(str("Digite sua senha para confirmar a exclusão da conta: ")).strip()
    if senha != usuario_logado['senha']:
        print('Senha incorreta. Exclusão de conta cancelada.')
        sleep(2)
        return False
    
    while True:
        confirmacao = input(str("Tem certeza que deseja EXCLUIR PERMANENTEMENTE sua conta? (S/N): ")).strip().lower()
        if confirmacao == 's':
            break
        elif confirmacao == 'n':
            print('Exclusão de conta cancelada.')
            sleep(2)
            return False
        else:
            print('Resposta inválida. Por favor, digite "s" para sim ou "n" para não.')
            sleep(1)

    arquivo_usuario = uc.carregar_dados('usuarios.json')
    
    novo_arquivo_usuarios = []
    for usuarios in arquivo_usuario:
        if usuarios['id'] != usuario_logado['id']:
            novo_arquivo_usuarios.append(usuarios)
    
    uc.salvar_dados('usuarios.json', novo_arquivo_usuarios)
    
    print('\nSua conta foi excluída com sucesso. Você será deslogado.')
    sleep(2)
    return True