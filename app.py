import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


with open('nasalogo.txt', 'r') as myfile: #read the long web address of nasa space apps logo
    nasasrc=myfile.read().replace('\n', '')

temperature_data = {
    'Fire Ants': {'x': ["Temp","Temp","Temp"], 'y': [0, 30, 40]},
    'Species B': {'x': ["Temp","Temp","Temp"], 'y': [0, 40, 50]},
    'Species C': {'x': ["Temp","Temp","Temp"], 'y': [0, 20, 70]}
}
rainfall_data = {
    'Fire Ants': {'x': ["Rain","Rain","Rain"], 'y': [0, 10, 20]},
    'Species B': {'x': ["Rain","Rain","Rain"], 'y': [0, 40, 50]},
    'Species C': {'x': ["Rain","Rain","Rain"], 'y': [0, 20, 70]}
}

external_stylesheets = ['https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css']
mapbox_access_token="pk.eyJ1IjoidXRwYWxrdW1hciIsImEiOiJjam1sczJueW4wYmtjM3ZwZGlnZTE0YXE0In0.rhFz5Uwk4kaTly1iaEyLkg"
app = dash.Dash(external_stylesheets=external_stylesheets)
app.title='FerryMan' #add the app name in the tab
server = app.server

app.layout = html.Div(
html.Div([
    html.Div([
            html.H1(children='FerryMan', #app title at the beginning
                    className = "five columns"),
            html.Img(
                src="http://www.earth.sinica.edu.tw/images/IES-logo-original.jpg", #logo for the webpage
                className='three columns',
                style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'right',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                },
            ),
            html.Img(
                src=nasasrc, #logo for the webpage
                className='three columns',
                style={
                    'height': '10%',
                    'width': '10%',
                    'float': 'right',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                },
            ),
            html.Div(children='''
                        This webpage logs the information about the pests.
                        ''', #some information about the project
                    className = 'nine columns')
        ], className = "row"),
    html.Div([
    html.H4('Select the Species', #request to select
    className = "four columns")], className="row"),
    html.Div([
    dcc.Dropdown( #dropdown menu to select the species
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['Fire Ants', 'Species B', 'Species C']],
        value='Fire Ants',className = 'four columns'
    )], className="row"),
    html.Div([html.Div(id='display-value')], className="row"),
    html.Div(html.H3(children='''
    Necessary environment for survival
    ''',className = 'four columns'), className="row"), #parameters range
    html.Div([dcc.Graph(
        id='example-graph',className = 'four columns'
    )], className="row")
], className='ten columns offset-by-one')
)

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return "You have selected {}".format(value)

@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')])
def update_image_src(selector):

    data=[ #data for the plot
                {'x':temperature_data[selector]['x'],'y':temperature_data[selector]['y'],'type':'box','name':'Temperature'},
                {'x':rainfall_data[selector]['x'],'y':rainfall_data[selector]['y'],'type':'box','name':'Avg Rainfall'},
            ]
    print (selector)
    figure = {
        'data': data,
        'layout': {
            'xaxis' : dict(
                title='Parameters',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='Values',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)