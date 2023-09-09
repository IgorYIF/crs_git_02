import streamlit as st
import pandas as pd

vet = [0, 1, 2, 3, 'teste']
st.title("Teste de Streamlit")
st. info("Digite o valor desejado")
val1 = st.number_input("digite o valor da nota 1", 0.0, 10.0)
st.text(vet)
df = pd.DataFrame({'nota 1':[val1], 'nota 2':[val1], 'média':[(val1+val1)/2]})
df
