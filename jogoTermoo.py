import random

reset_cor = '\033[0;0m'
letra_inexiste = '\033[40m'     # -> fundo preto
letra_pos_errado = '\033[43m'   # -> fundo amarelo
letra_pos_correta = '\033[42m'  # -> fundo verde

palavras = [
    "abate", "beijo", "cerca", "dente", "erva", "falar", "girar", "hotel", "igreja", "junto",
    "karma", "lua", "mover", "nariz", "ouvir", "papel", "queim", "rosa", "sabor", "trem",
    "urso", "vapor", "xadrez", "yacht", "zebra",
    "acaso", "bravo", "cinto", "dedos", "estil", "fugir", "globo", "humor", "imagem", "jurar",
    "kilo", "lindo", "marco", "ninho", "orval", "paz", "quase", "risco", "salto", "toco",
    "unha", "varar", "xerox", "yoga", "zombar"
]

# Escolhe uma palavra aleatoriamente da lista
termo = random.choice(palavras).upper()
game_over = False
chances = 6

print("------------------------------------ INSTRUÇÕES ------------------------------------")
print("Você deve escolher uma palavra com até 05 letras (letras excedentes serão ignoradas)")
print(letra_pos_correta + "T" + reset_cor + "URMA -> a letra 'T' faz parte da palavra e está na posição correta")
print("VI" + letra_pos_errado + "O" + reset_cor + "LA -> a letra 'O' faz parte da palavra mas em outra posição")
print("PUL" + letra_inexiste + "G" + reset_cor + "A -> a letra 'G' não faz parte da palavra")
print("------------------------------------------------------------------------------------")

while not game_over:
    display = []
    chute = str(input("Digite uma palavra com 5 letras: "))
    # converte o input para CAIXA ALTA e ignora caracteres depois da 5ª posicao (palavras somente com 5 letras)
    chute = chute.upper()[:5]
    chances -= 1

    if chances == 0:
        print("Acabaram as chances")
        game_over = True

    elif chute == termo:
        print("Parabéns, voce acertou o termo!")
        print(letra_pos_correta + chute + reset_cor)
        game_over = True

    else:
        i = 0
        for c in chute:
            display.append(c)
            #se o caracter não existe no termo
            if c not in termo:
                display[i] = letra_inexiste + display[i] + reset_cor

            #se o caracter existe e está na posição correta em relação ao termo
            elif display[i] == termo[i]:
                display[i] = display[i] = letra_pos_correta + display[i] + reset_cor

            #se o caracter existe, mas está na posição errada em relação ao termo
            else:
                display[i] = display[i] = letra_pos_errado + display[i] + reset_cor
            i += 1

        for c in display:
            print(c, end='')
        print("\n")