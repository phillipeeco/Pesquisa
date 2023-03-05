from dash import dash, dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.express as px
import plotly.graph_objs as go
import json

layout = dbc.Container([
        #Título --------------------------
        dbc.Row([
            dbc.Col([
                html.H3('Cruzamento das Perguntas', style={'text-align':'center', 'margin-top':'2%'})
            ]),
        ]),

        #dropdown questões ---------------
        dbc.Row([
            dbc.Col([
                html.H5('Linha', style={'text-align':'right'})
            ], width=2),
            dbc.Col([
                html.Div(id='drop-pergunta-1')
            ], width=8),
        ], justify='center'),

     dbc.Row([
            dbc.Col([
                html.H5('Coluna', style={'text-align': 'right'})
            ], width=2),
            dbc.Col([
                html.Div(id='drop-pergunta-2')
            ], width=8),        
     ], justify='center', style={'margin-top':'20px'}),

        #GRAFICOS:        
        dbc.Row([
            # RELIGIÃO ==============================
            dbc.Col([                
                html.Div(id='tabela-cruzamento-pergunta'),
            ],width=12, style={'margin-top':'25px'}),       
        ]),

], fluid='True')
