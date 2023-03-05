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

def callback_genero(app):
#DROP-DOWN -------------------------------------
    @app.callback(Output('drop-questoes', 'children'),
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
                id='dropdown-perguntas',
                value='Q1',
                options=perguntas,
                clearable=False,
            )
        ]
    
# SELECIONAR SEXO -------------------------------------
    @app.callback(Output('select-sex', 'children'),
                  [Input('url', 'pathname')])

    def drop_perguntas(data):
        button_group = html.Div(
            [
                dbc.RadioItems(
                    id="radio-sex",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-primary",
                    labelCheckedClassName="active",
                    options=[
                        {"label": "GERAL", "value": 0},
                        {"label": "MASCULINO", "value": 'MASCULINO'},
                        {"label": "FEMININO", "value": 'FEMININO'},
                    ],
                    value=0,
                ),
            ],
            className="radio-group",
        )        
        return button_group

#GRÁFICOS=============================================
#RELIGIÃO - CATÓLICO =================================
    @app.callback(Output('religion-catolico', 'figure'),
                  [Input('radio-sex', 'value'),
                  Input('dropdown-perguntas', 'value')])

    def religiao_catolico(sexo, questao):
        if sexo == 'MASCULINO' or sexo == 'FEMININO':
            df_sexo = df[df['SEXO'] == sexo]            
        else:
            df_sexo = df            
        df_sexo = pd.crosstab(index=df_sexo[questao], columns = df_sexo['RELIGIAO'], margins = True, margins_name = 'Total', normalize='columns')
        df_sexo = round(df_sexo * 100, 2).reset_index()

        fig = go.Figure(data=[go.Pie(labels=df_sexo[questao], values=df_sexo['CATOLICO'], textinfo='label+percent',
                             insidetextorientation='radial'
                             )])
        fig.update(layout_title_text='CATÓLICO',layout_showlegend=False)
        return fig

# RELIGIÃO - EVANGÉLICO =================================
    @app.callback(Output('religiao-evangelico', 'figure'),
                  [Input('radio-sex', 'value'),
                  Input('dropdown-perguntas', 'value')])
    def religiao_evangelico(sexo, questao):
        if sexo == 'MASCULINO' or sexo == 'FEMININO':
            df_sexo = df[df['SEXO'] == sexo]
        else:
            df_sexo = df
        df_sexo = pd.crosstab(index=df_sexo[questao], columns=df_sexo['RELIGIAO'],margins=True, margins_name='Total', normalize='columns')
        df_sexo = round(df_sexo * 100, 2).reset_index()

        fig = go.Figure(data=[go.Pie(labels=df_sexo[questao], values=df_sexo['EVANGELICO'], textinfo='label+percent',insidetextorientation='radial')])
        fig.update(layout_title_text='EVANGÉLICO', layout_showlegend=False)
        return fig

# RELIGIÃO - SEM RELIGIAO =================================
    @app.callback(Output('religiao-sem-religiao', 'figure'),
                  [Input('radio-sex', 'value'),
                  Input('dropdown-perguntas', 'value')])
    def religiao_sem_religiao(sexo, questao):
        if sexo == 'MASCULINO' or sexo == 'FEMININO':
            df_sexo = df[df['SEXO'] == sexo]
        else:
            df_sexo = df
        df_sexo = pd.crosstab(index=df_sexo[questao], columns=df_sexo['RELIGIAO'],
                              margins=True, margins_name='Total', normalize='columns')
        df_sexo = round(df_sexo * 100, 2).reset_index()

        fig = go.Figure(data=[go.Pie(labels=df_sexo[questao], values=df_sexo['S/R/OUTROS'], textinfo='label+percent',
                                     insidetextorientation='radial'
                                     )])
        fig.update(layout_title_text='SEM RELIGIÃO/OUTRAS', layout_showlegend=False)
        return fig

