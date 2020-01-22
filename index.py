import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd	

from app import app
from layouts import layout
import callbacks
from app import server


app.layout = layout


if __name__ == '__main__':
	app.run_server(debug=True)