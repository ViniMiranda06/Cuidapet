import json
import os
from time import sleep

#TODAS AS FUNÇÕES DOCUMENTADAS

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

def cadastrar_animal():
    """Cadastra um novo animal a partir dos dados:
    Nome:
    Espécie:
    Sexo:
    Idade: ex: 8 meses ou 2 anos
    Outras informações e caraterísticas"""
    print("--- Cadastro de animais ---")

    # Dependendo da resposta do "tipo_cadastro" o animal será posto em 2 arquivos json diferentes, um pra animais em adoção e outro pra animais em tratamento
    while True:
        tipo_cadastro = input("Cadastrar animal para 'tratamento' ou 'adocao'? ").strip().lower()
        if tipo_cadastro == 'tratamento':
            nome_arquivo = 'animais_tratamento.json'
            break
        elif tipo_cadastro == 'adocao':
            nome_arquivo= 'animais_adocao.json'
            break
        else:
            print("Opção inválida. Por favor, digite 'tratamento' ou 'adocao'.")
            sleep(1)

    animais = carregar_dados(nome_arquivo)
    #Esse é o primeiro momento em que o arquivo .json é criado, no caso ele irá carregar um dicionários dentro de uma lista "animais.json_tramento/adoção", e caso não exista ele criará.

#Cadastra o nome do animal
    while True:
        nome = input(str("Digite o nome ou apelido do pet: "))
        if nome == '':
            print('Nome não pode estar vazio. Tente novamente.')
        elif nome.replace(' ', '').isalnum() == False:
            print('Nome deve conter apenas letras e espaços. Tente novamente.')
        else:
            break
#Cadastra a espécie do animal
    while True:
        especie = input("Digite a espécie do animal (Exemplo: Cão Doméstico (Canis lupus familiaris) ou apenas 'gato'): ").strip()
        if especie == '':
            print('A espécie não pode estar vazia. Tente novamente.')
        elif especie.replace(' ', '').isalnum() == False:
            print('A espécie deve conter apenas letras, números e parênteses. Tente novamente.')
        else:
            break

#Cadastra o sexo do animal
    while True:
        sexo = str(input('Informe o sexo do animal [M/F]: ')).strip().upper()[0]
        if sexo != 'M' and sexo != "F":
            print('Digite um valor válido. Tente novamente.')
        else:
            break

#Cadastra a idade do animal
    while True:
        idade = str(input("Digite a idade do animal (Ex: 8 meses, 2 Anos ou 2 anos e 8 meses)): ")).strip()
        if idade == '':
            print('A idade não pode estar vazia. Tente novamente.')
        elif idade.replace(' ', '').isalnum() == False:
            print('A idade deve conter apenas letras e números. Tente novamente.')
        else:
            break

#Cadastra outras informações
    info = str(input("Insira informações sobre o animal, tramento, castração etc. Caso não queria, apenas aperte a tecla ENTER: ")).strip()
    # Não há loop while True nem validação de conteúdo. Aceita o que for digitado ou vazio.

#Cadastra o id do animal
    maior_id = -1 # Começa com -1 para garantir que o primeiro ID seja 0 se a lista estiver vazia
    for id in animais: # Percorre a lista para encontrar o maior ID
        if id['id'] > maior_id:
            maior_id = id['id']
#Cria uma lista com as informações do animal
    novo_animal = {
        'id': maior_id,
        'nome': nome,
        'sexo': sexo,
        'especie': especie,
        'idade': idade,
        'informacões': info # Usando a chave 'informações'
    }
#Adiciona o animal que foi cadastrado
    animais.append(novo_animal)
    salvar_dados(nome_arquivo, animais) # Salva no arquivo correto
    print('\n')
    print("PET cadastrado com sucesso!")
    print("|||Caso deseje editar alguma informação, isso será possível no menu de opções administrativas|||")
    print('\n')

