import pandas as pd
import numpy as np
import sys
import os
from os.path import dirname
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')
sys.path.append(dirname('../src'))
from src.utils import utils, processing


def create_new_features(df):
    """
    """
    # Rango de edad
    df = processing.edad_range(df)
    
    # Época nacimiento
    df = processing.epoca_nac(df)
    
    # IMC
    df["imc_calculado"] = np.nan
    df["imc_calculado"] = np.where(~pd.isna(df["peso"])&~pd.isna(df["altura"]), \
                                           (df["peso"]/(df["altura"]**2)), 
                                           np.nan)
    df = processing.imc_calculo_range(df)
    
    # Ventanas fecha_consulta: desde la primera consulta y entre consultas
    df = processing.ventana_ini_consulta(df)
    df = processing.ventana_entre_consultas(df)
    # Ventanas fecha_laboratorio: desde el primer laboratorio y entre laboratorios
    df = processing.ventana_ini_lab(df)
    
    # Existencia del primer DX DM
    df = processing.dm_unic(df)
    
    # Existencia del primer DX HTA
    df, d_dx_hta_u = processing.hta_unic(df)
    
    # Existencia del primer DX Insuficiencia Renal
    df = processing.renal_unic(df)
    
    # Ajustando rengo de valores hba1c
    df['hba1c'] = np.where((df['hba1c']<3)|(df['hba1c']>15),np.nan,df['hba1c'])
    
    # Ajustando rango de valores plaquetas
    df['plaquetas'] = np.where((df['plaquetas']<100000)|(df['plaquetas']>500000),np.nan,df['plaquetas'])
    
    # Ajustando rango de valores presion
    df['sistolica_a'] = np.where((df['sistolica']<70),np.nan,df['sistolica'])
    df['diastolica_a'] = np.where((df['diastolica']<50),np.nan,df['diastolica'])
    
    # Número de consultas
    df = df.sort_values(['cx_curp', 'fecha_consulta'], ascending=[True, True])
    df['num_consultas'] = df.groupby(['cx_curp']).cumcount()+1
    
    # MAP
    df['map'] = (df['sistolica_a'] + (2*df['diastolica_a']))/3
    
    # Variables categoricas, existencia laboratorios
    df = processing.laboratories(df)
    
    # CIE DX
    df['dm_cie_unic'] = np.where(df['dm_cie_unic']==1, 1, 0)
    df['dm_años_int'] = np.where(df['dm_años_int']<0, 0, df['dm_años_int'])
    df['dm_años_flt_ini_db_dx'] = np.where(df['dm_años_flt_ini_db_dx']<0, 0, df['dm_años_flt_ini_db_dx'])
    df['dm_años_int_ini_db_dx'] = np.where(df['dm_años_int_ini_db_dx']<0, 0, df['dm_años_int_ini_db_dx'])

    df['hta_cie_unic'] = np.where(df['hta_cie_unic']==1, 1, 0)
    df['hta_años_int'] = np.where(df['hta_años_int']<0, 0, df['hta_años_int'])
    df['hta_años_flt'] = np.where(df['hta_años_flt']<0, 0, df['hta_años_flt'])
    df['hta_años_flt_ini_db_dx'] = np.where(df['dm_años_flt_ini_db_dx']<0, 0, df['hta_años_flt_ini_db_dx'])
    df['hta_años_int_ini_db_dx'] = np.where(df['hta_años_int_ini_db_dx']<0, 0, df['hta_años_int_ini_db_dx'])

    df['renal_cie_unic'] = np.where(df['renal_cie_unic']==1, 1, 0)
    
    # TARGET -------------------------------------------------------------------------------------------------
    df_hta = df[(df['sistolica']>=140)&(df['diastolica']>=90)].\
                sort_values(by=['cx_curp','fecha_consulta'], ascending=True)\
                [['cx_curp','fecha_consulta','sistolica','diastolica']]
    
    df_hta['dup_number'] = df_hta.groupby(['cx_curp']).cumcount()+1
    df_hta = df_hta[df_hta['dup_number']==3]
    
    df_hta_comp = pd.merge(d_dx_hta_u, df_hta, on='cx_curp', how='outer')
    
    df_hta_comp['fecha_dx_hta'] = np.nan
    df_hta_comp['target'] = np.nan
    for i in range(len(df_hta_comp['cx_curp'])):
        df_hta_comp['target'][i] = 1

        if ~(isinstance(df_hta_comp['fecha_consulta_x'][i], type(pd.NaT))) & \
            (isinstance(df_hta_comp['fecha_consulta_y'][i], type(pd.NaT))):
            df_hta_comp['fecha_dx_hta'][i] = df_hta_comp['fecha_consulta_x'][i]

        elif (isinstance(df_hta_comp['fecha_consulta_x'][i], type(pd.NaT))) & \
        ~(isinstance(df_hta_comp['fecha_consulta_y'][i], type(pd.NaT))):
            df_hta_comp['fecha_dx_hta'][i] = df_hta_comp['fecha_consulta_y'][i]

        elif ~(isinstance(df_hta_comp['fecha_consulta_x'][i], type(pd.NaT))) & \
             ~(isinstance(df_hta_comp['fecha_consulta_y'][i], type(pd.NaT))):
            if(df_hta_comp['fecha_consulta_x'][i] <= df_hta_comp['fecha_consulta_y'][i]):
                df_hta_comp['fecha_dx_hta'][i] = df_hta_comp['fecha_consulta_x'][i]

            elif (df_hta_comp['fecha_consulta_x'][i] > df_hta_comp['fecha_consulta_y'][i]):
                df_hta_comp['fecha_dx_hta'][i] = df_hta_comp['fecha_consulta_y'][i]

            else:
                print(6)

        else:
            print(5)

    df_hta_comp = df_hta_comp[['cx_curp','fecha_dx_hta','target']]
    df_hta_comp.rename(columns = {'fecha_dx_hta':'fecha_consulta'}, inplace = True)
    df_hta_comp['fecha_consulta']= pd.to_datetime(df_hta_comp['fecha_consulta'])

    df = pd.merge(df, df_hta_comp, on = ["cx_curp",'fecha_consulta'], how="left")
    df.rename(columns = {'target_y':'target'}, inplace = True)
    
    df = pd.merge(df, df_hta_comp, on = ["cx_curp"], how="left")
    df.rename(columns = {'target_x':'target'}, inplace = True)
    
    # Actualiza hta seguimiento
    df['target'] = np.where((pd.isna(df['target']))&(df['fecha_consulta_x']>=df['fecha_consulta_y']),\
                            2, df['target'])
    # Calcula años con dx
    df['hta_dx_años_flt'] = np.where((~pd.isna(df['target'])),\
                             (df['fecha_consulta_x'] - df['fecha_consulta_y']) / np.timedelta64(1, 'Y'), 
                             np.nan)

    # Calcula años con dx
    df['hta_dx_años_flt'] = df['hta_dx_años_flt'].fillna(0) 
    df['hta_dx_años_int'] = df['hta_dx_años_flt'].astype('int')
    
    df.sort_values(by=['cx_curp','fecha_consulta_x'])[['cx_curp','target','fecha_consulta_x',\
                       'fecha_consulta_y','hta_dx_años_flt','hta_dx_años_int']]
    df.drop('fecha_consulta_y', inplace=True, axis=1)
    df.drop('target_y', inplace=True, axis=1)
    df.rename(columns = {'fecha_consulta_x':'fecha_consulta'}, inplace = True)
    
    return df


