import random
############################### MODO HUMANOxCOMPUTADOR ##################################################
while True:
    
    print("Bem vindo(a) ao jogo digital de Jokenpô!")
    escolha = print("Nesse jogo, você pode jogar de três modos: HUMANOxHUMANO, HUMANOxCOMPUTADOR, COMPUTADORxCOMPUTADOR")
    escolha1 = print("1. HUMANOxHUMANO")
    escolha2 = print("2. HUMANOxCOMPUTADOR")
    escolha3 = print("3. COMPUTADORxCOMPUTADOR")
    
    opcao = print(input("Escolha seu modo: "))

    while opcao == '1':
        jogada1 = input("pedra papel ou tesoura?: ").lower()

        if jogada1 == "pedra" or "papel" or "tesoura":
            jogada2 = input("pedra papel ou tesoura?: ").lower()

        if jogada1 == "pedra" and jogada2 == "papel":
                print("jogador 1 ganhou! ")
                
        elif jogada1 == "pedra" or "papel" or "tesoura":
             jogada2 = input("pedra papel ou tesoura? ").lower()

#############################################HUMANOvsHUMANO 2#############
while escolha == '1':
    jogada1 = input("Jogador 1: pedra, papel ou tesoura?: ").lower()
    jogada2 = input("Jogador 2: pedra, papel ou tesoura?: ").lower()
    if jogada1 == jogada2:
        print("Empate :(")
    elif (jogada1 == "pedra" and jogada2 == "tesoura") or (jogada1 == "papel" and jogada2 == "pedra") or (jogada1 == "tesoura" and jogada2 == "papel"):
        print("jogador 1 ganhou!")
    else:
        print("jogador 2 ganhou!")

###### MODO 2 (HUMANOxCOMPUTADOR)
while escolha == escolha2:
        print("1. Pedra")
        print("2. Papel")
        print("3. Tesoura")
        jogador = int(input("Digite o número de sua jogada: "))
        computador = random.randint(1,3)
        print(computador)
        if jogador == computador:
                print("Empate!")
        elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador ==2):
                print("Você venceu!!")
        else:
            print("Você perdeu!")
############################## COMPUTADOR X COMPUTADOR ############################################################

opcoes = ("pedra", "papel", "tesoura")
pontosComputador1 = 0
pontosComputador2 = 0
while True:
    if opcao == "3":
        print("\nModo: Computador vs Computador")
    computador1 = random.randint(1, 4)
    computador2 = random.randint(1, 4)

    if computador1 == 1:
        print("Jogada do Computador 1: Pedra")
    elif computador1 == 2:
        print("Jogada do Computador 1: Papel")
    elif computador1 == 3:
        print("Jogada do Computador 1: Tesoura")

    if computador2 == 1:
        print("Jogada do Computador 2: Pedra")
    elif computador2 == 2:
        print("Jogada do Computador 2: Papel")
    elif computador2 == 3:
        print("Jogada do Computador 2: Tesoura")

#1 pedra
#2 papel
#3 tesoura

    if computador1 == computador2:
        print("Empate!")
    elif (computador1 == 1 and computador2 == 3) or \
            (computador1 == 3 and computador2 == 2) or  \
            (computador1 == 2 and computador2 == 1):
            print("Computador 1 ganhou!")
            pontosComputador1 += 1
            #somar um no placar do pc 1
    else:
        print("Computador 2 ganhou")
        pontosComputador2 +=1
    x = input("Voce deseja continuar a jogar?")
    if x == "Sim" or x == "sim":
        continue
    y = input("Deseja ver o placar do jogo?")
    if y == "Sim" or y == "sim":
        print("Placar")
        print("Computador 1:", pontosComputador1)
        print("Computador 2:", pontosComputador2)
        print("Obrigada por jogar nosso Jokenpo!")
        print("Agradecimento de Alana, Brenda, Laura e Letícia")
        break
