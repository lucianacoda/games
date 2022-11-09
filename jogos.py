import forca2
import Adivinhacao5

def escolhe_jogo():

    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca  (2) Adivinhação")

    jogo = int(input ("Qual jogo deseja jogar?"))

    if (jogo == 1):
        print ("Jogando Forca")
        forca2.jogar()
    elif(jogo == 2):
        print ("Jogando Adivinhação")
        Adivinhacao5.jogar()

if (__name__ == "__main__"):
   escolhe_jogo()
