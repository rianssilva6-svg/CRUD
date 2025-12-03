import time
from dataclasses import dataclass
import os
os.system("cls || clear")

lista_aluno = []

@dataclass
class Endereco:
    logra: str
    numero: str
    cidade: str
    estado: str

@dataclass
class Aluno:
    nome: str
    nascimento: str
    ra: str
    curso: str
    endereco: Endereco

    def exibir_dados(self):
        print(30 * "=")
        print(f"Nome: {self.nome}\nNascimento: {self.nascimento}\nRA: {self.ra}\nCurso: {self.curso}")
        print("\n")
        print(f"Endereço: {self.endereco.logra}\n Numero: {self.endereco.numero}\nCidade: {self.endereco.cidade}\nEstado: {self.endereco.estado}")
        print(30 * "=")

def lista_vazia (lista_aluno):
    if not lista_aluno:
        print("Não tem aluno cadastrado.")
        return True
    return False

def adicionar_aluno(lista_aluno):
    print ("--- Adicionar Alunos ---")
    nome = input("Digite o nome: ")
    nascimento = input("Digite o ano de nascimento: ")
    ra = input("Digite o RA: ")
    curso = input("Digite o curso que a pessoa está: ")

    endereco = Endereco(
        logra=input("Digite o bairro: "),
        numero=input("Digite o número: "),
        cidade=input("Digite a cidade: "),
        estado=input("Digite o Estado: "))


    novo_aluno = Aluno(nome=nome, nascimento=nascimento, ra=ra,curso=curso, endereco=endereco)
    lista_aluno.append(novo_aluno)
    print (f"\nAluno {nome} adicionado com sucesso!")

def encontrar_aluno_nome (lista_aluno, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for aluno in lista_aluno:
        if aluno.nome.lower() == nome_buscar_lower:
            return aluno

def mostrar_todos_alunos(lista_aluno):
    if lista_vazia(lista_aluno):
        return 
    
    print("\n--- Lista de Alunos ---")
    for aluno in lista_aluno:
        aluno.exibir_dados()

def atualizar_aluno(lista_aluno):
    if lista_vazia(lista_aluno):
        return
    
    mostrar_todos_alunos(lista_aluno)
    print("--- Atualizar dados do cliente ---") 
    nome_buscar = input("\nDigite o nome do aluno: ")
    aluno_para_atualizar = encontrar_aluno_nome(lista_aluno, nome_buscar)

    if aluno_para_atualizar:
        print("\nPessoa encontrada.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {aluno_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"\nNascimento atual: {aluno_para_atualizar.nascimento}")
        novo_nascimento = int(input("Novo nascimento: "))

        print(f"\nRA atual: {aluno_para_atualizar.ra}")
        novo_ra = int(input("Novo RA: "))

        print(f"\nCurso atual: {aluno_para_atualizar.curso}")
        novo_curso = input("Novo curso: ")

        print(f"\nEndereço atual: {aluno_para_atualizar.endereco.logra}")
        novo_endereco = (input("Novo bairro: "))
        
        print(f"\nNúmero atual: {aluno_para_atualizar.endereco.numero}")
        novo_numero = int(input("Novo número: "))
        
        print(f"\nCidade atual: {aluno_para_atualizar.endereco.cidade}")
        nova_cidade = input("Nova Cidade: ")
        
        print(f"\nEstado atual: {aluno_para_atualizar.endereco.cidade}")
        novo_estado = input("Novo Estado: ")
        
      


        if novo_nome:
            aluno_para_atualizar.nome = novo_nome
        if novo_nascimento:    
            aluno_para_atualizar.nascimento = novo_nascimento
       
        if novo_nome:
            aluno_para_atualizar.nome = novo_ra
        if novo_nascimento:    
            aluno_para_atualizar.email = novo_curso
       
        if novo_nome:
            aluno_para_atualizar.nome = novo_endereco
        if novo_nascimento:    
            aluno_para_atualizar.email = novo_numero
       
        if novo_nome:
            aluno_para_atualizar.nome = nova_cidade
        if novo_nascimento:    
            aluno_para_atualizar.email = novo_estado
       

        print(f"\nAluno (a): {nome_buscar} atualizados com sucesso!")
    else:
        print (f"\nAluno (a): {nome_buscar} não encontrado.")  

def excluir_aluno(lista_aluno):
    if lista_vazia(lista_aluno):
        return

    mostrar_todos_alunos(lista_aluno)

    nome_buscar = input("\nDigite o nome do aluno que deseja excluir: ")

    aluno_para_remover = encontrar_aluno_nome(lista_aluno, nome_buscar)

    if aluno_para_remover:
        lista_aluno.remove(aluno_para_remover)
        print(f"\nAluno {aluno_para_remover.nome} excluido com sucesso!")
    else:
        print(f"\nAluno com o nome {nome_buscar} não encontrado.")  

while True:

    print("""
--- Gerenciador de Alunos ---
1 - Adicionar 
2 - Mostrar todos
3 - Atualizar
4 - Excluir
0 - Sair
          """)          
    
    try:
        opcao = int(input("Digite uma das opções acima: "))
    except ValueError:
        print("\nEntrada inválida. Digite um número...")
        time.sleep (2)
        os.system("cls || clear")
        continue

    match opcao:
        case 1:
            adicionar_aluno(lista_aluno)
        case 2:
            mostrar_todos_alunos(lista_aluno)
        case 3:
            atualizar_aluno(lista_aluno)
        case 4:
            excluir_aluno(lista_aluno)
        case 0:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida. \nTente novamente.")

    if opcao != 1 and opcao != 0:
        time.sleep(4)
    elif opcao == 1:
        time.sleep(1)


    if opcao != 0:
        os.system("cls || clear")    

