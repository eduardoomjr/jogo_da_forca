palavra="GIRAFA"
resposta=[]
erros=6
palpites=[]
dica="ANIMAL"

def preparacao():
    global palavra
    for i in range(len(palavra)):
        resposta.append("_ ")
        
def jogar():
    global resposta
    global erros
    global palpites
    if "".join(resposta) == palavra:
        return print("A palavra é",palavra,"Você acertou \O/")
    print("Letras que você ja palpitou",palpites)
    print("A palavra é um(a)",dica,"com",len(palavra),"letras","".join(resposta))
    print("Se quiser chutar a palavra, digite chutar")
    boneco()
    if erros != 0:
        palpite=input("Digite uma letra")
        palpite=palpite.upper()
        palpites.append(palpite)
        if palpite == "CHUTAR":
            palpite_chute=input("Digite o seu chute")
            palpite_chute=palpite_chute.upper()
            if palpite_chute == palavra:
                return print("A palavra é",palavra,"Você acertou \O/")
            else:
                return print("A palavra era",palavra,"Você errou")
        if palpite in palavra:
            for n in range(len(palavra)):
                if palpite == palavra[n]:
                    resposta[n] = palpite
            print("")
            print("Tem a letra",palpite)
            print("")
            jogar() 
        else:
            erros -= 1
            print("")
            print("Errou, não tem a letra",palpite)
            print("Você ainda tem",erros,"tentativas")
            print("")
            jogar()
    else:
        return print("Números de tentativas esgotadas.\n Você perdeu")
    
def boneco():
    if erros == 6:
        print("________    ")
        print("|      |    ")
        print("|           ")
        print("|           ")
        print("|           ")
    if erros == 5:
        print("________    ")
        print("|      |    ")
        print("|      O    ")
        print("|           ")
        print("|           ")
    if erros == 4:
        print("________    ")
        print("|      |    ")
        print("|      O    ")
        print("|      |    ")
        print("|           ")
    if erros == 3:
        print("________    ")
        print("|      |    ")
        print("|      O    ")
        print("|     /|    ")
        print("|           ")
    if erros == 2:
        print("________    ")
        print("|      |    ")
        print("|      O    ")
        print("|     /|\   ")
        print("|           ")
    if erros == 1:
        print("________    ")
        print("|      |    ")
        print("|      O    ")
        print("|     /|\   ")
        print("|     /     ")
    if erros == 0:
        print("________    ")
        print("|      |    ")
        print("|      O    ")
        print("|     /|\   ")
        print("|     / \   ")