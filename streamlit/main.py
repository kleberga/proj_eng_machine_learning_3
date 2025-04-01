import streamlit as st
import requests

st.markdown("""
## Projeto da disciplina de Engenharia de Machine Learning [25E1_3]
            
### Aplicativo para realizar as projeções de arremessos do Kobe Bryant
""")

latitude = st.number_input("Latitude do estádio em que o jogo foi realizado:", min_value=-90, max_value=90)
longitute = st.number_input("Longitude do estádio em que o jogo foi realizado:", min_value=-180, max_value=180)
minutes_remaining = st.number_input("Quantidade de minutos que faltam para o período do jogo terminar (mín: 0 e máx: 12):", min_value=0, max_value=12)
period = st.number_input("Período do jogo (incluindo prorrogação)(mín: 1 e máx: 7):", min_value=1, max_value=7)
playoffs_string = st.radio("O arremesso foi realizado em jogos de playoffs?", options=["Sim", "Não"])
shot_distance = st.number_input("Distância do arremesso em relação à cesta (em metros) (mín: 0 e máx: 23):", min_value=0, max_value=23)

def projecao(dados):
    payload = [
            list(dados.values())
    ]
    response = requests.post(
        url="http://127.0.0.1:5001/invocations",
        json={
            'inputs': payload
        }
    )
    resultado = response.json()
    return resultado['predictions'][0]

input_data = {
    "latitude": latitude,
    "longitude": longitute,
    "minutes_remaining": minutes_remaining,
    "period": period,
    "playoffs": 1 if playoffs_string == "Sim" else 0,
    "shot_distance": shot_distance
}

st.write("Dados de entrada:")
st.json(list(input_data.values()))

projecao_arremesso = projecao(input_data)

st.write(f"O arremesso foi bem sucedido: %s" %("Sim" if projecao_arremesso == 1 else "Não"))