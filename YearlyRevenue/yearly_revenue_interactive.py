import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os


def make_racing_line_chart(datasets_path):
    # load csv file
    df = pd.read_csv(os.path.join(datasets_path, "cleaned_revenue.csv"))

    service_colors = {
        "Netflix": '#d70c1b',
        "Hulu": '#57e880',
        "Disney+": '#50b9ca',
        "Prime Video": '#48a8e2'
    }

    # interpolate each service's revenue over the new double value years
    services = df.columns[1:]  # skip 'Year'
    df[services] = df[services] / 1_000_000_000  # scale whole columns

    interp_steps = 20
    new_years = np.linspace(df['Year'].min(), df['Year'].max(), (len(df)-1)*interp_steps + 1)

    interp_data = pd.DataFrame({'Year': new_years})

    for service in services:
        interp_data[service] = np.interp(new_years, df['Year'], df[service])

    years = interp_data['Year']

    # create frames
    frames = []
    for i in range(1, len(interp_data) + 1):
        frame_data = []
        for service in services:
            frame_data.append(go.Scatter(
                x=years[:i],
                y=interp_data[service][:i],
                mode='lines',
                name=service,
                line=dict(color=service_colors[service]),
                hovertemplate='<b>%{fullData.name}</b><br>%{x:.0f}<br>$%{y:.2f}B<extra></extra>'
            ))
        frames.append(go.Frame(data=frame_data, name=str(round(years.iloc[i-1], 2))))

    # list of whole number years for the slider
    whole_years = list(range(int(df['Year'].min()), int(df['Year'].max()) + 1))

    slider_steps = []
    for target_year in whole_years:
        closest_idx = (np.abs(years - target_year)).argmin()
        closest_frame_name = str(round(years.iloc[closest_idx], 2))
        slider_steps.append({
            "args": [[closest_frame_name], {
                "frame": {"duration": 0, "redraw": True},
                "mode": "immediate",
                "transition": {"duration": 0}
            }],
            "label": str(target_year),
            "method": "animate"
        })

    # ✅ Change: initialize the figure with the **first frame's data** instead of empty traces
    initial_data = []
    for service in services:
        initial_data.append(go.Scatter(
            x=[years.iloc[0]],
            y=[interp_data[service].iloc[0]],
            mode='lines+markers',
            name=service,
            line=dict(color=service_colors[service]),
            hovertemplate=f"<b>{service}</b><br>%{{x:.0f}}<br>$%{{y:.2f}}B<extra></extra>"
        ))

    fig = go.Figure(
        data=initial_data,  # <-- real starting points
        layout=go.Layout(
            title="Streaming Service Revenue Over Time",
            xaxis=dict(title="Year", range=[years.min(), years.max()]),
            yaxis=dict(title="Revenue (in Billions USD)", range=[0, df[services].values.max() * 1.1]),
            showlegend=True,  # ✅ explicitly enable legend
            updatemenus=[dict(
                type="buttons",
                showactive=False,
                buttons=[
                    dict(label="Play",
                        method="animate",
                        args=[None, {
                            "frame": {"duration": 2, "redraw": False},
                            "fromcurrent": True,
                            "transition": {"duration": 0}
                        }]
                        ),
                    dict(label="Pause",
                        method="animate",
                        args=[[None], {
                            "frame": {"duration": 0, "redraw": False},
                            "mode": "immediate",
                            "transition": {"duration": 0}
                        }]
                        )
                ]
            )],
            sliders=[{
                "active": 0,
                "yanchor": "top",
                "xanchor": "left",
                "currentvalue": {
                    "font": {"size": 20},
                    "prefix": "Year: ",
                    "visible": True,
                    "xanchor": "right"
                },
                "transition": {"duration": 0},
                "pad": {"b": 10, "t": 50},
                "len": 0.9,
                "x": 0.1,
                "y": 0,
                "steps": slider_steps
            }]
        ),
        frames=frames
    )

    return fig
