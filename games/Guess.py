print("-----------------------------------------------------------")
print("|    _______                 ________   _____    _____    |")                               
print("|   |            |       |  |          |        |         |")        
print("|   |     _____  |       |  |_____     |_____   |_____    |")
print("|   |      |  |  |       |  |                |        |   |")      
print("|   |______|     |_______|  |________  ______|  ______|   |")        
print("|                                                         |")
print("-----------------------------------------------------------")

print("Seja bem vindo ao Guess, um jogo de adivinhação para você e seus amigos se divertirem tentando adivinhar \n palavras aleatórias.\n\n")

while True:
    nomeUsuario = input("Poderia me falar seu nome? \n")
    if nomeUsuario.isalpha():
        break
    else:               #Verificando se o nome digitado é um caracter alfabético
       print("Por favor, digite um nome válido. ")

idadeUsuario = ""

while True: 
     
    try: #Verificando se a idade digitada é um número inteiro
        idadeUsuario = int(input("Pode me falar a sua idade? \n"))
        break
    
    except ValueError:
        print("Por favor, insira um número válido para a idade.")
  
 # Aqui você pode tomar outras ações, como exibir uma mensagem de erro ou sair do programa
if idadeUsuario <= 17:
            print("Ahhhh, infelizmente não poderemos jogar juntos... Quando você fizer 18 anos, você volta aqui para nos divertirmos.")
            exit()
elif idadeUsuario >= 18:
            print("Beleza " +nomeUsuario+ ", vamos começar!!!")
