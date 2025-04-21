from artifacts.bubble_plot_with_time_slider import make_bubble_plot
from artifacts.tree_map_with_time_slider import make_tree_map
from artifacts.side_by_side_line_charts import make_side_line_charts
from artifacts.bump_chart import make_bump_chart
import dash
from dash import dcc, html
import os

DATASETS_PATH = os.path.join("artifacts", "datasets")

def initialize_dashboard(datasets_path):
    # Initialize the Dash app
    app = dash.Dash(__name__)

    app.layout = html.Div([
    html.H1("Streaming Services Revenue and Subscriptions", style={'textAlign': 'center'}),

    html.Div([
        dcc.Graph(figure=make_tree_map(datasets_path)),
        dcc.Graph(figure=make_bubble_plot(datasets_path)),
        dcc.Graph(figure=make_side_line_charts()),
        dcc.Graph(figure=make_bump_chart(datasets_path)),
    ], style={
        'display': 'block',            # Stack elements vertically
        'maxHeight': '90vh',           # Optional: Limit height of the container
        'overflowY': 'auto',           # Enable vertical scrolling
        'padding': '20px'
    })
])

    return app

if __name__ == "__main__":
    app = initialize_dashboard(DATASETS_PATH)
    app.run(debug=True)