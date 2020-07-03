import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import time

import base64
import cv2
import datetime
import json
import pandas as pd
import numpy as np

from dash.dependencies import Input, Output, State

from utils import *
from app import app


def patient_item(app, name, dob, age, gender, current_assessment, assessments_2breviewed, review_duedate, icon, pid):
    return html.Div(
            [
                dbc.Button(
                    html.Div(
                        [
                            html.Div(
                                html.Img(src=app.get_asset_url("profile_default"+str(icon)+".png"), style={"height":"2.5rem", "padding-top":"0px"}),
                                style={"width":"4rem"}
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        html.Div(
                                            html.H1(name, style={"font-size":"1rem"}),
                                            style={"text-align":"start","padding-left":"0.5rem"}
                                        ),
                                        width=2
                                    ),
                                    dbc.Col(
                                        html.Div(
                                            html.H6(dob, style={"font-size":"1rem"})
                                        ),
                                        width=2
                                    ),
                                    dbc.Col(
                                        html.Div(
                                            html.H6(str(age), style={"font-size":"1rem"})
                                        ),
                                        width=1
                                    ),
                                    dbc.Col(
                                        html.Div(
                                            html.H6(gender, style={"font-size":"1rem"})
                                        ),
                                        width=1
                                    ),
                                    dbc.Col(
                                        html.Div(
                                            html.H6(str(current_assessment), style={"font-size":"1rem"})
                                        ),
                                        width=2
                                    ),
                                    dbc.Col(
                                        html.Div(
                                            html.H1(str(assessments_2breviewed), style={"font-size":"1rem","color":"#fff","background-color":"#dc3545","border-radius":"10rem","width":"1.6rem","padding":"0.2rem","margin-left":"3rem","margin-top":"-0.2rem"}),
                                            style={"text-align":"center"}
                                        ),
                                        width=2
                                    ),
                                    dbc.Col(
                                        html.Div(
                                            html.H6(review_duedate, style={"font-size":"1rem"})
                                        ),
                                        width=2
                                    ),
                                ],
                                style={"width":"80rem","margin-top":"0.5rem"}
                            )
                        ],
                        style={"display":"flex"}
                    ),
                    color="light",
                    outline=True,
                    id={"type": "physician-open-patient", 'index': pid},
                    style={"box-shadow":"0 4px 8px 0 rgba(0, 0, 0, 0.05), 0 6px 20px 0 rgba(0, 0, 0, 0.05)","padding-left":"1rem","padding-right":"2rem", "border-radius":"10rem","text-align":"center","padding-top":"1rem","padding-bottom":"1rem","width":"100%"}
                ),
                dbc.Modal(
                        [
                            dbc.ModalHeader(
                                html.Div(
                                    [
                                        html.H2(str(pid), style={"font-size":"2rem", "color":"#1357DD"})
                                    ],
                                    style={"color":"#1357DD"}
                                )
                            ),
                            dbc.ModalBody(
                                
                            ),
                            dbc.ModalFooter(
                                dbc.Button(
                                    "CLOSE", id={"type": "physician-close-patient", 'index': pid}, className="ml-auto",
                                    style={"margin-right":"20px", "background-color":"#38160f", "border":"none", "border-radius":"10rem", "font-family":"NotoSans-Black", "font-size":"1rem"}
                                )
                            ),
                        ],
                        id={"type": "physician-modal-patient", 'index': pid},
                        size='xl',
                        scrollable=False,
                        backdrop = 'static',
                    ),
            ],
            style={"padding-left":"5rem","padding-right":"7rem","padding-top":"0.5rem"}
        )



if __name__ == "__main__":
    app.run_server(host="127.0.0.1",debug=True,port=8052)