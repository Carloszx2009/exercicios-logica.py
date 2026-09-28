input1 = float(input("Digite o valor da compra: "))
if input1 > 100:
    desconto = input1 * 0.10
    valor_final = input1 - desconto
    print("O valor final com desconto é:", valor_final)
else:
    print("Não há desconto disponível.")
