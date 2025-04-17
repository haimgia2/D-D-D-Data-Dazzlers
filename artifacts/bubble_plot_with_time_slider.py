import plotly.express as px
import pandas as pd
import os
import numpy as np
import itertools

FOLDER = "datasets"
HULU = "business_of_apps_Hulu.xlsx"
NETFLIX = "business_of_apps_Netflix.xlsx"
PRIME = "business_of_apps_Prime Video.xlsx"
DISNEY = "business_of_apps_Disney+.xlsx"
HBO = "business_of_apps_HBO Max.xlsx"
YOUTUBE = "business_of_apps_Youtube.xlsx"
TUBI = "business_of_apps_Tubi.xlsx"
TWITCH = "business_of_apps_Twitch.xlsx"

def getMarketShare(df):
    market_shares = []
    market_share_df = df[["year", "platform", "revenue"]]

    years = sorted(df["year"].unique())

    years = [int(year) for year in years]

    for year in years:

        year_records = market_share_df[market_share_df["year"] == year].to_dict(orient="records")

        # gets the total revenue
        total_revenue = 0
        for record in year_records:

            if pd.notnull(record["revenue"]):
                total_revenue += record['revenue']


        # calculates market share for each platform
        for record in year_records:
            if pd.notnull(record["revenue"]):
                market_share = (record['revenue'] / total_revenue) * 100
            else:
                market_share = np.nan

            market_shares.append(market_share)

    # adds the market_share column to the dataframe
    df["market share"] = market_shares

    return df
        
