import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(0,101)
    total_de_tentativas = 0
    pontos = 1000

    #rodada = 1

    print("Qual o nivel de dificuldade?")
    print("(1) Fácil  (2) Médio  (3) Difícil")

    nivel = int(input("Informe o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
    #while(rodada <= total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = input("Digite um número entre 1 e 100: ")
        chute = int(chute)

        if(chute < 1 or chute > 100):
            print("Você precisa digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        #rodada = rodada + 1

    print("Fim do jogo, o número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))

#Testa se o programa é chamado da linha de comando
if(__name__) == "__main__":
    jogar()