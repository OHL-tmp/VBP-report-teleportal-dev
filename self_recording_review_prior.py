import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table

import base64
import cv2
import datetime
import os
import pandas as pd
import numpy as np

import pathlib
import plotly.graph_objects as go

from plotly.subplots import make_subplots
from dash.dependencies import Input, Output, State

from utils import *
from app import app


def modal_self_recording_review_prior(app, filename, num):
	submit_date = filename.split('_')[0]
	d = submit_date.split('-')[1]+'/'+submit_date.split('-')[2]+'/'+submit_date.split('-')[0]
	path = str('configure/') + username +str('/upload/') + filename
	encoded_video = base64.b64encode(open(path, 'rb').read())
	cap = cv2.VideoCapture(path) 
	
	if cap.isOpened():
		rate = cap.get(5)
		FrameNumber = cap.get(7)
		duration = int(FrameNumber/rate)

	size = round(os.path.getsize(path)/(1024*1024),1)

	return html.Div(
		[
		dbc.Button(children = [html.Img(src=app.get_asset_url("icon-laptop-play-video-100.png"), style={"height":"2rem", "padding-top":"0px"})], color="light",style={"border-radius":"10rem"}, id = u'video-modal-review-prior-button-open-{}'.format(num)),
		dbc.Modal(
			[
			dbc.ModalHeader(
				html.Div([
					html.H4("Berg Balance Scale -- " + d + " Completed"),
					html.H5(filename + ' | ' + str(duration) + 's | ' + str(size) + 'MB ')
			])),
			dbc.ModalBody(
				html.Div([
				html.Video(src='data:image/png;base64,{}'.format(encoded_video.decode()), controls = True, style={"height":"30rem","border-bottom":"none", "text-align":"center"} ),
				])),
			dbc.ModalFooter(
				dbc.Button("close", id=u"video-modal-review-prior-button-submit-{}".format(num), className="mr-2"),
				)],
			id = u"modal-selfrecording-review-prior-{}".format(num),
			size = 'xl',
			backdrop = "static"
			)]
		)