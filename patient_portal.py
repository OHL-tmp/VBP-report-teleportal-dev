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
                        style={"padding-top":"3rem","background-color":"#fff"}
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
                            dbc.Col(html.Img(src=app.get_asset_url("profile_default.png"), style={"height":"2.5rem", "padding-top":"0px"}), style={"padding-right":"2rem"}, width="auto"),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H1("Kevin Scott", style={"font-size":"1rem", "line-height":"0.6"}),
                                        html.H6("68 | Male", style={"font-size":"0.8rem"}),
                                    ],
                                    style={"padding-top":"0.5rem"}
                                ), width="auto"),
                            dbc.Col(),

                        ],
                        align="center",
                        no_gutters=True,
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

            dbc.CardBody(
                [
                    dbc.Tabs(
                        [
                            dbc.Tab(tab_ca_content(app), tab_id="tab-ca", label="Current Assessment", tab_style={"margin-left": "8rem"}, label_style={"padding-left": "2rem", "padding-right":"2rem","font-family":"NotoSans-SemiBold", "font-size":"0.8rem", "color":"#381610"}),
                            dbc.Tab(tab_pa_content(app), tab_id="tab-pa", label="Prior Assessment", label_style={"padding-left": "2rem", "padding-right":"2rem","font-family":"NotoSans-SemiBold", "font-size":"0.8rem", "color":"#381610"}),
                        ],
                        active_tab="tab-ca"
                    )
                ]
            ),       
        ]
    )

    return card


def tab_ca_content(app):
    return html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            html.Div(
                                [
                                    html.H6("TOTAL TASKS", style={"color":"#1357dd","width":"3rem"}),
                                    dbc.Badge("2", style={"font-family":"NotoSans-SemiBold","font-size":"1.2rem","border-radius":"10rem","width":"4.5rem","background-color":"#1357dd"}),
                                ],
                                style={"border-radius":"0.8rem", "border":"1px solid #1357dd","padding":"0.5rem"}
                            ),
                            style={"padding":"1rem"}
                        ),
                        html.Div(
                            html.Div(
                                [
                                    html.H6("ACTIVE TASKS", style={"color":"#dc3545","width":"3rem"}),
                                    dbc.Badge("2", style={"font-family":"NotoSans-SemiBold","font-size":"1.2rem","border-radius":"10rem","width":"4.5rem","background-color":"#dc3545"}, id = 'patient-ca-active-tasks'),
                                ],
                                style={"border-radius":"0.8rem", "border":"1px solid #dc3545","padding":"0.5rem"}
                            ),
                            style={"padding":"1rem"}
                        ),
                        # html.Div(
                        #     html.Div(
                        #         [
                        #             html.H6("INCOMING TASKS", style={"color":"#6c757d","width":"4.5rem"}),
                        #             dbc.Badge("0", style={"font-family":"NotoSans-SemiBold","font-size":"1.2rem","border-radius":"10rem","width":"4.5rem","background-color":"#6c757d"}),
                        #         ],
                        #         style={"border-radius":"0.8rem", "border":"1px solid #6c757d","padding":"0.5rem"}
                        #     ),
                        #     style={"padding":"1rem"}
                        # ),
                    ], 
                    style={"width":"8rem"}),

                html.Div(
                    [
                        tab_assessment_item1(app),
                        tab_assessment_item2(app,1),
                        # tab_assessment_item2(app,2),
                        # tab_assessment_item2(app,3),
                        # tab_assessment_item2(app,4),
                        # tab_assessment_item2(app,5),
                        # tab_assessment_item2(app,6),
                        # tab_assessment_item2(app,7),
                    ], 
                    style={"width":"100%","padding-right":"6rem","padding-left":"2rem","overflow-y":"scroll"}),
            ],
            style={"display":"flex","height":"74vh"}
        )


