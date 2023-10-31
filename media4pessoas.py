mediaidade = 0
somaidade = 0
nome_do_homem_mais_velho= " "
maior_idade_homem = 0
mulher_menor_que_20 = 0

for i in range(1, 5) :
    nome = str(input(f"Digite o nome da {i}° pessoa: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o gênero da pessoa ('m' para MASCULINO e 'f' para FEMININO): "))
    sexo = sexo.upper()

    somaidade += idade

    if sexo == 'M' and idade >= maior_idade_homem:
        maior_idade_homem = idade
        nome_do_homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        mulher_menor_que_20 += 1

    else :
        print("Genero invalido.")

mediaidade = somaidade / 4

print(f"A média de idade do grupo é {mediaidade}.")
print(f"O nome do homem mais velho é {nome_do_homem_mais_velho} e ele tem {maior_idade_homem} anos.")
print(f"São {mulher_menor_que_20} mulheres menores de 20 anos ao todo.")