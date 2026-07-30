## Cleaning function

import pandas as pd
import re

def clean_country(df):
    """
    Clean and standardize the Country column.
    """
    df["Country"] = (
        df["Country"]
        .astype(str)
        .str.lower()
        .str.strip()
        .str.replace(r"[^\w\s]", "", regex=True)
        .str.title()
    )

    # Replace region names with Unknown
    region_list = ["Africa", "Asia", "Red Sea"]
    df["Country"] = df["Country"].replace(region_list, "Unknown")

    # Replace entries starting with "Between..."
    df["Country"] = df["Country"].replace(r"^Between.*", "Unknown", regex=True)

    return df


def clean_type(df):
    """
    Clean and standardize the Type column.
    """
    df["Type"] = (
        df["Type"]
        .astype(str)
        .str.lower()
        .str.strip()
        .str.replace(r"[^\w\s]", "", regex=True)
        .replace("", "Unknown")
        .fillna("Unknown")
    )

    type_map = {
        "unprovoked": "Unprovoked",
        "provoked": "Provoked",
        "invalid": "Invalid",
        "watercraft": "Watercraft",
        "sea disaster": "Sea Disaster",
        "questionable": "Questionable",
        "unconfirmed": "Unconfirmed",
        "unverified": "Unverified",
        "under investigation": "Under Investigation",
        "boat": "Boat"
    }

    df["Type"] = df["Type"].replace(type_map)

    # Group rare types into "Other"
    top_types = df["Type"].value_counts().nlargest(5).index
    df.loc[~df["Type"].isin(top_types), "Type"] = "Other"

    return df


def clean_activity(df):
    """
    Clean and standardize the Activity column.
    """
    df["Activity"] = (
        df["Activity"]
        .astype(str)
        .str.lower()
        .str.replace(r"[^\w\s]", " ", regex=True)
        .str.strip()
        .replace("", "unknown")
        .fillna("unknown")
    )

    typo_map = {
        "swmming": "swimming",
        "swimmingq": "swimming",
        "surf sking": "surfing",
        "surf skiing": "surfing",
        "surf ski": "surfing"
    }

    df["Activity"] = df["Activity"].replace(typo_map)

    activity_map = {
        "surfing": "surfing",
        "surf": "surfing",
        "surf bathing": "surfing",
        "surf paddling": "surfing",
        "surf skiing": "surfing",
        "surf fishing": "fishing",
        "surf fishing wading": "fishing",
        "swimming": "swimming",
        "treading water": "swimming",
        "standing": "standing",
        "wading": "wading",
        "diving": "diving",
        "free diving": "diving",
        "scuba diving": "diving",
        "snorkeling": "snorkeling",
        "spearfishing": "spearfishing",
        "fishing": "fishing",
        "fell overboard": "fell overboard",
        "kayaking": "kayaking",
        "bathing": "bathing",
        "body boarding": "body boarding",
        "body surfing": "body surfing",
        "pearl diving": "diving"
    }

    df["Activity"] = df["Activity"].replace(activity_map)

    # Group rare activities into "other"
    top_activities = df["Activity"].value_counts().nlargest(20).index
    df.loc[~df["Activity"].isin(top_activities), "Activity"] = "other"

    return df

