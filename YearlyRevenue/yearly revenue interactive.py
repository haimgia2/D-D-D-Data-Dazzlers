import pandas as pd
import plotly.graph_objects as go
import numpy as np

# load csv file
df = pd.read_csv('cleaned_revenue.csv')

service_colors = {
    "Netflix": '#d70c1b',
    "Hulu": '#57e880',
    "Disney+": '#50b9ca',
    "Prime Video": '#48a8e2'
}

# interpolate each service's revenue over the new double value years
services = df.columns[1:]  # skip 'Year'
df[services] = df[services] / 1_000_000_000  # scale whole columns

# interpolating data for smoother animation
interp_steps = 20  # 20 tiny steps between each real year

# create year points between whole number years
# ex instead of 2010 to 2011, will now be 2010, 2010.1, 2010.2, 2010.3,..., 2011
# creates smoother animation
new_years = np.linspace(df['Year'].min(), df['Year'].max(), (len(df)-1)*interp_steps + 1)

# create a new dataframe for interpolated data
interp_data = pd.DataFrame({'Year': new_years})

for service in services:
    interp_data[service] = np.interp(new_years, df['Year'], df[service])


# set up years for the plot
years = interp_data['Year']

# create frames for the animation
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
            hovertemplate='<b>%{fullData.name}</b><br>%{x:.0f}<br>$%{y:.2f}B<extra></extra>' # formatting hover data
        ))
    frames.append(go.Frame(data=frame_data, name=str(round(years.iloc[i-1], 2))))  # round year nicely

# list of whole number years (2010, 2011, 2013...) so the slider only displays these
whole_years = list(range(int(df['Year'].min()), int(df['Year'].max()) + 1))

slider_steps = []
for target_year in whole_years:
    # find index of closest interpolated year (ex. 2012 = 2012.00)
    closest_idx = (np.abs(years - target_year)).argmin()
    closest_frame_name = str(round(years.iloc[closest_idx], 2))

    slider_steps.append({
        "args": [[closest_frame_name], {
            "frame": {"duration": 0, "redraw": True},
            "mode": "immediate",  # jump without any transition delays
            "transition": {"duration": 0}
        }],
        "label": str(target_year),
        "method": "animate"
    })

# build figure
fig = go.Figure(

    data=[
        go.Scatter(
            x=[],
            y=[],
            mode='lines+markers',
            name=service,
            line=dict(color=service_colors[service]),  # <<<< Add color here!
            hovertemplate=(
                    f"<b>{service}</b><br>" +
                    "%{x:.0f}<br>" +
                    "$%{y:.2f}B<extra></extra>"
            )
        )
        for service in services
    ],
    layout=go.Layout(
        title="Streaming Service Revenue Over Time",
        xaxis=dict(title="Year", range=[years.min(), years.max()]),
        yaxis=dict(title="Revenue (in Billions USD)", range=[0, df[services].values.max() * 1.1]),
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            buttons=[
                # play button
                dict(label="Play",
                     method="animate",
                     args=[None, {
                         "frame": {"duration": 2, "redraw": False},  # faster animation
                         "fromcurrent": True,
                         "transition": {"duration": 0}
                     }]
                     ),
                # pause button
                dict(label="Pause",
                     method="animate",
                     args=[[None], {  # passing None list pauses
                         "frame": {"duration": 0, "redraw": False},
                         "mode": "immediate",
                         "transition": {"duration": 0}
                     }]
                     )
            ]
        )],

        # add slider to control animation manually
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

fig.show()
