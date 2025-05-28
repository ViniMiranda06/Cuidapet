# P.A.T.A.S.
Plataforma de Apoio ao Tratamento e Adoção Solidária

O P.A.T.A.S. tem como intuito auxiliar projetos voluntários que atuam no resgate, tratamento e adoção de animais. A proposta visa oferecer uma solução tecnológica acessível, funcional e organizada, capaz de centralizar informações importantes sobre animais acolhidos, seu estado de saúde, sua disponibilidade para adoção e o andamento dos cuidados prestados.

## 🚀 Tecnologia Utilizada
- Python 3.12.4
- bibliotecas usadas: JSON (*Uso de Listas e Dicionários, Podendo assim listar tanto em ordem com as Listas como em pares com os Dicionários, salvos em JSON) e Time
- Estruturas utilizadas:
 *if (executa um bloco se uma condição for verdadeira.)
 *elif (executa outra condição se a anterior for falsa.)
 *else (executa caso todas as condições anteriores sejam falsas.)
 *while (repete um bloco enquanto a condição for verdadeira.)
 *for (percorre itens de uma sequência (lista, string, etc.).)
 *try (tenta executar um bloco e trata erros com except se algo falhar.)

## 🔧 Instalação e Execução

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/patas.git
cd patas
```

2. Execute o programa:
```bash
main.py
```

## 👤 Funcionalidades para Usuários Comuns

### Visualização 
"""
    Menu principal para o usuário após o login.
    Contém opções para animais em tratamento, adoção, e opções administrativas (secreta).
    """
- Listagem de animais disponíveis para adoção
- Visualização de animais em tratamento
- Detalhes completos de cada animal

### Gerenciamento de Conta
"""Insere um menu de escolha para o usuário, contendo:
    [1] Cadastrar-se no P.A.T.A.S.
    [2] Fazer Login
    ...
    contém gerenciamento de conta dentro do padrão CRUD! contendo edição de perfil, Exclusçao de conta e sair da conta
    """
- Edição de informações pessoais
- Alteração de senha
- Logout

👑 Funcionalidades para Administradores

⚠️ Atenção: O acesso às funcionalidades administrativas é restrito e só pode ser feito por meio de um recurso secreto acessado após o login.

## 🔐 Como acessar o menu administrativo:
1. Faça login normalmente como qualquer usuário.

2. No Menu Principal, digite 1703 como opção.

3. Isso abrirá o Menu Administrativo, exclusivo para a equipe responsável.

## 🐾 Gestão de Animais
-Cadastro de novos animais
-Atualização de status (tratamento / adoção)
-Edição de informações detalhadas dos pets
-Registro de tratamentos e procedimentos realizados

📄 Gestão de Adoções (
-Visualização de todos os pedidos de adoção realizados
-Aprovação ou rejeição das solicitações enviadas por usuários

## 👨‍💻 Desenvolvedores
- Dhavi
(https://github.com/DhaviRodrigues)
- Vinícius De Oliveira
(https://github.com/ViniMiranda06)

## ⚠️ Estado do projeto
O projeto se encontra em estágio de desenvolvimento.

## 📝 Licença
Este é um projeto acadêmico desenvolvido para fins educacionais.
