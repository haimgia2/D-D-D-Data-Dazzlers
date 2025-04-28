import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os

FOLDER = "datasets"

def simple_darken(hex_color, amount=20):
    """Darken a hex color by subtracting `amount` from RGB values"""
    hex_color = hex_color.lstrip('#')
    r = max(0, int(hex_color[0:2], 16) - amount)
    g = max(0, int(hex_color[2:4], 16) - amount)
    b = max(0, int(hex_color[4:6], 16) - amount)
    return f'#{r:02x}{g:02x}{b:02x}'

def simple_lighten(hex_color, amount=20):
    """Lighten a hex color by adding `amount` to RGB values"""
    hex_color = hex_color.lstrip('#')
    r = min(255, int(hex_color[0:2], 16) + amount)
    g = min(255, int(hex_color[2:4], 16) + amount)
    b = min(255, int(hex_color[4:6], 16) + amount)
    return f'#{r:02x}{g:02x}{b:02x}'

def make_tree_map(datasets_path):

    # declares and initializes variables
    years = []
    platforms = []
    rev_sub = []
    values = []
    years_dict = {}
    
    revenue_subscribers = pd.read_csv(os.path.join(datasets_path, "cleaned_data.csv"))

    # cleaning data of null values before plotting it into a bubble plot
    revenue_subscribers["subscribers"] = revenue_subscribers["subscribers"].fillna(0)
    revenue_subscribers["revenue"] = revenue_subscribers["revenue"].fillna(0)
    revenue_subscribers["market share"] = revenue_subscribers["market share"].fillna(0)

    # preps data for treemap
    for index, row in revenue_subscribers.iterrows():
        years.append(row["year"])
        years.append(row["year"])
        platforms.append(row["platform"])
        platforms.append(row["platform"])
        rev_sub.append("💰")
        rev_sub.append("👥")
        values.append(row["revenue"] / 1000)    # converts revenue to billions
        values.append(row["subscribers"])


    # Hierarchical data
    data = {
        "Year": years,

        "Platform": platforms,
        
        "Revenue/Subscribers": rev_sub,
        
        "Values": values     
    }

    tree_df = pd.DataFrame(data)

    # Create a Label for each row
    tree_df["Label"] = tree_df["Platform"] + " - " + tree_df["Revenue/Subscribers"]
    # tree_df["Label"] = tree_df["Revenue/Subscribers"] # i wanted to encode icons as revenue/subscribers but it wouldn't let me unless i zoom into a particular box

    # Create Parent = Platform for Revenue/Subscriber rows
    tree_df["Parent"] = tree_df["Platform"]

    # Create total nodes (one per platform per year)
    totals = tree_df.groupby(["Year", "Platform"]).agg({"Values": "sum"}).reset_index()
    totals["Revenue/Subscribers"] = "Total"
    totals["Label"] = totals["Platform"]
    totals["Parent"] = ""  # root node

    # Combine back with original
    full_df = pd.concat([tree_df, totals], ignore_index=True)

    # Add color mapping
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

    # custom_colors = {
    #     "Youtube": "#ffe119",       # Yellow
    #     "Netflix": "#e6194b",       # Red
    #     "Hulu": "#3cb44b",          # Green
    #     "Disney+": "#4363d8",       # Blue
    #     "Prime Video": "#f58231",   # Orange
    #     "Twitch": "#911eb4",        # Purple
    #     "Tubi": "#42d4f4",          # Cyan
    #     "HBO MAX": "#f032e6"        # Magenta
    # }
    
    # maps the base color for each platform
    full_df["Color"] = full_df["Platform"].map(custom_colors)

    # adds gradient scale for each sub box in each platform
    for index, row in full_df.iterrows():
        #print(f"row {row}")
        if row["Revenue/Subscribers"] == "💰":
            full_df.loc[index, "Color"] = simple_darken(row["Color"], amount=50)
        elif row["Revenue/Subscribers"] == "👥":
            full_df.loc[index, "Color"] = simple_lighten(row["Color"], amount=50)

    

    # Sort years for slider
    years = sorted(full_df["Year"].unique())
    initial_year = years[0]
    initial_df = full_df[full_df["Year"] == initial_year]

    # makes tree map by frames (years)
    fig = go.Figure(
        data=[
            go.Treemap(
                labels=initial_df["Label"],
                parents=initial_df["Parent"],
                values=initial_df["Values"],
                marker=dict(colors=initial_df["Color"]),
                branchvalues="total"
            )
        ],
        frames=[
            go.Frame(
                data=[
                    go.Treemap(
                        labels=full_df[full_df['Year'] == year]['Label'],
                        parents=full_df[full_df['Year'] == year]['Parent'],
                        values=full_df[full_df['Year'] == year]['Values'],
                        marker=dict(colors=full_df[full_df['Year'] == year]['Color']),
                        branchvalues="total"
                    )
                ],
                name=str(year)
            )
            for year in years
        ],
        layout=go.Layout(
            title=f"Revenue and Subscribers by Platform Per Year",
            margin=dict(t=50, l=25, r=25, b=50),
            updatemenus=[{
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [None, {"frame": {"duration": 1000, "redraw": True}, "fromcurrent": True}]
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [[None], {"mode": "immediate", "frame": {"duration": 0}, "transition": {"duration": 0}}]
                    }
                ]
            }],
            sliders=[{
                "steps": [
                    {
                        "method": "animate",
                        "args": [[str(year)], {"mode": "immediate", "frame": {"duration": 1000, "redraw": True}}],
                        "label": str(year)
                    } for year in years
                ],
                "x": 0,
                "y": -0.1,
                "currentvalue": {"prefix": "Year: "},
                "len": 1.0
            }]
        )
    )

    # adds annotations
    fig.update_layout(
        annotations=[
            dict(
                text="Note: Some platforms are missing due to missing data per year. Some data on revenue or subscribers for a specific platform are also missing as well",
                xref="paper", yref="paper",
                x=0.5, y=-0.15,  
                showarrow=False,
                font=dict(size=12)
            ),
            dict(
                text=(
                    "💰 = Revenue (billions)<br>"
                    "👥 = Subscribers (millions)"
                ),
                xref="paper", yref="paper",
                x=-0.10, y=-0.10,  # Move to the bottom left
                xanchor='left',
                yanchor='bottom',
                showarrow=False,
                align='left',
                font=dict(size=12)
            ),
        ]

    )

    return fig