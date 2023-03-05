from dash import dash, dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.offline as pyo
import plotly.express as px
import plotly.graph_objs as go
import json
import pandas as pd

df = pd.read_excel('dados/portocalvo-marco.xlsx')

CARDS_STYLE = {
    'margin-left': '15px', 
    "width": "15rem",
    'text-align':'center'
}

app = dash.Dash(__name__)

def callback_questoes(app):
#DROP-DOWN-1 -------------------------------------
    @app.callback(Output('drop-pergunta-1', 'children'),
                    [Input('url', 'pathname')])

    def drop_perguntas(data):
        perguntas = [
            {'label': 'Avaliação da Gestão da Prefeita Eronita', 'value': 'Q1'},
            {'label': 'Você acha quem o prefeito vem cumprindo com os compromisso de campanha?', 'value': 'Q2'},
            {'label': 'Se as eleições fossem hoje, quem você votaria para prefeito? ESPONTÂNEA', 'value': 'Q3'},
            {'label': 'Se as eleições fossem hoje, quem você votaria para prefeito? INDUZIDA', 'value': 'Q4'},
            {'label': 'Como você avalia a atuação da VICE-PREFEITA?', 'value': 'Q5'},
            {'label': 'Quem é o vereador que mais trabalha em Porto Calvo?', 'value': 'Q6'},
            {'label': 'Qual é o filho/pessoa em Porto Calvo que você sente mais orgulho?', 'value': 'Q8'},
            {'label': 'Já pensou e morar em outra cidade?', 'value': 'Q9A'},
            #{'label': 'Motivo de morar em outra cidade', 'value': 'Q9B'},
            {'label': 'Como você avalia a gestão do governador Paulo Dantas?', 'value': 'Q10'},
            {'label': 'Como você avalia a gestão do presidente Lula?', 'value': 'Q11'}
        ]
        return[
            dcc.Dropdown(
                id='pergunta-1',
                value='Q1',
                options=perguntas,
                clearable=False,
            )
        ]
# DROP-DOWN-2 -------------------------------------

    @app.callback(Output('drop-pergunta-2', 'children'),
                  [Input('url', 'pathname')])
    def drop_perguntas_2(data):
        perguntas = [
            {'label': 'Avaliação da Gestão da Prefeita Eronita', 'value': 'Q1'},
            {'label': 'Você acha quem o prefeito vem cumprindo com os compromisso de campanha?', 'value': 'Q2'},
            {'label': 'Se as eleições fossem hoje, quem você votaria para prefeito? ESPONTÂNEA', 'value': 'Q3'},
            {'label': 'Se as eleições fossem hoje, quem você votaria para prefeito? INDUZIDA', 'value': 'Q4'},
            {'label': 'Como você avalia a atuação da VICE-PREFEITA?', 'value': 'Q5'},
            {'label': 'Quem é o vereador que mais trabalha em Porto Calvo?', 'value': 'Q6'},
            {'label': 'Qual é o filho/pessoa em Porto Calvo que você sente mais orgulho?', 'value': 'Q8'},
            {'label': 'Já pensou e morar em outra cidade?', 'value': 'Q9A'},
            {'label': 'Como você avalia a gestão do governador Paulo Dantas?','value': 'Q10'},
            {'label': 'Como você avalia a gestão do presidente Lula?', 'value': 'Q11'}
        ]
        return [
            dcc.Dropdown(
                id='pergunta-2',
                value='Q2',
                options=perguntas,
                clearable=False,
            )
        ]

#===================================================================
    @app.callback(Output('tabela-cruzamento-pergunta', 'children'),
                  [Input('pergunta-1', 'value'),
                  Input('pergunta-2', 'value')])
    def cruzamento_pergunta(pergunta1, pergunta2):
        df_sexo = df
        df_sexo = pd.crosstab(index=df_sexo[pergunta1], columns = df_sexo[pergunta2], margins = True, margins_name = 'Total', normalize='columns')
        df_sexo = round(df_sexo * 100, 2).reset_index()

        return [
            dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in df_sexo.columns],
                data=df_sexo.to_dict('records'),
                fixed_rows={'headers': True},
                style_table={'height': '400px', 'overflowY': 'auto'},
                style_header={'textAlign': 'center'},
                style_cell={'textAlign': 'center', 'font-size': '14px'},
                sort_action="native",
                sort_mode='multi',
                style_as_list_view=True,  
                style_data_conditional=[
                    {
                        "if": {"state": "selected"},
                        "backgroundColor": "rgba(205, 205, 205, 0.3)",
                        "border": "inherit !important",
                    }
                ],
            )
        ]
