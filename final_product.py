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

    # Summary Section
    html.Div([
        html.P("""This dashboard visualizes the evolution of revenue and subscription trends across major streaming platforms from 2010 to 2024. Key visualizations include bubble plots, treemaps, bump charts, and dual-axis comparisons, all designed to analyze performance and market dynamics.

Our proposal focuses on exploring the relationship between subscription counts and overall revenue in the streaming industry. This final release presents a collection of high-fidelity artifacts compiled to address various user tasks. We use a scrollytelling approach to guide users through the dashboard, allowing them to view and interact with each visualization in sequence.

Each artifact targets a specific analytical task. Users can compare revenue and subscription counts across multiple streaming platforms during specific time periods and explore correlations between the two metrics. All artifacts support interactive features such as hover effects and time sliders. Several visualizations also include animations to illustrate how revenue and subscriptions change over time."""),
    ], style={
        'padding': '20px',
        'backgroundColor': '#f9f9f9',
        'borderBottom': '1px solid #ccc',
        'fontSize': '16px',
        'lineHeight': '1.6'
    }),

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