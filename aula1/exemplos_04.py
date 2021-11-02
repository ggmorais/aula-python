# # # list # [1, 2, 3], ["Gustavo", "Morais"], ["Gustavo", 2021]
# # # dict # {'nome': 'Gustavo', 'idade': 21, 'localidade': {'cidade': 'São Paulo', 'estado': 'SP'}, 'localizacao2': [1123456, 123456]}

# # dados = ["Gustavo", "Morais", 2021, None, None]

# # print(dados)

# # dados[3] = "São Paulo"

# # print(dados)

# # del dados[1]

# # print(dados)

# # dados[0] = "Gustavo Morais"

# # dados.append("Brazil")

# # print(dados)



# pessoa = {
#     "nome": "Gustavo",
#     "cidade": "Novo Hamburgo",
#     "estado": "RS"
# }

# print(pessoa)

# pessoa["habilidade"] = "Python"

# print(pessoa)

# pessoa["nome"] = "Tiago"

# print(pessoa)

# pessoa["hobbies"] = ["leitura", "jogos", "corrida"]

# print(pessoa["hobbies"][1])

# pessoa["hobbies"].append("cinema")

# print(pessoa)


# pessoa["items"] = [
#     {"nome": "Notebook", "preco": 2000},
#     {"nome": "Notebook", "preco": 2000},
#     {"nome": "Notebook", "preco": 2000},
#     {"nome": "Notebook", "preco": 2000},
#     pessoa
# ]

# print(pessoa["items"])

# dados = ("Gustavo", "Morais", 2021, None, None)
# print(dados)
# dados[0] = "abc"
# dados.count("Gustavo")

# set # {1, 2, 3} {"a", 1, 2, "b"}
# set # {1, 1, 2, 1}

# print(set([1, 2, 3, 4, 4, 2]))

dados = ["Gustavo", "Gustavo", 1, 2, 1, 2, 2] * 100

dados = list(set(dados))

print(dados)
