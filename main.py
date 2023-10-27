
from modules import *

if __name__ == '__main__':
    while True:
        escolha = menu()

        if escolha == 1:
            jogoDaVelha().rodarJogo()
        elif escolha == 2:
            credits()
        elif escolha == 3:
            placar()
        elif escolha == 0:
            break