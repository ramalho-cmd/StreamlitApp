
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

@st.cache_data
def carregar_dados():
    df = pd.read_csv(r'C:\Users\pauli\OneDrive\Documentos\GitHub\StreamlitApp\StreamlitApp\base_dados.csv')
    return df 

st.write("""# Busque as musicas mais tocadas da época:""")
st.write("""## É só informar o mês e o ano!""")

mes = st.selectbox('Mês:',['1','2','3','4','5','6','7','8','9','10','11','12'])
ano = st.text_input('Ano:')
busca = mes + "/" + ano

df = carregar_dados()
dft = df[df['Data_abr'] == busca]
dft = dft[['Titulo','Autor','Spotify_link']]
dft = dft.reset_index(drop=True)
dft.index = dft.index+1

st.write(dft)
