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
import os

from dash.dependencies import Input, Output, State

from utils import *
from app import app



app = dash.Dash(__name__, url_base_pathname="/patient/")

server = app.server



q2=["2. Over the past 2 weeks, how many times did you have swelling in your feet, ankles or legs when you woke up in the morning?",
["Every morning",
"3 or more times per week but not every day",
"1-2 times per week",
"Less than once a week",
"Never over the past 2 weeks"]]

q3=["3. Over the past 2 weeks, on average, how many times has fatigue limited your ability to do what you wanted?",
["All of  the time",
"Several times per day",
"At least once a day",
"3 or more times per week but not every day",
"1-2 times per week",
"Less than once a week",
"Never over the  past 2 weeks"]]

q4=["4. Over the past 2 weeks, on average, how many times has shortness of breath limited your ability to do what you wanted?",
["All of  the time",
"Several times per day",
"At least once a day",
"3 or more times per week but not every day",
"1-2 times per week",
"Less than once a week",
"Never over the  past 2 weeks"]]

q5=["5. Over the past 2 weeks, on average, how many times have you been forced to sleep sitting up in a chair or with at least 3 pillows to prop you up because of shortness of breath?",
["Every night",
"3 or more times per week but not every day",
"1-2 times per week",
"Less than once a week",
"Never over the  past 2 weeks"]]
q6=["6. Over the past 2 weeks, how much has your heart failure limited your enjoyment of life?",
["It has extremely  limited my enjoyment of life",
"It has limited my enjoyment of life quite a bit",
"It has moderately  limited my enjoyment of life",
"It has slightly  limited my enjoyment of life",
"It has not limited  my enjoyment of life at all",]]

q7=["7. If you had to spend the rest of your life with your heart failure the way it is right now, how would you feel about this?",
["Not at all satisfied",
"Mostly dissatisfied",
"Somewhat satisfied",
"Mostly satisfied",
"Completely satisfied",]]

def modal_kccq_questionaire(app):
    return html.Div(
            [
                html.H6("Entry", style={"font-size":"0.7rem"}),
                dbc.Button(children = [html.Img(src=app.get_asset_url("icon-test-100.png"), style={"height":"2rem", "padding-top":"0px"})], color="light",style={"border-radius":"10rem"}, id = 'kccq-modal-button-open'),
                dbc.Modal(
                    [
                        dbc.ModalHeader(html.Div([
                                    html.H4("KCCQ-12 Questionnaire"),
                                    html.H5("Instructions: The following questions refer to your heart failure and how it may affect your life. Please read and complete the following questions. There are no right or wrong answers. Please mark the answer that best applies to you.")]
                                ),),
                        dbc.ModalBody(modal_kccq_questionaire_body()),
                        dbc.ModalFooter(
                            dbc.Button("Submit", id="kccq-modal-button-submit", className="mr-2"),
                            )
                    ],
                    id = "kccq-modal",
                    size = 'xl',
                    backdrop = "static"
                )
            ],
            style={"text-align":"center"}
        )

