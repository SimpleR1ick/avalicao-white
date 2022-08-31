#  exercicio_4.py
#  Copyright 2022
#  Autor: Henrique Dalmagro
"""
4) Pergunta Desafio - A Sequência de Fibonacci consiste numa sucessão infinita de números que
obedecem um padrão em que cada elemento subsequente é a soma dos dois anteriores. Assim,
formando a sequência [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…]. Faça um algoritmo que, ao ler um
número, tenha como resposta o valor da sua posição na sequência de Fibonacci. Exemplo: N =
6, saída = 5
"""
#############################
# Fonte code in Python 3.10 #
#############################

def fibonacci(n):
    if n in {0, 1}: # Se n < 2 então retorne n
       return n
    # Numeros seguintes
    return fibonacci(n - 1) + fibonacci(n - 2) 


def main():
    # Variaveis
    num = int()

    while True:
        try: # Entrada de dados
            num = int(input("Digite o número da posição: "))

            if num < 1:
                print("Erro! Digite apenas números maiores que 0!")
                continue

        except TypeError:
            print("Erro! Digite apenas números inteiros!")
        
        else: # Processamento
            sequencia = [fibonacci(n) for n in range(num)] # Compressão de lista

            # Saida de dados
            print(f"O {num}º número da sequência de fibonacci => {sequencia[num-1]}")
            break
    

if __name__ == "__main__":
    main()
    