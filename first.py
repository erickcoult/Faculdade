#atividade 1-------------
#nome = input('digite seu nome ')
#print(f"Olá {nome}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world, {nome}")

#atividade 2-------------
#a = 4
#b = 0.5
#c = 1
#x = input("digite o valor de x: ")
#x = float(x)
#y = a * x ** 2 + b * x + c
#print(f"O resultado de y para x = {x} é {y}.")

#atividade 3--------------
#a = input('valor 1: ')
#b = input('valor 2: ')
#if a < b:
#    print('B é maior que A')
#else:
#    print("A é maior do que B")

#a = 5
#b = 10
#if a < b:
# print("a é menor do que b")
#r = a + b
#print(r)

#atividade 4----------------
#codigo_compra = 5222

#if codigo_compra == 5222:
    #print("Compra à vista.")
#elif codigo_compra == 5333:
    #print("Compra à prazo no boleto.")
#elif codigo_compra == 5444:
    #print("Compra à prazo no cartão.")
#else:
    #print("Código não cadastrado")

#atividade 5 and, or, not----------------
#A = 15
#B = 9
#C = 9

#print(B == C or A < B and A < C)
#print((B == C or A < B) and A < C )

#atividade 6 while-----------------
#numero = 1
#while numero != 0:
#    numero = int(input("Digite um número: "))
#    if numero % 2 == 0:#
#        print("Número par!")
#    else:
#        print("Número ímpar!")

#atividade 7 for------------
#nome = "Guido"
#for o, u in enumerate(nome):
#    print(f"Posição = {o}, valor = {u}")

#computador = ['Processador', 'Teclado', 'Mouse', 'Tela']
#
#for item in computador:
# print(item)

#atividade 8 range----------
#for x in range(5):
#    print(x)

#Método 3
#for i in range(0, 20, 2):
# print(i)

while numero != 0:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")

#ativifsfr 9 break-------
#disciplina = "Linguagem de programação"
#for c in disciplina:
#    if c == 'z':
#        break
#    else:
#        print(c)

#atividade 10 continue------
#texto = """
#A inserção de comentários no código do programa é uma prática normal.
#Em função disso, toda linguagem de programação tem alguma maneira de permitir que comentários sejam inseridos nos programas.
#O objetivo é adicionar descrições em partes do código, seja para documentá-lo ou para adicionar uma descrição do algoritmo #implementado (BANIN, p. 45, 2018)."
#"""
#for i, c in enumerate(texto):
#    if c == 'a' or c == 'e':
#        print(f"Vogal '{c}' encontrada, na posição {i}")
#    else:
#        continue