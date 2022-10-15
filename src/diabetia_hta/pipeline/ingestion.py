import pandas as pd
import sys
import os
from os.path import dirname
sys.path.append(dirname('../src'))
from datetime import datetime
from src.utils import utils

def ingesta_data(path, path_save):
    df = pd.read_csv(path)
    utils.save_df(df, path_save)
    return df
