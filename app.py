import os
import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_trich_components as dtc
from chart import create_waterfall

# read data
x = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
y = [100, 400, -100, 230, -130, 160, 240, 248, 204, 743, 1121, 1366, -1228, -84]


app = Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
)
server = app.server

theme_toggle = dtc.ThemeToggle(
        bg_color_dark='#232323',
        # icon_color_dark='#EDC575',
        # bg_color_light='#07484E',
        icon_color_light='#C8DBDC',
        tooltip_text='Toggle light/dark theme'
    )
theme_switch = html.Div(theme_toggle, className='theme__switcher')
header = html.Div([
        html.H1('Waterfall Plot'),
        html.P('Waterfall description'),
], className='dash__header')

footer = html.Div([
    html.P('Created by:', style={}),

], className='dash__footer')

app.layout = html.Div([
                    header,
                    theme_switch,
                    html.Div([
                        html.Div([
                            html.Div('', className="table_name"),
                            dcc.Graph(figure=create_waterfall(x,y),
                                      config={"displayModeBar": False}),

                        ], style={'width':'100%'}),
                    ], className='dash__graph_block'),
                    footer

                ], className='dash__wrapper', style={})


# don't run when imported, only when standalone
if __name__ == '__main__':
    port = os.getenv("DASH_PORT", 8053)
    app.run_server(debug=True,  port=port)
