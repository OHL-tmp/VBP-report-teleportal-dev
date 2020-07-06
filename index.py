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

import physician_portal
import login_physician


app = dash.Dash(__name__, url_base_pathname='/login/')

server = app.server

username = "demo"
password = "demo2020"


app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/physician/":
        return physician_portal.layout
    
    else:
        return login_physician.layout




if __name__ == "__main__":
    app.run_server(host="127.0.0.1",debug=True,port=8052)