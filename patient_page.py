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
                    header(),
                    html.Div(style={"height":"4rem"}),
                    html.Div(
                        [
                            card_mainlist()
                        ],
                        style={}
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
                                        html.H6("3/1/1952", style={"font-size":"0.8rem"}),
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
            dbc.CardHeader(
                dbc.Tabs(
                    [
                        dbc.Tab(label="Current Assessment", tab_id="tab-ca", tab_style={"margin-left": "8rem"}, label_style={"padding-left": "2rem", "padding-right":"2rem","font-family":"NotoSans-SemiBold", "font-size":"0.8rem", "color":"#381610"}),
                        dbc.Tab(label="Prior Assessment", tab_id="tab-pa", label_style={"padding-left": "2rem", "padding-right":"2rem","font-family":"NotoSans-SemiBold", "font-size":"0.8rem", "color":"#381610"}),
                    ],
                    id="card-patient-tabs",
                    card=True,
                    active_tab="tab-ca"
                ),
                style={"background":"#f7f7f7"}

            ),
            dbc.CardBody(
                [
                    html.Div(
                        id="card-patient-main",
                        style={"height":"68vh"}
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
                        tab_assessment_item1(app),
                        tab_assessment_item2(app),
                        tab_assessment_item2(app),
                        tab_assessment_item2(app),
                        tab_assessment_item2(app),
                        tab_assessment_item2(app),
                        tab_assessment_item2(app),
                        tab_assessment_item2(app),
                    ], 
                    style={"width":"100%","padding-right":"6rem","padding-left":"2rem","overflow-y":"scroll"}),
            ],
            style={"display":"flex","height":"68vh"}
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
                                            html.H6("7/1/2020", style={"padding-left":"0.5rem","padding-right":"0.5rem"}),
                                            html.H6(" | "),
                                            html.H6("questionnaire", style={"padding-left":"0.5rem","padding-right":"0.5rem"}),
                                        ],
                                        style={"display":"flex","font-size":"0.8rem"}
                                    ),
                                ],
                                style={"width":"25rem"}
                            ),
                            html.Div(
                                [
                                    html.H6("Due Date", style={"font-size":"0.7rem"}),
                                    html.H1("7/31/2020", style={"font-size":"1.2rem"})
                                ],
                                style={"border-left":"1px solid #d0d0d0","padding-left":"1.6rem"}
                            ),
                            html.Div(
                                [
                                    html.H6("Status", style={"font-size":"0.7rem"}),
                                    html.H1("Not Started", style={"font-size":"1.2rem"})
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
                                    html.Img(src=app.get_asset_url("icon-upload-to-the-cloud-100.png"), style={"height":"2.5rem", "padding-top":"10px"}),
                                    html.Img(src=app.get_asset_url("icon-laptop-play-video-100.png"), style={"height":"2.5rem", "padding-top":"10px"}),
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


def tab_assessment_item2(app):
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
                                            html.H6("7/1/2020", style={"padding-left":"0.5rem","padding-right":"0.5rem"}),
                                            html.H6(" | "),
                                            html.H6("questionnaire", style={"padding-left":"0.5rem","padding-right":"0.5rem"}),
                                        ],
                                        style={"display":"flex","font-size":"0.8rem"}
                                    ),
                                ],
                                style={"width":"25rem"}
                            ),
                            html.Div(
                                [
                                    html.H6("Due Date", style={"font-size":"0.7rem"}),
                                    html.H1("7/31/2020", style={"font-size":"1.2rem"})
                                ],
                                style={"border-left":"1px solid #d0d0d0","padding-left":"1.6rem"}
                            ),
                            html.Div(
                                [
                                    html.H6("Status", style={"font-size":"0.7rem"}),
                                    html.H1("Not Started", style={"font-size":"1.2rem"})
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
                                    html.Img(src=app.get_asset_url("icon-test-100.png"), style={"height":"2.5rem", "padding-top":"10px"}),
                                    html.Img(src=app.get_asset_url("icon-inspection-100.png"), style={"height":"2.5rem", "padding-top":"10px"}),
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
                        tab_assessment_item1(app),
                        tab_assessment_item2(app),
                        tab_assessment_item2(app),
                        tab_assessment_item2(app),
                        tab_assessment_item2(app),
                        tab_assessment_item2(app),
                        tab_assessment_item2(app),
                        tab_assessment_item2(app),
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

@app.callback(Output("card-patient-main", "children"), [Input("card-patient-tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-ca":
        return tab_ca_content(app)
    elif at == "tab-pa":
        return tab_pa_content(app)
    return html.P("This shouldn't ever be displayed...")


if __name__ == "__main__":
    app.run_server(host="127.0.0.1",debug=True,port=8053)