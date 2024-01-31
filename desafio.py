#Suponha que você está gerenciando uma competição esportiva e tem
#uma lista de tuplas representando os resultados das equipes em
#diferentes modalidades. Cada tupla contém o nome da equipe, seguido
#por uma lista de pontuações obtidas em cada rodada da competição.

# Lista de tuplas representando os resultados das equipes
resultados = [
    ("Equipe A", [10, 8, 7, 9]),
    ("Equipe B", [9, 7, 6, 8]),
    ("Equipe C", [8, 6, 5, 7]),
    ("Equipe D", [7, 5, 4, 6])
]

# 1. Calcular a média das pontuações de cada equipe
medias = []

for equipe, pontuacoes in resultados:
    media = sum(pontuacoes) / len(pontuacoes)
    medias.append(media)
    print(media)

# 2. Ordenar a lista de médias em ordem decrescente
medias.sort(reverse=True)
print

# 3. Criar uma nova lista chamada classificacao com tuplas de nome da equipe e média de pontuações
classificacao = []

for media in medias:
    for equipe, pontuacoes in resultados:
        if sum(pontuacoes) / len(pontuacoes) == media:
            classificacao.append((equipe, media))
            resultados.remove((equipe, pontuacoes))
            break

# 4. Exibir a classificação final das equipes
print("Classificação Final:")
for equipe, media in classificacao:
    print(f"{equipe}: {media}")

