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

from dash.dependencies import Input, Output, State, MATCH, ALL

from utils import *
from app import app

from kccq_questionnaire import *
from kccq_questionnaire_answer import *

from patient_page import *

# app = dash.Dash(__name__, url_base_pathname='/physician/')
# server = app.server

def create_layout(app):
	
	return html.Div(
                [
                    header(app),
                    html.Div(style={"height":"0rem"}),
                    html.Div(
                        [
                            card_mainlist(app)
                        ],
                        style={"padding-top":"1rem","background-color":"#fff"}
                    )
                ]
            )



def header(app):
    search_bar = dbc.Row(
        [
            dbc.Col(
                dbc.Button("Log Out", outline=True, color="dark", style={"border-radius":"10rem", "width":"6rem","height":"2rem","font-size":"0.7rem"}),
                width="auto",
            ),
        ],
        no_gutters=True,
        className="ml-auto flex-nowrap mt-3 mt-md-0",
        align="center",
    )

    header = dbc.Navbar(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=app.get_asset_url("profile_default4.png"), style={"height":"2.5rem", "padding-top":"0px"}), style={"padding-right":"2rem"}, width="auto"),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H1("Dr. Smith", style={"font-size":"1rem", "line-height":"0.6"}),
                                        html.H6("NPI : CAR2398019880502", style={"font-size":"0.8rem"}),
                                    ],
                                    style={"padding-top":"0.5rem"}
                                ), width="auto"),
                            dbc.Col(width=3),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H1("Area of Specialty", style={"font-size":"0.8rem", "line-height":"0.6"}),
                                        html.H6("Cardiology", style={"font-size":"0.8rem"}),
                                    ],
                                    style={"padding-top":"0.5rem"}
                                ), width="auto"),
                            dbc.Col(width=1),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H1("Orignization", style={"font-size":"0.8rem", "line-height":"0.6"}),
                                        html.H6("XXX Physician Group", style={"font-size":"0.8rem"}),
                                    ],
                                    style={"padding-top":"0.5rem"}
                                ), width="auto"),
                        ],
                        align="center",
                        no_gutters=True,
                        style={"width":"50rem"}
                    ),
                ),
                dbc.NavbarToggler(id="navbar-toggler"),
                dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
            ],
            color="#fff",
            sticky = "top",
            expand = True,
            className="sticky-top",
            style={"box-shadow":"0 4px 8px 0 rgba(0, 0, 0, 0.05), 0 6px 20px 0 rgba(0, 0, 0, 0.05)","padding-left":"8rem","padding-right":"8rem","padding-top":"1rem","padding-bottom":"1rem"}
#            dark=True,
        )
    return header
    

def card_mainlist(app):

    card = dbc.Card(
        [
            html.Div(id = 'physician-patient-tempdata', style = {"display":"none"}),
            status(),
            list_header(),

            dbc.CardBody(
                [
                    html.Div(id="physician-patient-list"),
                ],
                id = 'physician-card-patient',
                style={"overflow-y":"scroll"}
            ),       
        ],
        style={"height":"120vh", "margin-top":"-2rem"}
    )

    return card

def list_header():
    return html.Div(
            [

                dbc.Row(
                    [
                        dbc.Col(html.H1("Patient List", style={"font-size":"2rem","color":"#000"})),
                        dbc.Col(),
                        dbc.Col(
                            [
                                # dbc.Badge("Sort By", pill=True, color="primary", className="mr-1"),
                                html.H1("Sort By", style={"width":"6rem","margin-top":"0.5rem","font-size":"0.8rem","padding-left":"1rem"}),
                                dbc.Select(
                                    id = 'physician-select-sorting',
                                    options = [
                                        {"label":"Patient Name", "value":0},
                                        {"label":"Assessments to be Reviewed", "value":5},
                                    ],
                                    value = 5,
                                    bs_size = 'sm',
                                    style={"border-radius":"10rem","font-family":"NotoSans-Regular","font-size":"0.8rem"}
                                )
                            ],
                            # style={"display":"flex"}
                        ),
                    ],
                    style={"text-align":"start","padding-bottom":"50px"},
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                html.H4("Patient Name", style={"font-size":"0.7rem","color":"#919191"})
                            ),
                            width=2
                        ),
                        dbc.Col(
                            html.Div(
                                html.H4("DOB", style={"font-size":"0.7rem","color":"#919191"})
                            ),
                            width=2
                        ),
                        dbc.Col(
                            html.Div(
                                html.H4("Age", style={"font-size":"0.7rem","color":"#919191"})
                            ),
                            width=1
                        ),
                        dbc.Col(
                            html.Div(
                                html.H4("Gender", style={"font-size":"0.7rem","color":"#919191"})
                            ),
                            width=1
                        ),
                        dbc.Col(
                            html.Div(
                                html.H4("Current Assessment", style={"font-size":"0.7rem","color":"#919191"})
                            ),
                            width=2
                        ),
                        dbc.Col(
                            html.Div(
                                html.H4("Assessments to be Reviewed", style={"font-size":"0.7rem","color":"#919191"})
                            ),
                            width=2
                        ),
                        dbc.Col(
                            html.Div(
                                html.H4("Review Due Date", style={"font-size":"0.7rem","color":"#919191"})
                            ),
                            width=2
                        ),
                    ]
                ),
                html.Hr(style={"margin-top":"-0.1rem"}),
            ],
            style={"padding-left":"11rem","padding-right":"11rem","padding-top":"2rem","text-align":"center"}
        )


