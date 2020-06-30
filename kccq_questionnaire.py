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
["Every night"
"3 or more times per week but not every day"
"1-2 times per week"
"Less than once a week"
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



def create_layout(app):
	
	return html.Div(
                [
                    html.H1("KCCQ Questionnaire"),
                    html.Div(
                        html.H2("Instructions: The following questions refer to your heart failure and how it may affect your life. Please read and complete the following questions. There are no right or wrong answers. Please mark the answer that best applies to you.")
                    ),
                    html.Div(
                        [
                            html.H6("1. Heart failure affects different people in different ways. Some feel shortness of breath while others feel fatigue. Please indicate how much you are limited by heart failure (shortness of breath or fatigue) in your ability to do the following activities over the past 2 weeks."),
                            html.Div(
                                [
                                    html.Div(
                                        dbc.Row(
                                            [
                                                dbc.Col(),
                                                dbc.Col("1"),
                                                dbc.Col("2"),
                                                dbc.Col("3"),
                                                dbc.Col("4"),
                                                dbc.Col("5"),
                                                dbc.Col("6"),
                                            ]
                                        )
                                    ),
                                    html.Div(
                                        dbc.Row(
                                            [
                                                dbc.Col("a. Showering/bathing"),
                                                dbc.Col("1"),
                                                dbc.Col("2"),
                                                dbc.Col("3"),
                                                dbc.Col("4"),
                                                dbc.Col("5"),
                                                dbc.Col("6"),
                                            ]
                                        )
                                    ),
                                    html.Div(
                                        dbc.Row(
                                            [
                                                dbc.Col("b. Walking 1 block on level ground"),
                                                dbc.Col("1"),
                                                dbc.Col("2"),
                                                dbc.Col("3"),
                                                dbc.Col("4"),
                                                dbc.Col("5"),
                                                dbc.Col("6"),
                                            ]
                                        )
                                    ),
                                    html.Div(
                                        dbc.Row(
                                            [
                                                dbc.Col("c. Hurrying or jogging (as if to catch a bus)"),
                                                dbc.Col("1"),
                                                dbc.Col("2"),
                                                dbc.Col("3"),
                                                dbc.Col("4"),
                                                dbc.Col("5"),
                                                dbc.Col("6"),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ]
                    ),
                    question_group(q2[0], q2[1], "kccq-q2"),
                    question_group(q3[0], q3[1], "kccq-q3"),
                    question_group(q4[0], q4[1], "kccq-q4"),
                    question_group(q5[0], q5[1], "kccq-q5"),
                    question_group(q6[0], q6[1], "kccq-q6"),
                    question_group(q7[0], q7[1], "kccq-q7"),

                    dbc.Button("submit", id="example-button", className="mr-2"),
                ],
                # style={"margin-top":"-30rem","background-color":"transparent","text-align":"center"}
            )


def question_group(label, value_list, id):
    value_list_len = len(value_list)

    options = []
    for i in range(value_list_len):
        options.append({"label":value_list[i], "value":i})

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



app.layout = create_layout(app)


@app.callback(Output('live-update-text', 'children'),
            [
              Input('interval-component', 'n_intervals'),
              Input("number-input", "value")
            ]
            )
def update_metrics(n, value):
    style = style={"box-shadow":"0 4px 8px 0 rgba(0, 0, 0, 0.05), 0 6px 20px 0 rgba(0, 0, 0, 0.05)", "border":"none", "border-radius":"0.5rem"}

    itemlist = []

    if value:
        value = int(value)
        for i in range(value):
            layout = html.Div(
                        html.H2(str(i)),
                        style = style
                    )
            itemlist.append(layout)

    else:
        itemlist

    return itemlist


if __name__ == "__main__":
    app.run_server(host="127.0.0.1",debug=True,port=8053)