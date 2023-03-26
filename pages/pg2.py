import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import json
import urllib.request
import numpy as np
import plotly.graph_objects as go

dash.register_page(__name__, name='PracticalWork2')

api_token = "pk.eyJ1IjoiZ2VvbmllIiwiYSI6ImNsM210Ymc3ODA4NGozaWw4aG1hNDJtMW4ifQ.mmjDtqmcSpEZM2JyXe9Q8g"

# page 2 data
df = px.data.tips()
gps_data = "https://raw.githubusercontent.com/Leonieen/MLBS/main/Data/df_altitude_final.csv"
gps_df = pd.read_csv(gps_data)
mileage = "https://raw.githubusercontent.com/Leonieen/MLBS/main/Data/df_mileage.csv"
df_mileage = pd.read_csv(mileage)
min_max = "https://raw.githubusercontent.com/Leonieen/MLBS/main/Data/df_min_max.csv"
df_min_max = pd.read_csv(min_max)
month_hour = "https://raw.githubusercontent.com/Leonieen/MLBS/main/Data/df_altitude_hour.csv"
df_month_hour = pd.read_csv(month_hour)
by_hour = df_month_hour['hour'].value_counts().sort_index()
df_hour = by_hour.rename_axis('hour').reset_index(name='counts')
by_month = pd.to_datetime(df_month_hour['date']).dt.to_period('d').value_counts().sort_index()
by_month.index = pd.PeriodIndex(by_month.index)
df_month = by_month.rename_axis('month').reset_index(name='counts')
df_month['Day'] = df_month.reset_index().index + 1
map_url = "https://raw.githubusercontent.com/Leonieen/MLBS/main/Data/California_County_Boundaries.geojson"
with urllib.request.urlopen(map_url) as url:
        jdata = json.loads(url.read().decode())

fig_table = go.Figure(data=[go.Table(
    header=dict(values=["days", "mileage"],
                fill_color='lightgrey',
                line_color='darkslategray',
                align='left'),
    cells=dict(values=[df_mileage.day, df_mileage.daily_mileage],
               fill_color='white',
               line_color='darkslategray',
               align='left'))
])

fig_min_max = go.Figure(data=[go.Table(
    header=dict(values=["id", 'speed', 'header_id', 'X', 'Y', 'new_datetime',
                       'stop_nr', 'date', 'time', 'altitude'],
                fill_color='lightgrey',
                line_color='darkslategray',
                align='left'),
    cells=dict(values=[df_min_max.id, df_min_max.speed, df_min_max.header_id, df_min_max.X, df_min_max.Y, df_min_max.new_datetime,
                       df_min_max.stop_nr, df_min_max.date, df_min_max.time, df_min_max.altitude],
               fill_color='white',
               line_color='darkslategray',
               align='left'))
])

fig_month = px.bar(df_month, x='Day', y="counts", title='Amount of Points of each day')
fig_hour = px.bar(df_hour, x='hour', y="counts", title='Amount of Points of each hour')

#Cards
card_content_longest = [
    dbc.CardHeader("Longest and shortest Trip"),
    dbc.CardBody(
        [
            html.P(
                [f"The daily mileage of the trips has been calculated with geopy.distance from the geodesic package.",
                 html.Br(),
                 f"For this a list of tuples of the Latitude and Longitude columns has been created.",
                 html.Br(),
                 f"The distance between two GPS points has been calculated with geodesic(point1, point2).miles",
                 html.Br(),
                 f"Then in a for-loop the total distance traveled in a day has been calculated"],
                className="card-text",
            ),
            html.H5("Longest trip:", className="card-titlelength1"),
            html.P(
                [f"Based on these calculations the day with the longest trip was 2018-05-02 with 1743.131766 miles.",
                 html.Br(),
                 f"This does not seem realistic and could be explained based on a gap in the data, as can be seen on the map.",
                 html.Br(),
                 f"Another source of error can be the conversion of days and their differentiation, where there were major difficulties."],
                className="card-text",
            ),

            html.H5("Shortest Trip:", className="card-titlelength2"),
            html.P(
                [f"Based on these calculations the day with the shortest trip was 2018-05-09 with 0.709665 miles.",
                 html.Br(),
                 f"On this day it seems like, the hotel has not been left by the GPS device.",
                 html.Br(),],
                className="card-text",
            ),
        ]
    ),
]

