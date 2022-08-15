
# Functions for EDA and GEDA Analysis

import pandas as pd 
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter
import pickle


def dejar_solo_cifras(txt):
    return "".join(c for c in txt if c.isdigit())

# Función number_formater

def number_formatter(number, pos = None):
    """Convert a number into a human readable format."""
    magnitude = 0
    while abs(number) >= 1000:
        magnitude += 1
        number /= 1000.0
    return '%.1f%s' % (number, ['', 'K', 'M', 'B', 'T', 'Q'][magnitude])



# Función integer_formatter

def int_formatter(number, pos=None):
    return int(number)



# Función get_repeated_values

def get_repeated_values(df, col, top):
    """Return top 't' of repeated values."""
    top_5 = df.groupby([col])[col]\
                    .count()\
                    .sort_values(ascending = False)\
                    .head(5)
    indexes_top_5 = top_5.index
    
    if ((top == 1) and (len(indexes_top_5) > 0)):
        return indexes_top_5[0]
    elif ((top == 2) and (len(indexes_top_5) > 1)):
        return indexes_top_5[1]
    elif ((top == 3) and (len(indexes_top_5) > 2)):
        return indexes_top_5[2]
    else: 
        return 'undefined'

    
def string_profiling(df_o, col):
    """
    Profiling for categoric columns. 
    
    :param: column to analyze
    :return: dictionary
    """
    profiling = {}
    
    # eliminate missing values
    df = df_o.copy()
    #df = df[df[col].notna()]

    profiling.update({'mode': df[col].mode().values,
                     'uniques': df[col].nunique(),
                     'missings': df[col].isnull().sum(),
                     'average lenght': df[col].astype(str).str.len().mean(),
                     'max lenght': df[col].astype(str).str.len().max(),
                     'min lenght': df[col].astype(str).str.len().min(),
                     'top1_repeated': get_repeated_values(df, col, 1),
                     'top2_repeated': get_repeated_values(df, col, 2),
                     'top3_repeated': get_repeated_values(df, col, 3)})
    
    return profiling    
    
# Función categoric_profiling

def categoric_profiling(df_o, col):
    """
    Profiling for categoric columns. 
    
    :param: column to analyze
    :return: dictionary
    """
    profiling = {}
    
    # eliminate missing values
    df = df_o.copy()
    #df = df[df[col].notna()]

    profiling.update({'mode': df[col].mode().values,
                     'uniques': df[col].nunique(),
                     'missings': df[col].isnull().sum(),
                     'top1_repeated': get_repeated_values(df, col, 1),
                     'top2_repeated': get_repeated_values(df, col, 2),
                     'top3_repeated': get_repeated_values(df, col, 3)})
    
    return profiling



# Función dates_profiling

def dates_profiling(df_o, col):
    """
    Profiling for dates and hours columns. 
    
    :param: column to analyze
    :return: dictionary
    """
    profiling = {}
    
    # eliminate missing values
    df = df_o.copy()
   # df = df[df[col].notna()]

    profiling.update({'max': df[col].max(),
                     'min': df[col].min(),
                     'missings': df[col].isnull().sum(),
                     'uniques': df[col].nunique(),
                     'top1_repeated': get_repeated_values(df, col, 1),
                     'top2_repeated': get_repeated_values(df, col, 2),
                     'top3_repeated': get_repeated_values(df, col, 3)})
    
    return profiling     
    
# Función que obtiene los valores unicos por columna       
 
def unicos_val_by_col(df_pkl):
   #Obtiene los valores únicos por columa, recibe un dataframe.
    for col in list(df_pkl):
        print(col + ": " , len(df_pkl[col].unique().tolist()))      
        

def clean_column(df):
    
    cols = df.columns
    new_column_names = []

    for col in cols:
        new_col = col.lstrip().rstrip().lower().replace(' ','_')\
              .replace(' ','_')\
              .replace('á','a')\
              .replace('é','e')\
              .replace('í','i')\
              .replace('ó','o')\
              .replace('ú','u')
        new_column_names.append(new_col)

    df.columns = new_column_names
    
    return df
        
    
    
    
def numeric_profiling(df_pkl, col):
    """
    Profiling for numeric columns. 
    
    :param: column to analyze
    :return: dictionary
    """
    profiling = {}

    profiling.update({'max': df_pkl[col].max(),
                     'min': df_pkl[col].min(),
                     'mean': df_pkl[col].mean(),
                     'stdv': df_pkl[col].std(),
                     '25%': df_pkl[col].quantile(.25),
                     'median': df_pkl[col].median(),
                     '75%': df_pkl[col].quantile(.75),
                     'kurtosis': df_pkl[col].kurt(),
                     'skewness': df_pkl[col].skew(),
                     'uniques': df_pkl[col].nunique(),
                     'valores_unicos': df_pkl[col].nunique(),
                     'renglones_totales': df_pkl[col].size,
                     'faltantes_totales': df_pkl[col].isna().sum(),
                     'prop_missings': df_pkl[col].isna().sum()/df_pkl.shape[0]*100,
                     'top1_repeated': get_repeated_values(df_pkl, col, 1),
                     'top2_repeated': get_repeated_values(df_pkl, col, 2),
                     'top3_repeated': get_repeated_values(df_pkl, col, 3)})    
    
    return profiling




# Para variable categóricas y fechas
def categorical_profiling(df, col):
    """
    Profiling para variables categóricas.  
    :parametros: dataframe --> df ; columna a analizar --> col
    :return: diccionario de valores importantes
    """
    profiling = {}

    profiling.update({'mode': df[col].mode().values,
                     'numero_categorias': df[col].nunique(),
                     'nombres_categoria': df[col].unique(),
                     'valores_unicos': df[col].nunique(),
                     'renglones_totales': df[col].size,
                     'faltantes_totales': df[col].isna().sum(),
                     'proporcion_faltantes': df[col].isna().sum()/df[col].size*100,                      
                     'top1': get_repeated_values(df, col, 1),
                     'top2': get_repeated_values(df, col, 2),
                     'top3': get_repeated_values(df, col, 3)})
    
    return profiling


def get_repeated_values(df_pkl, col, top):
    top_5 = df_pkl.groupby([col])[col]\
                    .count()\
                    .sort_values(ascending = False)\
                    .head(3)
    indexes_top_5 = top_5.index
    
    if ((top == 1) and (len(indexes_top_5) > 0)):
        return indexes_top_5[0]
    elif ((top == 2) and (len(indexes_top_5) > 1)):
        return indexes_top_5[1]
    elif ((top == 3) and (len(indexes_top_5) > 2)):
        return indexes_top_5[2]
    else: 
        return 'undefined'


def load_df(path):
    """
    Carga datos dado una ruta
    :param: path
    :return: dataframe
    """
    # print("load")
    # print(path)
    # df_pkl = pickle.load(open(path, "rb"))
    file_p = open(path, 'rb')
    df_pkl = pickle.load(file_p)
    file_p.close()
    
    return df_pkl

def save_df(df, path):
    """
    Gurada un dataframe en una ruta
    :param: dateframe, path
    :return: file save
    """
    #print(path)
    #pickle.dump(df, open(path, "wb"))
    file_p = open(path, 'wb')
    pickle.dump(df, file_p)
    file_p.close()