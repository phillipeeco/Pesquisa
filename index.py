from dash import html, dcc
from dash.dependencies import Input, Output
from app import app
from pages import page1, page2
from components import navbar


nav = navbar.Navbar()

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav, 
    html.Div(id='page-content', children=[]), 
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page1':
        return page1.layout
    if pathname == '/page2':
        return page2.layout
    else:
        return "404 Page Error! Please choose a link"

if __name__ == '__main__':
    app.run_server(debug=True)
