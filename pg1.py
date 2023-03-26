from dash import Dash
import dash
import pandas as pd
from dash import dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from urllib.request import urlopen
import json

dash.register_page(__name__, path='/', name='PracticalWork1')  # '/' is home page

blackbold = {'color': 'black', 'font-weight': 'bold'}

# page 1 data
mapbox_access_token = ("pk.eyJ1IjoiZ2VvbmllIiwiYSI6ImNsM210Ymc3ODA4NGozaWw4aG1hNDJtMW4ifQ.mmjDtqmcSpEZM2JyXe9Q8g")

#load data
url = (
    "https://raw.githubusercontent.com/Leonieen/MLBS/main/Data/"
)

shape = f'{url}ee_municipalities_WGS84.geojson'
site = f"{url}site_2011_03.csv"
site_df = pd.read_csv(site)
antennas_count = f"{url}df_ant_count.csv"
antennas_count_df = pd.read_csv(antennas_count)
antennas_color = f"{url}df_merge_color.csv"
antennas_color_df = pd.read_csv(antennas_color)
df_heatmap_data = f"{url}df_heatmap_time.csv"
df_heatmap = pd.read_csv(df_heatmap_data)
df_merge_Date_data = f"{url}df_datetime.csv"
df_merge_Date = pd.read_csv(df_merge_Date_data)
df_data_unique_data = f"{url}df_data_unique.csv"
df_data_unique = pd.read_csv(df_merge_Date_data)
df_antenna_unique_data = f"{url}df_antenna_unique.csv"
df_antenna_unique = pd.read_csv(df_merge_Date_data)
df_okood = pd.read_csv("https://raw.githubusercontent.com/Leonieen/MLBS/main/Data/df_okood.csv")
df_charts = pd.read_csv(f"{url}df_charts.csv")
df_counts = pd.read_csv(f"{url}counts_df.csv")
df_counts_fox = pd.read_csv(f"{url}counts_df_fox.csv")
df_counts_bear = pd.read_csv(f"{url}counts_df_bear.csv")
df_counts_wolf = pd.read_csv(f"{url}counts_df_wolf.csv")
df_bar_charts = pd.read_csv(f"{url}Date_charts.csv")

#Visits
top_okood = df_merge_Date.OKOOD.value_counts().rename_axis('OKOOD').reset_index(name='counts')
top_okood_unique = df_counts.OKOOD.value_counts().rename_axis('OKOOD').reset_index(name='counts')
top1 = str(top_okood["OKOOD"].values[0])
top1_count = str(top_okood["counts"].values[0])
top1_unique = str(top_okood_unique["counts"].values[0])
top1_unique_m = str(top_okood_unique["OKOOD"].values[0])
top2 = str(top_okood["OKOOD"].values[1])
top2_count = str(top_okood["counts"].values[1])
top2_unique = str(top_okood_unique["counts"].values[1])
top2_unique_m = str(top_okood_unique["OKOOD"].values[1])
top3 = str(top_okood["OKOOD"].values[2])
top3_count = str(top_okood["counts"].values[2])
top3_unique = str(top_okood_unique["counts"].values[2])
top3_unique_m = str(top_okood_unique["OKOOD"].values[2])
top4 = str(top_okood["OKOOD"].values[3])
top4_count = str(top_okood["counts"].values[3])
top4_unique = str(top_okood_unique["counts"].values[3])
top4_unique_m = str(top_okood_unique["OKOOD"].values[3])
top5 = str(top_okood["OKOOD"].values[4])
top5_count = str(top_okood["counts"].values[4])
top5_unique = str(top_okood_unique["counts"].values[4])
top5_unique_m = str(top_okood_unique["OKOOD"].values[4])
#Weekdays
monday = df_bar_charts.loc[df_bar_charts['weekday'] == 0]
tuesday = df_bar_charts.loc[df_bar_charts['weekday'] == 1]
wednesday = df_bar_charts.loc[df_bar_charts['weekday'] == 2]
thursday = df_bar_charts.loc[df_bar_charts['weekday'] == 3]
friday = df_bar_charts.loc[df_bar_charts['weekday'] == 4]
saturday = df_bar_charts.loc[df_bar_charts['weekday'] == 5]
sunday = df_bar_charts.loc[df_bar_charts['weekday'] == 6]
#Months
june = df_bar_charts.loc[df_bar_charts['month'] == 6]
july = df_bar_charts.loc[df_bar_charts['month'] == 7]
august = df_bar_charts.loc[df_bar_charts['month'] == 8]
september = df_bar_charts.loc[df_bar_charts['month'] == 9]
#Fox
monday_fox_sum = monday['fox'].sum()
tuesday_fox_sum = tuesday['fox'].sum()
wednesday_fox_sum = wednesday['fox'].sum()
thursday_fox_sum = thursday['fox'].sum()
friday_fox_sum = friday['fox'].sum()
saturday_fox_sum = saturday['fox'].sum()
sunday_fox_sum = sunday['fox'].sum()
june_fox_sum = june['fox'].sum()
july_fox_sum = july['fox'].sum()
august_fox_sum = august['fox'].sum()
september_fox_sum = september['fox'].sum()
#Bear
monday_bear_sum = monday['bear'].sum()
tuesday_bear_sum = tuesday['bear'].sum()
wednesday_bear_sum = wednesday['bear'].sum()
thursday_bear_sum = thursday['bear'].sum()
friday_bear_sum = friday['bear'].sum()
saturday_bear_sum = saturday['bear'].sum()
sunday_bear_sum = sunday['bear'].sum()
june_bear_sum = june['bear'].sum()
july_bear_sum = july['bear'].sum()
august_bear_sum = august['bear'].sum()
september_bear_sum = september['bear'].sum()
#Wolf
monday_wolf_sum = monday['wolf'].sum()
tuesday_wolf_sum = tuesday['wolf'].sum()
wednesday_wolf_sum = wednesday['wolf'].sum()
thursday_wolf_sum = thursday['wolf'].sum()
friday_wolf_sum = friday['wolf'].sum()
saturday_wolf_sum = saturday['wolf'].sum()
sunday_wolf_sum = sunday['wolf'].sum()
june_wolf_sum = june['wolf'].sum()
july_wolf_sum = july['wolf'].sum()
august_wolf_sum = august['wolf'].sum()
september_wolf_sum = september['wolf'].sum()

