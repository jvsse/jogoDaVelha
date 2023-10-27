import os
import json

def menu() -> int:

    while True:
         
        for _ in ["[1] - Jogar", "[3] - Placar", "[0] - Sair", "[2] - Créditos"]:
            print(f"{_}")
        try:
            escolha = int(input("\nOpções: ").strip())
        except:
             
            print("Ação Inválida!")
            input()
        else:
            break

    return escolha

def credits() -> None:
    print("Créditos: Gabriel Vieira e Jesse Lima.")
    input()

def placar() -> None:
     

    pontos = json.load(open('./pontos.json', 'r'))


    print(' '*10, f'{"jogador": ^10}|{"WINS": ^10}')
    for jogador, points in pontos.items():
        print(' '*10, '-'*21)
        print(' '*10, f'{jogador: ^10}|{points: ^10}')

    input()

class jogoDaVelha:
    empty = ' '

    def __init__(self):
        self.board = [
            [jogoDaVelha.empty, jogoDaVelha.empty, jogoDaVelha.empty],
            [jogoDaVelha.empty, jogoDaVelha.empty, jogoDaVelha.empty],
            [jogoDaVelha.empty, jogoDaVelha.empty, jogoDaVelha.empty]
        ]
        self.jogadores = ['X', 'O']
        self.jogador = self.jogadores[0]
        self.pontos = json.load(open('./pontos.json', 'r'))
    
    def rodarJogo(self) -> None:
        labels = 9

        while labels:
             
            while True:
                try:
                     
                    jogoDaVelha.mostrarPlacar(self)
                    op = int(input(f"Vez do {self.jogador}\nNúmero de 1 a 9: "))
                except:
                     
                    print("Ação Inválida!")
                    input()
                else:
                    break

            verify, new_board = jogoDaVelha.marcarPonto(self, self.board, op, self.jogador)

            if verify:
                labels -= 1
                self.board = new_board
                win_check = jogoDaVelha.checarVencedor(self, self.board, self.jogador)

                if win_check:
                     
                    self.pontos[self.jogador] += 1
                    json.dump(self.pontos, open('./pontos.json', 'w'))
                    if self.jogador == 'X':
                        print("Jogador X ganhou!")
                        input()
                        return
                    
                    print("Jogador O ganhou!")
                    input()
                    return

                self.jogador = jogoDaVelha.swapjogador(self, self.jogador, self.jogadores)
         
        print("Velha! (Empate)")
        input()
        

    def mostrarPlacar(self) -> None:
        jogoDaVelha.showpontos(self)
        for line in range(3):
            for column in range(3):
                if column != 2:
                    print(f'{self.board[line][column]: ^5}', end=' | ')
                    continue
                print(f'{self.board[line][column]: ^5}')
            print('-'*20)

    def showpontos(self) -> None:
        x = self.pontos['X']
        o = self.pontos['O']
        print(f'{"="*5}{"pontos": ^10}{"="*5}\n{f"X: {x}  O: {o}": ^20}')

    def swapjogador(self, current_jogador: str, jogadores: list) -> str:
        jogador_index = jogadores.index(current_jogador)

        if jogadores[jogador_index] == jogadores[-1]:
            return jogadores[0]
        return jogadores[-1]

    def returnNumberOfNumBoard(self, num: int) -> tuple:
        num_board = [
            [7, 8, 9],
            [4, 5, 6],
            [1, 2, 3]
        ]

        for line in range(3):
            for column in range(3):
                if num_board[line][column] == num:
                    return line, column
        
        return 404, False # Not found

    def marcarPonto(self, board: list, num: int, jogador: str) -> tuple:
        line, column = jogoDaVelha.returnNumberOfNumBoard(self, num)

        if line == 404 or board[line][column] != ' ':
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação inválida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
            input()
            return False, '_'

        board[line][column] = jogador

        return True, board

    def checarVencedor(self, board: list, jogador: str) -> bool:
        # Diagonal direita
        if (board[0][2] == jogador) and (board[1][1] == jogador) and (board[2][0] == jogador):
            return True

        # Diagonar esquerda
        elif (board[0][0] == jogador) and (board[1][1] == jogador) and (board[2][2] == jogador):
            return True

        # Horizontal
        for line in range(3):
            if (board[line][0] == jogador) and (board[line][1] == jogador) and (board[line][2] == jogador):
                return True

        # Vertical
        for column in range(3):
            if (board[0][column] == jogador) and (board[1][column] == jogador) and (board[2][column] == jogador):
                return True

        return False