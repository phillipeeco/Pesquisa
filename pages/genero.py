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
                html.H3('Análise por Gênero', style={'text-align':'center'})
            ]),
        ]),

        #dropdown questões ---------------
        dbc.Row([
            dbc.Col([
                html.Div(id='drop-questoes', style={'padding-top':'20px'})
            ], width=8),

            dbc.Col([
                html.Div(id='select-sex', style={'text-align':'center','padding-top': '20px'})
            ], width=12),
        ], justify='center'),

        #GRAFICOS:        
        dbc.Row([
            # RELIGIÃO ==============================
            dbc.Col([                
                dcc.Graph(id='religion-catolico'),                
            ],width=4),

            dbc.Col([
                dcc.Graph(id='religiao-evangelico'), 
            ],width=4),

            dbc.Col([
                dcc.Graph(id='religiao-sem-religiao'),
            ],width=4),
        
            # ESCOLARIDADE ==============================
            dbc.Col(
                dcc.Graph(id='escolaridade-analfabeto'),
                width=4),
            dbc.Col(
                dcc.Graph(id='escolaridade-fundamental'),
                width=4),
            dbc.Col(
                dcc.Graph(id='escolaridade-medio'),
                width=4),
            dbc.Col(
                dcc.Graph(id='escolaridade-superior'),
                width=4),

            # IDADE ==============================
            dbc.Col(
                dcc.Graph(id='idade-16-24'),
                width=4),
            dbc.Col(
                dcc.Graph(id='idade-25-34'),
                width=4),
            dbc.Col(
                dcc.Graph(id='idade-35-44'),
                width=4),           
            dbc.Col(
                dcc.Graph(id='idade-60'),
                width=4),
        


        ]),



], fluid='True')
