import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def calc_missing_data(df: pd.DataFrame, plot=False) -> pd.DataFrame:
    """
    Calculates number of missing values.
    Input:
    df - pd.DataFrame containing the data
    plot - default: False, change to True to plot a bar chart

    Return:
    pd.DataFrame with missing data per column
    """
    missing = df.isna().sum().rename("missing_total").to_frame()
    missing["ratio"] = missing / len(df)
    if plot:
        plt.figure(figsize=(12,6))
        plt.title("Missing values in %")
        missing.loc[missing["ratio"]>0, "ratio"].sort_values().plot.bar()
        plt.show()
    return missing


def format_price(price: pd.Series):
    """
    Removes dollar signs and comma from a series of prices
    Input:
    - price: pd.Series containing the prices

    Returns:
    - formatted pd.Series with prices as float32
    """
    price = price.str.replace("\\$|\\,|\\€","", regex=True)
    price = price.astype(np.float32)
    return price