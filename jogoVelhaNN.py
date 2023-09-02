class TicTacToeNxN:
    """
    Classe que implementa o jogo da velha NxN (tamanho do tabuleiro definido pelo usuário).

    O tabuleiro é representado como uma lista de listas, onde cada elemento pode ser 'X', 'O' ou vazio (' ').
    """

    def __init__(self, n):
        """
        Inicializa um novo jogo da velha NxN com um tabuleiro vazio.
        """
        self.size = n
        self.board = [[' ' for _ in range(n)] for _ in range(n)]
        self.current_player = 'X'

    def __str__(self):
        """
        Retorna uma representação legível do tabuleiro.
        """
        board_str = ""
        for row in self.board:
            board_str += ' | '.join(row) + '\n'
            if row != self.board[-1]:
                board_str += '–––' * 3 + '\n'
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
        Verifica se há um vencedor no jogo.
        Pra verificar o vencedor, conta quantas vezes o primeiro elemento da linha/coluna aparece nessa linha/coluna.
        Se o primeiro elemento aparecer o mesmo número de vezes que o tamanho do tabuleiro (self.size)
        e não for um espaço em branco, isso significa que um jogador preencheu toda a linha/colun com
        seu símbolo ('X' ou 'O'). Nesse caso, a função retorna o símbolo do jogador que ganhou.
        """
        for row in self.board:
            if row.count(row[0]) == self.size and row[0] != ' ':
                return row[0]

        for col in range(self.size):
            if all(self.board[row][col] == self.board[0][col] and self.board[0][col] != ' ' for row in range(self.size)):
                return self.board[0][col]

        for i in range(self.size):
            if all(self.board[i][i] == self.board[0][0] and self.board[0][0] != ' ' for i in range(self.size)):
                return self.board[0][0]

        for i in range(self.size):
            if all(self.board[i][self.size - 1 - i] == self.board[0][self.size - 1] and self.board[0][self.size - 1] != ' ' for i in range(self.size)):
                return self.board[0][self.size - 1]

        if all(cell != ' ' for row in self.board for cell in row):
            return 'Empate'

        return None

# Solicita ao usuário o tamanho do tabuleiro
try:
    size = int(input("Digite o tamanho do tabuleiro (n x n): "))
    if size < 3:
        raise ValueError("O tamanho mínimo do tabuleiro é 3.")
except ValueError as e:
    print("Entrada inválida. O tamanho do tabuleiro deve ser um número inteiro maior ou igual a 3.")
else:
    game = TicTacToeNxN(size)
    print("Começando o jogo da velha", size, "x", size)
    print(game)
    winner = None

    while winner is None:
        try:
            row = int(input("Digite a linha da sua jogada: "))
            col = int(input("Digite a coluna da sua jogada: "))
            if row < 0 or row >= size or col < 0 or col >= size:
                raise ValueError("Posição fora dos limites do tabuleiro.")
        except ValueError as e:
            print("Entrada inválida. Digite um número de linha e coluna válido.")
            continue

        if game.make_move(row, col):
            print(game)
            winner = game.check_winner()

            if winner == 'Empate':
                print("O jogo terminou em empate!")
            elif winner is not None:
                print("O jogador", winner, "venceu!")
        else:
            print("Essa posição já está ocupada. Tente novamente.")