def tab_assessment_item1(app):
    return html.Div(
            [
                html.Div(
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H1("Berg Balance Scale", style={"font-size":"1.5rem"}),
                                    html.Div(
                                        [
                                            dbc.Badge("Functional Assessment", color="info", style={"font-family":"NotoSans-Light","font-size":"0.8rem"}),
                                            html.H6("Dr.Smith", style={"padding-left":"0.5rem","padding-right":"0.5rem"}),
                                            html.H6(" | "),
#                                            html.H6("7/1/2020", style={"padding-left":"0.5rem","padding-right":"0.5rem"}),
#                                            html.H6(" | "),
                                            html.H6("self-recording", style={"padding-left":"0.5rem","padding-right":"0.5rem"}),
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
                                    html.H1("Not Started", style={"font-size":"1.2rem"}, id = 'patient-assessment-status')
                                ],
                                style={"border-left":"1px solid #d0d0d0","padding-left":"1.6rem"}
                            ),
                            html.Div(
                                [
                                    html.H6("Completion Date", style={"font-size":"0.7rem"}),
                                    html.H1("")
                                ],
                                style={"border-left":"1px solid #d0d0d0","padding-left":"1.6rem"}
                            ),
                            html.Div(
                                [
                                    html.Div(modal_self_recording(app), id = u'patient-selfrecording-todo-{}'.format(num), hidden = False),
                                   
                                    html.Div(modal_self_recording_review(app), id = u'patient-selfrecording-done-{}'.format(num), hidden = True)
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


def tab_pa_content(app):
    return html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            html.Div(
                                [
                                    html.H6("TOTAL TASKS", style={"color":"#1357dd","width":"3rem"}),
                                    dbc.Badge("2", style={"font-family":"NotoSans-SemiBold","font-size":"1.2rem","border-radius":"10rem","width":"4.5rem","background-color":"#1357dd"}),
                                ],
                                style={"border-radius":"0.8rem", "border":"1px solid #1357dd","padding":"0.5rem"}
                            ),
                            style={"padding":"1rem"}
                        ),
                        html.Div(
                            html.Div(
                                [
                                    html.H6("ACTIVE TASKS", style={"color":"#dc3545","width":"3rem"}),
                                    dbc.Badge("2", style={"font-family":"NotoSans-SemiBold","font-size":"1.2rem","border-radius":"10rem","width":"4.5rem","background-color":"#dc3545"}),
                                ],
                                style={"border-radius":"0.8rem", "border":"1px solid #dc3545","padding":"0.5rem"}
                            ),
                            style={"padding":"1rem"}
                        ),
                        html.Div(
                            html.Div(
                                [
                                    html.H6("INCOMING TASKS", style={"color":"#6c757d","width":"4.5rem"}),
                                    dbc.Badge("0", style={"font-family":"NotoSans-SemiBold","font-size":"1.2rem","border-radius":"10rem","width":"4.5rem","background-color":"#6c757d"}),
                                ],
                                style={"border-radius":"0.8rem", "border":"1px solid #6c757d","padding":"0.5rem"}
                            ),
                            style={"padding":"1rem"}
                        ),
                    ], 
                    style={"width":"8rem"}),

                html.Div(
                    [
                        # tab_assessment_item1(app),
                        # tab_assessment_item2(app),
                        # tab_assessment_item2(app),
                        # tab_assessment_item2(app),
                        # tab_assessment_item2(app),
                        # tab_assessment_item2(app),
                        # tab_assessment_item2(app),
                        # tab_assessment_item2(app),
                    ], 
                    style={"width":"100%","padding-right":"6rem","padding-left":"2rem","overflow-y":"scroll"}),
            ],
            style={"display":"flex","height":"68vh"}
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


@app.callback(
    Output('patient-ca-active-tasks', 'children'),
    [Input('patient-questionnaire-status-1','children'),
    Input('patient-assessment-status', 'children')]
    )
def update_active_tasks(s1,s2):
    status = [s1, s2]
    return status.count("Not Started")


# questionnaire modal
@app.callback(
    [Output('patient-questionnaire-todo-1', 'hidden'),
    Output('patient-questionnaire-done-1', 'hidden'),
    Output('patient-questionnaire-status-1', "children"),
    Output('patient-questionnaire-completdate-1',"children")],
    [Input('kccq-modal-button-submit', 'n_clicks')]
    )
def toggle_todo_done(n):
    d = datetime.datetime.now().strftime('%m/%d/%Y')

    if n:
        return True, False, "Completed", str(d)
    return False, True, "Not Started", ""

@app.callback(
    Output("kccq-modal-tempdata", "children"),
    [Input("kccq-modal-button-submit", "n_clicks")],
    [State("kccq-modal-radio-q1a", "value"),
    State("kccq-modal-radio-q1b", "value"),
    State("kccq-modal-radio-q1c", "value"),
    State("kccq-modal-radio-q2", "value"),
    State("kccq-modal-radio-q3", "value"),
    State("kccq-modal-radio-q4", "value"),
    State("kccq-modal-radio-q5", "value"),
    State("kccq-modal-radio-q6", "value"),
    State("kccq-modal-radio-q7", "value")]
    )
def store_questionaire_answer(n, q1a, q1b, q1c, q2, q3, q4, q5, q6, q7):
    submit_date = str(datetime.datetime.now().date())
    answer = {"answer-date" : str(datetime.datetime.now().date().strftime('%m/%d/%Y')), 
                "q1a" : q1a, "q1b" : q1b, "q1c" : q1c,
                "q2" : q2,
                "q3" : q3,
                "q4" : q4,
                "q5" : q5,
                "q6" : q6,
                "q7" : q7}
    path = str('configure/') + username +str('/kccq_questionarie_') + submit_date + str('.json')
    if not os.path.exists(str('configure/') + username +str('/')):
        os.makedirs(str('configure/') + username +str('/'))
    with open(path,'w') as outfile:
        json.dump(answer, outfile)
    return json.dumps(answer)

@app.callback(
    Output("kccq-modal", 'is_open'),
    [Input("kccq-modal-button-open", "n_clicks"),
    Input("kccq-modal-button-submit", "n_clicks")],
    [State("kccq-modal", 'is_open')]
    )
def open_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    else:
        return is_open

# questionnaire_answer modal

@app.callback(
    [Output("kccq-modal-answer-radio-q1a", "value"),
    Output("kccq-modal-answer-radio-q1b", "value"),
    Output("kccq-modal-answer-radio-q1c", "value"),
    Output("kccq-modal-answer-radio-q2", "value"),
    Output("kccq-modal-answer-radio-q3", "value"),
    Output("kccq-modal-answer-radio-q4", "value"),
    Output("kccq-modal-answer-radio-q5", "value"),
    Output("kccq-modal-answer-radio-q6", "value"),
    Output("kccq-modal-answer-radio-q7", "value"),
    Output("kccq-modal-answer-header", "children")],
    [Input("kccq-modal-tempdata", "children"),
    Input("kccq-modal-answer-button-open", "n_clicks")]
    )
def store_questionaire_answer(data, n):
    if n:
        answer = json.loads(data)
        header = "KCCQ Questionnaire --" + answer["answer-date"] + " Completed" 
        return answer["q1a"],answer["q1b"],answer["q1c"],answer["q2"],answer["q3"],answer["q4"],answer["q5"],answer["q6"],answer["q7"], header
    return "","","","","","","","","",""

@app.callback(
    Output("kccq-modal-answer", 'is_open'),
    [Input("kccq-modal-answer-button-open", "n_clicks"),
    Input("kccq-modal-answer-button-submit", "n_clicks")],
    [State("kccq-modal-answer", 'is_open')]
    )
def open_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    else:
        return is_open


if __name__ == "__main__":
    app.run_server(host="127.0.0.1",debug=True,port=8052)