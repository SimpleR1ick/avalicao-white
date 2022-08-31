#  exercicio_1.py
#  Copyright 2022
#  Autor: Henrique Dalmagro
"""
1) As maçãs custam R$1,30 cada se forem compradas menos de uma dúzia, e R$1,00 se forem
compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas,
calcule e escreva o custo total da compra.
"""
#############################
# Fonte code in Python 3.10 #
#############################

def main():
    # Declaração de variaveis
    precoFinal = int(0)
    qtdMacas = int()

    while True:
        try: # Entrada de dados
            qtdMacas = int(input("Quantidade de maçãs compradas: "))
            
            if qtdMacas < 1:
                print("Digite uma quantidade maior que 0!\n")
                continue # Retorna ao inicio do loop

        except ValueError: # Inappropriate argument value (of correct type) != int
            print("Digite apenas numeros inteiros!")
        
        else: # Processamento - Calculando preço da maçã(s)
            if qtdMacas < 12: # Menor que uma duzia
                precoFinal = qtdMacas * 1.30

            else: # Uma duzia, preço de 1 real
                precoFinal = float(qtdMacas)

            # Saida de dados
            print(f"Custo total da compra: R$ {precoFinal:.2f}")
            break
    

if __name__ == "__main__":
    main()