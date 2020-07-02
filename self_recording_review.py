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


def modal_self_recording_review(app):
    return html.Div(
        [
        dbc.Button(children = [html.Img(src=app.get_asset_url("icon-laptop-play-video-100.png"), style={"height":"2.5rem", "padding-top":"10px"})], outline = True, id = 'video-modal-review-button-open'),
        dbc.Modal(
            [
            dbc.ModalHeader(id="video-modal-review-header"),
            dbc.ModalBody(id = "video-modal-review-body"),
            dbc.ModalFooter(
                dbc.Button("close", id="video-modal-review-button-submit", className="mr-2"),
                )],
            id = "modal-selfrecording-review",
            size = 'xl',
            backdrop = "static"
            )]
        )