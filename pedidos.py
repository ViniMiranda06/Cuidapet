import json
import os
from time import sleep
import ac
import pedidos

def carregar_dados(arquivo):
    """Carrega o arquivo json dos animais"""
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
    """Salva as informações no arquivo json dos animais"""
    with open(arquivo, 'w') as arquivo:
        #Abre o arquivo json em modo 'w'(write)
        json.dump(dados, arquivo, indent=6)
        #json é a biblioteca importada, .dump() é a função que vai jogar da primeira variável, dentro do "arquivo" de animais.json, indent=6 é apenas para deixar mais organizado na hora da escrita do arquivo

def enviar_pedido_adocao(usuario_logado):
    animais_adocao = ac.carregar_dados('animais_adocao.json')
    while True:
        if not animais_adocao:
            print("Não há animais disponíveis para adoção no momento.")
            sleep(2)
            return

        id_animal = input ("Informe o id que gostaria de adotar (Digite VOLTAR para ir ao menu principal): ")
        if id_animal.upper() == "VOLTAR":
            return

        if id_animal.isdigit() == False:
            print("Insira apenas números")
            continue
        else:
            id_animal = int(id_animal)

        animal_selecionado = None
        for animal_lista in animais_adocao:
            if animal_lista.get('id') == id_animal:
                animal_selecionado = animal_lista
                break

        if animal_selecionado is None:
            print(" O ID digitado não corresponde a nenhum animal disponível para adoção.")
            sleep(2)
            continue

        nome_animal = animal_selecionado.get('nome') 

        print("\n--- Enviar Pedido de Adoção ---") 
        while True:
            confirmacao = input(str(f"Tem certeza que deseja fazer um pedido de adoção para o animal ID {id_animal}? (S/N): ")).strip().upper()
            if confirmacao == 's':
                break
            elif confirmacao == 'n':
                print("Pedido de adoção cancelado.")
                sleep(2)
                return
            else:
                print("Resposta inválida. Digite 'S' para sim ou 'N' para não.")
                sleep(1)
        sleep(1)
        print("\n--- Escreva seu Pedido de Adoção ---")
        print("--------------------------------------------------")
        print("Modelo Sugerido:")
        print("--------------------------------------------------")
        print("""Bom dia, gostaria de adotar um animal, seu id é XX,
para entrar em contato comigo use meu email, ou meu
telefone: (81) 9.1234-5678""")
        sleep(2)

        mensagem = input(str("Digite sua mensagem, siga o modelo se preferir: (apenas aperte ENTER quando digitar toda mensagem) ")).strip()
        while not mensagem:
            print("A mensagem não pode estar vazia. Por favor, digite seu pedido.")
            mensagem = input(str("Sua mensagem: ")).strip()

        pedidos = carregar_dados('pedidos.json')

        id_mensagem = 0
        if pedidos:
            maior_id_atual = -1 
            for pedido_existente in pedidos:
                if pedido_existente['id_mensagem'] > maior_id_atual:
                    maior_id_atual = pedido_existente['id_mensagem']
            id_mensagem = maior_id_atual + 1

        novo_pedido = {
            'id_mensagem': id_mensagem,
            'nome_animal': nome_animal,
            'id_animal_adotado': id_animal,
            'nome_solicitante': usuario_logado['nome'],
            'email_solicitante': usuario_logado['email'],
            'mensagem_pedido': mensagem
        }

        pedidos.append(novo_pedido)
        salvar_dados('pedidos.json', pedidos)
        
        print("\nPedido de adoção enviado com sucesso!")
        print("Entraremos em contato em breve através do e-mail fornecido.")
        sleep(2)
        return