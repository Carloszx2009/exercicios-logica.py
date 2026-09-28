idade = int(input("Digite a idade da pessoa: ")) 
if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("A pessoa é uma criança.")
elif idade <= 17:
    print("A pessoa é um adolescente.")
else:
    print("A pessoa é um adulto.")