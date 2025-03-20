"""Tipos, módulos e funções no Python"""

"""
- As variáveis podem receber diversos tipos de dados, int(inteiros), float(números flutuantes/"quebrados"), str(strings/textos), bool(booleanos, True ou False),
list(listas), tuple(tuplas/listas imutáveis), set(conjuntos de elementos sem duplicatas), dict(dicionários), objetos de classes, entre outros...

- Operações de variáveis numéricas(ints e floats): + para somar, - para subtrair, * para multiplicar, / para dividir com resultado no formato float, 
// para dividir com resultado no formato int e % para calcular o módulo (resto da divisão).

Funções são blocos de código reutilizáveis que executam uma tarefa específica quando são chamados.

Módulos são os arquivos .py (respeitam o snake-case) que ficam num repositório (biblioteca) qualquer, eles podem conter funções, classes e constantes.

Ex: logica.py é um módulo da biblioteca learning
"""

"""Built-in modules e built-in functions"""
# Leia: do módulo random importe a função random
from random import random  # o módulo random é usado para gerar números pseudoaleatórios e realizar seleções aleatórias.

# para chamar uma função usa-se os "()"
aleatorio:float = random() # aleatorio irá receber da função random um número aleatório do tipo float entre 0 e 1... # usando typing float para facilitar legibilidade
print(aleatorio)
aleatorio = int(random()) # não vai adiantar realizar casting de aleatorio, pois a parte inteira dele é o 0
print(aleatorio) # saída será '0'
aleatorio = random() * 100 # isso retornará um número float com dois dígitos inteiros antes da vírgula
print(aleatorio)
# funções podem receber parâmetros, que são separados por ','
aleatorio = round(random() * 100, 2) # a built-in function round faz o arredondamento de um número, nesse caso, para duas casas depois da vírgula
print(aleatorio)
aleatorio = int(round(random() * 100, 2)) # esse casting retornará apenas a parte inteira do arredondamento
print(aleatorio) # nesse exemplo, caso o primeiro dígito seja 0, ele imprimirá apenas um dígito, cas contrário imprimirá dois dígitos

"""Funções personalizadas"""
# def é usado para definir uma função
def minha_funcao(): # função minha_funcao (respeita o snake-case)
    # bloco de código de minha_funcao
    pass # palavra-chave para ignorar um bloco de código

# Só é possível chamar uma função depois que ela declarada no código
# Um erro de execução ocorrerá se tentar chamar minha_funcao antes dela ser declarada
minha_funcao() # para chamar as funções personalizadas, nesse caso minha_funcao não fará e nem retornará nada pois ela não possui nenhum conteúdo exceto o pass

# exemplo de função que recebe dois parâmetros e retorna um valor
def soma_dois_valores(x:int, y:int):  # Para facilitar a leitura, podemos usar typing do Python para demonstrar ao dev qual tipo de variável essa função espera
    return x + y # return para declarar que a função retorna algum valor

# x e y são variáveis globais, acessíveis em qualquer bloco de código dentro do módulo após serem declaradas
x, y = 2, 3
soma_dois_valores(x,y) # chamando a função

def cara_ou_coroa(): # exemplo de função sem parâmetros mas que retorna um bool
    # moeda é uma variável local, só é acessível nesse bloco de código
    moeda = random() < 0.5 # ao usar operadores de comparação, a variável irá receber um bool
    return moeda

print("Vamos ver qual lado da moeda você vai tirar:")
print("Coroa") if cara_ou_coroa() else print("Cara") # Se cara_ou_coroa retornar verdadeiro, exibe "Coroa", senão exibe "Cara"

continua = True 
while(continua):
    resposta = input("Você gostaria de jogar cara ou coroa mais uma vez? (S/N)\n")
    continua = True if 'S' in resposta else False
    if continua: print("Coroa") if cara_ou_coroa() else print("Cara")

mensagem = input("Qual a sua mensagem antes de finalizar?\n") # variável de escopo global

def exibe_mensagem(): # exemplo de função sem parâmetros e sem retorno
    global mensagem # use a palavra-chave 'global' para acessar e alterar o valor de uma variável global
    mensagem += " foi a sua mensagem."
    print(mensagem)

exibe_mensagem() # chamando função antes de encerrar

