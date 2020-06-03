# -*- coding: utf-8 -*-
"""
Clube de Python do dia 27/05/2020
Iniciativa da wtmcuritiba

Workflow inicial para introduzir tarefas prévias à análise de conjuntos pequenos e médios de dados em python (básico)
Conjunto de dados: Gender Equality Index e Dados Associados (European Institute for Gender Equality)
"Belgium":"BE","Greece":"EL","Lithuania":"LT","Portugal":"PT","Bulgaria":"BG","Spain":"ES","Luxembourg":"LU","Romania":"RO","Czechia":"CZ","France":"FR","Hungary":"HU","Slovenia":"SI","Denmark":"DK","Croatia":"HR","Malta":"MT","Slovakia":"SK","Germany":"DE","Italy":"IT","Netherlands":"NL","Finland":"FI","Estonia":"EE","Cyprus":"CY","Austria":"AT","Sweden":"SE","Ireland":"IE","Latvia":"LV","Poland":"PL", "United Kingdom":"UK"}

@author: sanchesdeangelo@gmail.com (Ana)  
- telegram: @anaedeangelo
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm



######### 1. Criação de DataFrames a partir de listas ou de dicionários ##########

cadastro = [['Joana', 'Equatoriana', 3334444], ['Cláudia', 'Argentina', 22244455], ['Renata', 'Brasileira', 995544333]]

dfcadastro = 

cadastrodic = {'Nome': ['Joana', 'Claudia', 'Renata'], 'Nacional':['Equatoriana', 'Argentina', 'Brasileira'], 'Telefones':[3334444, 22244455, 995544333]}

dfcadastro2 = 





###########   2. Utilizando uma base públicamente disponível   ###########
#dados públicos -- que nem sempre (nunca) virão limpos e lindos 


url = "https://eige.europa.eu/sites/all/modules/custom/eige_gei/app/content/downloads/gender-equality-index-2005-2010-2012-2015-217.xls"

dadosteste = 

dados = pd.ExcelFile(url)  #Lê o excel - considerando a estrutura em planilhas

######### 3. Trabalhando com dados excel (ou csv) e organizando-os em DataFrames ##########

nomes_planilhas = dados.sheet_names
planilhas = dict()

for n in nomes_planilhas:
    df = pd.read_excel(dados, sheet_name = n, header = 0)
    planilhas[n] = df

print(planilhas)
print(nomes_planilhas)





######## 4. Explorando brevemente um dos dataframes e SUBSETS com os dados de 2005 ######## 

dados2005 = planilhas['2005']
dados2005.info()
dados2005.head(2)
list(dados2005.columns)


dados2005['Gender gap metric'] #uma coluna e todas as linhas 
dados2005[7:20] # as linhas desde 7 até 19 e todas as colunas


dados2005.loc[]  # loc seleciona UMA OU MAIS colunas por atributos textuais e por linhas
dados2005.iloc[]


dados2005 = dados2005.rename(dados2005.iloc[0, ], axis = 1, inplace = False)
dados2005 = dados2005.drop([0], axis = 0, inplace = False)




######### 5. Mais subsets e descrições gerais com os dados de 2005 #########

list(dados2005.columns)

interess = ['Country', 'Gender Equality Index', 'Mean monthly earnings (PPS)', 'Share of ministers (%) W', 'Share of ministers (%) M']

selecao = dados2005.loc[2:29, interess]

pd.set_option('display.max_columns', 300) #expandir a exibição de colunas

selecao.mean()
selecao.std()
selecao.median()
selecao.max() #FALÁCIA!!!! voltemos ao dataframe

selecao[]   # conferir o valor de UK! busca os valores de todas as colunas, apenas para o UK
selecao[].max() # valor máximo da coluna Gender Equality

selecao[]   #busca os valores para todas as colunas para o máximo para Gender Equality


###### INTERVALO #####



######### 6. Preparar para unir com dados de outros dfs (todos os anos), para analisar diferentes anos PARTE 1 - preparação #########
######### Criar uma pequena série histórica para a variável Gender Equality Index ###########

dados2010 = planilhas['2010']
dados2012 = planilhas['2012']
dados2015 = planilhas['2015']
dados2017 = planilhas['2017']

gei2010 = dados2010.rename(dados2010.iloc[0,], axis = 1, inplace = False).iloc[2:29, 0:2]


'''

ALERTA DE TAREFA REPETITIVA
se vamos repetir processos em mais de um conjunto de dados, porque não criamos uma função?

'''

#criar um novo dicionário com as alterações que devem ser aplicadas aos dados de todos os anos, ou seja, todos os dataframes
planilhasnovo = dict()

def preparo(lista):
    for l in lista:
        dadosano = 
        dadosano = dadosano.rename(dadosano.iloc[0,], axis = 1, inplace = False).iloc[2:29, 0:2]
        planilhasnovo[l] = dadosano
    return(planilhasnovo)

# Aplicando a função criada na lista de dfs



######### 7. Analisar o mesmo parâmetro em diferentes anos PARTE 1 #########
######## concat ########

geigeral = planilhasnovo['2005']  #planilha base, à qual uniremos as outras!
novosnomes = 

for i in nomes_planilhas[2:]:
    geigeral = pd.concat([geigeral, planilhasnovo[i].iloc[:, 1]], axis = 1)      #sobrescrevendo a geigeral a cada for

geigeral.set_axis(novosnomes, axis = 1, inplace = True)
geigeral



######### 8. Sorts e Plots simples #########


geigeral.index = geigeral['Country']  # da mesma forma que setamos os nomes das colunas, setamos índices para as linhas
geigeral.drop(['Country'], axis = 1, inplace = True)


geigeral.plot # básico linhas
geigeral.plot.area()  #area
geigeral.plot.barh()  #barh 


geigeral['Medias'] = geigeral.iloc[:, 1:].mean(axis = 1)  #cria nova coluna com dados descritivos


plt.figure()
geigeral['Medias'].plot.barh()

plt.figure()
geigeral['Medias'].plot.hist(color = 'purple')



plt.figure()
cm.datad.keys() #paletas de cores (colormaps)
graf = geigeral['Medias'].plot(kind = 'barh', title = "Média histórica - Gender Equality Index", color = cm.datad['Spectral'])


graf.vlines(geigeral['Medias'].mean())
graf.axis()
limites = list(graf.get_ylim())
#graf.vlines(geigeral['Medias'].mean(), limites[0], limites[1])


###########

# noções sobre os pais mais e menos desiguais
# dois plots distintos na mesma figura

menores = geigeral.sort_values(by = 'Medias', ascending = True).head(5).iloc[:, 0:-1]
maiores = geigeral.sort_values(by = 'Medias', ascending = False).head(5).iloc[:, 0:-1]

menores.plot()

menores2 =       #mudar forma
maiores2 =       #mudar forma


novafig, elementos = 

elementos[0].plot(maiores2)
elementos[0].legend(maiores2.columns)
elementos[0].set_title('Países com maiores índices de igualdade de gênero - EU')

#plot de baixo


plt.tight_layout()

#no mesmo gráfico


maior = maiores2.plot.line(title = 'Países com maiores índices de igualdade de gênero - EU')
menores2.plot.line(ax = maior, title = 'índices de igualdade de gênero - EU')




'''
"Belgium":"BE","Greece":"EL","Lithuania":"LT","Portugal":"PT","Bulgaria":"BG","Spain":"ES",
"Luxembourg":"LU","Romania":"RO","Czechia":"CZ","France":"FR","Hungary":"HU","Slovenia":"SI",
"Denmark":"DK","Croatia":"HR","Malta":"MT","Slovakia":"SK","Germany":"DE","Italy":"IT",
"Netherlands":"NL","Finland":"FI","Estonia":"EE","Cyprus":"CY","Austria":"AT","Sweden":"SE",
"Ireland":"IE","Latvia":"LV","Poland":"PL", "United Kingdom":"UK"
    
'''