def lista_animais_tratamento():
    """ Imprime os animais que estão em processo de tratamento."""
    print("\n--- Animais em Processo de Tratamento ---")
    animais_tratamento = carregar_dados('animais_tratamento.json') # Carrega os dados do arquivo 'animais_tratamento.json'

    if not animais_tratamento: #Caso não jaka animais em tratamento, ele irá imprimir a mensagem abaixo
        print("Não há animais cadastrados em tratamento no momento.")
        sleep(2)
        return

    for animal in animais_tratamento: #Imprime uma lista com os animais em tratamento
        print("-" * 30)
        print(f"ID: {animal.get('id')}")
        print(f"Nome: {animal.get('nome')}")
        print(f"Espécie: {animal.get('especie')}")
        print(f"Sexo: {animal.get('sexo')}")
        print(f"Idade: {animal.get('idade')}")
        if animal.get('informações'):
            print(f"Informações: {animal.get('informações')}")
        print("-" * 30)
    sleep(3)

def lista_animais_adocao():
    """ Imprime os animais que estão em processo de adoçao."""
    print("\n--- Animais em Processo de Adoção ---")
    animais_adocao = carregar_dados('animais_adocao.json') # Carrega os dados do arquivo 'animais_adocao.json'

    if not animais_adocao: #Caso não jaka animais em tratamento, ele irá imprimir a mensagem abaixo
        print("Não há animais cadastrados em adoção no momento.")
        sleep(2)
        return

    for animal in animais_adocao: #Imprime uma lista com os animais em tratamento
        print("-" * 30)
        print(f"ID: {animal.get('id')}")
        print(f"Nome: {animal.get('nome')}")
        print(f"Espécie: {animal.get('especie')}")
        print(f"Sexo: {animal.get('sexo')}")
        print(f"Idade: {animal.get('idade')}")
        if animal.get('informações'):
            print(f"Informações: {animal.get('informações')}")
        print("-" * 30)
    sleep(3)

def editar_animal_adocao():
    print(f"\n--- Editar Animal para Adoção ---")

    nome_arquivo = 'animais_adocao.json'
    animais_da_lista = carregar_dados(nome_arquivo)
    
    if not animais_da_lista:
        print(f"Não há animais para adoção para editar.")
        sleep(2)
        return

    id_animal = None
    animal_novo = None

    while True:
        id_animal = input(str(f"Digite o ID do animal para adoção que deseja editar (ou 'VOLTAR' para cancelar): ")).strip().lower()
        if id_animal == 'voltar':
            print("Operação de edição cancelada.")
            sleep(1)
            return

        id_animal_editar = id_animal
        for animal in animais_da_lista:
            if animal.get('id') == id_animal_editar:
                animal_para_atualizar = animal
                break
            else:
                print("Informe um ID existente")
                continue
    
        print("\n--- Informações Atuais ---")
        print(f"ID: {animal_para_atualizar.get('id')}")
        print(f"Nome: {animal_para_atualizar.get('nome')}")
        print(f"Espécie: {animal_para_atualizar.get('especie')}")
        print(f"Sexo: {animal_para_atualizar.get('sexo')}")
        print(f"Idade: {animal_para_atualizar.get('idade')}")
        print(f"Informações: {animal_para_atualizar.get('informacões')}")

        print("\n--- Digite o novo valor ou deixe em branco para manter o atual ---")
        while True:
            novo_nome = input("Nome: ").strip()
            if not novo_nome:
                break
            elif novo_nome.replace(' ', '').isalnum() == False:
                print('Nome deve conter apenas letras e espaços. Tente novamente.')
            else:
                animal_para_atualizar['nome'] = novo_nome
                break

        while True:
            nova_especie = input("Espécie: ").strip()
            if not nova_especie:
                break
            elif nova_especie.replace(' ', '').isalnum() == False:
                print('A espécie deve conter apenas letras, números e parênteses. Tente novamente.')
            else:
                animal_para_atualizar['especie'] = nova_especie
                break

        while True:
            novo_sexo = input("Sexo [M/F]: ").strip().upper()
            if not novo_sexo:
                break
            elif novo_sexo not in ('M', 'F'):
                print('Digite um valor válido (M ou F). Tente novamente.')
            else:
                animal_para_atualizar['sexo'] = novo_sexo
                break

        while True:
            nova_idade = input("Idade: ").strip()
            if not nova_idade:
                break
            elif nova_idade.replace(' ', '').isalnum() == False:
                print('A idade deve conter apenas letras e números. Tente novamente.')
            else:
                animal_para_atualizar['idade'] = nova_idade
                break

        nova_info = input("Informações: ").strip()
        if nova_info:
            animal_para_atualizar['informacões'] = nova_info

        salvar_dados(nome_arquivo, animais_da_lista)
        
        print('\nAnimal atualizado com sucesso!')
        sleep(2)

