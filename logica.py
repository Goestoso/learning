"""Lógica básica do Python"""

# variável nome é um elemento que recebe algum valor específico 
nome = input("Digite um nome:") # built-in function (função interna do python) input() que congela a execução do código aguardando um valor de entrada no terminal (prompt)
print("O nome é " + nome) # print imprime uma saída textual no terminal
idade = int(input("Digite uma idade:")) # input retorna str, precisa converter (realizar casting) para int, logo use a built-in function int() 
print("Tem " + str(idade) + " anos") # Só é possível concatenar str com str, precisa realizar casting de idade para str usando function str()


"""Condicionais"""
# se idade maior que 18
if idade > 18:  # ':' determina um bloco de código
    # bloco de código da condicional if
    print(nome + "é maior de 18") # py é sensível a indentação de 4 espaços por bloco de código
# senão se igual a 18    
elif idade == 18: 
    # bloco de código da condicional elif
    print(nome + "já pode ser preso")
# senão
else: 
    # bloco de código da condicional else
    print(nome + "menor de 18")
    
    
"""Loops"""
print("Vou soletrar seu nome:")
# para cada index e letra na enumeração de nome # for
for index, letra in enumerate(nome): # enumera as letras do nome
    # bloco de código do loop for
    print("Posição " + str(index) + ": " + letra)
    
print("última letra: " + letra) # último valor alocado para letra no laço for
    
print("Vou contar de 0 a 10:")

# para cada número inteiro i num intervalo x
for i in range(11): # itera um intervalo, no qual 0 <= x < 10, ou seja, um intervalo de 0 a 10 (11 números)
    print(i)
    
# while
continua = True # sinalizador de verificação do loop
# Enquanto continua for verdadeiro
while(continua): 
    # bloco de código do loop while
    resposta = input("Quer continuar(S/N)?\n") # a variável resposta recebe um valor digitado 
    continua = True if resposta == 'S' else False # Ternário, continua recebe True se resposta for 'S', senão continua recebe False
    
count = 10 # delimitador
print("Vou contar de 10 a 0:")
while(count >= 0): # enquanto count for maior que e igual a 0
    print(count) 
    count -= 1 # count = count - 1, ou seja, variável count recebe ela mesma menos o valor 1