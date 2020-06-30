import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import time

import datetime
import json
import pandas as pd
import numpy as np

from dash.dependencies import Input, Output, State

from utils import *
from app import app

app = dash.Dash(__name__, url_base_pathname='/login/')

server = app.server


def create_layout(app):
	
	return html.Div(
                [
                    html.Div(
                    	[
                        	html.H1("ValueGen Solution"),
                        	dbc.Card(
                        		dbc.CardBody(
                        			[	
                        				html.Div(
                        					dbc.Input(placeholder="Username", type="text", style={"border-radius":"10rem"}),
                        					style={"padding":"0.5rem"}
                        				),
                        				html.Div(
                        					dbc.Input(placeholder="Password", style={"border-radius":"10rem"}),
                        					style={"padding":"0.5rem"}
                        				),
                        				dbc.Row(
                        					[
                        						dbc.Col(
                        							html.Div(),
                        						),
                        						dbc.Col(
                        							[
                        								dbc.Button(
										                    "Log In",
										                    # id = 'manager-button-openmodal-pmpm',
										                    className="mb-3",
										                    style={"background-color":"#38160f", "border":"none", "border-radius":"10rem", "font-family":"NotoSans-Regular", "font-size":"1rem","width":"6rem"},
										                ),
                        							],
                        							width=3
                        						)
                        					],
                        					style={"padding-top":"3rem", "padding-right":"1rem"}
                        				)
                        			]
                        		),
				                className="mb-3",
				                style={"box-shadow":"0 4px 8px 0 rgba(0, 0, 0, 0.05), 0 6px 20px 0 rgba(0, 0, 0, 0.05)", "border":"none", "border-radius":"1rem"}
                        	)
                    	],
                    style={"background-color":"transparent", "border":"none", "width":"500px", "margin":"auto", "padding-top":"25vh"}
                    ),
                ],
                # style={"margin-top":"-30rem","background-color":"transparent","text-align":"center"}
            )


app.layout = create_layout(app)

if __name__ == "__main__":
    app.run_server(host="127.0.0.1",debug=True,port=8052)