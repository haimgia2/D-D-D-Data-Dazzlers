from sjvisualizer import plot as plt


plt.line(
    excel="cleaned_revenue.xlsx",
    title="2010-2024 Streaming Service Revenue",
    sub_title="in millions of US$",
    colors={
            "Netflix": (215, 12, 27),
            "Hulu": (87, 232, 128),
            "Disney+": (80, 185, 202),
            "Prime Video": (72, 168, 226),
    }
)
