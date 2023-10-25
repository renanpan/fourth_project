import streamlit as st
import pandas as pd
import plotly_express as px


car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') #criar um botão

print(car_data.head())

if hist_button: # se o botão for clicado
         # escrever uma mensagem
         st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um histograma
         fig = px.histogram(car_data, x="odometer")
     
         # exibir um gráfico Plotly interativo
         st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar um gráfico de dispersão') #criar botão

if scatter_button:
        #escrever mensagem
        st.write("Criando um gráfico de dispersão com o conjunto de dados de anuncios de vendas de carros")

        #exibir o gráfico de dispersão entre preço e milhas
        fig = px.scatter(car_data, x="odometer", y="price")

        #exibir um gráfico plotly interativo
        st.plotly_chart(fig, use_container_width=True)
