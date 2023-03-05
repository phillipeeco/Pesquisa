from dash import dash, dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.express as px
import plotly.graph_objs as go
import json


layout = dbc.Container([

    # Título --------------------------
    dbc.Row([
            dbc.Col([
                html.H3('Análise por Área',
                        style={'text-align': 'center'})
            ]),
            ]),

    # dropdown questões ---------------
    dbc.Row([
            dbc.Col([
                html.Div(id='drop-questoes-area', style={'padding-top': '20px'})
            ], width=8),

            dbc.Col([
                html.Div(id='select-area', style={'text-align': 'center', 'padding-top': '20px'})
            ], width=12),
            ], justify='center'),

    # GRAFICOS:
    dbc.Row([
            # RELIGIÃO ==============================
            dbc.Col([
                dcc.Graph(id='religion-catolico-area'),
            ], width=4),

            dbc.Col([
                dcc.Graph(id='religiao-evangelico-area'),
            ], width=4),

            dbc.Col([
                dcc.Graph(id='religiao-sem-religiao-area'),
            ], width=4),

            # ESCOLARIDADE ==============================
            dbc.Col(
                dcc.Graph(id='escolaridade-analfabeto-area'),
                width=4),
            dbc.Col(
                dcc.Graph(id='escolaridade-fundamental-area'),
                width=4),
            dbc.Col(
                dcc.Graph(id='escolaridade-medio-area'),
                width=4),
            dbc.Col(
                dcc.Graph(id='escolaridade-superior-area'),
                width=4),

            # IDADE ==============================
            dbc.Col(
                dcc.Graph(id='idade-16-24-area'),
                width=4),
            dbc.Col(
                dcc.Graph(id='idade-25-34-area'),
                width=4),
            dbc.Col(
                dcc.Graph(id='idade-35-44-area'),
                width=4),
            dbc.Col(
                dcc.Graph(id='idade-60-area'),
                width=4),



            ]),



], fluid='True')
