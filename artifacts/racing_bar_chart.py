import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

def make_racing_bar_chart(dataset_path):
    df = pd.read_csv(os.path.join(dataset_path, "cleaned_data.csv"))

    platforms = ['Hulu', 'Youtube', 'Netflix', 'Twitch', 'Prime Video', 'Tubi', 'Disney+', 'HBO MAX']
    years = df['year'].unique()

    full_grid = pd.MultiIndex.from_product([years, platforms], names=['year', 'platform']).to_frame(index=False)

    df['revenue'] = df['revenue'].fillna(0)
    df_full = pd.merge(full_grid, df[['year', 'platform', 'revenue']], on=['year', 'platform'], how='left')
    df_full['revenue'] = df_full['revenue'].fillna(0)

    # defines custom colors
    custom_colors = {
        "Netflix": '#d70c1b',      # Red
        "Hulu": '#57e880',         # Light Green
        "HBO MAX": '#2f16e1',          # Dark Blue/Purple
        "Disney+": '#50b9ca',      # Teal Blue
        "Prime Video": '#48a8e2', # Light Blue
        "Tubi": '#6800c2',         # Purple
        "Twitch": '#f032e6',       # Primary Blue
        "Youtube": '#ff7b00'       # Primary Bright Orange
    }

    fig = px.bar(
        df_full,
        x='revenue',
        y='platform',
        color='platform',
        orientation='h',
        animation_frame='year',
        range_x=[0, df_full['revenue'].max() + 5000],
        title='Streaming Services Revenue Over the Years (2010-2024)',
        labels={'revenue': 'Revenue (in Millions)', 'platform': 'Streaming Services'},
        color_discrete_map=custom_colors
    )

    fig.update_layout(
        xaxis_title="Revenue (in Millions)",
        yaxis_title="Streaming Services",
        showlegend=False,
        template='plotly_white',
        height=500
    )

    return fig