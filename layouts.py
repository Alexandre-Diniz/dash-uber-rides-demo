import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime as dt

horario = []
for i in range(0,24):
	horario.append({'label':str(i)+':00', 'value':str(i)+':00'})

values = [138,66,55,93,166,333,722,1001,780,532,477,547,469,591,763,967,1152,1262,1122,1018,597,878,529,317]

a = []
for i in range(0,24):
	a.append(str(i)+':00')

trace = go.Bar(x=a,
			   y=values)
data = [trace]
layout = go.Layout(barmode='group', width=850, height=400)
figure = {
	'data':data,
	'layout':layout
}
barGraph = go.Figure(figure)

layout = html.Div(className='root', children=[
	
	html.Div(className='div1', children=[
		html.Div(className='div1-1', children=[

			html.Div(className='div1-1-1', children=[
				html.P(className='title', children=['DASH - UBER DATA APP'])
			]),
			html.Div(className='div1-1-2', children=[
				html.P("""Select different days using the date 
				picker or by selecting different time frames on the histogram.""")
			]),
			html.Div(className='div1-1-3', children=[
				dcc.DatePickerSingle(
					id='date-picker-single',
					date=dt(2014, 4, 1)
				)
			]),
			html.Div(className='div1-1-4', children=[
				dcc.Dropdown(
					options=[
						{'label': 'Madson Square Garden', 'value': 'MSQ'},
						{'label': 'Yankee Stadium', 'value': 'YS'},
						{'label': 'Empire State Building', 'value': 'ESB'},
						{'label': 'New York Stock Exchange', 'value': 'NYSE'},
						{'label': 'JFK Airport', 'value': 'JFKA'},
						{'label': 'Grand Central Station', 'value': 'GCS'},
						{'label': 'Times Square', 'value': 'TS'},
						{'label': 'Columbia University', 'value': 'CU'},
						{'label': 'United Nations HQ', 'value': 'UNHQ'}
					],
					value='MSQ'
				) 
			]),
			html.Div(className='div1-1-6', children=[
				dcc.Dropdown(
					options=horario,
					value='0:00'
				)
			]),
			html.Div(className='div1-1-6', children=[
				html.P(["Total Number of rides: 14,546"]),
				html.P(["Total rides in selection: 317"]),
				html.P(["2014-04-01 - showing hour(s): 23-23"]),
				html.P(["Source: FiveThirtyEight"])
			]),
		]),

		html.Div(className='div1-2', children=[

			html.Div(className='div1-2-1', children=[

			]),

			html.Div(className='div1-2-2', children=[
				dcc.Graph(figure=barGraph)
			])

		])
	]),

])