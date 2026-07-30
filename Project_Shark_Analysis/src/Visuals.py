## Visuals 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_top_countries(df):
    """
    Plot the top 10 countries by shark incident percentage.
    """
    country_counts = df["Country"].value_counts().head(10)
    country_percent = (country_counts / country_counts.sum()) * 100

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=country_counts.index,
        y=country_percent,
        palette="Blues_d"
    )
    plt.title("Top 10 Countries by Shark Incident Share (%)")
    plt.ylabel("Percentage of incidents (%)")
    plt.xlabel("Country")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_attack_types(df):
    """
    Plot the distribution of attack types.
    """
    type_counts = df["Type"].value_counts()
    type_percent = (type_counts / type_counts.sum()) * 100

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=type_counts.index,
        y=type_percent,
        palette="Reds_d"
    )
    plt.title("Distribution of Attack Types (%)")
    plt.ylabel("Percentage of incidents (%)")
    plt.xlabel("Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_top_activities(df):
    """
    Plot the top 20 activities by incident percentage.
    """
    activity_counts = df["Activity"].value_counts().head(20)
    activity_percent = (activity_counts / activity_counts.sum()) * 100

    plt.figure(figsize=(12, 6))
    sns.barplot(
        x=activity_counts.index,
        y=activity_percent,
        palette="Greens_d"
    )
    plt.title("Top 20 Activities by Incident Share (%)")
    plt.ylabel("Percentage of incidents (%)")
    plt.xlabel("Activity")
    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.show()


def plot_swimming_by_country(df):
    """
    Plot the top 10 countries for swimming-related incidents.
    """
    swim_df = df[df["Activity"] == "swimming"]
    swim_counts = swim_df["Country"].value_counts().head(10)
    swim_percent = (swim_counts / swim_counts.sum()) * 100

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=swim_counts.index,
        y=swim_percent,
        palette="Blues"
    )
    plt.title("Top 10 Countries for Swimming-Related Incidents (%)")
    plt.ylabel("Percentage of swimming incidents (%)")
    plt.xlabel("Country")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_swim_vs_surf_country(df):
    """
    Compare swimming vs surfing incidents by country (top 10).
    """
    swim_df = df[df["Activity"].str.contains("swimming", na=False)]
    surf_df = df[df["Activity"].str.contains("surfing", na=False)]

    swim_country = swim_df["Country"].value_counts()
    surf_country = surf_df["Country"].value_counts()

    combined = pd.DataFrame({
        "swimming": swim_country,
        "surfing": surf_country
    }).fillna(0)

    combined["total"] = combined["swimming"] + combined["surfing"]
    top10 = combined.sort_values("total", ascending=False).head(10)

    plot_df = top10[["swimming", "surfing"]].reset_index().melt(
        id_vars="index",
        var_name="Activity",
        value_name="Count"
    )
    plot_df.rename(columns={"index": "Country"}, inplace=True)

    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=plot_df,
        x="Country",
        y="Count",
        hue="Activity",
        palette=["#1f77b4", "#ff7f0e"]
    )
    plt.title("Swimming vs Surfing Incidents by Country (Top 10)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_swim_vs_surf_month(df):
    """
    Compare swimming vs surfing incidents by month.
    """
    swim_df = df[df["Activity"].str.contains("swimming", na=False)]
    surf_df = df[df["Activity"].str.contains("surfing", na=False)]

    swim_month = swim_df["Month"].value_counts().sort_index()
    surf_month = surf_df["Month"].value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=swim_month.index, y=swim_month.values, label="Swimming", marker="o")
    sns.lineplot(x=surf_month.index, y=surf_month.values, label="Surfing", marker="o")

    plt.title("Swimming vs Surfing Incidents by Month")
    plt.xlabel("Month")
    plt.ylabel("Number of incidents")
    plt.xticks(range(1, 13))
    plt.tight_layout()
    plt.show()