if __name__ == "__main__":

    # data cleaning
    hulu_revenue = pd.read_excel(os.path.join(FOLDER, HULU), sheet_name="Hulu annual revenue")
    hulu_subscribers = pd.read_excel(os.path.join(FOLDER, HULU), sheet_name="Hulu annual streaming subscribe")
    netflix_revenue = pd.read_excel(os.path.join(FOLDER, NETFLIX), sheet_name="Netflix annual revenue")
    netflix_subscribers = pd.read_excel(os.path.join(FOLDER, NETFLIX), sheet_name="Netflix annual subscribers")
    prime_revenue = pd.read_excel(os.path.join(FOLDER, PRIME), sheet_name="Amazon prime video revenue")
    prime_subscribers = pd.read_excel(os.path.join(FOLDER, PRIME), sheet_name="Amazon prime video users")
    disney_revenue = pd.read_excel(os.path.join(FOLDER, DISNEY), sheet_name="Disney Plus annual revenue")
    disney_subscribers = pd.read_excel(os.path.join(FOLDER, DISNEY), sheet_name="Disney Plus annual subscribers")
    hbo_revenue = pd.read_excel(os.path.join(FOLDER, HBO), sheet_name="HBO Max annual revenue")
    hbo_subscribers = pd.read_excel(os.path.join(FOLDER, HBO), sheet_name="HBO Max subs")
    youtube_revenue = pd.read_excel(os.path.join(FOLDER, YOUTUBE), sheet_name="YouTube annual revenue")
    youtube_subscribers = pd.read_excel(os.path.join(FOLDER, YOUTUBE), sheet_name="YouTube Premium subscribers")
    tubi_revenue = pd.read_excel(os.path.join(FOLDER, TUBI), sheet_name="Tubi revenue")
    tubi_subscribers = pd.read_excel(os.path.join(FOLDER, TUBI), sheet_name="Tubi users")
    twitch_revenue = pd.read_excel(os.path.join(FOLDER, TWITCH), sheet_name="Twitch annual revenue")
    twitch_subscribers = pd.read_excel(os.path.join(FOLDER, TWITCH), sheet_name="Twitch annual concurrent viewer")


    hulu_revenue_records = hulu_revenue.to_dict(orient="records")
    hulu_subscribers_records = hulu_subscribers.to_dict(orient="records")
    netflix_revenue_records = netflix_revenue.to_dict(orient="records")
    netflix_subscribers_records = netflix_subscribers.to_dict(orient="records")
    prime_revenue_records = prime_revenue.to_dict(orient="records")
    prime_subscribers_records = prime_subscribers.to_dict(orient="records")
    disney_revenue_records = disney_revenue.to_dict(orient="records")
    disney_subscribers_records = disney_subscribers.to_dict(orient="records")
    hbo_revenue_records = hbo_revenue.to_dict(orient="records")
    hbo_subscribers_records = hbo_subscribers.to_dict(orient="records")
    youtube_revenue_records = youtube_revenue.to_dict(orient="records")
    youtube_subscribers_records = youtube_subscribers.to_dict(orient="records")
    tubi_revenue_records = tubi_revenue.to_dict(orient="records")
    tubi_subscribers_records = tubi_subscribers.to_dict(orient="records")
    twitch_revenue_records = twitch_revenue.to_dict(orient="records")
    twitch_subscribers_records = twitch_subscribers.to_dict(orient="records")

    data = {}

    # addds data from hulu
    for record in hulu_revenue_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
            
        if "Revenue ($bn)" in record:
            data[record["Year"]][f"Hulu Revenue ($mm)"] = record["Revenue ($bn)"] * 1000
        elif "Revenue ($mm)" in record:
            data[record["Year"]][f"Hulu Revenue ($mm)"] = record["Revenue ($mm)"]

    for record in hulu_subscribers_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
            
        data[record["Year"]][f"Hulu Subscribers ($mm)"] = record["Subscribers (mm)"]

    # add data from netflix
    for record in netflix_revenue_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
            
        if "Revenue ($bn)" in record:
            data[record["Year"]][f"Netflix Revenue ($mm)"] = record["Revenue ($bn)"] * 1000
        elif "Revenue ($mm)" in record:
            data[record["Year"]][f"Netflix Revenue ($mm)"] = record["Revenue ($mm)"]

    for record in netflix_subscribers_records:
        
        if record["Date"] not in data:
            data[record["Date"]] = {}
        
        data[record["Date"]][f"Netflix Subscribers ($mm)"] = record["Subscribers (mm)"]

    # adds data from prime video
    for record in prime_revenue_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
            
        if "Revenue ($bn)" in record:
            data[record["Year"]][f"Prime Video Revenue ($mm)"] = record["Revenue ($bn)"] * 1000
        elif "Revenue ($mm)" in record:
            data[record["Year"]][f"Prime Video Revenue ($mm)"] = record["Revenue ($mm)"]

    for record in prime_subscribers_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
            
        data[record["Year"]][f"Prime Video Subscribers ($mm)"] = record["Users (mm)"]

    # adds data from disney+
    for record in disney_revenue_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
            
        if "Revenue ($bn)" in record:
            data[record["Year"]][f"Disney+ Revenue ($mm)"] = record["Revenue ($bn)"] * 1000
        elif "Revenue ($mm)" in record:
            data[record["Year"]][f"Disney Revenue ($mm)"] = record["Revenue ($mm)"]

    for record in disney_subscribers_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
            
        data[record["Year"]][f"Disney+ Subscribers ($mm)"] = record["Subscribers (mm)"]

    # adds data from HBO MAX
    for record in hbo_revenue_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
            
        if "Revenue ($bn)" in record:
            data[record["Year"]][f"HBO MAX Revenue ($mm)"] = record["Revenue ($bn)"] * 1000
        elif "Revenue ($mm)" in record:
            data[record["Year"]][f"HBO MAX Revenue ($mm)"] = record["Revenue ($mm)"]

    for record in hbo_subscribers_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
        
        data[record["Year"]][f"HBO MAX Subscribers ($mm)"] = record["Subscribers (mm)"]

    # adds data from youtube
    for record in youtube_revenue_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
            
        if "Revenue ($bn)" in record:
            data[record["Year"]][f"Youtube Revenue ($mm)"] = record["Revenue ($bn)"] * 1000
        elif "Revenue ($mm)" in record:
            data[record["Year"]][f"Youtube Revenue ($mm)"] = record["Revenue ($mm)"]

    for record in youtube_subscribers_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
        
        data[record["Year"]][f"Youtube Subscribers ($mm)"] = record["Subscribers (mm)"]

    # adds data from tubi
    for record in tubi_revenue_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
            
        if "Revenue ($bn)" in record:
            data[record["Year"]][f"Tubi Revenue ($mm)"] = record["Revenue ($bn)"] * 1000
        elif "Revenue ($mm)" in record:
            data[record["Year"]][f"Tubi Revenue ($mm)"] = record["Revenue ($mm)"]

    for record in tubi_subscribers_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
        
        data[record["Year"]][f"Tubi Subscribers ($mm)"] = record["Users (mm)"]

    # adds data from twitch
    for record in twitch_revenue_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
            
        if "Revenue ($bn)" in record:
            data[record["Year"]][f"Twitch Revenue ($mm)"] = record["Revenue ($bn)"] * 1000
        elif "Revenue ($mm)" in record:
            data[record["Year"]][f"Twitch Revenue ($mm)"] = record["Revenue ($mm)"]

    for record in twitch_subscribers_records:
        
        if record["Year"] not in data:
            data[record["Year"]] = {}
        
        data[record["Year"]][f"Twitch Subscribers ($mm)"] = record['Concurrent viewers (mm)']


    data = dict(sorted(data.items()))
    new_dataframe = pd.DataFrame.from_dict(data, orient='index')

    new_dataframe = new_dataframe.sort_index().sort_index(axis=1)

    # Reset index to bring 'year' into a column
    new_dataframe = new_dataframe.reset_index().rename(columns={"index": "year"})

    # Melt to long format
    long_df = new_dataframe.melt(id_vars="year", var_name="metric", value_name="value")

    # Extract platform and metric type from column names
    long_df["platform"] = long_df["metric"].str.extract(r"^(.*?) (?:Revenue|Subscribers)")
    long_df["type"] = long_df["metric"].str.extract(r"(Revenue|Subscribers)")

    # Drop missing values
    long_df = long_df.dropna(subset=["value"])

    
    # Pivot revenue and subscribers into columns
    bubble_df = long_df.pivot_table(index=["year", "platform"], columns="type", values="value").reset_index()

    # Rename for clarity
    bubble_df = bubble_df.rename(columns={"Revenue": "revenue", "Subscribers": "subscribers"})

    # adds the market share column
    bubble_df = getMarketShare(bubble_df)

    # gets all unique years and platforms
    years = bubble_df["year"].unique()
    platforms = bubble_df["platform"].unique()

    full_index = pd.DataFrame(list(itertools.product(years, platforms)), columns=["year", "platform"])

    bubble_df = pd.merge(full_index, bubble_df, on=["year", "platform"], how="left")

    # saves dataframe to csv
    bubble_df.to_csv(os.path.join(FOLDER, 'cleaned_data.csv'), index=False)

    # cleaning data of null values before plotting it into a bubble plot
    bubble_df["subscribers"] = bubble_df["subscribers"].fillna(0)
    bubble_df["revenue"] = bubble_df["revenue"].fillna(0)
    bubble_df["market share"] = bubble_df["market share"].fillna(0)

    custom_colors = {
        "Youtube": "#ffe119",         # Yellow
        "Netflix": "#e6194b",      # Red
        "Hulu": "#3cb44b",      # Green
        "Disney+": "#4363d8",      # Blue
        "Prime Video": "#f58231",  # Orange
        "Twitch": "#911eb4",       # Purple
        "Tubi": "#42d4f4",          # Cyan
        "HBO Max": "#f032e6"       # Magenta
    }

    # makes the bubble plot
    fig = px.scatter(
        bubble_df,
        x="subscribers",
        y="revenue",
        animation_frame="year",
        size="market share",
        color="platform",
        hover_name="platform",
        size_max=60,
        color_discrete_map=custom_colors
    )

    fig.update_layout(
        title="Streaming Platform Market Overview (2010-2024)",
        xaxis=dict(
            title="Subscribers (in millions)",
            range=[0, 300], 
            tick0=0,
            dtick=50,  
        ),
        yaxis=dict(
            title="Revenue (in millions USD)",
            range=[0, 40000],  
            tick0=0,
            dtick=5000,
        ),
        legend_title_text="Streaming Platforms",
        annotations=[
            dict(
                text="Note: Bubble size represents market share (%). Some platforms are missing due to missing data per year",
                xref="paper", yref="paper",
                x=0.5, y=-0.15,  
                showarrow=False,
                font=dict(size=12)
            ),
            dict(
                text=(
                    "Start Dates:<br>"
                    "• Youtube: 2005<br>"
                    "• Netflix: 2007<br>"
                    "• Hulu: 2008<br>"
                    "• Prime Video: 2011<br>"
                    "• Twitch: 2011<br>"
                    "• Tubi: 2014<br>"
                    "• Disney+: 2019<br>"
                    "• HBO Max: 2020"
                ),
                xref="paper", yref="paper",
                x=1.05, y=0.05,  # Move to the right of the chart, near the top
                xanchor='left',
                yanchor='top',
                showarrow=False,
                align='left',
                font=dict(size=12)
            ),
        ]

    )
    fig.show()