# -*- coding: utf-8 -*-
"""
Material prévio de revisão de conceitos - 
Clube de Python 
@author: sanchesdeangelo@gmail.com (Ana)  - telegram: @anaedeangelo

"""

####
#PACOTES (pastas)
    #MÓDULOS (arquivos .py)
        #FUNÇÕES 
        #VARIÁVEIS
        #CLASSES
        #ETC...


#####  1. INSTALL DE PACOTES 
# Pacotes são pastas com um conjunto de módulos. Cada módulo é um arquivo .py
# Python 2 ou superior já vem com pacote voltado à instalação e atualização de pacotes. Ele se chama PIP.

# Para instalar um pacote, digite no console do spyder: 
pip install nomedopacote

# Para instalar um pacote, digite em uma célula do colab: 
!pip install nomedopacote

#No caso de ter instalado o python a partir do Anaconda, muitos pacotes mais conhecidos já vêm instalados, aí basta importá-los no seu código!



#####  2. IMPORT DE PACOTES E MÓDULOS

# Uma vez instalado, seu pacote deve ser previamente importado no código da seguinte maneira:
import pacote     

# ou é possível apelidar o pacote: 
import pacote as pc
 
# Para importar apenas um módulo de um pacote:
from pacote import modulo

#para utilizar um módulo especifico do pacote:
pacote.modulo(parametros)

#ou utilizar um modulo diretamente:
modulo(parametros)

#ou aplicar uma funcao/classe do módulo já importado a uma estrutura de dados para o qual foi feito.
objeto.modulo(parametros)



#####  3. FUNÇÕES 

#  As funções são executadas e retornam o resultado. Elas podem ser criadas dessa forma: 
def funcao(parametro1, parametro2):
    objeto = parametro1 + parametro2
    return(objeto)



##### 4. ESTRUTURAS BÁSICAS (LISTAS)
#4.1. LISTAS - INDICADOR --> []    colchetes

#Há duas formas básicas de criar uma lista vazia:
lista = []
lista = list()   #classe

# ou a partir de objetos pre-existentes
# modo 1
t = 7
y = 78
v = 'test'
lista2 = [t, y, v]

#modo2
objeto = 'palavra'  #objeto iterável
lista = list(objeto)    #aplicando a classe list() a esse objeto iterável e mudando sua forma para list


#4.2. ACESSANDO ELEMENTOS DA LISTA
#a forma mais simples de acesso é a partir do índice posicional
#lembrando que em python começa no 0

lista2[1]
lista2[0:2] # sempre os intervalos desse tipo são abertos no último termo, ou seja, não contém o último valor

#4.3. INSERIR ELEMENTOS NO FINAL DA LISTA (INCLUSIVE OUTRAS LISTAS)
elemento = 657
lista2.append(elemento)

lista3 = [543, 65, 78, 987]

[lista2.append(i) for i in lista3]     #list comprehension  --- uma forma bem fast-forward de resolver problemas de iterações com lista


#4.4. DELETAR UM ELEMENTO DA LISTA

del lista2[1]     #remove o segundo elemento
lista2.remove('test')       #remove o item por ele mesmo, sem indexação
lista2.pop(5)            #remove pelo index e printa o que foi removido 
lista2.clear()             #esvazia a lista




##### 5. ESTRUTURAS BÁSICAS (DICIONÁRIOS)
#5.1. DICIONÁRIOS - INDICADOR --> {}      chaves

#duas formas de criar um dic. vazio:
dici1 = {}
dici2 = dict() classe

#ou a partir de objetos iteraveis pré-existentes
paises = [["Belgium","BE"],["Greece","EL"],["Lithuania","LT"],["Portugal","PT"],["Bulgaria","BG"],["Spain","ES"],["Luxembourg","LU"],["Romania","RO"],["Czechia","CZ"],["France","FR"],["Hungary","HU"],["Slovenia","SI"],["Denmark","DK"],["Croatia","HR"],["Malta","MT"],["Slovakia","SK"],["Germany","DE"],["Italy","IT"],["Netherlands","NL"],["Finland","FI"],["Estonia","EE"],["Cyprus","CY"],["Austria","AT"],["Sweden","SE"],["Ireland","IE"],["Latvia","LV"],["Poland","PL"],["United Kingdom","UK"]]
paises = dict(paises)

#5.2. ESTRUTURA E INDEXAÇÃO
#{key:value}     chave:valor
dictexemplo = {1: 'teste1', 2: 'teste2', 3: 'teste3'}
dictexemplo2 = {'teste1':1, 'teste2':2, 'teste3':3}

dictexemplo2['teste1']     #pela chave entre colchetes, retorna o value

#5.3. ADIÇÃO E DELETE DE ELEMENTOS
dictexemplo2['teste1']

dictexemplo2['teste4'] = 4
del dictexemplo2['teste4']

dictexemplo2['teste4'] = 4
dictexemplo2.pop('teste4')
