import dash
import dash_auth

VALID_USERNAME_PASSWORD_PAIRS = {
	'admin': '123'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

auth = dash_auth.BasicAuth(
	app,
	VALID_USERNAME_PASSWORD_PAIRS
)


server = app.server
app.config.suppress_callback_exceptions = True