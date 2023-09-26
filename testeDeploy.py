import streamlit as st
from PIL import Image
import requests
import matplotlib.pyplot as plt


# brew install gh
# github key:   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
# github key2:  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
# Injetando CSS para fazer o dashboard ocupar toda a tela
st.markdown(
	"""
	<style>
		.reportview-container {
			max-width: 100%;
			flex: 1;
		}
		.block-container {
			max-width: 100%;
			padding: 0;
		}
	</style>
	""",
	unsafe_allow_html=True,
)

hist = """
A linguagem de programação Python foi criada por Guido van Rossum e teve sua primeira versão lançada em 1991. Inspirada em linguagens como ABC e Modula-3, Python foi desenvolvida com o objetivo de ser simples de ler e escrever, promovendo a legibilidade do código e permitindo que programadores expressassem conceitos de forma concisa. Ao longo dos anos, Python evoluiu e ganhou popularidade em diversas áreas, desde desenvolvimento web até ciência de dados, aprendizado de máquina e automação.

A linguagem é conhecida por sua filosofia que enfatiza a simplicidade e a elegância, encapsulada no "Zen do Python", uma coleção de 19 "aforismos" que capturam a essência do design da linguagem. Python tem uma grande comunidade de desenvolvedores e uma vasta biblioteca padrão, além de milhares de bibliotecas de terceiros disponíveis, o que contribuiu para sua adoção em larga escala em diversas indústrias e campos acadêmicos.
"""

codIn = """
# Lendo strings
str = input("Digite seu nome: ")

# Lendo valores numéricos
val_int = int(input("Digite um valor inteiro: "))
val_float = float(input("Digite um valor Real: "))
"""
codOut = """
print("Valor digitado:", val_int)

print("Valor digitado: %d.2", val_float)

print("Valor: {:.2f}".format(val_float))

print("x={} e y={}".format(val_int, val_float))

print("Olá, {}!".format(nome))



"""

desv = """
if val > 0:
	print("Valor positivo")
elif val < 0:
	print("Valor negativo")
else:
	print("Valor = 0")
"""

para = """
for i in range(100):
	print(i)

for i in range(50, 100, 2):
	print(i)

vet = [1, 2, 3, 4, 5, 6]
for i in vet:
	print i
"""

enq = """
while i < 11:
	print(i+1)

vet = [1, 2, 3, 4, 5, 6]
while i in vet:
	print(i*2)

str = "texto"
while i in str:
	if i in [a, e, i, o, u]:
		print i
"""

st.title(":rainbow[Python DashBoard]")
st.header("Histórico:")
ca1, ca2 = st.columns([3, 1])
image = Image.open('guido.jpeg')

if 'carregar' not in st.session_state:
	st.session_state.carregar = True
	
if 'github_stats' not in st.session_state:
	st.session_state.github_stats = {}

with ca1:
	st.info(hist)
	recarregar_grafico = st.button('Recarregar Gráfico')
with ca2:
	st.image(image, caption='Guido Van Rossum')

c1, c2, c3 = st.columns([4, 1, 2])
with c2:
	st.header("Sintaxe:")
	option = st.radio("selecione", ["Entrada", "Saída", "Desvio Condicional", "Laço FOR", "Laço WHILE"], label_visibility="collapsed")
	
with c3:
	with st.container():
		if option == "Entrada":
#			st.subheader("Entrada")
			st.code(codIn, language="python", line_numbers=False)
		elif option == "Saída":
#			st.subheader("Saída")
			st.code(codOut, language="python", line_numbers=False)
		elif option == "Desvio Condicional":
#			st.subheader("Desvio Condicional")
			st.code(desv, language="python", line_numbers=False)
		elif option == "Laço FOR":	
#			st.subheader("Laço FOR")
			st.code(para, language="python", line_numbers=False)
		elif option == "Laço WHILE":
#			st.subheader("Laço WHILE")
			st.code(enq, language="python", line_numbers=False)

if recarregar_grafico:
	st.session_state.carregar = True

if st.session_state.carregar :
	# Número de repositórios no GitHub que usam Python
	github_stats = {}
	
	for linguagem in ['python', 'javascript', 'java', 'c', 'c#', 'typescript', 'c++', 'php']:
		response = requests.get(f"https://api.github.com/search/repositories?q=language:{linguagem}", headers={"Authorization": "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"})
		if response.status_code == 200:
			github_data = response.json()
			total_count = github_data.get('total_count', 0)
			github_stats[linguagem] = total_count
	st.session_state.github_stats = github_stats
	#else:
	#	st.write(f"Erro ao buscar dados para {linguagem}. Código de status HTTP: {response.status_code}")
	with c1:
		plt.figure(figsize=(6, 2))
		plt.bar(st.session_state.github_stats.keys(), st.session_state.github_stats.values(), color=['blue', 'green', 'red', 'purple', 'yellow', 'orange', 'pink', 'magenta'])
		plt.xlabel('Linguagens de Programação')
		plt.ylabel('Número de Repositórios')
		plt.title('Número de Repositórios no GitHub por Linguagem')
		
		st.pyplot(plt)
		st.session_state.carregar = False

			