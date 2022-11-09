def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo de Forca***!")
    print("*********************************")

    palavra_secreta = "banana".upper()  # aceitar letras maiusculas
    letras_acertadas = ["_" for letra in palavra_secreta]



    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    # enquanto não enforcou e nao acertou
    while (not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute= chute.strip().upper()  # aceitar letras maiusculas

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1   # incrementar
        else:
            erros += 1  # incrementar

        enforcou = erros == 6   # quando chegar 6 vezes stop
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")


    print ("Fim do jogo")



if (__name__ == "__main__"):
    jogar()
