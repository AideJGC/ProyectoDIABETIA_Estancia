import pandas as pd
import numpy as np
import sys
import os
from os.path import dirname
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')
sys.path.append(dirname('../src'))
from src.utils import utils

def clean_pa_hba1c(df):
    """
    Recibe dataframe y limpia datos de presion arterial 
    y hemoglobina glucosilada 
    :param: dataframe
    :return: dataframe
    """
    df['presion_arterial'] =  np.where(df.hba1c.str.contains("/") & df['presion_arterial'].isnull(), \
                                       df['hba1c'],\
                                       df['presion_arterial'])

    df['hba1c'] =  np.where(df.hba1c.str.contains("/"), \
                            np.nan, \
                            df['hba1c'])
    
    df['presion_arterial'] = df['presion_arterial'].replace('NULL', np.nan, regex=True)
    df_pa = df['presion_arterial'].str.split('/', expand=True)
    df_pa.columns = ['sistolica', 'diastolica']
    df_pa['sistolica'] = df_pa['sistolica'].astype(float)
    df_pa['diastolica'] = df_pa['diastolica'].astype(float)
    df["sistolica"] = df_pa["sistolica"]
    df["diastolica"] = df_pa["diastolica"]

    return df


def split_glucosa(df):
    """
    Recibe dataframe y divide glucosa (pre/post)
    :param: dataframe
    :return: dataframe
    """
    df["glucosa"]=df["glucosa"].astype(str)
    df['glucosa'] = df['glucosa'].apply(lambda x: x if len(x) < 12 else np.nan)
    df['glucosa'] = df['glucosa'].str.replace('[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]', '')
    df_g = df['glucosa'].str.split('|', expand=True)
    df_g.columns = ['glucosa1', 'glucosa2']
    df_g['glucosa1']=df_g['glucosa1'].astype(float)
    df_g['glucosa2']=df_g['glucosa2'].astype(float)
    df["glucosa1"] = df_g["glucosa1"]
    df["glucosa2"] = df_g["glucosa2"]

    df['glucosa'] = np.where(df['glucosa']=='nan', np.nan, df['glucosa'])

    return df

def clean_data_num(df,cols):
    """
    Limpia datos de: 'colesterol','trigliceridos','hdl','ldl','hba1c',
    'plaquetas','creatinina','acido_urico','urea','peso','altura',
    'tfg','imc','año_de_diagnostico_diabetes',
    'año_de_diagnostico_hipertensión', quitando letras o caracteres
    especiales
    :param: dataframe
    :return: dataframe
    """
    for col in cols:
        df[col] = df[col].astype(str)
        df[col] = df[col].replace(',', '', regex=True)
        df[col] = df[col].replace(' ', '', regex=True)
        df[col] = df[col].replace('-', '', regex=True)
        df[col] = df[col].replace('NA', np.nan, regex=True)
        df[col] = df[col].str.replace('[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]', '')
        if (col == 'año_de_diagnostico_diabetes') or (col == 'año_de_diagnostico_hipertensión'):
            df[col] = df[col].astype(np.float).astype("Int32")
            for i in range(len(df[col])):
                x = df[col][i]
                if pd.isna(x):
                    x=x
                else:
                    if(x > 2022):
                        df[col][i] = np.nan 
            df[col]=df[col].map(lambda x: pd.NA if pd.isna(x) else int(x))
        elif col == 'tfg':
            for i in range(len(df[col])):
                x = df[col][i]
                if(x.count(".")>1):
                    df[col][i] = df[col][i][:5]
            df[col] = df[col].astype(float)
        elif col == 'imc':
            for i in range(len(df[col])):
                x = df[col][i]
                if(x.count(".")>1):
                    df[col][i] = df[col][i][:5]
            df[col] = df[col].astype(float)
        else:
            df[col] = df[col].astype(float)
            
    return df


def transform(df ,path_save):
    """
    Recibe la ruta del pickle que hay que transformar y devuelve en una ruta los datos transformados en pickle.
    :param: path
    :return: file
    """
    print("Inicio proceso: Transformación y limpieza")    
    # Limpieza de datos
    df = clean_pa_hba1c(df)
    # Dividiendo datos de glucosa
    df = split_glucosa(df)
    # Limpieza de datos númericos
    df = clean_data_num(df,['colesterol','trigliceridos','hdl','ldl','hba1c',
                            'plaquetas','creatinina','acido_urico','urea','peso',
                            'altura','tfg','imc','año_de_diagnostico_diabetes',
                            'año_de_diagnostico_hipertensión'])
    # Limpieza de fechas de laboratorios

    
    # Se guarda pkl
    u.save_df(df, path_save)
    print("Archivo 'pkl_transform.pkl' escrito correctamente")   
    
    print("Finalizó proceso:  Transformación y limpieza")
    
    return df