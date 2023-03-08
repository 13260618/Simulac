# pip install dash-bootstrap-components
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, dash_table
from dash_bootstrap_components._components.Container import Container
from datetime import datetime, date
import pandas as pd


import time
import numpy as np
import plotly.graph_objects as go





dataClima = "C:/Users/LANREF/Documents/ss_imr/Python/Simulac/docs/clima.xlsx"
dataHist = "C:/Users/LANREF/Documents/ss_imr/Python/Simulac/docs/historicos.csv"
logo = "/assets/lanref.png"



df = pd.read_excel(dataClima)
df0 = pd.read_csv(dataHist)

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
    suppress_callback_exceptions=True,
)

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #213b31',
    'padding': '3px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '3px'
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "Ceratitis", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Ciclo de vida", href="/", active="exact"),
                dbc.NavLink("Simulador", href="/page-1", active="exact"),
                dbc.NavLink("Manual", href="/page-2", active="exact"),
            ]
        )
    ]
)
spinners = html.Div(
    [
        dbc.Spinner(color="primary"),
        dbc.Spinner(color="secondary"),
        dbc.Spinner(color="success"),
        dbc.Spinner(color="warning"),
        dbc.Spinner(color="danger"),
        dbc.Spinner(color="info"),
        dbc.Spinner(color="light"),
        dbc.Spinner(color="dark"),
    ]
)

graf = dbc.Container(
    [
        dcc.Store(id="store"),
       #html.H1("Prueba"),
        html.Hr(),
        dbc.Button(
            "Reiniciar",
            color="primary",
            id="button",
            className="mb-3",
        ),
        dbc.Tabs(
            [
                dbc.Tab(label="Scatter", tab_id="scatter"),
                dbc.Tab(label="Histograms", tab_id="histogram"),
            ],
            id="tabs",
            active_tab="scatter",
        ),
        html.Div(id="tab-content", className="p-4"),
    ]
)






card_content = [
    dbc.CardHeader("Gráfica (a)"),
    dbc.CardBody(
        [
            html.H5("Modelo a", className="card-title"),
            graf

        ]
    ),
]


card_content0 = [
    dbc.CardHeader("Gráfica (b)"),
    dbc.CardBody(
        [
            html.H5("Modelo b", className="card-title"),
            dbc.Spinner(spinner_style={"width": "3rem", "height": "3rem"}),

        ]
    ),
]

nav = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src=logo, height="50px")),
                    dbc.Col(dbc.NavbarBrand("SIMULAC 2023", className="ms-2")),
                ],
                align="center",
                className="g-0",
            ),

            dbc.NavItem(dbc.NavLink("Ciclo de vida", active=True, href="/")),
            dbc.NavItem(dbc.NavLink("Simulador", href="/page-1")),
            dbc.NavItem(dbc.NavLink("Manual", href="/page-2")),
            dbc.NavItem(dbc.NavLink("Acerca de", disabled=True, href="#")),
            dbc.NavItem(dbc.NavLink("Datos", href="/page-4")),
            dbc.NavItem(dbc.NavLink("Pruebas", href="/page-3"))

               # dbc.DropdownMenu(
               # [dbc.DropdownMenuItem("Clima"), dbc.DropdownMenuItem("Históricos")],
              #  label="Datos",
             #   nav=True,
            #), href="/page-3"),
        ])
)


def make_a_tab(icon, title):
    return dcc.Tab(
        label=title, className=icon + " custom-tab",
        selected_className="custom-tab--selected",
        value=title.lower().replace(" ", "-"),
        children=[
            html.H3(title),
            html.P(f"This is the tab {title}."),
        ])


icons = ["fas fa-globe", "fas fa-chart-area", "fas fa-box", "fas fa-globe"]
titles = ["INFESTACIÓN", "MANEJO", "COSECHA", "CLIMA"]

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    nav,
    content
])




tab_uno = dbc.Card(
    dbc.CardBody(
        [
            html.P("Estimaciones a Fecha", className="card-text"),
            dbc.Button("Ver", color="success"),
        ]
    ),
    className="mt-3",
)
tab_dos = dbc.Card(
    dbc.CardBody(
        [
            html.P("Estimaciones a Fecha", className="card-text"),
            dbc.Button("Ver", color="danger"),
        ]
    ),
    className="mt-3",
)

card_frutos = dbc.Card(
    dbc.CardBody(
        [
            html.P("Gráfica del modelo de frutos infestados")
        ]
    ),
    className="mt-3",
)