def editar_animal_tratamento():
    print(f"\n--- Editar Animal em Tratamento ---")

    nome_arquivo = 'animais_tratamento.json'
    animais_da_lista = carregar_dados(nome_arquivo)
    
    if not animais_da_lista:
        print(f"Não há animais em tratamento para editar.")
        sleep(2)
        return

    animal_para_atualizar = None

    while True:
        id_input_str = input(str(f"Digite o ID do animal em tratamento que deseja editar (ou 'VOLTAR' para cancelar): ")).strip().lower()
        if id_input_str == 'voltar':
            print("Operação de edição cancelada.")
            sleep(1)
            return

        try:
            id_animal_editar = int(id_input_str)
        except ValueError:
            print("ID inválido. Por favor, digite um número.")
            sleep(1)
            continue
            
        animal_encontrado_nesta_iteracao = None
        for animal in animais_da_lista:
            if animal.get('id') == id_animal_editar:
                animal_encontrado_nesta_iteracao = animal
                break
        
        if animal_encontrado_nesta_iteracao:
            animal_para_atualizar = animal_encontrado_nesta_iteracao
            break
        else:
            print(f"ID {id_animal_editar} não encontrado na lista de tratamento. Tente novamente.")
            sleep(1)
            
    print("\n--- Informações Atuais ---")
    print(f"ID: {animal_para_atualizar.get('id')}")
    print(f"Nome: {animal_para_atualizar.get('nome')}")
    print(f"Espécie: {animal_para_atualizar.get('especie')}")
    print(f"Sexo: {animal_para_atualizar.get('sexo')}")
    print(f"Idade: {animal_para_atualizar.get('idade')}")
    print(f"Informações: {animal_para_atualizar.get('informacões')}")

    print("\n--- Digite o novo valor ou deixe em branco para manter o atual ---")
    while True:
        novo_nome = input("Nome: ").strip()
        if not novo_nome:
            break
        elif novo_nome.replace(' ', '').isalnum() == False:
            print('Nome deve conter apenas letras e espaços. Tente novamente.')
        else:
            animal_para_atualizar['nome'] = novo_nome
            break

    while True:
        nova_especie = input("Espécie: ").strip()
        if not nova_especie:
            break
        elif nova_especie.replace(' ', '').isalnum() == False:
            print('A espécie deve conter apenas letras, números e parênteses. Tente novamente.')
        else:
            animal_para_atualizar['especie'] = nova_especie
            break

    while True:
        novo_sexo = input("Sexo [M/F]: ").strip().upper()
        if not novo_sexo:
            break
        elif novo_sexo not in ('M', 'F'):
            print('Digite um valor válido (M ou F). Tente novamente.')
        else:
            animal_para_atualizar['sexo'] = novo_sexo
            break

    while True:
        nova_idade = input("Idade: ").strip()
        if not nova_idade:
            break
        elif nova_idade.replace(' ', '').isalnum() == False:
            print('A idade deve conter apenas letras e números. Tente novamente.')
        else:
            animal_para_atualizar['idade'] = nova_idade
            break

    nova_info = input("Informações: ").strip()
    if nova_info: # Somente atualiza se algo for digitado
        animal_para_atualizar['informacões'] = nova_info

    salvar_dados(nome_arquivo, animais_da_lista)
    
    print('\nAnimal atualizado com sucesso!')
    sleep(2)
