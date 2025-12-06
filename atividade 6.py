from dataclasses import dataclass
import time
import os 
os.system("cls")

lista_produto = []
lista_cliente = []

@dataclass
class Cliente:
    nome: str
    email: str 
    telefone: str
    endereco: str 
    
    def exibir_dados_clientes(self):
        print(f"Nome do cliente: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}\n Endereço: {self.endereco}")
       

@dataclass
class Produto:
    nome: str
    quantidade: int
    lote: int
    validade: str

    def exibir_produtos(self):
        print(f"Produto: {self.nome}\nQuantidade: {self.quantidade}\nLote: {self.lote}\nValidade: {self.validade}")    


def adicionar_clientes (lista_cliente):
    os.system("cls")
    print("=== Adicionar clientes ===")
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")
    endereco = input("Digite o endereço: ")
    novo_cliente = Cliente(nome=nome, 
                           email=email, 
                           telefone=telefone, 
                           endereco=endereco)
    lista_cliente.append(novo_cliente)

    os.system("cls")

def lista_vazia_cliente(lista_cliente):
    if not lista_cliente:
        print("===== Cliente não cadastrado. =====")
        return True
    return False

def encontrar_cliente(lista_cliente, cliente_buscar):
    cliente_buscar_lower = cliente_buscar.lower()
    for cliente in lista_cliente:
        if cliente.nome.lower() == cliente_buscar_lower:
            return cliente
        
def mostrar_todos_clientes (lista_cliente):
    if lista_vazia_cliente (lista_cliente):
        return
    print("\n==== Lista dos clientes =====")
    for cliente in lista_cliente:
        cliente.exibir_dados_clientes()

def atualizar_cliente(lista_cliente):
    if lista_vazia_cliente(lista_cliente):
        return
    
    mostrar_todos_clientes(lista_cliente)
    print ("===== Atualizar Dados Clientes =====")
    cliente_buscar = input("\nDigite o nome do cliente:") 
    cliente_atualizar = encontrar_cliente(lista_cliente, cliente_buscar)

    if cliente_atualizar:
        print ("===== Cliente encontrado =====")
        time.sleep(3)
        os.system("cls")
        print("=====\nDigite os novos dados ou deixe em branco. =====")

        print(f"Cliente atual: {cliente_atualizar.nome}")
        novo_cliente = input("Digite o novo nome do cliente: ")  

        print(f"Cliente atual: {cliente_atualizar.email}")
        novo_email = input("Digite o novo email: ")

        print(f"Cliente atual: {cliente_atualizar.telefone}")
        novo_telefone = input("Digite o novo telefone: ")           
        
        print(f"Cliente atual: {cliente_atualizar.endereco}")
        novo_endereco = input("Digite o novo endereço: ")

        if novo_cliente:
            cliente_atualizar.nome = novo_cliente
        if novo_email:    
            cliente_atualizar.email = novo_email
       
        if novo_telefone:
            cliente_atualizar.telefone = novo_telefone
        if novo_endereco:    
            cliente_atualizar.endereco = novo_endereco

def excluir_cliente (lista_cliente):
    if lista_vazia_cliente(lista_cliente):
        return
    mostrar_todos_clientes(lista_cliente)
    cliente_buscar = input("Digite o nome do cliente que deseja excluir: ")
    cliente_remover = encontrar_cliente(lista_cliente, cliente_buscar)
    if cliente_remover:
        lista_cliente.remove(cliente_remover)
        print(f"===== Cliente {cliente_remover.nome} excluido com sucesso. =====")  
    else:
        print(f"===== Cliente {cliente_buscar} não encontrado. =====")                       



def adicionar_produto(lista_produto):
    print("=== Adicionar produto ===")
    nome = input("Digite o nome do produto: ")    
    quantidade = int(input("Digite a quantidade: "))    
    lote = int(input("Digite o lote: "))    
    validade = input("Digite a validade: ")
    novo_produto = Produto(nome=nome, 
                           quantidade=quantidade, 
                           lote=lote, 
                           validade=validade)
    lista_produto.append(novo_produto)
    

def lista_vazia_produto(lista_produto):
    if not lista_produto:
        print("===== Não tem produto cadastrado. =====")
        return True
    return False


def encontrar_produto(lista_produto, produto_buscar):
    produto_buscar_lower = produto_buscar.lower()
    for produto in lista_produto:
        if produto.nome.lower() == produto_buscar_lower:
            return produto