def status():
    return html.Div(
                html.Div(
                    [
                        html.Div(
                            html.H1("Overview", style={"font-size":"2rem","color":"#000"}),
                            style={"text-align":"start","padding-bottom":"0rem"},
                        ),
                        html.Div(
                            [
                                html.Div(
                                    html.Div(
                                        [
                                            html.H6("TOTAL PATIENT ASSIGNED", style={"color":"#fff","width":"7rem"}),
                                            dbc.Badge("", id = 'physician-badge-patientct',style={"font-family":"NotoSans-SemiBold","font-size":"1.2rem","border-radius":"10rem","width":"4.5rem","background":"#fff","color":"#1357dd"}),
                                        ],
                                        style={"border-radius":"0.8rem", "border":"1px solid #1357dd","background":"#1357dd","padding":"0.5rem","box-shadow":"0 4px 8px 0 rgba(19, 86, 221, 0.4), 0 6px 20px 0 rgba(19, 86, 221, 0.1)"}
                                    ),
                                    style={"padding":"1rem"}
                                ),
                                html.Div(
                                    html.Div(
                                        [
                                            html.H6("TOTAL ACTIVE TASKS", style={"color":"#fff","width":"7rem"}),
                                            dbc.Badge("", id = 'physician-badge-activetasks', style={"font-family":"NotoSans-SemiBold","font-size":"1.2rem","border-radius":"10rem","width":"4.5rem","background":"#fff","color":"#dc3545"}),
                                        ],
                                        style={"border-radius":"0.8rem", "border":"1px solid #dc3545","background":"#dc3545","padding":"0.5rem","box-shadow":"0 4px 8px 0 rgba(220, 53, 70, 0.4), 0 6px 20px 0 rgba(220, 53, 70, 0.1)"}
                                    ),
                                    style={"padding":"1rem"}
                                ),
                                
                            ], 
                            style={"display":"flex"}
                        ),
                    ],
                    style={"padding-top":"3rem", "padding-left":"11rem", "padding-bottom":"2rem", "background":"#f5f5f5"}
                )
                
            )

            

def list_patients():
    return html.Div(
            [
                patient_item(app),
                # tab_assessment_item2(app,1),
                # tab_assessment_item2(app,2),
                # tab_assessment_item2(app,3),
                # tab_assessment_item2(app,4),
                # tab_assessment_item2(app,5),
                # tab_assessment_item2(app,6),
                # tab_assessment_item2(app,7),
            ], 
            style={"width":"100%","padding-right":"6rem","padding-left":"2rem","overflow-y":"scroll"}
        )





layout = create_layout(app)

@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("physician-patient-tempdata","children"),
    [Input("physician-select-sorting","value"),]
    )
def refresh_patient_info(v):
    infos = [["Kevin Scott","3/1/1952",68,"M",2,2,"8/15/2020",3],
            ["Rhianna Kenny","9/19/1994",25,"F",4,0,"8/15/2020",1],
            ["Mary Kim","5/12/1988",32,"F",2,0,"8/15/2020",2],]
    if v:
        infos = sorted(infos, key = lambda x: x[int(v)], reverse = True)

    physician_patient_tempdata = dict(patient_info=infos)
    return json.dumps(physician_patient_tempdata)

@app.callback(
        [
            Output("physician-patient-list", "children"),
            Output('physician-badge-patientct', 'children'),
            Output('physician-badge-activetasks', 'children'),
        ],
        [
            Input("physician-patient-tempdata", 'children'),
        ]
    )
def update_patient_card(data):
    physician_patient_tempdata = json.loads(data)
    infos = physician_patient_tempdata['patient_info']
    patient_list = [
            html.Div(patient_item(app, *patient, pid=i)) for i, patient in enumerate(infos)
        ]
    return patient_list, len(infos), sum(int(patient[5]) for patient in infos)


@app.callback(
    Output({"type": "physician-modal-patient", 'index': MATCH}, "is_open"),
    [Input({"type": "physician-open-patient", 'index': MATCH}, "n_clicks"), Input({"type": "physician-close-patient", 'index': MATCH}, "n_clicks")],
    [State({"type": "physician-modal-patient", 'index': MATCH}, "is_open")],
)
def toggle_modal_patient_item(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output({"type": "physician-assessment-collapse", 'index': MATCH}, "is_open"),
    [Input({"type": "physician-assessment-open-item", 'index': MATCH}, "n_clicks")],
    [State({"type": "physician-assessment-collapse", 'index': MATCH}, "is_open")],
)
def toggle_modal_patient_item(n,  is_open):
    if n:
        return not is_open
    return is_open




if __name__ == "__main__":
    app.run_server(host="127.0.0.1",debug=True,port=8052)