card_brotes = dbc.Card(
    dbc.CardBody(
        [
            html.P("Gráfica del modelo de brotes infestados")
        ]
    ),
    className="mt-3",
)


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
            dbc.Row([
                dbc.Col([

                       html.H1("Proceso del ciclo de vida Ceratitis Capitata", style={"textAlign": "center"}),

                ], width=12)
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "/assets/a.png", "header": "Ovipostura",
                             "caption": "Eclosión"}, #, "img_style": {"max-height": "350px", "max-width": "350px"}
                            {"key": "2", "src": "/assets/b.png", "header": "Colonización",
                             "caption": "Infestación"},
                            {"key": "3", "src": "/assets/c.jpg", "header": "Dentro de fruto",
                             "caption": "1er Instar Larval"},
                            {"key": "4", "src": "/assets/d.png", "header": "Emergencia adulto"},
                            {"key": "5", "src": "/assets/e.png", "header": "Ovipostura Oi",
                             "caption": "Multiplicación"},
                            {"key": "6", "src": "/assets/f.png", "header": "Muere", "caption": ""},
                        ],
                        variant="dark",
                        controls=True,
                        indicators=True,
                        interval=5000,
                        ride="carousel",
                    )], width=4)
            ], justify="center"),
            dbc.Row([
                html.Br(), html.Br(), html.Br(), html.Br(),
                dbc.Col([], width=2),
                dbc.Col([
                    html.P("Tiempo de inicio (ti)"),
                    dbc.Input(id='fi',type='date')
                ], width=2),
                dbc.Col([], width=2),
                dbc.Col([
                    html.Div([
                        html.P("Intervalo de tiempo (it)"),
                        dbc.Input(type="number", value=1, min=0, max=10, step=1),
                    ],
                        id="ti",
                    )], width=2),
                dbc.Col([], width=2),
                dbc.Col([
                    html.P("Tiempo Máximo (tf)"),
                    dbc.Input(id='ff', type='date',value=""),

                ], width=2)

            ]),
            dbc.Row(
                [html.Hr(),
                 dbc.Col([
                     html.Div([
                         html.P("Período de Incubación (Pi)"),
                         dbc.Input(type="number", value=3, min=0, max=3, step=1),
                     ],
                         id="ti",
                     )], width=3),
                 dbc.Col([
                     html.Div([
                         html.P("Periodo de Infestación (PI)"),
                         dbc.Input(type="number", value=18, min=18, max=24, step=1),
                     ],
                         id="ti",
                     )], width=3),
                 dbc.Col([
                     html.Div([
                         html.P("Periodo de Copulación (Pc)"),
                         dbc.Input(type="number", value=25, min=0, max=30, step=1),
                     ],
                         id="ti",
                     )], width=3),
                 dbc.Col([
                     html.Div([
                         html.P("Número de Oviposturas"),
                         dbc.Input(type="number", value=1, min=0, max=10, step=1),
                     ],
                         id="ti2",
                     )], width=3),

                 ]

            )

        ]
    elif pathname == "/page-1":
        return [

            dbc.Row([
                dbc.Col([
                    html.H3("Parámetros de Inicialización"),
                    html.Div([
                        dcc.Tabs(
                            [
                                dcc.Tab(label='INFESTACIÓN', id='tab-1', style=tab_style),
                                dcc.Tab(label='MANEJO', id='tab-2', style=tab_style),
                                dcc.Tab(label='COSECHA', id='tab-3', style=tab_style),
                                dcc.Tab(label='CLIMA', id='tab-4', style=tab_style),
                            ], id="parameters", style=tabs_styles),
                        html.Div(id='contenido'),
                    ]
                    )
                ], width=6),

                dbc.Col([
                    html.H2("Estimaciones del modelo"),
                    dbc.Tabs([
                        dbc.Tab(tab_uno, label="Registro uno"),
                        dbc.Tab(tab_dos, label="reporte")
                    ]

                    )

                ], width=6)

            ]),
            html.Br(), html.Br(),
            dbc.Row([
                dbc.Col(
                    [
                        dbc.Tabs(
                            [
                                dbc.Tab(
                                    dbc.Card(card_content, color="danger", outline=True),

                                    label="Modelo de frutos infestados"
                                ),
                            ]
                        )
                    ], width=6),
                dbc.Col(
                    [
                        dbc.Tabs(
                            [
                                dbc.Tab(
                                    dbc.Card(card_content0, color="success", outline=True),
                                   # dbc.Spinner(spinner_style={"width": "3rem", "height": "3rem"}),
                                    label="Modelo de Brotes"
                                ),

                            ]
                        )
                    ], width=6),

            ])
        ]

    elif pathname=='/page-4':
        return [
            html.Div([
            dash_table.DataTable(df.to_dict('records'),[{"name": i, "id": i} for i in df.columns], id='tbl'),
            dbc.Alert(id='tbl_out')
            ])
        ]

    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


