#Giovanna Saori Arata RM99403
#Pedro Luca de Andrade Nunes RM550366
#Pedro Henrique Pontes Farath RM98608
#Lucca Vilaça Okubo RM551538 

 
#imports
import random
import re

# validação do ano 
def validarAno(x):
    padrao_data = r'^\d{4}$'
    if re.match(padrao_data, str(x)):
        print("Data de nascimento válida.")
    else:
        print("Data de nascimento inválida.")
        exit()

# validação do nome 
def validarNome(nome):
    padrao_nome = r'^[a-zA-Z\s]+$'
    if re.match(padrao_nome, nome):
        return True
    else:
        return False

# validação do cep 
def validarCEP(cep):
    padrao_cep = r'^\d{5}-?\d{3}$'
    if re.match(padrao_cep, cep):
        return True
    else:
        return False

# selecionando atendente
nomes = ('PH', 'Lucca', 'PL', 'Giovanna')
sorteado = random.choice(nomes)

# lista dos vinhos 
vinhos = {
    'vinho 1': {'preço': 48, 'estoque': 0, 'id': 1, 'nome': 'Arbane'},
    'vinho 2': {'preço': 123, 'estoque': 1, 'id': 2, 'nome': 'Cabernet sauvigno'},
    'vinho 3': {'preço': 89, 'estoque': 2, 'id': 3, 'nome': 'Albariño'},
    'vinho 4': {'preço': 56, 'estoque': 3, 'id': 4, 'nome': 'Carignan'},
    'vinho 5': {'preço': 77, 'estoque': 4, 'id': 5, 'nome': 'Chardonnay'}
}

# pedindo as informações do cliente 
print(f"Olá meu nome é {sorteado} e irei realizar seu atendimento hoje, para começar irei precisar de alguma informação")
nome = input("Nome: ")
cep = input("CEP: ")
ano = int(input("Em que ano você nasceu? "))
idade = 2023 - int(ano)
validarAno(ano)

#verifica o nome
if not validarNome(nome):
    print("Nome inválido.")
    exit()

#verifica o cep
if not validarCEP(cep):
    print("CEP inválido.")
    exit()

cliente = dict(nome=nome, idade=idade, cep=cep)

#verifica idade
if idade < 18:
    print("Você é menor de idade, sinto muito!")

    #mostrando as opções de vinhos
else:
    print('Temos estes vinhos: ')
    for i in vinhos.values():
        if i['estoque'] != 0:
            print(f"Vinho {i['id']}: {i['nome']} - R${i['preço']:.2f}")

pedido_final = []

#comprando o vinho
while True:
    print('Escolha o vinho desejado pelo número (ou digite 0 para sair): ')
    escolha = int(input())
    
    if escolha == 0:
        print("Pedido finalizado.")
        break
    
    vinho_escolhido = None
    for i in vinhos.values():
        if escolha == i['id']:
            vinho_escolhido = i
            break
    
    if vinho_escolhido:
        print(f'O vinho escolhido foi {vinho_escolhido["nome"]}')
        num_garrafas = int(input('Quantas garrafas deseja? '))
        
        if num_garrafas > vinho_escolhido['estoque']:
            print("Quantidade de garrafas indisponível.")
            continue
        
        subtotal = vinho_escolhido['preço'] * num_garrafas
        pedido = [vinho_escolhido["nome"], vinho_escolhido['preço'], num_garrafas, subtotal]
        vinho_escolhido['estoque'] -= num_garrafas
        pedido_final.append(pedido)
        print("Pedido adicionado:", pedido)
    else:
        print("Vinho não encontrado.")

# finalização do pedido 
print("\nDetalhes do Pedido:")
print(f"Nome do cliente: {cliente['nome']}")
for pedido in pedido_final:
    nome_vinho, preco_vinho, qtd_garrafas, subtotal = pedido
    print('-----------------------------------------------------------------------------')
    print(f"Vinho: {nome_vinho} - Preço: R${preco_vinho:.2f} - Quantidade: {qtd_garrafas} - Subtotal: R${subtotal:.2f}")
print('---------------------------------------------------------------------------')
print("Obrigado por sua compra! Volte sempre.")
