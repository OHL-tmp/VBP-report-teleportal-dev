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


username = "demo"
password = "demo2020"
# app = dash.Dash(__name__, url_base_pathname='/physician/')
# server = app.server

def login_layout(app):
    return html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                html.Img(src=app.get_asset_url("coeus.png"),style={"height":"4rem"}),
                                style={"text-align":"center","padding":"4rem"}
                            ),
                            html.Div(
                                html.H2("Physician",style={"font-size":"1.6rem","padding-left":"20px"}),
                                style={"text-align":"start"}
                            ),
                            html.Div(id = 'store-location'),
                            dbc.Card(
                                dbc.CardBody(
                                    [   
                                        html.Div(style={"padding-top":"20px"}),
                                        dbc.Collapse(children = ["\u2757", "Please check your username and password."],
                                            id = 'login-collapse-check',
                                            is_open = False,
                                            style={"text-align":"center"}
                                            ),
                                        html.Div(
                                            [
                                                html.Form(
                                                    [
                                                        html.Div(
                                                            dbc.Input(placeholder="Username", type="text", style={"border-radius":"10rem"}, id = "login-input-username"),
                                                            style={"padding":"0.5rem"}
                                                        ),
                                                        html.Div(
                                                            dbc.Input(placeholder="Password", style={"border-radius":"10rem"}, type = 'password', id = "login-input-password"),
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
                                                                            id = "login-button-submit"
                                                                        ),
                                                                    ],
                                                                    width=3
                                                                ),
                                                                dbc.Col(
                                                                    html.Div(),
                                                                ),
                                                            ],
                                                            style={"padding-top":"2rem", "padding-right":"1rem"}
                                                        )
                                                    ], 
                                                    action='/login', 
                                                    method='post'
                                                )
                                            ]
                                        )
                                    ],
                                    style={"padding-left":"2rem","padding-right":"2rem"}
                                ),
                                className="mb-3",
                                style={"box-shadow":"0 4px 8px 0 rgba(0, 0, 0, 0.1), 0 6px 20px 0 rgba(0, 0, 0, 0.1)", "border":"none", "border-radius":"1rem"}
                            )
                        ],
                        style={"background-color":"transparent", "border":"none", "width":"500px", "margin":"auto", "padding-top":"5vh"}
                    ),
                ],
                style={"background":"url(./assets/physician-login.png)","height":"100vh"},
                id="login-layout"
            )


def physician_layout(app):
	
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
                ],
                id="physician-layout"
            )



def header(app):
    search_bar = dbc.Row(
        [
            dbc.Col(
                dbc.Button(
                    "Log Out", 
                    outline=True, 
                    color="dark", 
                    style={"border-radius":"10rem", "width":"6rem","height":"2rem","font-size":"0.7rem"},
                    id = "logout-button"
                ),
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





app.layout = html.Div(
        [
            
            login_layout(app),
            
            dbc.Fade(
                physician_layout(app),
                id="fade-transition",
                is_in=True,
                style={"transition": "opacity 100ms ease"},
            ),
        ]
    )


@app.callback(
    [
        Output("login-collapse-check", "is_open"),
        Output("login-layout", "hidden"),
        Output("physician-layout", "hidden"),
    ],
    [
        Input("login-button-submit", "n_clicks"),
        Input("logout-button", "n_clicks")
    ],
    [
        State("login-input-username", "value"),
        State("login-input-password", "value")
    ]
    )
def login_check(nin, nout, un, pw):
    ctx = dash.callback_context
    if ctx.triggered[0]['prop_id'].split('.')[0] == 'login-button-submit':
        if un == username and pw == password:
            return False, True, False
        else: 
            return True, False, True
    elif ctx.triggered[0]['prop_id'].split('.')[0] == 'logout-button':
        return False, False, True
    else:
        return False, False, True


# @app.callback(
#     [
#         Output("login-layout", "hidden"),
#         Output("physician-layout", "hidden"),
#     ],
#     [
#         Input("logout-button", "n_clicks")
#     ]
#     )
# def login_check(n, un, pw):
#     if n:
#         return True, False



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
    infos = [["Kevin Scott","3/1/1952",68,"M",2,2,"8/15/2020",3, 0],["Rhianna Kenny","9/19/1994",25,"F",0,0,"8/15/2020",1, 1],["Mary Kim","5/12/1988",32,"F",0,0,"8/15/2020",2, 2],]

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

            html.Div(patient_item(app, *patient)) for patient in infos
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
    Output({'type':'physician-modal-patient-modalbody', 'index':MATCH}, "children"),
    [Input({'type':'physician-modal-select-sorting', 'index':MATCH}, "value")],
    [State({'type':'physician-modal-select-sorting', 'index':MATCH}, "id")]
    )
def update_review_assessment(v, id):
    patient_assessment_detail = [ ["Functional Assessment","Berg Balance Scale","Self Recording",str(datetime.datetime.now().date().strftime('%m/%d/%Y')),"Start Review", 0, 0],["Functional Assessment","Berg Balance Scale","Self Recording","04/01/2020","50", 0, 1],["Functional Assessment","Berg Balance Scale","Self Recording","01/01/2020","45", 0, 2],["Patient Health Status","KCCQ-12","Questionnaire",str(datetime.datetime.now().date().strftime('%m/%d/%Y')),"Start Review", 0, 3],["Patient Health Status","KCCQ-12","Questionnaire","04/15/2020","75", 0, 4],["Patient Health Status","KCCQ-12","Questionnaire","01/15/2020","69", 0, 5] ]

    patient_assessment_detail_filtered = [item for item in patient_assessment_detail if item[5] == id['index']]
    if v:
        patient_assessment_detail_filtered = sorted(patient_assessment_detail_filtered, key = lambda x: x[int(v)], reverse = True)

    patient_assessment_list = [
      physician_assessment_item(*assessment) for assessment in patient_assessment_detail_filtered
    ]

    return patient_assessment_list

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