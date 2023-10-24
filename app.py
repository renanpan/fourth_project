import streamlit as st
import pandas as pd
import plotly_express as px


car_data = pd.read_csv('/workspaces/fourth_project/vehicles.csv') # lendo os dados

if hist_button: # se o botão for clicado
         # escrever uma mensagem
         st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um histograma
         fig = px.histogram(car_data, x="odometer")
     
         # exibir um gráfico Plotly interativo
         st.plotly_chart(fig, use_container_width=True)