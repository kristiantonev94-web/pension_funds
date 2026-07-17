"""
Charts module for Pension Funds Dashboard
Creates reusable Plotly visualizations
"""

import plotly.express as px


def create_prices_line_chart(df):
    """
    Create line chart for pension fund prices
    
    Args:
        df: Processed prices dataframe
        
    Returns:
        Plotly figure object
    """
    fig = px.line(
        df,
        x="Date",
        y="Value",
        color="Fund",
        title="UPF pension fund prices (EUR)",
    )
    
    fig.update_layout(
        yaxis_title="Price (€)",
        xaxis_title="Date",
        hovermode="x unified",
        legend_title="Fund",
        legend=dict(
            itemclick="toggleothers",
            itemdoubleclick="toggle"
        ),
        height=500
    )
    
    return fig


def create_members_trend_chart(df):
    """
    Create line chart for insured persons trend
    
    Args:
        df: Processed members dataframe
        
    Returns:
        Plotly figure object
    """
    fig = px.line(
        df,
        x="Date",
        y="Value",
        color="Fund",
        title="Number of insured persons in UPF",
    )
    
    fig.update_layout(
        yaxis_title="Insured persons",
        xaxis_title="Date",
        hovermode="x unified",
        legend_title="Fund",
        legend=dict(
            itemclick="toggleothers",
            itemdoubleclick="toggle"
        ),
        height=500
    )
    
    return fig


def create_market_share_chart(df):
    """
    Create stacked area chart for market share
    
    Args:
        df: Market share dataframe with categorical Fund ordering
        
    Returns:
        Plotly figure object
    """
    fig = px.area(
        df.sort_values("Date"),
        x="Date",
        y="Market Share",
        color="Fund",
        groupnorm="percent",
        title="UPF market share by insured persons (%)",
    )
    
    fig.update_layout(
        yaxis_title="Market share (%)",
        xaxis_title="Date",
        hovermode="x unified",
        legend_title="Fund",
        legend=dict(
            itemclick="toggleothers",
            itemdoubleclick="toggle"
        ),
        height=500
    )
    
    return fig