def mostrar_todos_produtos(lista_produto):
    if lista_vazia_produto (lista_produto):
        return
    print("\n==== Lista dos produtos =====")
    for produto in lista_produto:
        produto.exibir_produtos()

def atualizar_produto(lista_produto):
    print("===== Atualizar dados do produto =====") 
    produto_buscar = input("\nDigite o nome do produto: ")
    produto_atualizar = encontrar_produto(lista_produto, produto_buscar)       

    if produto_atualizar:
        print("\n===== Produto encontrado. =====")
        time.sleep(3)
        os.system("cls")
        print("\n===== Digite os novos dados ou deixe em branco para manter o valor atual. =====")

        print(f"\nProduto atual: {produto_atualizar.nome}")
        novo_produto = input("Novo produto: ")

        print(f"\nQuantidade atual: {produto_atualizar.quantidade}")
        nova_quantidade = int(input("Quantidade: "))

        print(f"\nLote atual: {produto_atualizar.lote}")
        novo_lote = int(input("Novo lote: "))

        print(f"\nValidade atual: {produto_atualizar.validade}")
        nova_validade = input("Nova validade: ")

        if novo_produto:
            produto_atualizar.nome = novo_produto
        if nova_quantidade:    
            produto_atualizar.quantidade = nova_quantidade
       
        if novo_lote:
            produto_atualizar.lote = novo_lote
        if nova_validade:    
            produto_atualizar.validade = nova_validade
        
        print(f"\n===== Produto: {produto_buscar} atualizados com sucesso! =====")
    else:
        print (f"\n===== Produto: {produto_buscar} não encontrado. =====")  

def excluir_produto(lista_produto):
    if lista_vazia_produto (lista_produto):
        return
    mostrar_todos_produtos(lista_produto)

    produto_buscar = input("\nDigite o nome do produto que deseja excluir: ")
    produto_remover = encontrar_produto(lista_produto, produto_buscar)

    if produto_remover:
        lista_produto.remove(produto_remover)
        print(f"\n===== Produto {produto_remover.nome} excluido com sucesso! =====")
    else:
        print(f"\n===== Produto {produto_buscar} não encontrado. =====")  


while True:

    print("""
===== Escolha uma das opções abaixo =====
1 - Adicionar cliente
2 - Adicionar produto
""")
    
    try:
        opcao = int(input("Escolha uma das opções: "))
    except ValueError:
        print("\nEntrada inválida. Digite um número...")
        time.sleep (2)
        os.system("cls || clear")
        continue
    match opcao:
        case 1:
            print("\n===== Menu Cliente =====")
            print("""
1 - Adicionar cliente
2 - Mostrar todos os clientes
3 - Atualizar cliente
4 - Excluir cliente
0 - Sair do programa
""")
            try:
                opcao_cliente = int(input("Escolha uma das opções: "))
            except ValueError:
                print("\nEntrada inválida. Digite um número...")
                time.sleep (2)
                os.system("cls || clear")
                continue
            match opcao_cliente:
                case 1:
                    adicionar_clientes(lista_cliente)
                case 2:
                    mostrar_todos_clientes(lista_cliente)
                case 3:
                    atualizar_cliente(lista_cliente)
                case 4:
                    excluir_cliente(lista_cliente)
                case 0:
                    print("\nSaindo do programa...")
                    time.sleep(2)
                    os.system("cls || clear")
                    break
                case _:
                    print("\nOpção inválida. Tente novamente.")
                    time.sleep(2)
                    os.system("cls || clear") 
        case 2:
            print("\n===== Menu Produto =====")
            print("""
1 - Adicionar produto
2 - Mostrar todos os produtos
3 - Atualizar produto
4 - Excluir produto
0 - Sair do programa
""")
            try:
                opcao_produto = int(input("Escolha uma das opções: "))
            except ValueError:
                print("\nEntrada inválida. Digite um número...")
                time.sleep (2)
                os.system("cls || clear")
                continue
            match opcao_produto:
                case 1:
                    adicionar_produto(lista_produto)
                case 2:
                    mostrar_todos_produtos(lista_produto)
                case 3:
                    atualizar_produto(lista_produto)
                case 4:
                    excluir_produto(lista_produto)
                case 0:
                    print("\nSaindo do programa...")
                    time.sleep(2)
                    os.system("cls || clear")
                    break
                case _:
                    print("\nOpção inválida. Tente novamente.")
                    time.sleep(2)
                    os.system("cls || clear") 
        case _:
            print("\nOpção inválida. Tente novamente.")
            time.sleep(2)
            os.system("cls || clear")


    

