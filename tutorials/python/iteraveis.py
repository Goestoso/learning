"""Iteráveis no Python"""

"""
Os iteráveis são qualquer tipo de conjuntos de dados que nos permite percorrer (iterar) pelos seus elementos.
No Python, os iteráveis mais comuns são as strings, listas, tuplas, conjuntos e dicionários!
"""

"""Strings"""
texto = "Olá, mundo!" # Strings (str) são consideradas listas de caracteres, o que permite acessar cada caractere de uma variável do tpo string
print(texto[0]) # exibe o primeiro caractere
n_caracteres = len(texto) # captura a quantidade de caracteres
"""Interpolação de strings"""
# Usando interpolação, não há a necessidade de converter as variáveis, pois a interpolação faz um casting automático
print("{} tem {} caracteres.".format(texto, n_caracteres)) # cada {} representa os locais da interpolação, que ocorrerá na ordem de variáveis passadas para o método .format().
"""f-strings"""
print(f"Soletrando o texto {texto}:") # cada {} pode ser preenchido com uma variável, o Python automaticamenbte fará a interpolação.
for index, char in enumerate(texto): # a built-in function enumera qualquer tipo de iterável e permite acessar a posição index de cada elemento
    print(f"Na posição {index}: {char}")
outro_texto = "7 = sorte, 6 = azar"
dizima_periodica:float = 2/3 # isso vai resultar numa dízima periódica 0,6666...
print(f"{dizima_periodica} é uma dízima periódica.")
# usando formatação de type f (float) 
print(f"{dizima_periodica:.2f} é a dízima perídica considerando 2 casas depois da vírgula.") # :.xf (x = qualquer int) para formatar um número x de casas depois da vírgula. 
x = 123.456
print(f"{x} é o valor d x, {x:7.2f} é o valor de x com 7 caracteres de largura (espaçamento) e duas casas depois da vírgula.") # :x.f (x = qualquer int) para formatar x caracteres de largura. 
x = 2 
print(f"{x} é o valor de x, {x:02d} é valor de x com um zero à esquerda.") # :0xd (x = qualquer int) para formatar um número com x 0s à esquerda.
for char in outro_texto:
    if char.isnumeric(): print(f"{char} é número.") # verifica se é número
    elif char.isalpha(): print(f"{char} é letra.") # verifica se é do alfabeto
    else: print(f"{char} é espaço/pontuação.") # verifica se é alguma pontuação ou tabulação
lista = texto.split(" ") # converte uma str em uma lista conforme delimitador passado
print(lista)
texto = " ".join(lista) # para unir os elementos de uma lista em uma str
print(texto)

"""Listas"""
lista = [] # criando uma lista vazia
print(lista) # saída será '[]'
lista = [1,2,3,4,5] # criando uma lista de números
print(lista) # saída será '[1,2,3,4,5]'
print(lista[0]) # exibe o valor da primeira posição da lista
lista = ['Joao', 2, 'Maria', 4] # criando uma lista de números e strings
print(lista)
lista[1], lista[3] = "Marco", "Ana" # modificando os valores da lista na segunda posição e última posição 
print(lista)
"""As listas do Python são dinâmicas, ou seja, podem receber qualquer tipo de valor!"""
lista = list() # cria uma lista vazia também
lista.append(1) # adiciona um valor ao final da lista
lista.insert(0,0) # insere um valor na posição indicada, caso o index não exista, ocorerrá um erro de execução, nesse caso, insere na posição 0 o valor 0
lista.extend([2,3,4,5]) # extendendo os valores de uma lista com os valores de outro iterável
print(lista)
print(lista.pop()) # remove o último elemento da lista, pode receber a posição index do valor a ser excluído
lista.remove(0) # remove um valor específico da lista
lista.reverse() # inverte a lista
print(lista)
lista.sort() # reeordena a lista
print(lista)
print(len(lista)) # exibe a quantidade de elementos (comprimento) da lista
print(max(lista)) # exibe o valor máximo da lista
print(min(lista)) # exibe o valor mínimo da lista

