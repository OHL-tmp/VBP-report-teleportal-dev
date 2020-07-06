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
                                            [
                                                html.H1(str(assessments_2breviewed), style={"font-size":"1rem","color":"#fff","background-color":"#dc3545","border-radius":"10rem","width":"1.6rem","padding":"0.2rem","margin-left":"3rem","margin-top":"-0.2rem"})
                                            if assessments_2breviewed > 0
                                            else
                                                html.H1("--", style={"font-size":"1rem","color":"#000","background-color":"#fff","border-radius":"10rem","width":"1.6rem","padding":"0.2rem","margin-left":"3rem","margin-top":"-0.2rem"}),
                                            ],
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
                            
                            dbc.ModalBody(
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.Img(src=app.get_asset_url("profile_default"+str(icon)+".png"), style={"height":"80px", "padding":"10px","margin-top":"30px"}),
                                                        html.Div(
                                                            [
                                                                html.H2(name, style={"font-size":"1.6rem", "color":"#000", "padding-bottom":"32px", "padding-top":"16px"}),
                                                                html.H6("DATE OF BIRTH", style={"font-size":"0.6rem"}),
                                                                html.Div(dbc.Badge(str(dob), pill=True, style={"background":"#857698"}), style={"margin-top":"-10px", "padding-bottom":"16px"}),
                                                                html.H6("AGE", style={"font-size":"0.6rem"}),
                                                                html.Div(dbc.Badge(str(age), pill=True, style={"background":"#857698"}), style={"margin-top":"-10px", "padding-bottom":"16px"}),
                                                                html.H6("GENDER", style={"font-size":"0.6rem"}),
                                                                html.Div(dbc.Badge(str(gender), pill=True, style={"background":"#857698"}), style={"margin-top":"-10px", "padding-bottom":"16px"}),
                                                            ]
                                                        )
                                                    ],
                                                    style={"padding":"20px","text-align":"center"}
                                                ),
                                            ],
                                            style={"width":"260px", "border-radius":"1rem","background":"#f5f5f5","margin-top":"60px","margin-left":"20px"}
                                        ),
                                        html.Div(
                                            [
                                                physician_assessment_item("07/03/2020", pid, itemid = 1)   
                                            ],
                                            style={"padding-left":"20px","margin-top":"60px"}
                                        ),
                                    ],
                                    style={"display":"flex", "padding-bottom":"60px"}
                                )
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

def physician_assessment_item(completion_date, pid, itemid):
    cd = datetime.datetime.strptime(completion_date, '%m/%d/%Y')
    rd = cd + datetime.timedelta(days = 7)
    rd = str(datetime.datetime.strftime(rd, '%m/%d/%Y'))
    return html.Div(
            [
                html.Div([
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H1("Berg Balance Scale", style={"font-size":"1.5rem"}),
                                    html.Div(
                                        [
                                            dbc.Badge("Functional Assessment", color="info", style={"font-family":"NotoSans-Light","font-size":"0.8rem",}),
                                            html.H6("Dr.Smith", style={"padding-left":"0.5rem","padding-right":"0.5rem"}),
                                            html.H6(" | "),
                                            html.H6("self-recording", style={"padding-left":"0.5rem","padding-right":"0.5rem"}),
                                        ],
                                        style={"display":"flex","font-size":"0.8rem"}
                                    ),
                                ],
                                style={"width":"26rem","padding-left":"10px"}
                            ),
                            html.Div(
                                [
                                    html.H6("Patient Completion Date", style={"font-size":"0.6rem","height":"1.5rem"}),
                                    html.H1(completion_date, style={"font-size":"1.2rem","text-align":"center"}, 
#                                        id = u'patient-assessment-completdate-{}'.format(num)
                                        )
                                ],
                                style={"border-left":"1px solid #d0d0d0","padding-left":"1rem","padding-right":"1rem"}
                            ),
                            html.Div(
                                [
                                    html.H6("Review Due Date", style={"font-size":"0.6rem","height":"1.5rem"}),
                                    html.H1(rd, style={"font-size":"1.2rem","color":"#dc3545"}, 
#                                        id = u'patient-assessment-status-{}'.format(num)
                                        )
                                ],
                                style={"border-left":"1px solid #d0d0d0","padding-left":"1rem","padding-right":"1rem"}, 
                            ),
                            html.Div(
                                [  
                                    dbc.Button("Start Review", id = {"type": "physician-assessment-open-item", 'index': str(pid)+str(itemid)}, outline=True, color="dark", style={"border-radius":"0.8rem","font-size":"0.8rem","font-family":"NotoSans-Regular"}),
                                ],
                                style={"border-left":"1px solid #d0d0d0","padding-left":"1rem","padding-right":"1rem"}
                            ),
                        ],
                        style={"display":"flex","padding-top":"1rem","padding-bottom":"1rem","justify-content":"space-around"}
                    ),
                    html.Div([
                        dbc.Collapse(str(pid)+str(itemid), id = {"type": "physician-assessment-collapse", 'index': str(pid)+str(itemid)})
                        ]
                    ),],
                    style={"box-shadow":"0 4px 8px 0 rgba(0, 0, 0, 0.05), 0 6px 20px 0 rgba(0, 0, 0, 0.05)","padding-left":"0.5rem","padding-right":"1rem", "border-radius":"0.8rem"}
                )
            ],
            style={"padding":"0.5rem"}
        )



if __name__ == "__main__":
    app.run_server(host="127.0.0.1",debug=True,port=8052)