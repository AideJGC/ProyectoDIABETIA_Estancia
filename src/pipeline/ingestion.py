import pandas as pd
import sys
import os
from os.path import dirname
from src.utils import utils
sys.path.append(dirname('../src'))

def ingesta_data(path):
    df = pd.read_csv(path)
    utils.save_df(df, "../Data/data.pkl")