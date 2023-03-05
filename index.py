from dash import html, dcc
from dash.dependencies import Input, Output
from app import app
from pages import area, genero
from callbacks import cb_genero, cb_area
from components import navbar


nav = navbar.Navbar()

cb_genero.callback_genero(app)
cb_area.callback_area(app)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav, 
    html.Div(id='page-content', children=[]), 
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/genero':
        return genero.layout
    if pathname == '/area':
        return area.layout
    else:
        return "404 Page Error! Please choose a link"

if __name__ == '__main__':
    app.run_server(debug=True)
