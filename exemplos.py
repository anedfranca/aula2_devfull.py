#MDIGITE QUANTAS VEZES QUER QUE APAREÇA = 
vezes = int(input("Vezes? "))

for i in range(1,vezes+1):
    print('='*i)


#LETRA UMA EM BAIXO DA OUTRA
nm = input ('nome: ')

for letra in nm:
    print(letra)

#PRINT TELA
nome = 'Ane'
print('oi',754,nome)
print(f'este é o print do {nome}')
print('oi, '+nome+', tudo bem?')
print('='*10)

#LISTAS
x = 5
numeros = [22,1,54,67,99,78]
bichos = ['papagaio', 'gato', 'cobra', 'elefante']
diversos = [12, 'Ane', 45.5, False, 'navio']

print(numeros)
print(numeros[3])
print(bichos)
print(bichos[0])
print(diversos)
print(diversos[2])

#OUTRA FORMA
numeros = [111,112,113,114,115,]

print(numeros)