card_length = dbc.Row(
    [
        dbc.Col(card_content_longest, width=12),
    ]
)

#Cards
card_content_height = [
    dbc.CardHeader("Highest and lowest Point"),
    dbc.CardBody(
        [
            html.P(
                [f"The elevation information of the route travelled is located in the 3D scatterplot based on its coordinates. .",
                 html.Br(),
                 f"For spatial classification, the outline of California (based on a geojson) was also plotted.",
                 html.Br(),
                 f"The table above shows the information on the lowest and highest points.",
                 html.Br(),],
                className="card-text",
            ),
            html.H5("Lowest Point:", className="card-titlelowest2"),
            html.P(
                [f"Based on the altitude information the highest point is -105 underneath NN.",
                 html.Br(),
                 f"It is located in 601 Wave St, Monterey, CA 93940, USA.",
                 html.Br(),],
                className="card-text",
            ),
            html.H5("Highest Point:", className="card-titlehighest1"),
            html.P(
                [f"Based on the altitude information the highest point is 3067m above NN.",
                 html.Br(),
                 f"It is located near the Methuselah (Tree), White Mountains, Inyo.",
                 html.Br(),
                 f"This is a longleaf pine that grows in the Inyo National Forest in the highest region of the White Mountains between Nevada and Death Valley at an altitude of over 3000m."],
                className="card-text",
            ),
        ]
    ),
]

card_height = dbc.Row(
    [
        dbc.Col(card_content_height, width=12),
    ]
)

#Cards
card_content_time = [
    dbc.CardHeader("Longest and shortest Trip"),
    dbc.CardBody(
        [
            html.P(
                [f"The bar charts above show the distributions/frequencies of GPS data.",
                 html.Br(),
                 f"These visualisations were included to see if there are certain temporal trends or if, for example, lunch breaks or overnight stays are also visible.",
                 html.Br(),
                 f"However, this visualisation method is not entirely unproblematic for the evaluation of this question. For example, all data were previously thinned out in the data set where there were duplicate time entries, these could have a significant influence on the results.",
                 html.Br(),
                 f"Likewise, the frequency of GPS data is probably not the best measure, but rather distances travelled between time points."],
                className="card-text",
            ),
            html.H5("Analysis of the days:", className="card-titleday1"),
            html.P(
                [f"This problem becomes very visible here in the visualisation of the distribution over the days.",
                 html.Br(),
                 f"According to the evaluation of the maps and coordinates, there was hardly any movement on the last few days, although the values in the diagrams are rather low, the comparison with the remaining days is nevertheless not drastic enough. ",
                 html.Br(),
                 f"Overall, there are also too large differences here to the distance values from the upper table."],
                className="card-text",
            ),

            html.H5("Analysis of the days:", className="card-titlehour2"),
            html.P(
                [f"A similar picture emerges when looking at the frequency of hours.",
                 html.Br(),
                 f"It is very visible here that most of the activities took place between 8 am and 5 pm.",
                 html.Br(),
                 f"And a small drop around midday is also visible, but here, too, a visualisation of the distance travelled would make much more sense.",
                 html.Br(),],
                className="card-text",
            ),
        ]
    ),
]

card_time = dbc.Row(
    [
        dbc.Col(card_content_time, width=12),
    ]
)