"""Tuplas"""
tupla = () # criando uma tupla vazia
tupla = (1,2,3,4,5) # criando uma tupla de números
print(tupla) 
"""Diferente das listas, as tuplas são imutáveis, isso significa que seus valores são inalteráveis!"""
tupla = ("João", "Marcos", 1, 2, "Marcos") # criando uma tupla de números e strings
print(tupla.count("Marcos")) # exibe a quantidade de vezes que um elemento aparece na tupla
print(tupla.index(1)) # exibe o elemento da posição index passada
# Esses são os únicos métodos possíveis da tupla, outros métodos provocarão erros!
lista = list(tupla) # após converter uma tupla em lista, posso usar os métodos de lista

"""Conjuntos"""
conjunto = {} # criando um conjunto vazio
conjunto = {1,1,2,3,4,5,5} # criando um conjunto de números
print(conjunto) # saída será a a lista de números sem duplicatas (repetição)
"""Conjuntos são utilizado quando se quer obter valores únicos em um iterável!"""
n = 0
while(n < 11):
    conjunto.add(n) # vai adicionando elementos ao conjunto mas sempre garantindo que ele não é duplicata
    n += 1
print(conjunto)
conjunto.update([5,6,7,8,9,10,11,12]) # atualiza o conjunto com os valores do iterável, sem repetir valores
print(conjunto)
conjunto.discard(12) # discarta um elemento do conjunto, se o elemento não existir NÃO causa erro!
conjunto.remove(0) # remove um elemento do conjunto, se o elemento não existir causa erro!
print(conjunto.pop()) # remove o último elemento adicionado ao conjunto
print(conjunto)
conjunto_um = {0,1,2,3,4,5}
print(conjunto_um)
conjunto_dois = {4,5,6,7,8,9}
print(conjunto_dois)
print(conjunto_um.intersection(conjunto_dois)) # exibe os valores da intersecção dos conjuntos
print(conjunto_um.union(conjunto_dois)) # exibe os valores da união dos conjuntos
print(conjunto_um.difference(conjunto_dois)) # exibe os valores que estão no conjunto_um mas não no conjunto_dois
conjunto.clear() # esvazia o conjunto
print(conjunto)

"""Dicionários"""
dicionario = dict(chave="valor") # criando um dicionário usando dict
print(dicionario)
"""Dicionários são associações de chaves e seus respecitvos valores!"""
dicionario = dict(lista=[1,2,3,4,5]) # criando um dicionário com uma lista
print(dicionario)
dicionario.update(outra_lista=[6,7,8,9,10]) # adicionando mais uma lista para o  dicionario
print(dicionario)
dicionario["nome"] = "Marco Antônio Pereira" # adicionando um nome para o dicionario
print(dicionario)
print(dicionario.keys()) # exibe as chaves do dicionario
print(dicionario.values()) # exibe os valores do dicionario
print(dicionario.get("nome")) # exibe o valor da chave 'nome'
print(dicionario.items()) # exibe as chaves e valores do dicionario
outro_dicionario = {'chave': "valor"} # criando um dicionário usando {}
print(dicionario)
dicionario_copia = outro_dicionario.copy() # copia o dicionario para uma variável
print(dicionario_copia)
outro_dicionario = dicionario.fromkeys([1,2,3,4,5], "Segura o shape!") # cria um novo dicionário da lista de chaves com o valor definido
print(outro_dicionario)
print(dicionario.setdefault("nome", "Não encontrado!")) # Verifica se a chave já existe, se não existir irá criar uma chave com o valor definido
print(dicionario.setdefault("linguagem", "Não encontrado!"))
print(dicionario.popitem()) # remove a última chave adicionada ao dicionario
print(dicionario.pop('nome')) # remove a chave definida
for key, items in dicionario.items(): # percorrendo um dicionario pelas suas chaves
    print(f"Chave {key}:")
    for item in items: # percorrendo os valores (listas) das chaves
        print(f"{item}")
