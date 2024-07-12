import pandas
import bs4
import requests
import streamlit as st
import matplotlib.pyplot as plt


cabecalho = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}

url = 'https://cecijoias.com.br/product-category/gargantilha/'

resposta = requests.get(url , verify=False,headers=cabecalho)
sopa = bs4.BeautifulSoup(resposta.content,'html.parser')

lista_joias = []
lista_preco = []

texto = sopa.find_all('h3')
textop = sopa.find_all('bdi')

for i in texto :
    lista_joias.append(i.text)

for i in textop :
    lista_preco.append(i.text)

lista_joias.pop(0)

dicionario = dict(joias = lista_joias, preco = lista_preco)
dataframe = pandas.DataFrame(dicionario)

print(dataframe)


plt.figure(figsize=(15, 5))
plt.plot(lista_preco, lista_joias, 'o-r')
plt.show()


st.title("CECIJOIAS")
st.image("1.jpg", "Colar De Corrente Gargantilha Olho Tigre Facetado Folheado A Ouro")
st.image("2.jpg", "Colar Gargantilha Unaquita Trançado A Mao Folheado A Ouro")
st.image("3.jpg", "Colar Gargantilha Corrente Elo Portugues Coral Facetado Folheados A Ouro")
st.image("4.jpeg", "Colar Gargantilha De Elo Portugues, Sodalita E Lapis Lazuli Folheado A Ouro")
st.image("5.jpg", "Colar Gargantilha Turmalina Negra Elo Português Folheado A Ouro")
