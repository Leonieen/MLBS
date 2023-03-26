import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

#load data
url = (
    "https://raw.githubusercontent.com/Leonieen/MLBS/main/Data/"
)
df_merge_Date_data = f"{url}df_datetime.csv"
df_merge_Date = pd.read_csv(df_merge_Date_data)


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])
server = app.server

blackbold = {'color': 'black', 'font-weight': 'bold'}
# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "15rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    'color': 'black',
    "overflow": "scroll",
}

sidebar = html.Div(
    [
        html.H1("MLBS WS22/23", style={'textAlign': 'center', 'color': 'black'}),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
            ),
        html.Hr(),


        html.Label(children=['by Leonie Engemann']),

    ],
    style=SIDEBAR_STYLE,
)

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "20rem",
    "padding": "2rem 1rem",
}
content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = dbc.Container([
    dbc.Row([
        #dbc.Col(html.H1("Mobile and Location Based Services",
                        # style={'textAlign': 'center', 'color': 'black'}))
    ]),

    html.Hr(),

    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar,
                    content
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
], fluid=True)


if __name__ == "__main__":
    app.run(debug=False)