# ESCOLARIDADE ============================================
# ANALFABETO/SO LE E ESCREVE===============================
    @app.callback(Output('escolaridade-analfabeto', 'figure'),
                  [Input('radio-sex', 'value'),
                  Input('dropdown-perguntas', 'value')])
                  
    def escolaridade_analfabeto(sexo, questao):
        if sexo == 'MASCULINO' or sexo == 'FEMININO':
            df_escolaridade = df[df['SEXO'] == sexo]
        else:
            df_escolaridade = df
        df_escolaridade = pd.crosstab(index=df_escolaridade[questao], columns=df_escolaridade['ESCOLARIDADE'],margins=True, margins_name='Total', normalize='columns')
        df_escolaridade = round(df_escolaridade * 100, 2).reset_index()

        fig = go.Figure(data=[go.Pie(labels=df_escolaridade[questao], values=df_escolaridade['ANALFABETO'], textinfo='label+percent',
                                     insidetextorientation='radial'
                                     )])
        fig.update(layout_title_text='ANALFABETO/SÓ LÊ E ESCREVE', layout_showlegend=False)
        return fig

# FUNDAMENTAL ===============================
    @app.callback(Output('escolaridade-fundamental', 'figure'),
                  [Input('radio-sex', 'value'),
                  Input('dropdown-perguntas', 'value')])
    def escolaridade_fundamental(sexo, questao):
        if sexo == 'MASCULINO' or sexo == 'FEMININO':
            df_escolaridade = df[df['SEXO'] == sexo]
        else:
            df_escolaridade = df
        df_escolaridade = pd.crosstab(
            index=df_escolaridade[questao], columns=df_escolaridade['ESCOLARIDADE'], margins=True, margins_name='Total', normalize='columns')
        df_escolaridade = round(df_escolaridade * 100, 2).reset_index()

        fig = go.Figure(data=[go.Pie(labels=df_escolaridade[questao], values=df_escolaridade['FUNDAMENTAL'], textinfo='label+percent',
                                     insidetextorientation='radial'
                                     )])
        fig.update(layout_title_text='ENSINO FUNDAMENTAL COMPLETO/INCOMPLETO',
                   layout_showlegend=False)
        return fig

# MEDIO ===============================
    @app.callback(Output('escolaridade-medio', 'figure'),
                  [Input('radio-sex', 'value'),
                  Input('dropdown-perguntas', 'value')])
    def escolaridade_medio(sexo, questao):
        if sexo == 'MASCULINO' or sexo == 'FEMININO':
            df_escolaridade = df[df['SEXO'] == sexo]
        else:
            df_escolaridade = df
        df_escolaridade = pd.crosstab(
            index=df_escolaridade[questao], columns=df_escolaridade['ESCOLARIDADE'], margins=True, margins_name='Total', normalize='columns')
        df_escolaridade = round(df_escolaridade * 100, 2).reset_index()

        fig = go.Figure(data=[go.Pie(labels=df_escolaridade[questao], values=df_escolaridade['MEDIO'], textinfo='label+percent',
                                     insidetextorientation='radial'
                                     )])
        fig.update(layout_title_text='ENSINO MÉDIO COMPLETO/INCOMPLETO',
                   layout_showlegend=False)
        return fig

# SUPERIOR ===============================
    @app.callback(Output('escolaridade-superior', 'figure'),
                  [Input('radio-sex', 'value'),
                  Input('dropdown-perguntas', 'value')])
    def escolaridade_superior(sexo, questao):
        if sexo == 'MASCULINO' or sexo == 'FEMININO':
            df_escolaridade = df[df['SEXO'] == sexo]
        else:
            df_escolaridade = df
        df_escolaridade = pd.crosstab(
            index=df_escolaridade[questao], columns=df_escolaridade['ESCOLARIDADE'], margins=True, margins_name='Total', normalize='columns')
        df_escolaridade = round(df_escolaridade * 100, 2).reset_index()

        fig = go.Figure(data=[go.Pie(labels=df_escolaridade[questao], values=df_escolaridade['SUPERIOR'], textinfo='label+percent',
                                     insidetextorientation='radial'
                                     )])
        fig.update(layout_title_text='ENSINO SUPERIOR COMPLETO/INCOMPLETO',
                   layout_showlegend=False)
        return fig

