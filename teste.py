"""Lógica básica do Python"""

nome = input("Digite um nome:") 
print("O nome é " + nome)
idade = int(input("Digite uma idade:")) # input retorna str, precisa converter para int
print("Tem " + str(idade) + " anos")

if idade > 18: # condicional
    print(nome + "é maior de 18") # py é sensível a indentação
elif idade == 18:
    print(nome + "já pode ser preso")
else: 
    print(nome + "menor de 18")

print("Vou soletrar seu nome:")
for index, letra in enumerate(nome): # enumera as letras do nome
    print("Posição " + str(index) + ": " + letra)
    
print("última letra: " + letra) # último valor alocado para letra no laço for
    
print("Vou contar de 0 a 10:")

for i in range(11): # itera um intervalo
    print(i)

continua = True # sinalizador
while(continua):
    resposta = input("Quer continuar(S/N)?\n")
    continua = True if resposta == 'S' else False # Ternário
    
count = 10
print("Vou contar de 10 a 0:")
while(count >= 0):
    print(count) 
    count -= 1 # count = count - 1