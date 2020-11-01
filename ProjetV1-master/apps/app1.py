import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps.nav import NavBar
import plotly.express as px
from app import app
import dash_bootstrap_components as dbc
from data import recuperationDataAlcool

active = "page1"
nav = NavBar(active)

def choroplethGraph(scope,data,color,colorFrench,legendColor):
    fig = px.choropleth(data , locations='Alpha-3 code', color=color,
                               color_continuous_scale=legendColor,
                               range_color=(0, 100),
                               scope=scope,
                               labels={color:colorFrench},
                               template="plotly_dark",
                              )
    return fig

# Ouverture du csv
youth = recuperationDataAlcool("data")
# Data récupérant la moyenne du pourcentage d'alcool par continents
moy = recuperationDataAlcool("moyenne")

# Data montrant le pourcentage de jeune qui consomme de l'alcool pour les 15-19 ans
youthColor,youthColorFrench = recuperationDataAlcool("total")

# Data montrant le pourcentage de jeune homme qui consomme de l'alcool pour les 15-19 ans
youthColorMan,youthColorManFrench = recuperationDataAlcool("man")

# Data montrant le pourcentage de jeune femme qui consomme de l'alcool pour les 15-19 ans
youthColorFemales,youthColorFemalesFrench = recuperationDataAlcool("female")

# Data pour récupérer les pays et continents
continents_possibles = recuperationDataAlcool("continent")

# Figure map consommation d'alcool h+f
figTotal = choroplethGraph("world",youth,youthColor,youthColorFrench,"Peach")
figTotal.update_layout(title_text = "% de jeune consommant de l'alcool"),


figTotal3 = px.bar(moy , y = youthColor,
                labels={youthColor:youthColorFrench},
                template = "plotly_dark",
            )
figTotal3.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})

#figure map consommation d'alcool hommes
figTotalMan = choroplethGraph("world",youth,youthColorMan,youthColorManFrench,"Peach")
figTotalMan.update_layout(title_text = "% de jeune hommes consommant de l'alcool"),
figTotalMan.update_layout(margin={"r":0,"t":30,"l":0,"b":30}),
figTotalMan3 = px.bar(moy , y = youthColorMan,
                labels={youthColorMan:youthColorManFrench},
                template = "plotly_dark",
            )
figTotalMan3.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})

#figure map consommation d'alcool femmes
figTotalFemales = choroplethGraph("world",youth,youthColorFemales,youthColorFemalesFrench,"Peach")
figTotalFemales.update_layout(title_text = "% de jeune femmes consommant de l'alcool"),
figTotalFemales.update_layout(margin={"r":0,"t":30,"l":0,"b":30}),
figTotalFemales3 = px.bar(moy , y = youthColorFemales,
                labels={youthColorFemales:youthColorFemalesFrench},
                template = "plotly_dark",
            )
figTotalFemales3.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})



#style défaut
StyleDropDown = {"width":"95%","height":"100%","display":"inline-block","margin-left":"50px","margin-right":"50px"}

# menu déroulant pour map
def MenuDeroulantMap(id):
    Menu = dcc.Dropdown(
            id = id,
            options = [{'label': str(i), 'value': str(i)} for i in continents_possibles if str(i)!="nan" and str(i)!="OC"],
            value="EU"
            )
    return Menu




tab_total = dbc.Card(
    dbc.CardBody([
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='map',
                    figure=figTotal
                ),
            ]),
        ]),
        dbc.Row([
            MenuDeroulantMap("pays_select"),
        ],style= StyleDropDown ),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='map2',
                ),
            ]),
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='histogramme', figure = figTotal3,
                    style = {'width': '100%','height': '100%',"background":"#000000"},

                ),
            ]),
        ]),

    ]), className ="mt-3", style = {'width': '100%','height': '100%',"background":"#131414"},
)

tab_homme = dbc.Card(
    dbc.CardBody([
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='mapMan',
                    figure=figTotalMan
                ),
            ]),
        ]),
        dbc.Row([
            MenuDeroulantMap("pays_select2"),
        ],style= StyleDropDown ),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='mapMan2',
                ),
            ]),
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='histogrammeMan', figure = figTotalMan3,
                    style = {'width': '100%','height': '100%',"background":"#000000"},

                ),
            ]),
        ]),

    ]), className ="mt-3", style = {'width': '100%','height': '100%',"background":"#131414"},
)

tab_femme = dbc.Card(
    dbc.CardBody([
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='mapFemales',
                    figure=figTotalFemales
                ),
            ]),
        ]),
        dbc.Row([
            MenuDeroulantMap("pays_select3"),
        ],style= StyleDropDown ),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='mapFemales2',
                ),
            ]),
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='histogrammeFemales', figure = figTotalFemales3,
                    style = {'width': '100%','height': '100%',"background":"#000000"},

                ),
            ]),
        ]),

    ]), className ="mt-3", style = {'width': '100%','height': '100%',"background":"#131414"},
)

# Layout de la page permettant d'afficher les differents éléments
layout = html.Div([
    html.Div(className="NavBar",children=[nav]),

    html.Div([
        html.H1(["Visualisation sur la consommation d'alcool chez les jeunes"],style={"color":"white","text-align":"center",}),
        dbc.Tabs([
            dbc.Tab(tab_total,label="Total"),
            dbc.Tab(tab_homme,label="Homme"),
            dbc.Tab(tab_femme, label="Femme"),
        ])

    ], style={'width': '100%','height': '100%',"background":"#131414","margin-top":"70px"})
]),

#Interprétation menu déroulant
def InterMenu(pays_selected):
    pays = "europe"
    name = "Europe"
    if pays_selected == "SA":
        pays = "south america"
        name = "Amerique du sud"
    elif pays_selected == "AS":
        pays = "asia"
        name = "Asie"
    elif pays_selected == "AF":
        pays = "africa"
        name = "Afrique"
    else :
        pays = "europe"

    return pays,name


@app.callback(
    Output("map2","figure"),
    [Input("pays_select","value")]
)
def upgrade_map(pays_select):
    pays,name = InterMenu(pays_select)
    fig2 = choroplethGraph(pays,youth,youthColor,youthColorFrench,"Viridis")
    fig2.update_layout(title_text = "% de jeune consommant de l'alcool en "+ name),
    fig2.update_layout(margin={"r":0,"t":30,"l":0,"b":0})

    return fig2

@app.callback(
    Output("mapMan2","figure"),
    [Input("pays_select2","value")]
)
def upgrade_map(pays_select):
    pays,name = InterMenu(pays_select)
    fig2 = choroplethGraph(pays,youth,youthColorMan,youthColorManFrench,"Viridis")
    fig2.update_layout(title_text = "% de jeunes hommes consommant de l'alcool en "+ name),
    fig2.update_layout(margin={"r":0,"t":30,"l":0,"b":0})

    return fig2

@app.callback(
    Output("mapFemales2","figure"),
    [Input("pays_select3","value")]
)
def upgrade_map(pays_select):
    pays,name = InterMenu(pays_select)
    fig2 = choroplethGraph(pays,youth,youthColorFemales,youthColorFemalesFrench,"Viridis")
    fig2.update_layout(title_text = "% de jeunes femmes consommant de l'alcool en "+ name),
    fig2.update_layout(margin={"r":0,"t":30,"l":0,"b":0})

    return fig2
