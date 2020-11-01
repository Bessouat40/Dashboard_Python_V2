import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps.nav import NavBar


import plotly.express as px
import pandas as pd
from app import app
import dash_bootstrap_components as dbc
from data import recuperationDataAccident, recuperationDataTolerance

from app import app

# mettre le code ici ( layout + callbacks)

active = "page2"
nav = NavBar(active)

def choroplethGraph(scope,data,color,colorFrench,legendColor):
    fig = px.choropleth(data , locations='Alpha-3 code', color=color,
                               color_continuous_scale=legendColor,
                               range_color=(0, 0.1),
                               scope=scope,
                               labels={color:colorFrench},
                               template="plotly_dark",
                              )
    return fig

jeunes_morts = recuperationDataAccident("data")
#-----------------------------------------------------------------------------------------
csv = recuperationDataAccident("dataClear")
print(csv)
#------------------------------------------------------------------------------------------
pays_possibles = recuperationDataAccident("PaysSelect")
data = pd.read_csv("data/tolerance_compl.csv")
dataSelect,dataFrench = recuperationDataTolerance("MapTolerance")




#fig2 = choroplethGraph("world",jm,"Value","Valeur","Viridis")

tolerance = html.Div(
                dcc.Graph(
                        id="MapTolerance",
                        ),
                )

Accidents = html.Div(
                dcc.Graph(
                        id="MapAccident",
                        ),
                )

layout = html.Div([
    html.Div(className="NavBar",children=[nav]),
    html.Div([
        html.H1(["Visualisation sur la législation liée à l'alcool et les accidents de la route"],style={"color":"white","text-align":"center",}),
        dbc.Row([
                html.Div([
                    dcc.Dropdown(
                        id='xaxis-column1',
                        options=[{'label':"Europe","value":"europe"},
                                 {'label':"Asie","value":"asia"},
                                 {'label':"USA","value":"usa"},
                                 {'label':"Amerique du nord","value":"north america"},
                                 {'label':"Amerique du sud","value":"south america"},
                                 {'label':"Monde","value":"world"},
                        ],
                        value='europe'
                    )],
                    style={"width":"95%","height":"100%","display":"inline-block","margin-left":"50px","margin-right":"50px"}
                ),
            ]),
            dbc.Row([
                dbc.Col([
                    Accidents,
                ],md=6),
                dbc.Col([
                    tolerance,

                ],),

        ],
        no_gutters = True,
        ),
        dbc.Row([
                html.Div([
                    dcc.Dropdown(
                    id='xaxis-column',
                    options=[{'label': str(i), 'value': str(i)} for i in pays_possibles],
                    value='France',
                    )],
                style={"width":"95%","height":"100%","display":"inline-block","margin-left":"50px","margin-right":"50px"}
                ),
                dcc.Graph(id='indicator-graphic'),

        ],
        style={"width":"100%","height":"100%","display":"inline-block"}
        ),
        ],style={'width': '100%','height': '100%',"background":"#131414","margin-top":"70px"}),
])



@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value')])
def update_graph(xaxis_column_name):
    df = jeunes_morts[jeunes_morts.Country == xaxis_column_name]
    df1 = df[['Year' , 'Value']].groupby("Year").max()
    fig = px.histogram(df1,y=df1["Value"],x=df["Year"].unique(),template="plotly_dark",labels={"variable":"Nbr de morts"},nbins=20)
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest',bargap=0.2)
    fig.update_xaxes(title=xaxis_column_name)


    return fig

@app.callback(
    Output('MapAccident', 'figure'),
    [Input('xaxis-column1', 'value')])

def update_graph(scope):
    max = 10000
    if scope == "usa" :
        max = 50000
    fig = px.choropleth(csv , locations='COUNTRY', color="Value",
                               animation_frame = "Year",
                               color_continuous_scale="Peach",
                               range_color=(0, max),
                               scope=scope,
                               labels={"Value":"Nombre de morts"},
                               template="plotly_dark",
                              )

    fig.update_layout(margin={"r":0,"t":30,"l":0,"b":30}),
    return fig

@app.callback(
    Output('MapTolerance', 'figure'),
    [Input('xaxis-column1', 'value')])

def update_graph(scope):
    fig = choroplethGraph(scope,data,dataSelect,dataFrench,"Viridis")
    fig.update_layout(margin={"r":0,"t":30,"l":0,"b":30}),
    return fig
