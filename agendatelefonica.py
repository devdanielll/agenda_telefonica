agenda = []

def nome_1():
     return(input("Nome: "))

def telefone_1():
     return(input("Telefone: "))

def listar_dados(nome, telefone):  
     print("Nome: %s\nTelefone: %s\n" % (nome, telefone))


def pesquisa(nome):
     name = nome.lower()
     for d, e in enumerate(agenda):
         if e[0].lower() == name:       
               return d
     return None

def novo():
    global agenda
    nome = nome_1()
    telefone = telefone_1()
    agenda.append([nome, telefone])

def apagar():
     global agenda
     nome = nome_1()
     p = pesquisa(nome)
     if p != None:
         del agenda[p]
     else:
         print("Nome não encontrado.")


def editar():
     p = pesquisa(nome_1())
     if p != None:
         nome = agenda[p][0]
         telefone = agenda[p][1]
         print("Encontrado:")
         listar_dados(nome, telefone,)
         nome = nome_1()
         telefone = telefone_1()
         agenda[p] = [nome, telefone]
     else:
         print("Nome não encontrado.")



def listar():
     print("\n Agenda de Contatos \n\n------")
     for e in agenda:
         listar_dados(e[0], e[1])
     print("------\n")

def pesquisar():
     p = pesquisa(nome_1())
     if p != None:
         nome = agenda[p][0]
         telefone = agenda[p][1]
         print('=-' * 10)
         print("Encontrado:")
         listar_dados(nome, telefone)
     else:
          print("Nome não encontrado.")

def validar(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                   return(valor)
               return                        
         except ValueError:                  
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menu():
  print('=-=-=-=-= Agenda de Contatos =-=-=-=-=')
  print("""
   1 - Adicionar novo contato
   2 - Editar um contato
   3 - Pesquisar contato
   4 - Lista de contatos
   5 - Apagar um contato
   6 - Sair
""")
  print('-=' * 19)
   
  return validar("Escolha uma opção: ",1,6)


while True:
  opção = menu()
  if opção == 6:                   
    break
  elif opção == 1:
    novo()
  elif opção == 2:
    editar()
  elif opção == 3:
    pesquisar()
  elif opção == 4:
    listar()
  elif opção == 5:
    apagar()