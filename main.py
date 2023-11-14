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
print(data_frames['E_f1'])

def montar_grafico_contagem_pa():
    count_dict = {}
    for key in data_frames:
        count_dict[key] = data_frames[key]['PA'].count() 

    count_df = pd.DataFrame(list(count_dict.items()), columns=['Bloco/Andar', 'Contagem de PA'])

    fig = px.bar(count_df, x='Bloco/Andar', y='Contagem de PA', title='Número de pontos de acesso por Bloco/Andar')

    return fig

def montar_grafico_media_pa():
    count_dict = {}
    for key in data_frames:
        sinal_df = pd.to_numeric(data_frames[key]['Sinal'])
        count_dict[key] = sinal_df.mean() 

    count_df = pd.DataFrame(list(count_dict.items()), columns=['Bloco/Andar', 'Média sinal'])
    
    
    fig = px.bar(count_df, x='Média sinal', y='Bloco/Andar', title='Media do sinal por Bloco/Andar', color='Bloco/Andar')

    return fig

fig = montar_grafico_media_pa()

app = Dash(__name__)
app.layout = html.Div(children=[
    dcc.Graph(
        id='grafico-pa-bloco-e-t',
        figure=fig,
        style={'width': '500px'}
    ),
])

if __name__ == '__main__':
    app.run(debug=True)