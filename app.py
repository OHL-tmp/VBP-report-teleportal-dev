#!/usr/bin/env python3

import dash
import dash_auth

# from configure.login import *

app = dash.Dash(__name__)
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

server = app.server

app.config.suppress_callback_exceptions = True

app.title = 'Physician Portal'


# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
# )