#Cards
card_content_ProCon = [
    dbc.CardHeader("Pros and cons of the data in this kind of tourism analysis:"),
    dbc.CardBody(
        [
            html.P(
                [f"The elevation information of the route travelled is located in the 3D scatterplot based on its coordinates. .",
                 html.Br(),
                 f"For spatial classification, the outline of California (based on a geojson) was also plotted.",
                 html.Br(),
                 f"The table above shows the information on the lowest and highest points.",
                 html.Br(),],
                className="card-text",
            ),
            html.H5("Pros:", className="card-titlePro2"),
            html.P(
                [f"1. Accuracy: GPS data provides highly accurate location information that can be used to track the exact location of tourists, which is valuable in analyzing travel patterns and behavior.",
                 html.Br(),
                 f"2. Real-time data: GPS data provides real-time data that can be used to monitor tourist behavior in real-time, allowing for quick decision-making and adjustments to travel plans.",
                 html.Br(),
                 f"3. Contextual information: GPS data can provide contextual information about a tourist's surroundings, such as weather conditions, traffic patterns, and nearby attractions, which can help identify factors that influence travel decisions.",
                 html.Br(),
                 f"4. Personalization: GPS data can be used to personalize travel recommendations and experiences, by understanding the individual preferences and behavior of tourists.",
                 html.Br(),
                 f"5. Cost-effective: GPS data can be collected using low-cost devices and does not require significant investment in infrastructure or personnel, making it an affordable option for tourist trip analysis.",
                 html.Br(),
                 ],
                className="card-text",
            ),
            html.H5("Cons:", className="card-titleCon1"),
            html.P(
                [f"1. Privacy concerns: GPS data can raise privacy concerns, as it involves tracking the movement of individuals. This may require additional safeguards and regulations to protect user privacy.",
                 html.Br(),
                 f"2. Limited data points: GPS data provides limited data points, which may not provide a complete picture of tourist behavior or travel patterns.",
                 html.Br(),
                 f"3. Device dependency: GPS data is dependent on the use of GPS-enabled devices, which may not be used by all tourists. This can limit the availability of data for analysis.",
                 html.Br(),
                 f"4. Accuracy limitations: GPS data may be less accurate in areas with poor satellite coverage or interference, which can limit its usefulness in certain contexts.",
                 html.Br(),
                 f"5. Bias: GPS data may be biased towards certain tourist groups or behaviors, such as those who are more likely to use GPS-enabled devices or travel to areas with good satellite coverage. This may skew the analysis of tourist behavior and travel patterns.",
                 html.Br(),],
                className="card-text",
            ),
        ]
    ),
]

card_ProCon = dbc.Row(
    [
        dbc.Col(card_content_ProCon, width=12),
    ]
)