#Cards
card_content1 = [
    dbc.CardHeader("Top5 most visited municipalities:"),
    dbc.CardBody(
        [
            html.H5("Top5 most visited municipalities by All:", className="card-title1"),
            html.P(
                [f"Municipality with most visits: {top1_unique_m}, Count: {top1_count} visits",
                 html.Br(),
                 f"Municipality with second most visits: {top2_unique_m}, Count: {top2_count} visits",
                 html.Br(),
                 f"Municipality with third most visits: {top3_unique_m},  Count: {top3_count} visits",
                 html.Br(),
                 f"Municipality with fourth most visits: {top4_unique_m}, Count: {top4_count} visits",
                 html.Br(),
                 f"Municipality with fifth most visits: {top5_unique_m},  Count: {top5_count} visits"],
                className="card-text",
            ),

            html.H5("Top5 most visited municipalities by Fox:", className="card-title2"),
            html.P(
                [f"Municipality with most visits: 784, Count: 1996 visits",
                 html.Br(),
                 f"Municipality with second most visits: 795, Count: 224 visits",
                 html.Br(),
                 f"Municipality with third most visits: 625,  Count: 219 visits",
                 html.Br(),
                 f"Municipality with fourth most visits: 890, Count: 142 visits",
                 html.Br(),
                 f"Municipality with fifth most visits: 887,  Count: 135 visits"],
                className="card-text",
            ),

            html.H5("Top5 most visited municipalities by Bear:", className="card-title3"),
            html.P(
                [f"Municipality with most visits: 784, Count: 1424 visits",
                 html.Br(),
                 f"Municipality with second most visits: 890, Count: 141 visits",
                 html.Br(),
                 f"Municipality with third most visits: 795,  Count: 93 visits",
                 html.Br(),
                 f"Municipality with fourth most visits: 625, Count: 89 visits",
                 html.Br(),
                 f"Municipality with fifth most visits: 198,  Count: 71 visits"],
                className="card-text",
            ),

            html.H5("Top5 most visited municipalities by Wolf:", className="card-title4"),
            html.P(
                [f"Municipality with most visits: 784, Count: 1526 visits",
                 html.Br(),
                 f"Municipality with second most visits: 890, Count: 175 visits",
                 html.Br(),
                 f"Municipality with third most visits: 625,  Count: 124 visits",
                 html.Br(),
                 f"Municipality with fourth most visits: 353, Count: 83 visits",
                 html.Br(),
                 f"Municipality with fifth most visits: 795,  Count: 71 visits"],
                className="card-text",
            ),
        ]
    ),
]
card_content2 = [
    dbc.CardHeader("Top5 most visited by unique visitors municipalities:"),
    dbc.CardBody(
        [
            html.H5("Top5 most visited municipalities by All:", className="card-title5"),
            html.P(
                [f"Municipality with most visits: {top1}, Count: {top1_unique} visits",
                 html.Br(),
                 f"Municipality with second most visits: {top2}, Count: {top2_unique} visits",
                 html.Br(),
                 f"Municipality with third most visits: {top3},  Count: {top3_unique} visits",
                 html.Br(),
                 f"Municipality with fourth most visits: {top4}, Count: {top4_unique} visits",
                 html.Br(),
                 f"Municipality with fifth most visits: {top5},  Count: {top5_unique} visits"],
                className="card-text",
            ),

            html.H5("Top5 most visited municipalities by Fox:", className="card-title6"),
            html.P(
                [f"Municipality with most visits: 784, Count: 9848 visits",
                 html.Br(),
                 f"Municipality with second most visits: 795, Count: 942 visits",
                 html.Br(),
                 f"Municipality with third most visits: 625,  Count: 731 visits",
                 html.Br(),
                 f"Municipality with fourth most visits: 890, Count: 428 visits",
                 html.Br(),
                 f"Municipality with fifth most visits: 887,  Count: 384 visits"],
                className="card-text",
            ),

            html.H5("Top5 most visited municipalities by Bear:", className="card-title7"),
            html.P(
                [f"Municipality with most visits: 784, Count: 13369 visits",
                 html.Br(),
                 f"Municipality with second most visits: 795, Count: 865 visits",
                 html.Br(),
                 f"Municipality with third most visits: 625,  Count: 567 visits",
                 html.Br(),
                 f"Municipality with fourth most visits: 511, Count: 416 visits",
                 html.Br(),
                 f"Municipality with fifth most visits: 890,  Count: 376 visits"],
                className="card-text",
            ),

            html.H5("Top5 most visited municipalities by Wolf:", className="card-title8"),
            html.P(
                [f"Municipality with most visits: 784, Count: 12004 visits",
                 html.Br(),
                 f"Municipality with second most visits: 795, Count: 766 visits",
                 html.Br(),
                 f"Municipality with third most visits: 625,  Count: 509 visits",
                 html.Br(),
                 f"Municipality with fourth most visits: 890, Count: 367 visits",
                 html.Br(),
                 f"Municipality with fifth most visits: 511,  Count: 262 visits"],
                className="card-text",
            ),
        ]
    ),
]
cards = dbc.Row(
    [
        dbc.Col(card_content1, width=6),
        dbc.Col(card_content2, width=6),
    ]
)
card_monday = [
    dbc.CardHeader("Mondays:"),
    dbc.CardBody(
        [
            html.H5("Fox:", className="card-title1"),
            html.P(
                [f"Number of calling activities: {monday_fox_sum}",],
                className="card-text",
            ),

            html.H5("Bear:", className="card-title2"),
            html.P(
                [f"Number of calling activities: {monday_bear_sum}",],
                className="card-text",
            ),

            html.H5("Wolf:", className="card-title3"),
            html.P(
                [f"Number of calling activities: {monday_wolf_sum}",],
                className="card-text",
            ),
        ]
    ),
]
card_tuesday = [
    dbc.CardHeader("Tuesdays:"),
    dbc.CardBody(
        [
            html.H5("Fox:", className="card-title1"),
            html.P(
                [f"Number of calling activities: {tuesday_fox_sum}",],
                className="card-text",
            ),

            html.H5("Bear:", className="card-title2"),
            html.P(
                [f"Number of calling activities: {tuesday_bear_sum}",],
                className="card-text",
            ),

            html.H5("Wolf:", className="card-title3"),
            html.P(
                [f"Number of calling activities: {tuesday_wolf_sum}",],
                className="card-text",
            ),
        ]
    ),
]
card_wednesday = [
    dbc.CardHeader("Wednesdays:"),
    dbc.CardBody(
        [
            html.H5("Fox:", className="card-title1"),
            html.P(
                [f"Number of calling activities: {wednesday_fox_sum}",],
                className="card-text",
            ),

            html.H5("Bear:", className="card-title2"),
            html.P(
                [f"Number of calling activities: {wednesday_bear_sum}",],
                className="card-text",
            ),

            html.H5("Wolf:", className="card-title3"),
            html.P(
                [f"Number of calling activities: {wednesday_wolf_sum}",],
                className="card-text",
            ),
        ]
    ),
]
card_thursday = [
    dbc.CardHeader("Thursdays:"),
    dbc.CardBody(
        [
            html.H5("Fox:", className="card-title1"),
            html.P(
                [f"Number of calling activities: {thursday_fox_sum}",],
                className="card-text",
            ),

            html.H5("Bear:", className="card-title2"),
            html.P(
                [f"Number of calling activities: {thursday_bear_sum}",],
                className="card-text",
            ),

            html.H5("Wolf:", className="card-title3"),
            html.P(
                [f"Number of calling activities: {thursday_wolf_sum}",],
                className="card-text",
            ),
        ]
    ),
]
card_friday = [
    dbc.CardHeader("Fridays:"),
    dbc.CardBody(
        [
            html.H5("Fox:", className="card-title1"),
            html.P(
                [f"Number of calling activities: {friday_fox_sum}",],
                className="card-text",
            ),

            html.H5("Bear:", className="card-title2"),
            html.P(
                [f"Number of calling activities: {friday_bear_sum}",],
                className="card-text",
            ),

            html.H5("Wolf:", className="card-title3"),
            html.P(
                [f"Number of calling activities: {friday_wolf_sum}",],
                className="card-text",
            ),
        ]
    ),
]
card_saturday = [
    dbc.CardHeader("Saturdays:"),
    dbc.CardBody(
        [
            html.H5("Fox:", className="card-title1"),
            html.P(
                [f"Number of calling activities: {saturday_fox_sum}",],
                className="card-text",
            ),

            html.H5("Bear:", className="card-title2"),
            html.P(
                [f"Number of calling activities: {saturday_bear_sum}",],
                className="card-text",
            ),

            html.H5("Wolf:", className="card-title3"),
            html.P(
                [f"Number of calling activities: {saturday_wolf_sum}",],
                className="card-text",
            ),
        ]
    ),
]
card_sunday = [
    dbc.CardHeader("Sundays:"),
    dbc.CardBody(
        [
            html.H5("Fox:", className="card-title1"),
            html.P(
                [f"Number of calling activities: {sunday_fox_sum}",],
                className="card-text",
            ),

            html.H5("Bear:", className="card-title2"),
            html.P(
                [f"Number of calling activities: {sunday_bear_sum}",],
                className="card-text",
            ),

            html.H5("Wolf:", className="card-title3"),
            html.P(
                [f"Number of calling activities: {sunday_wolf_sum}",],
                className="card-text",
            ),
        ]
    ),
]
cards_weekdays = dbc.Row(
    [
        dbc.Col(card_monday, width=3),
        dbc.Col(card_tuesday, width=3),
        dbc.Col(card_wednesday, width=3),
        dbc.Col(card_thursday, width=3),
        dbc.Col(card_friday, width=3),
        dbc.Col(card_saturday, width=3),
        dbc.Col(card_sunday, width=3),
    ]
)
card_june = [
    dbc.CardHeader("June:"),
    dbc.CardBody(
        [
            html.H5("Fox:", className="card-title1"),
            html.P(
                [f"Number of calling activities: {june_fox_sum}",],
                className="card-text",
            ),

            html.H5("Bear:", className="card-title2"),
            html.P(
                [f"Number of calling activities: {june_bear_sum}",],
                className="card-text",
            ),

            html.H5("Wolf:", className="card-title3"),
            html.P(
                [f"Number of calling activities: {june_wolf_sum}",],
                className="card-text",
            ),
        ]
    ),
]
card_july = [
    dbc.CardHeader("July:"),
    dbc.CardBody(
        [
            html.H5("Fox:", className="card-title1"),
            html.P(
                [f"Number of calling activities: {july_fox_sum}",],
                className="card-text",
            ),

            html.H5("Bear:", className="card-title2"),
            html.P(
                [f"Number of calling activities: {july_bear_sum}",],
                className="card-text",
            ),

            html.H5("Wolf:", className="card-title3"),
            html.P(
                [f"Number of calling activities: {july_wolf_sum}",],
                className="card-text",
            ),
        ]
    ),
]
card_august = [
    dbc.CardHeader("August:"),
    dbc.CardBody(
        [
            html.H5("Fox:", className="card-title1"),
            html.P(
                [f"Number of calling activities: {august_fox_sum}",],
                className="card-text",
            ),

            html.H5("Bear:", className="card-title2"),
            html.P(
                [f"Number of calling activities: {august_bear_sum}",],
                className="card-text",
            ),

            html.H5("Wolf:", className="card-title3"),
            html.P(
                [f"Number of calling activities: {august_wolf_sum}",],
                className="card-text",
            ),
        ]
    ),
]
card_september = [
    dbc.CardHeader("September:"),
    dbc.CardBody(
        [
            html.H5("Fox:", className="card-title1"),
            html.P(
                [f"Number of calling activities: {september_fox_sum}",],
                className="card-text",
            ),

            html.H5("Bear:", className="card-title2"),
            html.P(
                [f"Number of calling activities: {september_bear_sum}",],
                className="card-text",
            ),

            html.H5("Wolf:", className="card-title3"),
            html.P(
                [f"Number of calling activities: {september_wolf_sum}",],
                className="card-text",
            ),
        ]
    ),
]
cards_months = dbc.Row(
    [
        dbc.Col(card_june, width=3),
        dbc.Col(card_july, width=3),
        dbc.Col(card_august, width=3),
        dbc.Col(card_september, width=3),
    ]
)

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "20rem",
    "padding": "2rem 1rem",
}
content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

