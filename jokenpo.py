import random
##menu
print("1, 2, 3, 4")
escolha = input("escolha: ")

##humano vs humano
while escolha == '1':
    jogada1 = input("pedra papel ou tesoura?: ").lower()

    if jogada1 == "pedra" or "papel" or "tesoura":
        jogada2 = input("pedra papel ou tesoura?: ").lower()

        if jogada1 == "pedra" and jogada2 == "papel":
                print("jogador 1 ganhou! ")
                