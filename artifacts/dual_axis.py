import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

def make_dual_axis(datasets_path):
    df = pd.read_csv(os.path.join(datasets_path, "cleaned_data.csv"))

    df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
    df['subscribers'] = pd.to_numeric(df['subscribers'], errors='coerce')

    platforms = df['platform'].dropna().unique()

    fig = go.Figure()

    for platform in platforms:
        platform_data = df[df['platform'] == platform]
        fig.add_trace(go.Bar(
            x=platform_data['year'],
            y=platform_data['revenue'],
            name=f'{platform} Revenue',
            yaxis='y1'
        ))

    for platform in platforms:
        platform_data = df[df['platform'] == platform]
        fig.add_trace(go.Scatter(
            x=platform_data['year'],
            y=platform_data['subscribers'],
            name=f'{platform} Subscribers',
            mode='lines+markers',
            yaxis='y2'
        ))

    fig.update_layout(
        title='Revenue and Subscribers Over Time by Streaming Platform (Dual Axis)',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Revenue ($M)', side='left'),
        yaxis2=dict(title='Subscribers (M)', overlaying='y', side='right'),
        barmode='group',
        template='plotly_white',
        legend=dict(x=1.02, y=1, traceorder='normal', borderwidth=1)
    )

    return fig