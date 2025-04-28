import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#Data
years = [2020, 2021, 2022, 2023, 2024]

subscribers = {
    "Netflix":     [192.95, 209, 220.6, 238.3, 260],
    "Hulu":        [36.6, 43.8, 47.2, 48.5, 52],
    "MAX":         [55.6, 67, 81.2, 95.8, 117],
    "Prime Video": [146, 161.7, 168.3, 174.9, 180.1],
    "Disney+":     [73.7, 118.1, 164.2, 150.2, 125.3]
}

prices = {
    "Netflix":     [8.99, 8.99, 9.99, 9.99, 15.49],
    "Hulu":        [11.99, 11.99, 12.99, 14.99, 17.99],
    "MAX":         [14.99, 14.99, 14.99, 15.99, 15.99],
    "Prime Video": [8.99, 8.99, 8.99, 8.99, 11.99],
    "Disney+":     [6.99, 7.99, 7.99, 10.99, 13.99]
}

#Consistent color map
color_map = {
    "Netflix": "#d70c1b",
    "Hulu": "#57e880",
    "MAX": "#2f16e1",
    "Prime Video": "#48a8e2",
    "Disney+": "#50b9ca"
}

# Create subplot layout
fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=("📈 Subscribers Over Time", "💰 Prices Over Time")
)

# Add subscriber lines with consistent colors
for platform, values in subscribers.items():
    fig.add_trace(go.Scatter(
        x=years,
        y=values,
        mode='lines+markers',
        name=platform,
        marker=dict(size=8, color=color_map[platform]),
        line=dict(width=3, color=color_map[platform])
    ), row=1, col=1)

# Add price lines with same colors
for platform, values in prices.items():
    fig.add_trace(go.Scatter(
        x=years,
        y=values,
        mode='lines+markers',
        name=platform,
        marker=dict(size=8, color=color_map[platform]),
        line=dict(width=3, color=color_map[platform]),
        showlegend=False  # prevent duplicate legend
    ), row=1, col=2)

# Layout and styling
fig.update_layout(
    title=dict(
        text="Streaming Services: Subscribers and Prices (2020–2024)",
        x=0.5,
        font=dict(size=24, color='black')
    ),
    template="plotly_white",
    height=600,
    width=1100,
    legend=dict(
        title='Platform',
        orientation="h",
        yanchor="bottom", y=1.05,
        xanchor="center", x=0.5,
        font=dict(size=12)
    ),
    margin=dict(l=50, r=50, t=100, b=50)
)

# Axis titles
fig.update_xaxes(title_text="Year", showgrid=False)
fig.update_yaxes(title_text="Subscribers (millions)", row=1, col=1)
fig.update_yaxes(title_text="Price (USD)", row=1, col=2)

fig.show()
