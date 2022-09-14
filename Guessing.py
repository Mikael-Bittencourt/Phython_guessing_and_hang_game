import random

def jogar():

    print("*****************************")
    print("Welcome to the guessing game")
    print("*****************************")

    numero_secreto = random.randrange(1,101)
    Total_de_tentativas = 0
    pontos = 1000

    print("What level of difficulty?")
    print("(1) Easy (2) Medium (3) Hard")

    nivel = int(input("Choose a level: "))

    if(nivel == 1):
        Total_de_tentativas = 20
    elif(nivel == 2):
        Total_de_tentativas = 10
    else:
        Total_de_tentativas = 5

    for rodada in range(1, Total_de_tentativas + 1):
        print("Attempt {} of {}".format(rodada, Total_de_tentativas))

        chute_str = input("Choose a number between 1 to 100: ")
        print("You chose ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("You must choose a number between 1 to 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("You guessed correctlyand got {} points!".format(pontos))
            break
        else:
            if (maior):
                 print("You guessed wrong! your guess was higher than the secret number.")
            elif (menor):
                 print("You guessed wrong! your guess was lower than the secret number.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("End of game")

if(__name__ == "__main__"):
    jogar()