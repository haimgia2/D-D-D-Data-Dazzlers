import pandas as pd
import plotly.express as px

# reads the excel file
df = pd.read_excel("datasets\\Box Office Mojo.xlsx", sheet_name="box office genre revenue", usecols=["Genre", "Total", "Titles"], engine="openpyxl")

print('DATAFRAME')
print(df)

# Create a bubble chart
fig = px.scatter(
    df,
    x="Titles",                     # X-axis
    y="Total",                   # Y-axis
    size="Total",           # Bubble size
    color="Genre",                # Color by region
    hover_name="Genre",          # Hover over product names
    title="Box Office: Number of Titles vs Revenue by Genre",
    labels={"Titles": "Number of Titles", "Revenue": "Revenue ($)"},
    size_max=60                    # Maximum bubble size
)

# Customize the layout
fig.update_layout(
    xaxis_title="Titles",
    yaxis_title="Revenue",
    template="plotly_dark",        # Dark theme
    hovermode="closest"
)

# Show the plot
fig.show()