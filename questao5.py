produtos = {
    "maçã": 2.50,
    "banana": 1.75,
    "laranja": 3.00
}

print("Questão 5 - Dicionário de produtos original:", produtos)

produtos["uva"] = 4.50
print("Questão 5 - Dicionário após adicionar uva:", produtos)

produtos["maçã"] = 2.75
print("Questão 5 - Dicionário após atualizar maçã:", produtos)

del produtos["banana"]
print("Questão 5 - Dicionário após remover banana:", produtos)


