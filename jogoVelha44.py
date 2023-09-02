class TicTacToe4x4:
    """
    O tabuleiro é representado como uma lista de listas, onde cada elemento pode ser 'X', 'O' ou vazio (' ').
    """

    def __init__(self):
        """
        Inicializa um novo jogo da velha 4x4 com um tabuleiro vazio.
        """
        self.board = [[' ' for _ in range(4)] for _ in range(4)]
        self.current_player = 'X'
        self.player_mapping = {'X': 1, 'O': -1, ' ': 0}

    def __str__(self):
        """
        Retorna uma representação legível do tabuleiro.
        """
        board_str = ""
        for row in self.board:
            board_str += ' | '.join(row) + '\n'
            if row != self.board[-1]:
                board_str += '- ' * 7 + '\n'
        return board_str

    def make_move(self, row, col):
        """
        Realiza uma jogada na posição (row, col) se a célula estiver vazia.
        """
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'X' if self.current_player == 'O' else 'O'
            return True
        return False

    def check_winner(self):
        """
        Verificação de vencedor.
        Loop que percorre todas as linhas do tabuleiro e todas as colunas do tabuleiro.
        Se a soma do mapeamento '1' ou '-1' for igual a 4 ou -4, o 'X' ou 'O' venceu, respectivamente.
        Se não houver um vencedor nas tuplas retornadas nas linhas e colunas, vai para as diagonais
        Se não houver vencedor nas diagonais, informa que o jogo ainda está em andamento.
        Se houver vencedor, retorna o 'X' ou 'O' como vencedor
        """
        for line in self.board + list(zip(*self.board)):
            if sum(self.player_mapping[cell] for cell in line) in [-4, 4]:
                return line[0]

        diag1 = [self.board[i][i] for i in range(4)]
        diag2 = [self.board[i][3 - i] for i in range(4)]

        if sum(self.player_mapping[cell] for cell in diag1) in [-4, 4]:
            return diag1[0]

        if sum(self.player_mapping[cell] for cell in diag2) in [-4, 4]:
            return diag2[0]

        if all(cell != ' ' for row in self.board for cell in row):
            return 'Empate'

        return None

# Iniciar o jogo
game = TicTacToe4x4()
print("Bem-vindo ao Jogo da Velha 4x4!")
print(game)

while True:
    try:
        row = int(input("Digite o número da linha (0-3): "))
        col = int(input("Digite o número da coluna (0-3): "))
        if 0 <= row <= 3 and 0 <= col <= 3:
            if game.make_move(row, col):
                print(game)
                winner = game.check_winner()

                if winner == 'Empate':
                    print("O jogo terminou em empate!")
                    break
                elif winner is not None:
                    print("O jogador", winner, "venceu!")
                    break
            else:
                print("Essa posição já está ocupada. Tente novamente.")
        else:
            print("Entrada inválida. Digite um número entre 0 e 3.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
