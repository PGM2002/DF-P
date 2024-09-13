path = '/workspaces/DF-P/notebooks/10_Dataviz/data/gapminder.csv'

import pandas as pd

df = pd.read_csv(path)
print(df)

import streamlit as st
st.write(df)

lista_paises = df['country'].unique()
pais = st.selectbox(label='Elegir país', options=lista_paises)

mask = df['country'] == pais
dff = df[mask]

import plotly.express as px
fig=px.line(data_frame=dff, x= 'year', y='lifeExp')

st.plotly_chart(fig)
