from dash import Dash, html, dcc
import plotly.express as px
import json
import pandas as pd

# Retorna um dicionario com dataframes para cada bloco e andar
# com o padrão de chave BLOCO_andar.
def montar_dataframes(nome_arquivo):
    with open('dados_tratados/' + nome_arquivo) as f:
        dados = json.load(f)
        f.close()

    # 'AB_terreo', 'AB_f1', 'AB_f2', 'C_terreo', 'C_f1', 'C_f2', 'D_terreo', 
    # 'D_f1', 'D_f2', 'E_terreo', 'E_f1', 'E_f2', 'E_f3', 'E_f4']
    data_frames = {}

    for chave_bloco in dados:
        andar = dados[chave_bloco]
        for chave_andar in andar:
            dt = pd.DataFrame(andar[chave_andar])
            data_frames[f'{chave_bloco}_{chave_andar}'] = dt

    return data_frames


data_frames = montar_dataframes('20_10_noite_tratado.json')

print(data_frames)

# df = pd.DataFrame(dados['AB']['terreo'])

# print(df.count())

# fig = px.bar()

# # fig0 = px.bar(df_andares[0], x="Ponto de Acesso", y="Sinal", color='Qualidade', color_discrete_map={
# #     'Boa': '#00CC96',
# #     'Média': '#FECB52',
# #     'Ruim': '#EF553B'
# # })

# app = Dash(__name__)
# app.layout = html.Div(children=[
#     dcc.Graph(
#         id='grafico-pa-bloco-e-t',
#         figure=fig,
#         style={'width': '500px'}
#     ),
# ])

# if __name__ == '__main__':
#     app.run(debug=True)