import Forca # the Hangman game
import Guessing # the Guessing game

def escolhe_jogo():
    print("*****************************")
    print("******Choose your game!******")
    print("*****************************")

    print("(1) Hangman (2) Guessing game")

    jogo = int(input("which game?"))

    if(jogo == 1):
        print("playing Hangman")
        Forca.jogar()
    elif(jogo == 2):
        print("playing Guessing game")
        Guessing.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
