#  exercicio_2.py
#  Copyright 2022
#  Autor: Henrique Dalmagro
"""
2) Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem
os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração
do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.
"""
#############################
# Fonte code in Python 3.10 #
#############################

def main():
    # Declaração de variaveis
    horaInicial = int(0)
    horaTermino = int(0)
    tempoTotal = int(0)
    
    while True:
        try: # Entrada de dados 
            horaInicial = int(input("Digite a hora inicial: "))
            horaTermino = int(input("Digite a hora final: "))

            if (horaInicial or horaTermino) < 0:
                print("Erro!\nNão existe horario negativo.\n")
                continue # Retorna ao inicio do loop while

        except ValueError: # Inappropriate argument value (of correct type). != int
            print("Digite apenas numeros inteiros.")
        
        else: # Processamento - Calculando tempo de jogo
            if horaInicial >= horaTermino: 
                tempoTotal = (24 - horaInicial) + horaTermino # Iniciou em um dia e terminou no seguinte
            else: 
                tempoTotal = horaTermino - horaInicial # Iniciou e terminou no mesmo dia  
            
            # Saida de dados
            if tempoTotal > 24:
                print("O jogo execedeu o limite de 24 horas de duração!")
   
            print(f"Tempo de jogo: {tempoTotal} horas.")
            break


if __name__ == "__main__":
    main()