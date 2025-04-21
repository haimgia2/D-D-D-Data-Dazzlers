import pandas as pd
import plotly
import plotly.express as px

import dash             #(version 1.8.0)
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

df = pd.read_csv("cleaned_revenue.csv")

