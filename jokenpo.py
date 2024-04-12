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

