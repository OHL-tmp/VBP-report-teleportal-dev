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

from kccq_questionnaire import *
from kccq_questionnaire_answer import *

app = dash.Dash(__name__, url_base_pathname='/login/')

server = app.server


def create_layout(app):
	
	return html.Div(
                [
                    header(),
                    html.Div(style={"height":"0rem"}),
                    html.Div(
                        [
                            card_mainlist()
                        ],
                        style={"padding-top":"1rem","background-color":"#fff"}
                    )
                ]
            )



def header():
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


def card_mainlist():
    card = dbc.Card(
        [
            status(),
            list_header(),

            dbc.CardBody(
                [
                    patient_item(app, "Kevin Scott","3/1/1952",68,"M",2,2,"8/15/2020",3),
                    patient_item(app, "Mary Kim","5/12/1988",32,"F",2,1,"8/15/2020",2),
                    patient_item(app, "Rhianna Kenny","9/19/1994",26,"F",4,3,"8/15/2020",1),
                    patient_item(app, "Rhianna Kenny","9/19/1994",26,"F",4,3,"8/15/2020",1),
                    patient_item(app, "Rhianna Kenny","9/19/1994",26,"F",4,3,"8/15/2020",1),
                    patient_item(app, "Rhianna Kenny","9/19/1994",26,"F",4,3,"8/15/2020",1),
                    patient_item(app, "Rhianna Kenny","9/19/1994",26,"F",4,3,"8/15/2020",1),
                    patient_item(app, "Rhianna Kenny","9/19/1994",26,"F",4,3,"8/15/2020",1),
                    patient_item(app, "Rhianna Kenny","9/19/1994",26,"F",4,3,"8/15/2020",1),
                    patient_item(app, "Rhianna Kenny","9/19/1994",26,"F",4,3,"8/15/2020",1),
                    patient_item(app, "Rhianna Kenny","9/19/1994",26,"F",4,3,"8/15/2020",1),
                    patient_item(app, "Rhianna Kenny","9/19/1994",26,"F",4,3,"8/15/2020",1),
                    patient_item(app, "Rhianna Kenny","9/19/1994",26,"F",4,3,"8/15/2020",1),
                ],
                style={"overflow-y":"scroll"}
            ),       
        ],
        style={"height":"120vh", "margin-top":"-2rem"}
    )

    return card

def list_header():
    return html.Div(
            [

                html.Div(
                    html.H1("Patient List", style={"font-size":"2rem","color":"#000"}),
                    style={"text-align":"start","padding-bottom":"2rem"},
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
                html.Hr(),
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
                                            dbc.Badge("5", style={"font-family":"NotoSans-SemiBold","font-size":"1.2rem","border-radius":"10rem","width":"4.5rem","background":"#fff","color":"#1357dd"}),
                                        ],
                                        style={"border-radius":"0.8rem", "border":"1px solid #1357dd","background":"#1357dd","padding":"0.5rem","box-shadow":"0 4px 8px 0 rgba(19, 86, 221, 0.4), 0 6px 20px 0 rgba(19, 86, 221, 0.1)"}
                                    ),
                                    style={"padding":"1rem"}
                                ),
                                html.Div(
                                    html.Div(
                                        [
                                            html.H6("TOTAL ACTIVE TASKS", style={"color":"#fff","width":"7rem"}),
                                            dbc.Badge("2", style={"font-family":"NotoSans-SemiBold","font-size":"1.2rem","border-radius":"10rem","width":"4.5rem","background":"#fff","color":"#dc3545"}),
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
                tab_assessment_item2(app,1),
                # tab_assessment_item2(app,2),
                # tab_assessment_item2(app,3),
                # tab_assessment_item2(app,4),
                # tab_assessment_item2(app,5),
                # tab_assessment_item2(app,6),
                # tab_assessment_item2(app,7),
            ], 
            style={"width":"100%","padding-right":"6rem","padding-left":"2rem","overflow-y":"scroll"}
        )


def patient_item(app, name, dob, age, gender, current_assessment, assessments_2breviewed, review_duedate, icon):
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
                    style={"box-shadow":"0 4px 8px 0 rgba(0, 0, 0, 0.05), 0 6px 20px 0 rgba(0, 0, 0, 0.05)","padding-left":"1rem","padding-right":"2rem", "border-radius":"10rem","text-align":"center","padding-top":"1rem","padding-bottom":"1rem","width":"100%"}
                )
            ],
            style={"padding-left":"5rem","padding-right":"7rem","padding-top":"0.5rem"}
        )


def tab_assessment_item2(app, num):
    return html.Div(
            [
                html.Div(
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H1("KCCQ-12", style={"font-size":"1.5rem"}),
                                    html.Div(
                                        [
                                            dbc.Badge("Patient Health Status", color="success", style={"font-family":"NotoSans-Light","font-size":"0.8rem"}),
                                            html.H6("Dr.Smith", style={"padding-left":"0.5rem","padding-right":"0.5rem"}),
                                            html.H6(" | "),
#                                            html.H6("7/1/2020", style={"padding-left":"0.5rem","padding-right":"0.5rem"}),
#                                            html.H6(" | "),
                                            html.H6("questionnaire", style={"padding-left":"0.5rem","padding-right":"0.5rem"}),
                                        ],
                                        style={"display":"flex","font-size":"0.8rem"}
                                    ),
                                ],
                                style={"width":"26rem"}
                            ),
                            html.Div(
                                [
                                    html.H6("Due Date", style={"font-size":"0.7rem"}),
                                    html.H1("07/31/2020", style={"font-size":"1.2rem"})
                                ],
                                style={"border-left":"1px solid #d0d0d0","padding-left":"1.6rem"}
                            ),
                            html.Div(
                                [
                                    html.H6("Status", style={"font-size":"0.7rem"}),
                                    html.H1("Not Started", style={"font-size":"1.2rem"}, id = u'patient-questionnaire-status-{}'.format(num))
                                ],
                                style={"border-left":"1px solid #d0d0d0","padding-left":"1.6rem"}
                            ),
                            html.Div(
                                [
                                    html.H6("Completion Date", style={"font-size":"0.7rem"}),
                                    html.H1("", style={"font-size":"1.2rem"}, id = u'patient-questionnaire-completdate-{}'.format(num))
                                ],
                                style={"border-left":"1px solid #d0d0d0","padding-left":"1.6rem"}
                            ),
                            html.Div(
                                [

                                    html.Div(modal_kccq_questionaire(app), id = u'patient-questionnaire-todo-{}'.format(num), hidden = False),
                                   
                                    html.Div(modal_kccq_questionaire_answer(app), id = u'patient-questionnaire-done-{}'.format(num), hidden = True)
                                ],
                                style={"border-left":"1px solid #d0d0d0","padding-left":"1.6rem"}

                            ),
                        ],
                        style={"display":"flex","padding-top":"1rem","padding-bottom":"1rem","justify-content":"space-around"}
                    ),
                    style={"box-shadow":"0 4px 8px 0 rgba(0, 0, 0, 0.05), 0 6px 20px 0 rgba(0, 0, 0, 0.05)","padding-left":"0.5rem","padding-right":"1rem", "border-radius":"0.8rem"}
                )
            ],
            style={"padding":"0.5rem"}
        )


app.layout = create_layout(app)

@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open







if __name__ == "__main__":
    app.run_server(host="127.0.0.1",debug=True,port=8052)