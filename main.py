from dash import Dash, html, dcc
import plotly.express as px
import json
import pandas as pd

with open('blocoE.json', 'r') as json_bloco:
    andares = json.load(json_bloco)

media = []
# 0 -> Térreo, 1 -> Primeiro andar, 2 -> Segundo andar ....
df_andares = []

for a in andares:
    for v in andares[a]:
        if v['Sinal'] > -60:
            v['Qualidade'] = 'Boa'
        elif v['Sinal'] > -79:
            v['Qualidade'] = 'Média'
        else:
            v['Qualidade'] = 'Ruim'

    df = pd.DataFrame(andares[a])
    df_andares.append(df)
    m = df['Sinal'].mean()
    media.append(round(m, 2))

fig0 = px.bar(df_andares[0], x="Ponto de Acesso", y="Sinal", color='Qualidade', color_discrete_map={
    'Boa': '#00CC96',
    'Média': '#FECB52',
    'Ruim': '#EF553B'
})

fig1 = px.bar(df_andares[1], x="Ponto de Acesso", y="Sinal", color='Qualidade', color_discrete_map={
    'Boa': '#00CC96',
    'Média': '#FECB52',
    'Ruim': '#EF553B'
})

fig2 = px.bar(df_andares[2], x="Ponto de Acesso", y="Sinal", color='Qualidade', color_discrete_map={
    'Boa': '#00CC96',
    'Média': '#FECB52',
    'Ruim': '#EF553B'
})

fig3 = px.bar(df_andares[3], x="Ponto de Acesso", y="Sinal", color='Qualidade', color_discrete_map={
    'Boa': '#00CC96',
    'Média': '#FECB52',
    'Ruim': '#EF553B'
})

fig4 = px.bar(df_andares[4], x="Ponto de Acesso", y="Sinal", color='Qualidade', color_discrete_map={
    'Boa': '#00CC96',
    'Média': '#FECB52',
    'Ruim': '#EF553B'
})

app = Dash(__name__)
app.layout = html.Div(children=[
    dcc.Graph(
        id='grafico-pa-bloco-e-t',
        figure=fig0,
        style={'width': '500px'}
    ),
    dcc.Graph(
        id='grafico-pa-bloco-e-1',
        figure=fig1,
        style={'width': '500px'}
    ),
    dcc.Graph(
        id='grafico-pa-bloco-e-2',
        figure=fig2,
        style={'width': '500px'}
    ),
    dcc.Graph(
        id='grafico-pa-bloco-e-3',
        figure=fig3,
        style={'width': '500px'}
    ),
    dcc.Graph(
        id='grafico-pa-bloco-e-4',
        figure=fig4,
        style={'width': '500px'}
    ),
])

if __name__ == '__main__':
    app.run(debug=True)