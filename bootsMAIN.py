#pip install dash-bootstrap-components
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from datetime import date

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)



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

nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Ciclo de vida", active=True, href="/")),
        dbc.NavItem(dbc.NavLink("Simulador", href="/page-1")),
        dbc.NavItem(dbc.NavLink("Manual", href="/page-2")),
        dbc.NavItem(dbc.NavLink("Acerca de", disabled=True, href="#")),
        dbc.DropdownMenu(
            [dbc.DropdownMenuItem("Clima"), dbc.DropdownMenuItem("Históricos")],
            label="Datos",
            nav=True,
        ),
    ]
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    nav,
    content
])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
                dbc.Row([
                    dbc.Col([
                        html.H1("Proceso del ciclo de vida Ceratitis Capitata", style={"textAlign":"center"})
                    ],width=12)
                ]),
                dbc.Row([
                    dbc.Col([
                        dbc.Carousel(
                            items=[
                                {"key": "1", "src": "/assets/a.png", "header":"Ovipostura",
                                 "caption":"Eclosión", "img_style":{"max-height": "350px","max-width": "350px"}},
                                {"key": "2", "src": "/assets/b.png", "header": "Colonización",
                                 "caption": "Infestación","img_style": {"max-height": "350px","max-width": "350px"}},
                                {"key": "3", "src": "/assets/c.jpg", "header": "Dentro de fruto",
                                 "caption": "1er Instar Larval", "img_style": {"max-height": "350px","max-width": "350px"}},
                                {"key": "4", "src": "/assets/d.png", "header": "Emergencia adulto",
                                 "img_style": {"max-height": "350px","max-width": "350px"}},
                                {"key": "5", "src": "/assets/e.png", "header": "Ovipostura Oi",
                                 "caption": "Multiplicación", "img_style": {"max-height": "350px","max-width": "350px"}},
                                {"key": "6", "src": "/assets/f.png", "header": "Muere", "caption": "",
                                 "img_style": {"max-height": "350px","max-width": "350px"}},
                            ],
                            controls=True,
                            indicators=True,
                            interval=5000,
                            ride="carousel",
                        )], width=4)
                ], justify="center"),
            dbc.Row([
                dbc.Col([
                    html.H5("Fecha inicial: "),
                    dcc.DatePickerSingle(
                        id='my-date-picker-single',
                        min_date_allowed=date(1995, 8, 5),
                        max_date_allowed=date(2017, 9, 19),
                        initial_visible_month=date(2017, 8, 5),
                        date=date(2017, 8, 25)
                    )
                ], width=2),

                dbc.Col([
                    html.Div([
            html.P("Intervalo de tiempo It"),
            dbc.Input(type="number", min=0, max=10, step=1),
            ],
            id="ti",
        )

                ], width=2)

            ]),






        ]
    elif pathname == "/page-1":
        return [
            dbc.Row([
                dbc.Col([
                    html.H2("Estimación de frutos y brotes infestados", style={"textAlign": "center"}),

                    html.H1('Ventana de parámetros',
                            style={'textAlign': 'center', 'color': 'blue'}),

                    dbc.Row([
                        dbc.Row([html.Label("Parámetros de Inicialización")]),
                        dbc.Col([
                            dbc.Input(id='Yo', type="number", value='18', min=0, max=20, step=2),
                            html.Br(),
                            dbc.Input(id='Yo', type="number", value='18', min=0, max=20, step=2),
                        ], width=2),
                        dbc.Col([
                            html.Label('Radio Items'),
                            dcc.RadioItems(options=['Ninguno', 'Quim 1', 'Quim 2'],
                                           value='Ninguno'),
                        ], width=2)
                    ]),


                    #dcc.Graph(figure={})
                ], width=12)
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



if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
