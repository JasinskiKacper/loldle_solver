import os
import json
import pandas as pd

def load_champions(filename: str) -> dict:
    champions = pd.read_json(filename)
    champions = champions.set_index('Champion')
    return champions

def load_quotes(filename: str) -> dict:
    return pd.read_json(filename)

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
