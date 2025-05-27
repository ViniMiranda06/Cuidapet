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
    print("\n--- Atualizar Perfil ---")
    
    usuarios = uc.carregar_dados('usuarios.json')
    
    indice_usuario_na_lista = -1
    for i, user in enumerate(usuarios):
        if user['id'] == usuario_logado['id']:
            indice_usuario_na_lista = i
            break
    
    if indice_usuario_na_lista == -1:
        print("Erro: Seu perfil não foi encontrado na base de dados. Por favor, faça login novamente.")
        sleep(2)
        return usuario_logado

    usuario_para_atualizar = usuarios[indice_usuario_na_lista] 

    print(f"\nNome atual: {usuario_para_atual['nome']}")
    novo_nome = input("Digite o novo nome (ou ENTER para manter): ").strip()
    if novo_nome:
        while True:
            if not novo_nome.replace(' ', '').isalpha():
                print('Nome deve conter apenas letras. Tente novamente.')
                novo_nome = input("Digite o novo nome: ").strip()
            else:
                usuario_para_atual['nome'] = novo_nome
                break
    
    print(f"\nE-mail atual: {usuario_para_atual['email']}")
    while True:
        novo_email = input("Digite o novo e-mail (ou ENTER para manter): ").strip().lower()
        if not novo_email:
            break
        
        email_ja_existe_por_outro = False
        for user_existente in usuarios:
            if user_existente['email'] == novo_email and user_existente['id'] != usuario_para_atual['id']:
                email_ja_existe_por_outro = True
                break
        
        if email_ja_existe_por_outro:
            print("Este e-mail já está em uso por outro usuário. Por favor, digite outro e-mail.")
            continue
        
        dominios_validos = ['@gmail.com', '@hotmail.com', '@yahoo.com', '@outlook.com', '@ufrpe.br']
        
        email_valido_dominio = False
        if '@' in novo_email:
            for dominio in dominios_validos:
                if dominio in novo_email:
                    email_valido_dominio = True
                    break
            if 'ufpe' in novo_email and not email_valido_dominio:
                 email_valido_dominio = True


        if not email_valido_dominio:
            print("Formato de e-mail inválido ou domínio não permitido. Por favor, digite um e-mail válido (ex: @gmail.com, @ufrpe.br, etc.).")
            continue
        
        usuario_para_atualizar['email'] = novo_email
        break

    print("\n--- Atualizar Senha ---")
    print("Deixe em branco para manter a senha atual.")
    while True:
        nova_senha = input("Digite a nova senha (mínimo 8 caracteres): ").strip()
        if not nova_senha:
            break
        
        if len(nova_senha) < 8:
            print("A senha deve ter no mínimo 8 caracteres.")
            continue
        
        confirmar_nova_senha = input("Confirme a nova senha: ").strip()
        if nova_senha != confirmar_nova_senha:
            print("As senhas não coincidem. Por favor, tente novamente.")
            continue
        
        usuario_para_atualizar['senha'] = nova_senha
        break

    uc.salvar_dados('usuarios.json', usuarios)
    
    print("\nPerfil atualizado com sucesso!")
    sleep(2)
    
    return usuario_para_atual