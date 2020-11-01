import dash_bootstrap_components as dbc
import dash_html_components as html

def NavBar(active):
    page1, page2, page3 = False, False, False,
    if active == "page1":
        page1 = True
    elif active == "page2":
        page2 = True
    elif active == "page3":
        page3 = True


    nav = dbc.Nav(
        [
            dbc.NavItem(dbc.Button("ALcool",outline=True,active=page1, href="page1",external_link=True,),className="p-2 bd-highlight"),
            dbc.NavItem(dbc.Button("Accident et legislation",outline=True, active=page2, href="page2",external_link=True,),className="p-2 bd-highlight"),
            dbc.NavItem(dbc.Button("Téléchargement",outline=True, active=page3, href="page3",external_link=True,),className="p-2 bd-highlight"),

            dbc.Row([
                dbc.NavItem(dbc.Input(type="search",placeholder="Recherche")),
                dbc.NavItem(dbc.Button("Recherche",color="primary"))
                ],
                no_gutters=True,
                className="ml-auto flex-nowrap mt-3 mt-md-0",
                align="center",
                )


        ],style={"background":"#212121"},

        pills=True,className="fixed-top"
    )
    return nav

def CollapseBar(active):

    Vnav = dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavLink("Graphe jeune"),

                    ],
                    vertical = True,

                ),
                id = "collapse",
    )