layout = html.Div(
    [
        dbc.Row([
            dbc.Col(
                [
                    html.H1('Practical Work 2',
                        style={'textAlign': 'center', 'color': 'black'}),
                ], width=12
            )
        ]),
        dbc.Row([
            dbc.Col(
                [
                    html.Hr(),
                    html.Div([
                        dcc.Markdown('Thematic map with overnight accommodation, places of interest and other locations.', style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
                        dcc.Markdown('Due to display problems of Iframes with multipage dash apps, the html map created with Folium can be accessed via the following link:', style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
                        html.A("Link to interactive Folium map", href='https://leonieen.github.io/gps_thematic.html', target="_blank", style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
                    ]),
                    html.Hr(),
                    dcc.Dropdown(df_mileage["day"].unique(),
                         id='day_dropdown',
                         value='2018-04-21',
                         style={'padding-left': '80px', 'padding-right': '20px'},# "display": "inline", 'color': 'black'},
                         searchable=True, ),
                    dbc.Spinner(children=[dcc.Graph(id='gps_map', config={'displayModeBar': False, 'scrollZoom': True},
                                                    style={'background': '#ffffff', 'padding-bottom': '2px',
                                                           'padding-left': '2px',
                                                           'height': '100vh', 'width': '150vh'}
                                                    )], size="lg", color="primary", type="border", fullscreen=False, ),
                    html.Div([
                        dcc.Graph(figure=fig_table)
                    ]),
                    dbc.Col(dbc.Card(card_length, color="primary", outline=True),
                                            style={'padding-left': '80px', 'padding-right': '20px',}),
                    html.Hr(),
                    dbc.Spinner(children=[dcc.Graph(id='plot3d', config={'displayModeBar': False, 'scrollZoom': True},
                                                    style={'background': '#ffffff', 'padding-bottom': '2px',
                                                           'padding-left': '2px',
                                                           'height': '100vh', 'width': '150vh'}
                                                    )], size="lg", color="primary", type="border", fullscreen=False, ),

                    html.Div([
                        dcc.Graph(figure=fig_min_max)
                    ]),
                    dbc.Col(dbc.Card(card_height, color="primary", outline=True),
                                            style={'padding-left': '80px', 'padding-right': '20px',}),
                    html.Hr(),
                    html.Div([
                        dcc.Graph(figure=fig_month)
                    ]),
                    html.Div([
                        dcc.Graph(figure=fig_hour)
                    ]),
                    dbc.Col(dbc.Card(card_time, color="primary", outline=True),
                                            style={'padding-left': '80px', 'padding-right': '20px',}),
                    html.Hr(),
                    dbc.Col(dbc.Card(card_ProCon, color="primary", outline=True),
                                            style={'padding-left': '80px', 'padding-right': '20px',}),
                ], width=12
            )
        ])
    ]
)


#Map1
@callback(
    Output('gps_map', 'figure'),
    Input('day_dropdown', 'value')
)
def update_graph(day_value):
    day = day_value
    df_day = df_month_hour[df_month_hour['date'] == day]
    fig = px.scatter_mapbox(df_day, lat="Y", lon="X", color='altitude',
                            color_continuous_scale=["black", "purple", "red"], size_max=30, zoom=6,
                            height=600, width=1000,  # center = dict(lat = g.center)
                            title='Drive Route with Mapbox',
                            mapbox_style="open-street-map",
                            #hover_name="time",
                            )
    fig.update_layout(font_size=16, title={'xanchor': 'center', 'yanchor': 'top', 'y': 0.9, 'x': 0.5, },
                      title_font_size=24, mapbox_accesstoken=api_token,),
                      #mapbox_style="mapbox://styles/strym/ckhd00st61aum19noz9h8y8kw")
    fig.update_traces(marker=dict(size=6))
    return fig

#3D Scatter
@callback(
    Output('plot3d', 'figure'),
    Input('day_dropdown', 'value')
)
def update_graph(value):
    pts = []  # list of points defining boundaries of polygons
    for feature in jdata['features']:
        if feature['geometry']['type'] == 'Polygon':
            pts.extend(feature['geometry']['coordinates'][0])
            pts.append([None, None])  # mark the end of a polygon

        elif feature['geometry']['type'] == 'MultiPolygon':
            for polyg in feature['geometry']['coordinates']:
                pts.extend(polyg[0])
                pts.append([None, None])  # end of polygon
        elif feature['geometry']['type'] == 'LineString':
            pts.extend(feature['geometry']['coordinates'])
            pts.append([None, None])
        else:
            pass
        # else: raise ValueError("geometry type irrelevant for map")
    x, y = zip(*pts)
    x_plot = tuple(list(gps_df["X"]))
    y_plot = tuple(list(gps_df["Y"]))
    z_plot = tuple(list(gps_df["altitude"]))
    h = 884
    z = h * np.ones(len(x))
    fig = go.Figure()
    fig.add_scatter3d(x=x, y=y, z=z, mode='lines', line_color='#999999', line_width=1.5)
    fig.add_scatter3d(x=x_plot, y=y_plot, z=z_plot, mode='lines', line=dict(color=z_plot, colorscale='Plasma', width=4))  # , line_color=z_plot, color='altitude')
    fig.add_scatter3d(x=[-118.178923], y=[37.385376], z=[3067], mode='markers', marker=dict(color='yellow'), hovertemplate='Highest Point Methuselah (Tree), White Mountains, Inyo, 3067m above NN')
    fig.add_scatter3d(x=[-121.901373], y=[36.614741], z=[-105], mode='markers', marker=dict(color='darkblue'), hovertemplate='Lowest Point in Monterey, -105m under NN')
    fig.update_layout(width=800, height=800, title='Altitude of the Route')
    return fig