now = datetime.now()
time = now.strftime("%H:%M:%S")


# print("time:", time)

@app.callback(
    Output("contenido", "children"),
    [Input("parameters", "value")]
)
def render_content(tab):
    if tab == 'tab-1':
        return [
            html.Br(), html.Br(),
            html.Div([
                dbc.Row([

                    dbc.Col([
                        html.Div([
                            html.P("No. Brote/Municipio"),
                            dbc.Input(type="number", value=18, min=0, max=20, step=2)
                        ], id='Yo'),
                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.P("No. Adultos/Trampa "),
                            dbc.Input(id='trampa', type="number", value=5, min=0, max=50, step=5)
                        ], id='Y1'),

                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.P("No. Huevos/Ovipostura"),
                            dbc.Select([1, 5, 10, 30], 5)
                        ], id='huevos')

                    ], width=3),

                    dbc.Col([
                        html.Div([
                            html.P("Proporción H/M"),
                            dbc.Input(id='propHM', type="number", value=0.51, min=0, max=1, step=0.01),
                        ], )
                    ], width=3),

                ])
            ])
        ]
    elif tab == 'tab-2':
        return [
            html.Br(), html.Br(),
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            html.P("Tipo de producto"),

                            dbc.Select(['Ninguno', 'Biológico 1', 'Biológico 2'], 'Ninguno')
                        ], id='producto')
                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.P("Fecha 1a aplicación"),
                            dbc.Input(id='dateaplic1', type='date'),
                            html.Br(), html.Br(),
                            html.P("% Efectividad"),
                            dbc.Input(id='efectividad', type="number", value=81, min=0, max=100, step=0.1),

                        ])
                    ], width=3),
                    dbc.Col([
                        html.Div([html.P("Fecha 2a aplicación"),
                                  dbc.Input(id='dateaplic2', type='date'),
                                  html.Br(), html.Br(),
                                  html.P("Período de efectividad"),
                                  dbc.Input(id='periefec', type="number", value=30, min=0, max=1000, step=1),
                                  ])
                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.P("Fecha 3a aplicación"),
                            dbc.Input(id='dateaplic3', type='date')
                        ])
                    ], width=3),

                ])

            ])

        ]
    elif tab == 'tab-3':
        return [
            html.Br(), html.Br(),
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            html.P("Inicio Cosecha"),
                            dbc.Input(id='inicose',type='date'),

                        ])
                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.P("Fin de cosecha"),
                                 dbc.Input(id='fincose', type='date')
                                  ])
                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.P("% Finalización cosecha"),
                            dbc.Input(id='finaliza', type="number", value=20, min=0, max=100, step=0.1),
                        ])
                    ], width=3),

                ])

            ])

        ]
    elif tab == 'tab-4':
        return [
            html.Br(), html.Br(),
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            html.P("Período (Desde)"),
                            dbc.Input(id='perdesd', type='date'),
                            html.Br(), html.Br(),
                            html.P("Hasta:"),
                            dbc.Input(id='perdhast', type='date'),
                        ])
                    ], width=3),

                    dbc.Col([
                        html.Div([html.P("Horas (Desde)"),
                                  dbc.Input(type='time', id='hora', value=time),
                                  html.Br(), html.Br(),
                                  html.P("Hasta: "),
                                  dbc.Input(type='time', id='hora', value=time),
                                  ])
                    ], width=3),
                    dbc.Col([
                        html.Div([html.P("Temperatura (Desde)"),
                                  dbc.Input(id='tempdesd', type="number", value=10, min=0, max=150, step=1),
                                  html.Br(), html.Br(),
                                  html.P("Hasta: "),
                                  dbc.Input(id='tempdhast', type="number", value=25, min=0, max=150, step=1),
                                  ])
                    ], width=3),
                    dbc.Col([
                        html.Div([html.P("HR (%)"),
                                  dbc.Input(id='hrdesd', type="number", value=80, min=0, max=100, step=1),
                                  html.Br(), html.Br(),
                                  html.P("Hasta"),
                                  dbc.Input(id='hrhast', type="number", value=100, min=0, max=100, step=1),
                                  ])
                    ], width=3),

                ])

            ])

        ]


@app.callback(
    Output('tbl-out','children'),
    Input('tbl', 'active_cell')
)

def update_graphs(active_cell):
    return str(active_cell) if active_cell else "Haga click en un dato"











if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
