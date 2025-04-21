from artifacts.bubble_plot_with_time_slider import make_bubble_plot
from artifacts.tree_map_with_time_slider import make_tree_map
import dash
from dash import dcc, html
import os

DATASETS_PATH = os.path.join("artifacts", "datasets")

def initialize_dashboard(datasets_path):
    # Initialize the Dash app
    app = dash.Dash(__name__)

    # Define the layout
    app.layout = html.Div([
        html.H1("Streaming Services Revenue and Subscriptions", style={'textAlign': 'center'}),
        
        html.Div([
            dcc.Graph(figure=make_tree_map(datasets_path)),
            dcc.Graph(figure=make_bubble_plot(datasets_path)),
        ], style={'display': 'flex', 'justifyContent': 'space-around'})
    ])

    return app

if __name__ == "__main__":
    app = initialize_dashboard(DATASETS_PATH)
    app.run(debug=True)