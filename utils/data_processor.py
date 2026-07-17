"""
Data processing module for Pension Funds Dashboard
Handles all data transformation and calculations
"""

import pandas as pd


def process_prices_data(df):
    """
    Process and clean prices data
    
    Args:
        df: Raw prices dataframe
        
    Returns:
        Processed dataframe
    """
    df = df.copy()
    df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
    df = df.sort_values(["Fund", "Date"])
    return df


def process_members_data(df):
    """
    Process and clean insured persons data
    
    Args:
        df: Raw members dataframe
        
    Returns:
        Processed dataframe
    """
    df = df.copy()
    df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
    df["Date"] = pd.to_datetime(
        dict(
            year=df["Year"],
            month=df["Month"],
            day=1
        )
    )
    df = df.sort_values(["Fund", "Date"])
    return df


def calculate_market_share(members_df):
    """
    Calculate market share from members data
    
    Args:
        members_df: Processed members dataframe
        
    Returns:
        Dataframe with market share column
    """
    market = members_df.copy()
    
    market["Total"] = (
        market
        .groupby("Date")["Value"]
        .transform("sum")
    )
    
    market["Market Share"] = (
        market["Value"] /
        market["Total"] *
        100
    )
    
    return market


def get_latest_ranking(market_df):
    """
    Get fund ranking by latest market share
    
    Args:
        market_df: Market share dataframe
        
    Returns:
        List of funds ordered by market share (highest to lowest)
    """
    latest_date = market_df["Date"].max()
    
    ranking = (
        market_df[market_df["Date"] == latest_date]
        .sort_values("Market Share", ascending=False)
        ["Fund"]
        .tolist()
    )
    
    return ranking


def order_funds_by_ranking(market_df, ranking):
    """
    Order funds by ranking for consistent visualization
    
    Args:
        market_df: Market share dataframe
        ranking: List of funds in desired order
        
    Returns:
        Dataframe with categorical fund ordering
    """
    market = market_df.copy()
    market["Fund"] = pd.Categorical(
        market["Fund"],
        categories=ranking[::-1],  # Reverse for bottom-to-top visualization
        ordered=True
    )
    return market
