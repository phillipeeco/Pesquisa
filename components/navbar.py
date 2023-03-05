# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


# Define the navbar structure
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Gênero", href="/genero", active="exact")),
                dbc.NavItem(dbc.NavLink("Área", href="/area", active="exact")),
                dbc.NavItem(dbc.NavLink("Personalizado", href="/personalizado", active="exact")),
            ] ,
            brand="PLANDESPP",
            brand_href="/genero",
            color="primary",
            dark=True,
        ), 
    ])

    return layout
