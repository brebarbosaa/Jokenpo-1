import random

while True:
######### MENU ##################################################################################################

        print('''
╔╗──────────╔╗───╔╗
║╚╦═╦══╗╔═╦═╬╬═╦╦╝╠═╗╔═╗╔═╗
║╬║╩╣║║║╚╗║╔╣║║║║╬║╬║║╬╚╣╬║
╚═╩═╩╩╩╝─╚═╝╚╩╩═╩═╩═╝╚══╩═╝
────╔╗─────────╔╗
─╔╦═╣╠╦═╦═╦╦═╦═╣║
─╠╣╬║═╣╩╣║║║╬║╬║║
╔╝╠═╩╩╩═╩╩═╣╔╩═╬╣
╚═╝────────╚╝──╚╝''')

        print("Nesse jogo, você pode jogar de três modos: ")
        print("1. HUMANOxHUMANO")
        print("2. HUMANOxCOMPUTADOR")
        print("3. COMPUTADORxCOMPUTADOR")
        opcao = int(input("Escolha seu modo: "))
        
        opcoesMenu = 1, 2, 3
        ## se o user digitar outro número, mensagem de erro
        if opcao not in opcoesMenu:
                print("insira uma opção válida")
                break

####### MODO 1: HUMANOvsHUMANO ###################################################################################
        placar1Jogador1 = 0
        placar1Jogador2 = 0
        opcoesJogadas = 1, 2, 3

        while opcao == 1:
                print("1. Pedra")
                print("2. Papel")
                print("3. Tesoura")
                jogada1 = int(input("Jogador 1: digite o número de sua jogada: "))
                jogada2 = int(input("Jogador 2: digite o número de sua jogada: "))
                
                if jogada1 not in opcoesJogadas:
                        print("insira uma jogada válida!")
                        break
                if jogada2 not in opcoesJogadas:
                        print("insira uma jogada válida!")
                        break
                if jogada1 == jogada2:
                        print("Empate :(")
                elif (jogada1 == 1 and jogada2 == 3) or (jogada1 == 2 and jogada2 == 1) or (jogada1 == 3 and jogada2 == 2):
                        print("jogador 1 ganhou!")
                        placar1Jogador1 += 1
                else:
                        print("jogador 2 ganhou!")
                        placar1Jogador2 += 1
                ## perguntar se deseja continuar a jogar e mostrar o placar
                continuar1 = input("Voce deseja continuar a jogar? ").lower()
                if continuar1 == "sim":
                        continue
                elif continuar1 == "nao" or continuar1 == "não":
                        print("Obrigada por jogar nosso Jokenpô!")
                placar1 = input("Deseja ver o placar do jogo? ").lower()
                if placar1 == "não" or placar1 == "nao":
                        break
                elif placar1 == "Sim" or placar1 == "sim":
                        print("Placar: \n")
                        print("Jogador 1:", placar1Jogador1)
                        print(f"Jogador 2: {placar1Jogador2} \n")
                        print("Obrigada por jogar nosso Jokenpo!")
                        print("Agradecimento de Alana, Brenda, Laura e Leticia \n")
                        break

####### MODO 2 HUMANOxCOMPUTADOR ###################################################################################
        placar2Jogador = 0
        placar2Computador = 0
        opcoesJogadas = 1, 2, 3

        while opcao == 2:
                print("1. Pedra")
                print("2. Papel")
                print("3. Tesoura")
                jogador = int(input("Digite o número de sua jogada: "))
                if jogador not in opcoesJogadas:
                        print("insira uma jogada válida!")
                        break
                computador = random.randint(1,3)

                if computador == 1:
                        print("o computador jogou: Pedra")
                if computador == 2:
                        print("o computador jogou: Papel")
                if computador == 3:
                        print("o computador jogou: Tesoura")
                if jogador == computador:
                        print("Empate!")
                elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
                        print("Você venceu!!")
                        placar2Jogador += 1
                else:
                        print("Você perdeu!")
                        placar2Computador += 1
                ##### perguntar se o usuario deseja continuar 
                continuar2 = input("Voce deseja continuar a jogar? ")
                if continuar2 == "Sim" or continuar2 == "sim":
                        continue
                elif continuar2 == "nao" or continuar2 == "não":
                        print("Obrigada por jogar nosso Jokenpo!")
                placar2 = input("Deseja ver o placar do jogo? ")
                if placar2 == "não":
                        break
                elif placar2 == "Sim" or placar2 == "sim":
                        print("Placar: \n")
                        print("Jogador:", placar2Jogador)
                        print(f"Computador: {placar2Computador} \n" )
                        print("Obrigada por jogar nosso Jokenpo!")
                        print("Agradecimento de Alana, Brenda, Laura e Leticia \n")
                        break

######################### MODO 3 COMPUTADOR X COMPUTADOR ############################################################
        pontosComputador1 = 0
        pontosComputador2 = 0

        while opcao == 3:
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

                if computador1 == computador2:
                        print("Empate!")
                elif (computador1 == 1 and computador2 == 3) or  (computador1 == 3 and computador2 == 2) or (computador1 == 2 and computador2 == 1):
                        print("Computador 1 ganhou!")
                        pontosComputador1 += 1
                #somar um no placar do pc 1
                else:
                        print("Computador 2 ganhou!")
                        pontosComputador2 += 1
                ## perguntar se o jogador deseja continuar, e mostrar o placar
                continuar3 = input("Voce deseja continuar a jogar? ").lower()
                if continuar3 == "Sim" or continuar3 == "sim":
                        continue
                elif continuar3 == "nao" or continuar3 == "não":
                        print("Obrigada por jogar nosso Jokenpo!")
                placar = input("Deseja ver o placar do jogo? ")
                if placar == "nao" or placar == "não":
                        break
                elif placar == "Sim" or placar == "sim":
                        print("Placar: \n")
                        print("Computador 1:", pontosComputador1)
                        print(f"Computador 2: {pontosComputador2} \n")
                        print("Obrigada por jogar nosso Jokenpo!")
                        print("Agradecimento de Alana, Brenda, Laura e Leticia \n")
                        break
