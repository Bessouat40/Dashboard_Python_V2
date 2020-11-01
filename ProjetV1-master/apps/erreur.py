import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from apps.nav import NavBar
from app import app

active = "Page2"
nav = NavBar(active)

layout = html.Div([
    html.Div(className="NavBar",children=[nav]),

    html.Div([
        dbc.Jumbotron(
        [
            html.H1("404: Page non trouvée ( utilisez la NavBar pou aller sur une page existante )", className="text-danger"),
        ])
    ,
    ], style={'width': '500',"background":"#212121","margin-top":"70px"})
])
