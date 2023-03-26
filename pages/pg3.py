import dash
from dash import dcc, html

dash.register_page(__name__, name='Comments')

layout = html.Div(
    [
        html.H1('Comments on the handling of the tasks:', style={'textAlign': 'center', 'color': 'black'}),
        dcc.Markdown('Github link to data and the app:', style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
        html.A("Link to interactive Folium map", href='https://github.com/Leonieen/MLBS', target="_blank", style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
        html.Hr(),
        dcc.Markdown('Data preparation', style={'padding-left': '80px', 'padding-right': '20px', 'font-weight': 'bold'}),
        dcc.Markdown('The data for both tasks were read in using Python and prepared accordingly. Problems arose with the format of the data set for the second task.', style={'padding-left': '80px', 'padding-right': '20px'}),
        dcc.Markdown('When trying to read in the CSV file, some time data was not readable and had to be corrected manually. ', style={'padding-left': '80px', 'padding-right': '20px'}),
        dcc.Markdown('The column separation also had to be adapted for better readability for python, and commas had to be replaced by full stops. ', style={'padding-left': '80px', 'padding-right': '20px'}),
        dcc.Markdown('Later, it turned out that there were problems with the date format when reading in the data, as some of the dates were in the year-month-day format or all May values were in the year-day-month format, which had to be corrected and adjusted with corresponding queries and loops in Python. ', style={'padding-left': '80px', 'padding-right': '20px'}),
        dcc.Markdown('This inconsistency made it particularly difficult to adjust the time difference by 10 hours, but it was eventually corrected.', style={'padding-left': '80px', 'padding-right': '20px'}),
        dcc.Markdown('To improve the performance of the application, all possible data processing was carried out in JupyterNotebooks and then exported as CSV files, which are then read into the dashboard.', style={'padding-left': '80px', 'padding-right': '20px'}),
    ]
)