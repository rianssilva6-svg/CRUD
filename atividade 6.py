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

@dataclass
class Produto:
    nome: str
    quantidade: int
    lote: int
    validade: str

def exibir_dados_clientes(self):
    print(f"Nome do cliente: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}\n Endereço: {self.endereco}")

def exibir_produtos(self):
    print(f"Produto: {self.nome}\nQuantidade: {self.quantidade}\nLote: {self.lote}\nValidade: {self.validade}")    


def adicionar_clientes (lista_cliente):
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

def lista_vazia_cliente(lista_cliente):
    if not lista_cliente:
        print("===== Cliente não cadastrado. =====")
        return True
    return False

def encontrar_cliente(lista_cliente, cliente_buscar):
    cliente_buscar_lower = cliente_buscar.lower()
    for cliente in lista_cliente:
        if cliente.nome.lower == cliente_buscar_lower:
            return cliente
        
def mostrar_todos_clientes (lista_cliente):
    if lista_vazia_cliente (lista_cliente):
        return
    print("\n==== Lista dos produtos =====")
    for cliente in lista_cliente:
        cliente.exibir_dados_clientes()

def atualizar_cliente        



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
        if produto.nome.lower == produto_buscar_lower:
            return produto

def mostrar_todos_produtos(lista_produto):
    if lista_vazia_produto (lista_produto):
        return
    print("\n==== Lista dos produtos =====")
    for produto in lista_produto:
        produto.exibir_produto()

def mostrar_todos_produtos(lista_produto):
    print("--- Atualizar dados do produto ---") 
    produto_buscar = input("\nDigite o nome do produto: ")
    produto_atualizar = encontrar_produto(lista_produto, produto_buscar)       

    if produto_atualizar:
        print("\nPessoa encontrada.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {produto_atualizar.nome}")
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

    produto_buscar = input("\nDigite o nome do aluno que deseja excluir: ")
    produto_remover = encontrar_produto(lista_produto, produto_buscar)

    if produto_remover:
        lista_produto.remove(produto_remover)
        print(f"\n===== Produto {produto_remover.nome} excluido com sucesso! =====")
    else:
        print(f"\n===== Produto {produto_buscar} não encontrado. =====")  




    

