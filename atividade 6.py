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


def lista_vazia(lista_produto):
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
    if lista_vazia (lista_produto):
        return
    print("\n==== Lista dos produtos =====")
    for produto in lista_produto:
        produto.exibir_dados()

