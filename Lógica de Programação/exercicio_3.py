#  exercicio_3.py
#  Copyright 2022
#  Autor: Henrique Dalmagro
"""
3) Uma Torre de Hanói é formada por três discos sobrepostos transpassados por uma haste. Tendo
três hastes e podendo mover um disco por vez, mas nunca deixando um disco maior sobre um
disco menor. Faça um programa para resolver o problema da Torre de Hanói!
"""
#############################
# Fonte code in Python 3.10 #
#############################

# Variaveis globais
qtdMovimentos = int(0)
intervalo = [i for i in range(3, 9)]


def torreDeHanoi(n , A, B, C):
    global qtdMovimentos

    if n == 1:
        qtdMovimentos += 1 
        print(f"Disco 1 de {A} para {B}")
        return

    qtdMovimentos += 1
         
    torreDeHanoi(n-1, A, C, B)
    print(f"Disco {n} de {A} para {B}")
    torreDeHanoi(n-1, C, B, A)
    

def main():
    # Declaração de variaveis
    qtdDiscos = int(0)

    while True:
        try: # Entrada de dados
            qtdDiscos = int(input("Digite a quantidade de discos: "))

            # Verifica se a quantidade de discos esta no intervalo de 3-8 
            if not qtdDiscos in intervalo: 
                print("A quantidade minima de discos e 3 e a maxima e 8.\n")
                continue

        except ValueError:
            print("Erro! Digite apenas numeros inteiros.")
        
        else: # Processamento
            torreDeHanoi(qtdDiscos,'A','B','C')

            # Saida de dados
            print(f"Total de jogadas: {qtdMovimentos}")
               

if __name__ == "__main__":
    main()    
    