#Layout
layout = html.Div(
    [
        html.H1('Practical Work 1',
                style={'textAlign': 'center', 'color': 'black'}),
        #Filter
        html.Hr(),
        html.Label(children=['Legend for first Map '], style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
        html.Ul([
            html.Li("Fox", className='circle', style={'background': '#ea3c12', 'color': 'black',
                                                          'list-style': 'none', 'text-indent': '17px'}),
            html.Li("Bear", className='circle', style={'background': '#6d412a', 'color': 'black',
                                                      'list-style': 'none', 'text-indent': '17px',
                                                      'white-space': 'nowrap'}),
            html.Li("Wolf", className='circle', style={'background': '#697e8d', 'color': 'black',
                                                            'list-style': 'none', 'text-indent': '17px'}),
        ], style={'padding-top': '6px'}
        ),
        html.Hr(),
        html.Label(children=['Filters for the first two Map and both Hexbinmaps:\n '], style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
        html.Br(),
        # Select Country
        html.Label(children=['Select Country: '], style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
        dcc.Checklist(id='country',
                      options=[
                          {'label': 'Fox', 'value': 0},
                          {'label': 'Bear', 'value': 1},
                          {'label': 'Wolf', 'value': 2},
                      ],
                      value=[b for b in sorted(df_merge_Date['value'].unique())],
                      style={'padding-left': '80px', 'padding-right': '20px', "display": "inline", 'color': 'black'},
                      labelStyle={"display": "inline", 'padding-top': '6px'}
                      ),
        html.Hr(),
        # Select Month
        html.Label(children=['Select Month: '], style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
        dcc.Checklist(id='month',
                      options=[
                          {'label': 'June', 'value': 6},
                          {'label': 'July', 'value': 7},
                          {'label': 'August', 'value': 8},
                          {'label': 'September', 'value': 9},
                      ],
                      value=[b for b in sorted(df_merge_Date['month'].unique())],
                      style={'padding-left': '100px', 'padding-right': '20px', "display": "inline", 'color': 'black'},
                      labelStyle={"display": "inline", 'padding-top': '6px'}
                      ),
        html.Hr(),
        # Select Weekday
        html.Label(children=['Select Weekday: '], style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
        dcc.Checklist(id='weekday',
                      options=[
                          {'label': 'Monday', 'value': 0},
                          {'label': 'Tuesday', 'value': 1},
                          {'label': 'Wednesday', 'value': 2},
                          {'label': 'Thurday', 'value': 3},
                          {'label': 'Friday', 'value': 4},
                          {'label': 'Saturday', 'value': 5},
                          {'label': 'Sunday', 'value': 6},
                      ],
                      value=[b for b in sorted(df_merge_Date['weekday'].unique())],
                      style={'padding-left': '100px', 'padding-right': '20px', "display": "inline", 'color': 'black'},
                      labelStyle={"display": "inline", 'padding-top': '6px'}
                      ),
        html.Hr(),
        # Select hour
        html.Label(children=['Select hour of the day: '], style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
        dcc.Checklist(id='hour',
                      options=[
                          {'label': '12AM', 'value': 0},
                          {'label': '1AM', 'value': 1},
                          {'label': '2AM', 'value': 2},
                          {'label': '3AM', 'value': 3},
                          {'label': '4AM', 'value': 4},
                          {'label': '5AM', 'value': 5},
                          {'label': '6AM', 'value': 6},
                          {'label': '7AM', 'value': 7},
                          {'label': '8AM', 'value': 8},
                          {'label': '9AM', 'value': 9},
                          {'label': '10AM', 'value': 10},
                          {'label': '11AM', 'value': 11},
                          {'label': '12PM', 'value': 12},
                          {'label': '1PM', 'value': 13},
                          {'label': '2PM', 'value': 14},
                          {'label': '3PM', 'value': 15},
                          {'label': '4PM', 'value': 16},
                          {'label': '5PM', 'value': 17},
                          {'label': '6PM', 'value': 18},
                          {'label': '7PM', 'value': 19},
                          {'label': '8PM', 'value': 20},
                          {'label': '9PM', 'value': 21},
                          {'label': '10PM', 'value': 22},
                          {'label': '11PM', 'value': 23},
                      ],
                      value=[b for b in sorted(df_merge_Date['hour'].unique())],
                      style={'padding-left': '100px', 'padding-right': '20px', "display": "inline", 'color': 'black'},
                      labelStyle={"display": "inline", 'padding-top': '6px'}
                      ),
        html.Hr(),

        # Map
        html.Div([
            # Karte 1 Auswahl
            dbc.Spinner(children=[dcc.Graph(id='map1', config={'displayModeBar': False, 'scrollZoom': True},
                                            style={'background': '#ffffff', 'padding-bottom': '2px',
                                                   'padding-left': '20px',
                                                   'height': '100vh', 'width': '150vh'}
                                            )], size="lg", color="primary", type="border", fullscreen=False, ),
            html.Hr(),
            dbc.Spinner(children=[dcc.Graph(id='map1_animated', config={'displayModeBar': False, 'scrollZoom': True},
                                            style={'background': '#ffffff', 'padding-bottom': '2px',
                                                   'padding-left': '20px',
                                                   'height': '100vh', 'width': '150vh'}
                                            )], size="lg", color="primary", type="border", fullscreen=False, ),
            html.Hr(),
            html.Label(children=['Select an user id: '], style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
            dcc.Dropdown(df_merge_Date["pos_usr_id"].unique(),
                         id='user_dropdown',
                         value=12244863,
                         style={'padding-left': '80px', 'padding-right': '20px'},# "display": "inline", 'color': 'black'},
                         searchable=True, ),
            dbc.Spinner(
                children=[dcc.Graph(id='map_movement_id', config={'displayModeBar': False, 'scrollZoom': True},
                                    style={'background': '#ffffff', 'padding-bottom': '2px',
                                           'padding-left': '2px',
                                           'height': '100vh', 'width': '150vh'}
                                    )], size="lg", color="primary", type="border", fullscreen=False, ),
            dbc.Spinner(
                children=[dcc.Graph(id='map2_movement_id', config={'displayModeBar': False, 'scrollZoom': True},
                                    style={'background': '#ffffff', 'padding-bottom': '2px',
                                           'padding-left': '20px',
                                           'height': '100vh', 'width': '150vh'}
                                    )], size="lg", color="primary", type="border", fullscreen=False, ),
            html.Hr(),
            # Heatmap
            dbc.Spinner(children=[dcc.Graph(id='map2', config={'displayModeBar': False, 'scrollZoom': True},
                                            style={'background': '#ffffff', 'padding-bottom': '2px',
                                                   'padding-left': '40px',
                                                   'height': '100vh', 'width': '150vh'}
                                            )], size="lg", color="primary", type="border", fullscreen=False, ),
            html.Hr(),
            # Choropleth municipality
            html.Label(children=['Select country: '], style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
            dcc.Dropdown(id='dropdown_country_municipality',
                         options=[
                             {'label': 'All', 'value': 'count'},
                             {'label': 'Fox', 'value': 'fox_count'},
                             {'label': 'Bear', 'value': 'bear_count'},
                             {'label': 'Wolf', 'value': 'wolf_count'},
                         ],
                         optionHeight=35,
                         value='count',
                         disabled=False,
                         multi=False,
                         searchable=True,
                         search_value='',
                         placeholder='Please select...',
                         clearable=True,
                         style={'padding-left': '80px', 'padding-right': '20px'}
                         ),
            dbc.Spinner(children=[dcc.Graph(id='map_municipality', config={'displayModeBar': False, 'scrollZoom': True},
                                            style={'padding-left': '80px', 'padding-right': '20px'}
                                            )], size="lg", color="primary", type="border", fullscreen=False, ),
            dbc.Col(dbc.Card(cards, color="primary", outline=True),
                                            style={'padding-left': '80px', 'padding-right': '20px',}),
            dbc.Spinner(children=[dcc.Graph(id='graph3', config={'displayModeBar': False, 'scrollZoom': True},
                                            style={'background': '#ffffff', 'padding-bottom': '2px',
                                                   'padding-left': '20px',
                                                   'height': '100vh', 'width': '150vh'}
                                            )], size="lg", color="primary", type="border", fullscreen=False, ),
            html.Hr(),
            dbc.Spinner(children=[dcc.Graph(id='graph4', config={'displayModeBar': False, 'scrollZoom': True},
                                            style={'padding-left': '100px', 'padding-right': '20px',}
                                            )], size="lg", color="primary", type="border", fullscreen=False, ),
            html.Hr(),
            # Chart 1
            html.Label(children=['Select country: '],
                       style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
            dcc.Dropdown(id='dropdown_country',
                         options=[
                             {'label': 'Fox', 'value': 'fox'},
                             {'label': 'Bear', 'value': 'bear'},
                             {'label': 'Wolf', 'value': 'wolf'},
                         ],
                         optionHeight=35,
                         value='fox',
                         disabled=False,
                         multi=False,
                         searchable=True,
                         search_value='',
                         placeholder='Please select...',
                         clearable=True,
                         style={'padding-left': '80px', 'padding-right': '20px'}
                         ),

        ],  # className='nine columns'
        ),
        dbc.Spinner(children=[dcc.Graph(id='graph2', config={'displayModeBar': False, 'scrollZoom': True},
                                        style={'background': '#ffffff', 'padding-bottom': '2px',
                                               'padding-left': '20px',
                                               'height': '100vh', 'width': '150vh'}
                                        )], size="lg", color="primary", type="border", fullscreen=False, ),
        html.Hr(),
        dbc.Spinner(children=[dcc.Graph(id='bar1', config={'displayModeBar': False, 'scrollZoom': True},
                                        style={'background': '#ffffff', 'padding-bottom': '2px',
                                               'padding-left': '20px',
                                               'height': '100vh', 'width': '150vh'}
                                        )], size="lg", color="primary", type="border", fullscreen=False, ),
        dbc.Col(dbc.Card(cards_weekdays, color="primary", outline=True),
                                        style={'padding-left': '80px', 'padding-right': '20px',}),
        html.Hr(),
        dbc.Spinner(children=[dcc.Graph(id='bar2', config={'displayModeBar': False, 'scrollZoom': True},
                                        style={'background': '#ffffff', 'padding-bottom': '2px',
                                               'padding-left': '20px',
                                               'height': '100vh', 'width': '150vh'}
                                        )], size="lg", color="primary", type="border", fullscreen=False, ),
        dbc.Col(dbc.Card(cards_months, color="primary", outline=True),
                                        style={'padding-left': '80px', 'padding-right': '20px',}),
        html.Hr(),
        dbc.Spinner(children=[dcc.Graph(id='bar3', config={'displayModeBar': False, 'scrollZoom': True},
                                        style={'background': '#ffffff', 'padding-bottom': '2px',
                                               'padding-left': '20px',
                                               'height': '100vh', 'width': '150vh'}
                                        )], size="lg", color="primary", type="border", fullscreen=False, ),
        html.Hr(),
        content,
    ]   #until here
)


# callback map1
@callback(Output('map1', 'figure'),
              [Input('country', 'value'),
               Input('month', 'value'),
               Input('weekday', 'value'),
               Input('hour', 'value'),])

def maps_fct(country_value, month_value, weekday_value, hour_value):
    filter_country = (df_merge_Date['value'].isin(country_value))
    filter_month = (df_merge_Date['month'].isin(month_value))
    filter_weekday = (df_merge_Date['weekday'].isin(weekday_value))
    filter_hour = (df_merge_Date['hour'].isin(hour_value))
    df_sub = df_merge_Date[filter_country & filter_month & filter_weekday & filter_hour]
    locations = [go.Scattermapbox(
        lon=df_sub['lon'],
        lat=df_sub['lat'],
        mode='markers',
        marker={'color': df_sub['color']},
        unselected={'marker': {'opacity': 1}},
        selected={'marker': {'opacity': 0.5, 'size': 25}},
        hoverinfo='text',
        hovertext=df_sub['name'],
        #customdata=df_sub['website']
    )]
    # Return figure
    return {
        'data': locations,
        'layout': go.Layout(
            uirevision='foo',  # preserves state of figure/map after callback activated
            clickmode='event+select',
            hovermode='closest',
            hoverdistance=2,
            title=dict(text="Antennas", font=dict(size=50, color='green')),
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=25,
                style='light',
                center=dict(
                    lat=58.729093,
                    lon=25.748348
                ),
                pitch=0,
                zoom=7
            ),
        )
    }

# callback map1 animated
@callback(Output('map1_animated', 'figure'),
              [Input('country', 'value'),
               Input('month', 'value'),
               Input('weekday', 'value'),
               Input('hour', 'value'), ])

def maps_animated_fct(country_value, month_value, weekday_value, hour_value):
    filter_country = (df_merge_Date['value'].isin(country_value))
    filter_month = (df_merge_Date['month'].isin(month_value))
    filter_weekday = (df_merge_Date['weekday'].isin(weekday_value))
    filter_hour = (df_merge_Date['hour'].isin(hour_value))
    df_sub = df_merge_Date[filter_country & filter_month & filter_weekday & filter_hour]
    fig = px.scatter_mapbox(df_sub, lat="lat", lon="lon",
                            #center = dict(lon = 134,lat = -25), zoom = 2.4,
                            animation_frame='Date', animation_group='Date',
                            color='iso_a2', #size="country",
                            #color_continuous_scale=px.colors.cyclical.IceFire,
                            size_max=70, zoom=6, hover_name='name',
                            #hover_data=['Confirmed', 'Deaths', 'Recovery'],
                            title='Animated')
    return fig

# callback map movement paths
@callback(Output('map_movement_id', 'figure'),
         [Input('user_dropdown', 'value'),])

def maps_user_fct(user_id):
    user = df_merge_Date.loc[df_merge_Date['pos_usr_id'] == user_id]
    #px.set_mapbox_access_token(open("https://raw.githubusercontent.com/Leonieen/MLBS/main/access.mapbox_token").read())
    px.set_mapbox_access_token('pk.eyJ1IjoiZ2VvbmllIiwiYSI6ImNsM210Ymc3ODA4NGozaWw4aG1hNDJtMW4ifQ.mmjDtqmcSpEZM2JyXe9Q8g')
    user_map = [go.Scattermapbox(
        mode="markers+lines",
        lat=user.lat.tolist(),
        lon=user.lon.tolist(),
        hovertext=user.call_time.tolist(),
        marker={'color': "red",
                "size": 10},
    )]
    # Return figure
    return {
        'data': user_map,
        'layout': go.Layout(
            uirevision='foo',  # preserves state of figure/map after callback activated
            clickmode='event+select',
            hovermode='closest',
            hoverdistance=2,
            title=dict(text="Movement unique user", font=dict(size=50, color='green')),
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=25,
                style='light',
                center=dict(
                    lat=58.729093,
                    lon=25.748348
                ),
                pitch=0,
                zoom=7
            ),
        )
    }

# callback map movement paths 2 animated
@callback(Output('map2_movement_id', 'figure'),
         [Input('user_dropdown', 'value'),])

def maps_user_animated_fct(user_id):
    user = df_merge_Date.loc[df_merge_Date['pos_usr_id'] == user_id]
    #px.set_mapbox_access_token(open("https://raw.githubusercontent.com/Leonieen/MLBS/main/access.mapbox_token").read())
    px.set_mapbox_access_token('pk.eyJ1IjoiZ2VvbmllIiwiYSI6ImNsM210Ymc3ODA4NGozaWw4aG1hNDJtMW4ifQ.mmjDtqmcSpEZM2JyXe9Q8g')
    map_user = px.scatter_mapbox(user, lat="lat", lon="lon",
                            animation_frame='Date', animation_group='Date',
                            color='site_id',
                            size_max=70, zoom=6, hover_name='name',
                            title='Animated')
    return map_user

# callback map2
@callback(Output('map2', 'figure'),
              [Input('country', 'value'),])

def heat_map1_fkt(country_value):
    x = country_value
    df = antennas_count_df
    geojson = shape
    lat = df_heatmap["lat"]
    lon = df_heatmap["lon"]
    frame = df_heatmap["Date"]
    fig = go.Figure(go.Densitymapbox(lat=df.lat, lon=df.lon, z=df.counts,
                                     radius=50))
    fig.update_layout(mapbox_style="carto-positron", mapbox_center_lat=58.729093, mapbox_center_lon=25.748348, mapbox_zoom=7)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

# callback municipality
@callback(Output('map_municipality', 'figure'),
              [Input('dropdown_country_municipality', 'value'),])

def municipality_fkt(country_value):
    df = df_okood
    cr = [0, df_okood[country_value].quantile(.95)]

    with urlopen(
            'https://raw.githubusercontent.com/Leonieen/MLBS/main/Data/ee_municipalities_WGS84.geojson') as response:
        estonia = json.load(response)
    fig = px.choropleth_mapbox(df, geojson=estonia, locations='OKOOD', color=country_value,
                               color_continuous_scale="plasma",
                               # range_color=(0, 12),
                               featureidkey="properties.lau2",
                               mapbox_style="carto-positron",
                               zoom=6, center={"lat": 58.729093, "lon": 25.748348},
                               opacity=0.5,
                               range_color=cr,
                               labels={'count': 'municipality count'}
                               )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

# callback home bar chart
@callback(Output('graph2', 'figure'),
              [Input('dropdown_country', 'value'),])
def bar_chart_fkt(dd_country_value):
    graph2 = px.bar(df_bar_charts, x='weekday', y=dd_country_value, color='month', title="Bar chart")
    return graph2

#Graph3
@callback(Output('graph3', 'figure'),
              [Input('country', 'value'),
               Input('month', 'value'),
               Input('weekday', 'value'),
               Input('hour', 'value'), ])

def hex_map1_fkt(country_value, month_value, weekday_value, hour_value):
    filter_country = (df_merge_Date['value'].isin(country_value))
    filter_month = (df_merge_Date['month'].isin(month_value))
    filter_weekday = (df_merge_Date['weekday'].isin(weekday_value))
    filter_hour = (df_merge_Date['hour'].isin(hour_value))
    df_sub = df_merge_Date[filter_country & filter_month & filter_weekday & filter_hour]
    #px.set_mapbox_access_token(open("https://raw.githubusercontent.com/Leonieen/MLBS/main/access.mapbox_token").read())
    px.set_mapbox_access_token('pk.eyJ1IjoiZ2VvbmllIiwiYSI6ImNsM210Ymc3ODA4NGozaWw4aG1hNDJtMW4ifQ.mmjDtqmcSpEZM2JyXe9Q8g')
    lat = df_sub["lat"]
    lon = df_sub["lon"]
    frame = df_sub["Date"]

    fig = ff.create_hexbin_mapbox(
        data_frame=df_sub, lat="lat", lon="lon",
        nx_hexagon=15, opacity=0.5, labels={"color": "Point Count"},
        min_count=1, color_continuous_scale="plasma",
        show_original_data=True,
        range_color=[0, 430],
        title='Hexbin Map for call density ',
        original_data_marker=dict(size=4, opacity=0.6, color="deeppink")
    )
    return fig

#Graph3
@callback(Output('graph4', 'figure'),
              [Input('country', 'value'),
               Input('month', 'value'),
               Input('weekday', 'value'),
               Input('hour', 'value'), ])
def hex_anim1_fkt(country_value, month_value, weekday_value, hour_value):
    filter_country = (df_merge_Date['value'].isin(country_value))
    filter_month = (df_merge_Date['month'].isin(month_value))
    filter_weekday = (df_merge_Date['weekday'].isin(weekday_value))
    filter_hour = (df_merge_Date['hour'].isin(hour_value))
    df_sub = df_merge_Date[filter_country & filter_month & filter_weekday & filter_hour]
    lat = df_sub["lat"]
    lon = df_sub["lon"]
    frame = df_sub["Date"]
    #px.set_mapbox_access_token(open("https://raw.githubusercontent.com/Leonieen/MLBS/main/access.mapbox_token").read())
    px.set_mapbox_access_token('pk.eyJ1IjoiZ2VvbmllIiwiYSI6ImNsM210Ymc3ODA4NGozaWw4aG1hNDJtMW4ifQ.mmjDtqmcSpEZM2JyXe9Q8g')
    graph4 = ff.create_hexbin_mapbox(
        lat=lat, lon=lon, nx_hexagon=15, animation_frame=frame,
        color_continuous_scale="plasma", labels={"color": "Point Count", "frame": "Period"},
        opacity=0.5, min_count=1,
        range_color=[0, 30],
        show_original_data=True, original_data_marker=dict(opacity=0.6, size=4, color="deeppink")
    )
    graph4.update_layout(margin=dict(b=0, t=0, l=0, r=0))
    graph4.layout.sliders[0].pad.t=20
    graph4.layout.updatemenus[0].pad.t=40
    return graph4

# callback home bar chart1
@callback(Output('bar1', 'figure'),
              [Input('dropdown_country', 'value'),])
def bar_chart1_fkt(dd_country_value):
    bar1 = px.bar(df_charts, x="weekday", y="count", color='country', title="Weekday")
    return bar1

# callback home bar chart1
@callback(Output('bar2', 'figure'),
              [Input('dropdown_country', 'value'),])
def bar_chart2_fkt(dd_country_value):
    bar2 = px.bar(df_charts, x="month", y="count", color='country', title="Month")
    return bar2

# callback home bar chart1
@callback(Output('bar3', 'figure'),
              [Input('dropdown_country', 'value'),])
def bar_chart_fkt(dd_country_value):
    bar3 = px.bar(df_charts, x="country", y="count", color='month', title="Country")
    return bar3

# callback map1
@callback(Output('map_gps', 'figure'),
              [Input('country', 'value'),
               Input('month', 'value'),
               Input('weekday', 'value'),
               Input('hour', 'value'),])

def maps3_fct(country_value, month_value, weekday_value, hour_value):
    filter_country = (df_merge_Date['value'].isin(country_value))
    filter_month = (df_merge_Date['month'].isin(month_value))
    filter_weekday = (df_merge_Date['weekday'].isin(weekday_value))
    filter_hour = (df_merge_Date['hour'].isin(hour_value))
    df_sub = df_merge_Date[filter_country & filter_month & filter_weekday & filter_hour]
    locations = [go.Scattermapbox(
        lon=df_sub['lon'],
        lat=df_sub['lat'],
        mode='markers',
        marker={'color': df_sub['color']},
        unselected={'marker': {'opacity': 1}},
        selected={'marker': {'opacity': 0.5, 'size': 25}},
        hoverinfo='text',
        hovertext=df_sub['name'],
    )]
    # Return figure
    return {
        'data': locations,
        'layout': go.Layout(
            uirevision='foo',
            clickmode='event+select',
            hovermode='closest',
            hoverdistance=2,
            title=dict(text="Antennas", font=dict(size=50, color='green')),
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=25,
                style='light',
                center=dict(
                    lat=58.729093,
                    lon=25.748348
                ),
                pitch=0,
                zoom=7
            ),
        )
    }