# IDADE ===============================
# 16 A 24 ============================
    @app.callback(Output('idade-16-24', 'figure'),
                  [Input('radio-sex', 'value'),
                  Input('dropdown-perguntas', 'value')])
    def idade_16_24(sexo, questao):
        if sexo == 'MASCULINO' or sexo == 'FEMININO':
            df_idade = df[df['SEXO'] == sexo]
        else:
            df_idade = df
        df_idade = pd.crosstab(index=df_idade[questao], columns=df_idade['IDADE'], margins=True, margins_name='Total', normalize='columns')
        df_idade = round(df_idade * 100, 2).reset_index()

        fig = go.Figure(data=[go.Pie(labels=df_idade[questao], values=df_idade['16 A 29'], textinfo='label+percent',
                                     insidetextorientation='radial'
                                     )])
        fig.update(layout_title_text='16 A 24 ANOS',
                   layout_showlegend=False)
        return fig

# 25 A 34 ============================
    @app.callback(Output('idade-25-34', 'figure'),
                  [Input('radio-sex', 'value'),
                  Input('dropdown-perguntas', 'value')])

    def idade_25_34(sexo, questao):
        if sexo == 'MASCULINO' or sexo == 'FEMININO':
            df_idade = df[df['SEXO'] == sexo]
        else:
            df_idade = df
        df_idade = pd.crosstab(index=df_idade[questao], columns=df_idade['IDADE'],margins=True, margins_name='Total', normalize='columns')
        df_idade = round(df_idade * 100, 2).reset_index()

        fig = go.Figure(data=[go.Pie(labels=df_idade[questao], values=df_idade['30 A 44'], textinfo='label+percent',
                                     insidetextorientation='radial'
                                     )])
        fig.update(layout_title_text='25 A 34 ANOS',
                   layout_showlegend=False)
        return fig

# 35 A 44 ============================
    @app.callback(Output('idade-35-44', 'figure'),
                  [Input('radio-sex', 'value'),
                  Input('dropdown-perguntas', 'value')])

    def idade_35_44(sexo, questao):
        if sexo == 'MASCULINO' or sexo == 'FEMININO':
            df_idade = df[df['SEXO'] == sexo]
        else:
            df_idade = df
        df_idade = pd.crosstab(index=df_idade[questao], columns=df_idade['IDADE'],margins=True, margins_name='Total', normalize='columns')
        df_idade = round(df_idade * 100, 2).reset_index()

        fig = go.Figure(data=[go.Pie(labels=df_idade[questao], values=df_idade['45 A 59'], textinfo='label+percent',
                                     insidetextorientation='radial'
                                     )])
        fig.update(layout_title_text='35 A 44 ANOS',
                   layout_showlegend=False)
        return fig

# 60+ ============================
    @app.callback(Output('idade-60', 'figure'),
                  [Input('radio-sex', 'value'),
                  Input('dropdown-perguntas', 'value')])

    def idade_60(sexo, questao):
        if sexo == 'MASCULINO' or sexo == 'FEMININO':
            df_idade = df[df['SEXO'] == sexo]
        else:
            df_idade = df
        df_idade = pd.crosstab(index=df_idade[questao], columns=df_idade['IDADE'],
                               margins=True, margins_name='Total', normalize='columns')
        df_idade = round(df_idade * 100, 2).reset_index()

        fig = go.Figure(data=[go.Pie(labels=df_idade[questao], values=df_idade['60+'], textinfo='label+percent',
                                     insidetextorientation='radial'
                                     )])
        fig.update(layout_title_text='60 ANOS OU MAIS',
                   layout_showlegend=False)
        return fig
