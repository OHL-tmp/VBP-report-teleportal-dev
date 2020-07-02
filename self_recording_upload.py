import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table

import pandas as pd
import numpy as np

import pathlib
import plotly.graph_objects as go

from plotly.subplots import make_subplots
from dash.dependencies import Input, Output, State

from utils import *
from app import app


def modal_self_recording(app):
    return html.Div(
        [
        dbc.Button(children = [html.Img(src=app.get_asset_url("icon-upload-to-the-cloud-100.png"), style={"height":"2.5rem", "padding-top":"10px"})], outline = True, id = 'video-modal-upload-button-open'),
        dbc.Modal(
            [
            dbc.ModalHeader("???"),
            dbc.ModalBody(video_modal_upload_body()),
            dbc.ModalFooter(
                dbc.Button("Submit", id="video-modal-upload-button-submit", className="mr-2"),
                )],
            id = "modal-selfrecording-upload",
            size = 'xl',
            backdrop = "static"
            )]
        )

def video_modal_upload_body():
    return html.Div([
            dcc.Upload(
                id = 'video-modal-upload-upload',
                children = html.Div([
                    'Select Related Files to Upload'
                    ],style={"font-family":"NotoSans-Regular","font-size":"0.8rem","text-decoration":"underline","color":"#1357DD"}),
                style={
                    'height': '40px',
                    'lineHeight': '40px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center'
                    },
                accept = "video/*"
                ),
            html.Div(id = "video-modal-upload-output")
        ])