import pandas as pd

def strong_beer_abv(df):
    """Cette fonction retourne la brasserie qui fabrique la biere la plus alcolisé"""
    return df[df['beer_abv']==df['beer_abv'].max()].brewery_name