def modal_kccq_questionaire_body():
	
	return html.Div(
                [
                    
                    html.Div(
                        [
                            html.H6("1. Heart failure affects different people in different ways. Some feel shortness of breath while others feel fatigue. Please indicate how much you are limited by heart failure (shortness of breath or fatigue) in your ability to do the following activities over the past 2 weeks."),
                            html.Div(
                                [
                                    html.Div(
                                        dbc.Row(
                                            [
                                                dbc.Col(width = 2),
                                                dbc.Col("Extremely Limited"),
                                                dbc.Col("Quite a bit Limited"),
                                                dbc.Col("Moderately Limited"),
                                                dbc.Col("Slightly Limited"),
                                                dbc.Col("Not at all Limited"),
                                                dbc.Col("Limited for other reasons or did not do the activity"),
                                            ],
                                            style = {"display" : "flex", "justify-content" : "space-around", "text-align" : "center"} 
                                        )
                                    ),
                                    html.Div(
                                        dbc.Row(
                                            [
                                                dbc.Col("a. Showering/bathing", width = 2),
                                                dbc.Col(
                                                    dbc.RadioItems(
                                                        options = [
                                                            {"label": "", "value" : 20},
                                                            {"label": "", "value" : 40},
                                                            {"label": "", "value" : 60},
                                                            {"label": "", "value" : 80},
                                                            {"label": "", "value" : 100},
                                                            {"label": "", "value" : 50},
                                                            ],
                                                        id = "kccq-modal-radio-q1a",
                                                        inline = True,
                                                        style = {"display" : "flex", "justify-content" : "space-around"} ),
                                                    
                                                    ),
                                            ]
                                        )
                                    ),
                                    html.Div(
                                        dbc.Row(
                                            [
                                                dbc.Col("b. Walking 1 block on level ground",width = 2),
                                                dbc.Col(
                                                    dbc.RadioItems(
                                                        options = [
                                                            {"label": "", "value" : 20},
                                                            {"label": "", "value" : 40},
                                                            {"label": "", "value" : 60},
                                                            {"label": "", "value" : 80},
                                                            {"label": "", "value" : 100},
                                                            {"label": "", "value" : 50},
                                                            ],
                                                        id = "kccq-modal-radio-q1b",
                                                        inline = True,
                                                        style = {"display" : "flex", "justify-content" : "space-around"} ),
                                                    
                                                    ),
                                            ]
                                        )
                                    ),
                                    html.Div(
                                        dbc.Row(
                                            [
                                                dbc.Col("c. Hurrying or jogging (as if to catch a bus)",width = 2),
                                                dbc.Col(
                                                    dbc.RadioItems(
                                                        options = [
                                                            {"label": "", "value" : 20},
                                                            {"label": "", "value" : 40},
                                                            {"label": "", "value" : 60},
                                                            {"label": "", "value" : 80},
                                                            {"label": "", "value" : 100},
                                                            {"label": "", "value" : 50},
                                                            ],
                                                        id = "kccq-modal-radio-q1c",
                                                        inline = True,
                                                        style = {"display" : "flex", "justify-content" : "space-around"} ),
                                                    
                                                    ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ]
                    ),
                    question_group(q2[0], q2[1], "kccq-modal-radio-q2"),
                    question_group(q3[0], q3[1], "kccq-modal-radio-q3"),
                    question_group(q4[0], q4[1], "kccq-modal-radio-q4"),
                    question_group(q5[0], q5[1], "kccq-modal-radio-q5"),
                    question_group(q6[0], q6[1], "kccq-modal-radio-q6"),
                    question_group(q7[0], q7[1], "kccq-modal-radio-q7"),
                    html.Div(
                        [
                            html.H6("8. How much does your heart failure affect your lifestyle? Please indicate how your heart failure may have limited your participation in the following activities over the past 2 weeks."),
                            html.Div(
                                [
                                    html.Div(
                                        dbc.Row(
                                            [
                                                dbc.Col(width = 2),
                                                dbc.Col("Severely Limited"),
                                                dbc.Col("Limited quite a bit"),
                                                dbc.Col("Moderately Limited"),
                                                dbc.Col("Slightly Limited"),
                                                dbc.Col("Did not limit at all"),
                                                dbc.Col("Does not apply or did not do for other reasons"),
                                            ],
                                            style = {"display" : "flex", "justify-content" : "space-around", "text-align" : "center"} 
                                        )
                                    ),
                                    html.Div(
                                        dbc.Row(
                                            [
                                                dbc.Col("a. Hobbies, recreational activities", width = 2),
                                                dbc.Col(
                                                    dbc.RadioItems(
                                                        options = [
                                                            {"label": "", "value" : 20},
                                                            {"label": "", "value" : 40},
                                                            {"label": "", "value" : 60},
                                                            {"label": "", "value" : 80},
                                                            {"label": "", "value" : 100},
                                                            {"label": "", "value" : 70},
                                                            ],
                                                        id = "kccq-modal-radio-q8a",
                                                        inline = True,
                                                        style = {"display" : "flex", "justify-content" : "space-around"} ),
                                                    
                                                    ),
                                            ]
                                        )
                                    ),
                                    html.Div(
                                        dbc.Row(
                                            [
                                                dbc.Col("b. Working or doing household chores",width = 2),
                                                dbc.Col(
                                                    dbc.RadioItems(
                                                        options = [
                                                            {"label": "", "value" : 20},
                                                            {"label": "", "value" : 40},
                                                            {"label": "", "value" : 60},
                                                            {"label": "", "value" : 80},
                                                            {"label": "", "value" : 100},
                                                            {"label": "", "value" : 70},
                                                            ],
                                                        id = "kccq-modal-radio-q8b",
                                                        inline = True,
                                                        style = {"display" : "flex", "justify-content" : "space-around"} ),
                                                    
                                                    ),
                                            ]
                                        )
                                    ),
                                    html.Div(
                                        dbc.Row(
                                            [
                                                dbc.Col("c. Visiting family or friends out of your home",width = 2),
                                                dbc.Col(
                                                    dbc.RadioItems(
                                                        options = [
                                                            {"label": "", "value" : 20},
                                                            {"label": "", "value" : 40},
                                                            {"label": "", "value" : 60},
                                                            {"label": "", "value" : 80},
                                                            {"label": "", "value" : 100},
                                                            {"label": "", "value" : 70},
                                                            ],
                                                        id = "kccq-modal-radio-q8c",
                                                        inline = True,
                                                        
                                                        style = {"display" : "flex", "justify-content" : "space-around"} ),
                                                    
                                                    ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ]
                    ),
                    

                    html.Div(id = "kccq-modal-tempdata", style = {"display":"none"})
                ],
                # style={"margin-top":"-30rem","background-color":"transparent","text-align":"center"}
            )


def question_group(label, value_list, id):
    value_list_len = len(value_list)

    options = []
    for i in range(value_list_len):
        options.append({"label":value_list[i], "value":i+1})

    return html.Div(
            [
                dbc.FormGroup(
                    [
                        dbc.Label(label),
                        dbc.RadioItems(
                            options=options,
                            id=id,
                        ),
                    ]
                )
            ]
        )



app.layout = modal_kccq_questionaire(app)






if __name__ == "__main__":
    app.run_server(host="127.0.0.1",debug=True,port=8052)