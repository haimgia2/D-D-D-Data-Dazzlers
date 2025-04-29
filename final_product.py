from artifacts.bubble_plot_with_time_slider import make_bubble_plot
from artifacts.tree_map_with_time_slider import make_tree_map
from artifacts.side_by_side_line_charts import make_side_line_charts
from artifacts.bump_chart import make_bump_chart
from artifacts.racing_bar_chart import make_racing_bar_chart
from artifacts.dual_axis import make_dual_axis
from YearlyRevenue.yearly_revenue_interactive import make_racing_line_chart
import dash
from dash import dcc, html
import os

DATASETS_PATH = os.path.join("artifacts", "datasets")
ASSETS_PATH = "YearlyRevenue"


def initialize_dashboard(datasets_path, assets_path):
    # Initialize the Dash app
    app = dash.Dash(__name__)

    app.layout = html.Div([
    html.H1("Streaming Services Revenue and Subscriptions", style={'textAlign': 'center'}),

        html.Div([
            dcc.Graph(figure=make_tree_map(datasets_path)),
            dcc.Graph(figure=make_bubble_plot(datasets_path)),
            dcc.Graph(figure=make_side_line_charts()),
            dcc.Graph(figure=make_bump_chart(datasets_path)),
            dcc.Graph(figure=make_racing_bar_chart(datasets_path)),
            #dcc.Graph(figure=make_dual_axis(datasets_path)),
            dcc.Graph(figure=make_racing_line_chart(assets_path)),
        ], style={
            'display': 'block',
            'maxHeight': '90vh', 
            'overflowY': 'auto',
            'padding': '20px'
        })
    ])

    return app

if __name__ == "__main__":
    app = initialize_dashboard(DATASETS_PATH, ASSETS_PATH)
    app.run(debug=True)