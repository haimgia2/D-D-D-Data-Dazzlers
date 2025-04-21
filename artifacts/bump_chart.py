##Create a Bump chart to rank number of subscribers for different streaming services

import pandas as pd
import plotly
import plotly.express as px
import os

def make_bump_chart(dataset_path):
    ## Load dataset from subscriber_counts file
    ## Data comes from webscraping of Business of Apps website, was combined by hand from various webscraping results
    df_subscriber_counts = pd.read_excel(os.path.join(dataset_path, "subscriber_counts.xlsx"), sheet_name="Sheet1")


    ##check top rows of dataframe
    #df_subscriber_counts.head()

    ## Add rank values to dataset
    ## To plot the bump chart each Service needs a rank for every year
    ## Rank will be based off Number of Subscribers

    #ensure number of subscribers is treanted as float
    df_subscriber_counts["Number Subscribers (mm)"] = df_subscriber_counts["Number Subscribers (mm)"].astype(float)

    #add rank column and rank services by number of subscribers
    df_subscriber_counts["Rank"] = df_subscriber_counts.groupby("Year")["Number Subscribers (mm)"].rank(ascending=False, method="dense").astype(int)

    #Show top rows of dataframe
    df_subscriber_counts

    #sort value by year and ranking
    df_subscriber_counts = df_subscriber_counts.sort_values(by=["Year", "Rank"])

    #Convert Year into string for plotting
    df_subscriber_counts["Year"] = df_subscriber_counts["Year"].astype(str)

    #df_subscriber_counts.head()

    ## Create custom color map for plotting
    ## Colors are pulled from Streaming Service logos using color picker

    color_dict = {
        "Netflix": '#d70c1b',
        "Hulu": '#57e880',
        "Max": '#2f16e1',
        "Disney+": '#50b9ca',
        "Amazon Prime": '#48a8e2',
        "Tubi": '#fbff00'
    }

    ##Create bump plot using data above
    fig = px.line(df_subscriber_counts, x="Year", y="Rank",
                color="Streaming Service",
                color_discrete_map=color_dict,
                markers=True,
                hover_name="Streaming Service",
                hover_data=["Revenue ($bn)", "Number Subscribers (mm)"]
                )
    fig.update_yaxes(autorange='reversed', title="Rank", visible=True, showticklabels=True)
    fig.update_xaxes(title="Year", visible=True, showticklabels=True)
    fig.update_layout(xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=False))

    #Show plot to check how it looks so far
    return fig