def cat_med_data_add(df):
    """
    """
    # Lectura de catalogo
    df_vac = pd.read_csv("../Data/med2.csv", encoding='ISO-8859-1')
    df_vac = df_vac.rename(columns={'ANTIMIGRAÃ\x91OSOS': 'ANTIMIGRANOSOS'})
    df = processing.clas_med(df,df_vac)
    
    return df
    

def gpo_med(df):
    """
    """
    df_m = pd.read_csv("../Data/CBM4.csv", encoding='ISO-8859-1')
    df_m = df_m.drop(['id','Grupo','Producto_Activo','Cve_Med.1','Cve_Med','GPO','GPO1','ESP','DIF',
                      'VAR','CUADRO_BASICO_SAI','PROGRAMA_MEDICO','Unidades', 'Medida','GRUPO'], axis=1)
    df_m = df_m.rename(columns={'g1_ANALGESICOS': 'g1','g2_ANESTESIA': 'g2'})
    df = processing.cod_medicamento(df_m,df)
    
    # Número de medicamentos
    df = proc.num_medicamentos(df)
    
    # Pegando atributos medicamentos
    df = proc.medicine_cat(df,df_m)
    
    return df
    

def feature_engineering(df, path_save):
    """
    Recibe la ruta del pickle transformado y devuelve un pickle con nuevos features 
    en una ruta epecificada
    :param: path
    :return: file
    """
    print("Inicio proceso: Feature_engineering")    
    # Crea nuevas variables
    df = create_new_features(df)
    
    # Pegando atributos medicamentos
    df = cat_med_data_add(df)
    
    # Clasificación lista mexicana
    df = processing.lista_mex_enf(df)
    
    # Grupo de medicamentos IMSS
    df = gpo_med(df)
    
    
    # Se guarda pkl
    utils.save_df(df_f, path_save)
    print("Finalizó proceso: Feature_engineering")
    
    return df_f