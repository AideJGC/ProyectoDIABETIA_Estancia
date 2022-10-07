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
    """    
    
    #today = datetime.date.today()
    #year = today.year
    
    today = datetime.now()
    year = today.year
    
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
                    if(x > year):
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

def clean_data_dates(df):
    
    #today = datetime.date.today()
    #year = today.year
    
    today = datetime.now()
    year = today.year
    
    df['fecha_laboratorio'] = df['fechas_procesadas'].astype(str)
    df['fecha_laboratorio'] = df['fecha_laboratorio'].apply(lambda x: x.strip())
    df['fecha_laboratorio'] = np.where(df.fecha_laboratorio.str.len() > 50, \
                                        "20"+df['fecha_laboratorio'].astype(str).str[6:8]+"-"+
                                             df['fecha_laboratorio'].astype(str).str[3:5]+"-"+
                                             df['fecha_laboratorio'].astype(str).str[0:2],\
                                             df['fecha_laboratorio'])
    df['fecha_laboratorio'] = df['fecha_laboratorio'].replace(' DE ', '/', regex=True)
    df['fecha_laboratorio'] = df['fecha_laboratorio'].replace(' DEL ', '/', regex=True)
    
    df['fecha_laboratorio'] = df['fecha_laboratorio'].astype(str)
    for i in range(len(df['fecha_laboratorio'])):
        x = df['fecha_laboratorio'][i]
        if ('GLUCOSA' in x) & (x.find('GLUCOSA') != -1) & (pd.isna(df['glucosa'][i])):
            y = "20"+x[6:8]+"-"+x[3:5]+"-"+x[0:2]
            #df['fecha_laboratorio'][i] = datetime.strptime(y, '%Y-%m-%d') 
            df['fecha_laboratorio'][i] = datetime.strptime(y, '%Y-%m-%d') 
            df['glucosa1'][i] = x[17:len(x)]

    df['fecha_laboratorio'] = df['fecha_laboratorio'].astype(str)
    df['fecha_laboratorio'] = df['fecha_laboratorio'].\
                          replace('/ENERO/', '/01/', regex=True).\
                          replace('/FEBRERO/', '/02/', regex=True).\
                          replace('/MARZO/', '/03/', regex=True).\
                          replace('/ABRIL/', '/04/', regex=True).\
                          replace('/MAYO/', '/05/', regex=True).\
                          replace('/JUNIO/', '/06/', regex=True).\
                          replace('/JULIO/', '/07/', regex=True).\
                          replace('/AGOSTO/', '/08/', regex=True).\
                          replace('/SEPTIEMBRE/', '/09/', regex=True).\
                          replace('/OCTUBRE/', '/10/', regex=True).\
                          replace('/NOVIEMBRE/', '/11/', regex=True).\
                          replace('/DICIEMBRE/', '/12/', regex=True).\
                          replace('DE', ' ', regex=True).\
                          replace('D E', ' ', regex=True).\
                          replace('  ', ' ', regex=True).\
                          replace('/ENERO ', '/01/', regex=True).\
                          replace('/FEBRERO ', '/02/', regex=True).\
                          replace('/MARZO ', '/03/', regex=True).\
                          replace('/ABRIL ', '/04/', regex=True).\
                          replace('/MAYO ', '/05/', regex=True).\
                          replace('/JUNIO ', '/06/', regex=True).\
                          replace('/JULIO ', '/07/', regex=True).\
                          replace('/AGOSTO ', '/08/', regex=True).\
                          replace('/SEPTIEMBRE ', '/09/', regex=True).\
                          replace('/OCTUBRE ', '/10/', regex=True).\
                          replace('/NOVIEMBRE ', '/11/', regex=True).\
                          replace('/DICIEMBRE ', '/12/', regex=True).\
                          replace(' ENERO/', '/01/', regex=True).\
                          replace(' FEBRERO/', '/02/', regex=True).\
                          replace(' MARZO/', '/03/', regex=True).\
                          replace(' ABRIL/', '/04/', regex=True).\
                          replace(' MAYO/', '/05/', regex=True).\
                          replace(' JUNIO/', '/06/', regex=True).\
                          replace(' JULIO/', '/07/', regex=True).\
                          replace(' AGOSTO/', '/08/', regex=True).\
                          replace(' SEPTIEMBRE/', '/09/', regex=True).\
                          replace(' OCTUBRE/', '/10/', regex=True).\
                          replace(' NOVIEMBRE/', '/11/', regex=True).\
                          replace(' DICIEMBRE/', '/12/', regex=True).\
                          replace(' ENERO ', '/01/', regex=True).\
                          replace(' FEBRERO ', '/02/', regex=True).\
                          replace(' MARZO ', '/03/', regex=True).\
                          replace(' ABRIL ', '/04/', regex=True).\
                          replace(' MAYO ', '/05/', regex=True).\
                          replace(' JUNIO ', '/06/', regex=True).\
                          replace(' JULIO ', '/07/', regex=True).\
                          replace(' AGOSTO ', '/08/', regex=True).\
                          replace(' SEPTIEMBRE ', '/09/', regex=True).\
                          replace(' OCTUBRE ', '/10/', regex=True).\
                          replace(' NOVIEMBRE ', '/11/', regex=True).\
                          replace(' DICIEMBRE ', '/12/', regex=True).\
                          replace('/ENE/', '/01/', regex=True).\
                          replace('/FEB/', '/02/', regex=True).\
                          replace('/MAR/', '/03/', regex=True).\
                          replace('/ABR/', '/04/', regex=True).\
                          replace('/MAY/', '/05/', regex=True).\
                          replace('/JUN/', '/06/', regex=True).\
                          replace('/JUL/', '/07/', regex=True).\
                          replace('/AGO/', '/08/', regex=True).\
                          replace('/SEP/', '/09/', regex=True).\
                          replace('/OCT/', '/10/', regex=True).\
                          replace('/NOV/', '/11/', regex=True).\
                          replace('/DIC/', '/12/', regex=True).\
                          replace(' ENE ', '/01/', regex=True).\
                          replace(' FEB ', '/02/', regex=True).\
                          replace(' MAR ', '/03/', regex=True).\
                          replace(' ABR ', '/04/', regex=True).\
                          replace(' MAY ', '/05/', regex=True).\
                          replace(' JUN ', '/06/', regex=True).\
                          replace(' JUL ', '/07/', regex=True).\
                          replace(' AGO ', '/08/', regex=True).\
                          replace(' SEP ', '/09/', regex=True).\
                          replace(' SEPT ', '/09/', regex=True).\
                          replace(' OCT ', '/10/', regex=True).\
                          replace(' NOV ', '/11/', regex=True).\
                          replace(' DIC ', '/12/', regex=True).\
                          replace('-', '', regex=True).\
                          replace('\.', '/', regex=True).\
                          replace(',', '/', regex=True).\
                          replace('//', '/', regex=True).\
                          replace(' ', '/', regex=True).\
                          replace('//', '/', regex=True).\
                          replace('/ENE/', '/01/', regex=True).\
                          replace('/FEB/', '/02/', regex=True).\
                          replace('/MAR/', '/03/', regex=True).\
                          replace('/ABR/', '/04/', regex=True).\
                          replace('/MAY/', '/05/', regex=True).\
                          replace('/JUN/', '/06/', regex=True).\
                          replace('/JUL/', '/07/', regex=True).\
                          replace('/AGO/', '/08/', regex=True).\
                          replace('/SEP/', '/09/', regex=True).\
                          replace('/OCT/', '/10/', regex=True).\
                          replace('/NOV/', '/11/', regex=True).\
                          replace('/DIC/', '/12/', regex=True).\
                          replace('//', '/', regex=True).\
                          replace('/SEPT/', '/09/', regex=True).\
                          replace('/JUNIO2', '/06/2', regex=True).\
                          replace('/JULIO2', '/07/2', regex=True).\
                          replace('/SPTIEMBRE/', '/09/', regex=True).\
                          replace('/MAYOP/', '/05/', regex=True).\
                          replace('/EENRO/', '/01/', regex=True).\
                          replace('/D/', '/', regex=True).\
                          replace('/DLE/', '/', regex=True).\
                          replace('/DLE', '/', regex=True).\
                          replace('/AGOST/O/L/', '/08/', regex=True).\
                          replace('/NOV2', '/11/2', regex=True).\
                          replace('/20017', '/2017', regex=True).\
                          replace('/0/1/2', '/01/2', regex=True).\
                          replace('/0/7/2', '/07/2', regex=True).\
                          replace('/08/820', '/08/20', regex=True)
    
    df['fecha_laboratorio'] = df['fecha_laboratorio'].astype(str)
    for i in range(len(df['fecha_laboratorio'])):
        x = df['fecha_laboratorio'][i]
        if ((~x[0].isdigit()) & (x != 'nan') & (x != 'NAN')):
            df['fecha_laboratorio'][i] = np.nan

    df['fecha_laboratorio'] = df['fecha_laboratorio'].astype(str)
    df['fecha_laboratorio'] = df['fecha_laboratorio'].apply(lambda x: x.strip())
    for i in range(len(df['fecha_laboratorio'])):
        x = df['fecha_laboratorio'][i]
        if ((x.isdigit()) & (len(x)==8)):
            if ((int(x[4:9]) < year) & (int(x[4:9]) > 1990)):
                df['fecha_laboratorio'][i] = x[0:2] + '/' + x[4:6] + '/' + x[4:9]

            elif ((int(x[0:4]) < year) & (int(x[0:4]) > 1990)):
                df['fecha_laboratorio'][i] = x[6:9] + '/' + x[4:6] + '/' + x[0:4]
    
    for i in range(len(df['fecha_laboratorio'])):
        x = df['fecha_laboratorio'][i]
        if (x == 'NAN' or x == 'nan'):
            df['fecha_laboratorio'][i] = np.nan
            
    df['fecha_laboratorio'] = df['fecha_laboratorio'].astype(str)
    for i in range(len(df['fecha_laboratorio'])):
        x = df['fecha_laboratorio'][i]
        if (x.find('/00:00:00') == -1) & (len(x) > 10): 
            if((x[0:2].isdigit()) & (x[2:3] == '/') & (x[3:5].isdigit()) & (x[5:6] == '/') & 
               (x[6:10].isdigit())):
                if (int(x[6:10]) < year) & (int(x[6:10]) > 1990):
                    df['fecha_laboratorio'][i] = x[0:2] + x[2:3] + x[3:5] + x[5:6] + x[6:10]
                    
    df['fecha_laboratorio'] = df['fecha_laboratorio'].astype(str)
    for i in range(len(df['fecha_laboratorio'])):
        x = df['fecha_laboratorio'][i]
        if (x.find('/00:00:00') == -1) & (len(x) > 10): 
            df['fecha_laboratorio'][i] = np.nan
            
    df['fecha_laboratorio'] = df['fecha_laboratorio'].astype(str)
    for i in range(len(df['fecha_laboratorio'])):
        x = df['fecha_laboratorio'][i]
        if ((len(x) < 6) & (x != 'nan') & (x != 'NAN')):
            df['fecha_laboratorio'][i] = np.nan
            
    df['fecha_laboratorio'] = df['fecha_laboratorio'].astype(str)
    for i in range(len(df['fecha_laboratorio'])):
        x = df['fecha_laboratorio'][i]
        try:
            df['fecha_laboratorio'][i] = pd.to_datetime(x)
        except ValueError:
            df['fecha_laboratorio'][i] = pd.to_datetime(np.nan)
            pass    
    
    return df


def creation_vars(df):
    
    # Edad
    df['edad'] = np.nan
    for i in range(len(df['newid'])): 
        if pd.isna(df['fecha_nacimiento'][i]):
            df['edad'][i] = np.nan        
        else: 
            df['edad'][i] = int(df['fecha_consulta'][i].year-\
                                df['fecha_nacimiento'][i].year)
            
    # HTA
    df['hta'] = np.nan
    for i in range(len(df['newid'])):
        x = df['hipertension'][i]
        #print(x)
        if pd.isna(x):
            df['hta'][i] = '0'
        elif ('HIPER' in x) or ('HTA' in x) or ('HAS' in x) or ('ARTERIAL' in x):
            df['hta'][i] = '1'
        else:
            df['hta'][i] = '0'
    df['hta'] = df['hta'].astype('category')  
    
    # DM
    df['dm_cie'] = np.nan
    for i in range(len(df['newid'])):
        x = df['codigos_cie'][i]
        #print(x)
        if pd.isna(x):
            df['dm_cie'][i] = '0'
        elif ('E10' in x) or ('E11' in x) or ('E12' in x) or ('E13' in x) or ('E14' in x):
            df['dm_cie'][i] = '1'
        else:
            df['dm_cie'][i] = '0'
    df['dm_cie'] = df['dm_cie'].astype('category')
    
    # HTA CIE
    df['hta_cie'] = np.nan
    for i in range(len(df['newid'])):
        x = df['codigos_cie'][i]
        if pd.isna(x):
            df['hta_cie'][i] = '0'
        elif ('I10' in x) or ('I11' in x) or ('I12' in x) or ('I13' in x) or ('I15' in x):
            df['hta_cie'][i] = '1'
        else:
            df['hta_cie'][i] = '0'
    df['hta_cie'] = df['hta_cie'].astype('category') 
    
    # RENAL
    df['renal_cie'] = np.nan
    for i in range(len(df['newid'])):
        x = df['codigos_cie'][i]
        if pd.isna(x):
            df['renal_cie'][i] = '0'
        elif ('N17' in x) or ('N19' in x):
            df['renal_cie'][i] = '1'
        else:
            df['renal_cie'][i] = '0'
    df['renal_cie'] = df['renal_cie'].astype('category') 
    
    return df


def uniq_lab(df, column_names, column):
    """    
    """
    # uniq values
    df_column = df[(~pd.isna(df[column])) & (~pd.isna(df['fecha_laboratorio'])) & (df['fuente'] == 'NER')]\
    [column_names]
    df_column = df_column.drop_duplicates()
    df_column['n_lab'] = column
    
    # duplicated values same date
    prop_codigo = df_column.groupby(['cx_curp','fecha_laboratorio'], as_index=False)['n_lab']\
    .count()\
    .rename(columns={'n_lab': 'count'})
    prop_codigo['prop'] = prop_codigo['count']/np.sum(prop_codigo['count'])
    df_rep = prop_codigo.sort_values(by = ['prop'], ascending = False)
    df_rep = df_rep[df_rep['count']>1]
    
    column_names.append('n_lab')
    
    # delete dupliacted values in same date
    df_merged = df_column.merge(df_rep, how="left", left_on=["cx_curp","fecha_laboratorio"],\
                             right_on=["cx_curp","fecha_laboratorio"], indicator=True)
    df_merged = df_merged.query("_merge == 'left_only'")[column_names]
    
    # comprobando
    prop_codigo = df_merged.groupby(['cx_curp','fecha_laboratorio'], as_index=False)['n_lab']\
    .count()\
    .rename(columns={'n_lab': 'count'})
    prop_codigo['prop'] = prop_codigo['count']/np.sum(prop_codigo['count'])
    df_rep2 = prop_codigo.sort_values(by = ['prop'], ascending = False)
    gd2 = df_rep2[df_rep2['count']>1]
    
    return df_merged    

def unir_lab(df1,df2):
    """
    """
    df_u = pd.merge(df1,df2, on = ['cx_curp','fecha_laboratorio'])
    df_lab = pd.merge(df1,df2, how = "outer", on = ['cx_curp','fecha_laboratorio']).\
                drop_duplicates()
    df_lab = df_lab[df_lab.columns.drop(list(df_lab.filter(regex='n_lab')))]
    
    return df_lab


def unique_labs(df):
    """
    """
    df_glucosa = uniq_lab(df.copy(),['cx_curp','glucosa','glucosa1','glucosa2','fecha_laboratorio'],'glucosa')
    df_colesterol = uniq_lab(df.copy(),['cx_curp','colesterol','fecha_laboratorio'],'colesterol')
    df_lab = unir_lab(df_glucosa,df_colesterol)
    df_trigliceridos = uniq_lab(df.copy(),['cx_curp','trigliceridos','fecha_laboratorio'],'trigliceridos')
    df_lab = unir_lab(df_lab,df_trigliceridos)
    df_hdl = uniq_lab(df.copy(),['cx_curp','hdl','fecha_laboratorio'],'hdl')
    df_lab = unir_lab(df_lab,df_hdl)
    df_ldl = uniq_lab(df.copy(),['cx_curp','ldl','fecha_laboratorio'],'ldl')
    df_lab = unir_lab(df_lab,df_ldl)
    df_presion = uniq_lab(df.copy(),['cx_curp','presion_arterial','sistolica','diastolica','fecha_laboratorio'],'presion_arterial')
    df_lab = unir_lab(df_lab,df_presion)
    df_hba1c = uniq_lab(df.copy(),['cx_curp','hba1c','fecha_laboratorio'],'hba1c')
    df_lab = unir_lab(df_lab,df_hba1c)
    df_plaquetas = uniq_lab(df.copy(),['cx_curp','plaquetas','fecha_laboratorio'],'plaquetas')
    df_lab = unir_lab(df_lab,df_plaquetas)
    df_creatinina = uniq_lab(df.copy(),['cx_curp','creatinina','fecha_laboratorio'],'creatinina')
    df_lab = unir_lab(df_lab,df_creatinina)
    df_acido_u = uniq_lab(df.copy(),['cx_curp','acido_urico','fecha_laboratorio'],'acido_urico')
    df_lab = unir_lab(df_lab,df_acido_u)
    df_urea = uniq_lab(df.copy(),['cx_curp','urea','fecha_laboratorio'],'urea')
    df_lab = unir_lab(df_lab,df_urea)
    df_peso = uniq_lab(df.copy(),['cx_curp','peso','fecha_laboratorio'],'peso')
    df_lab = unir_lab(df_lab,df_peso)
    df_altura = uniq_lab(df.copy(),['cx_curp','altura','fecha_laboratorio'],'altura')
    df_lab = unir_lab(df_lab,df_altura)
    df_tfg = uniq_lab(df.copy(),['cx_curp','tfg','fecha_laboratorio'],'tfg')
    df_lab = unir_lab(df_lab,df_tfg)
    df_imc = uniq_lab(df.copy(),['cx_curp','imc','fecha_laboratorio'],'imc')
    df_lab = unir_lab(df_lab,df_imc)
    
    # Eliminando filas sin datos
    df_lab[((df_lab['glucosa']=='nan') | pd.isna(df_lab['glucosa'])) & pd.isna(df_lab['glucosa1']) & \
       pd.isna(df_lab['glucosa2']) & pd.isna(df_lab['colesterol']) & pd.isna(df_lab['trigliceridos']) & \
       pd.isna(df_lab['hdl']) & pd.isna(df_lab['ldl']) & pd.isna(df_lab['sistolica']) & \
       pd.isna(df_lab['diastolica']) & pd.isna(df_lab['hba1c']) & pd.isna(df_lab['plaquetas']) & \
       pd.isna(df_lab['creatinina']) & pd.isna(df_lab['acido_urico']) & pd.isna(df_lab['urea']) & \
       pd.isna(df_lab['peso']) & pd.isna(df_lab['altura']) & pd.isna(df_lab['tfg']) & pd.isna(df_lab['imc'])]

    indexes = df_lab[((df_lab['glucosa']=='nan') | (pd.isna(df_lab['glucosa']))) & \
                                (pd.isna(df_lab['glucosa1'])) & (pd.isna(df_lab['glucosa2'])) & \
                                (pd.isna(df_lab['colesterol'])) & (pd.isna(df_lab['trigliceridos'])) & \
                                (pd.isna(df_lab['hdl'])) & (pd.isna(df_lab['ldl'])) & (pd.isna(df_lab['sistolica'])) & \
                                (pd.isna(df_lab['diastolica'])) & (pd.isna(df_lab['hba1c'])) & \
                                (pd.isna(df_lab['plaquetas'])) & (pd.isna(df_lab['creatinina'])) & \
                                (pd.isna(df_lab['acido_urico'])) & (pd.isna(df_lab['urea'])) & \
                                (pd.isna(df_lab['peso'])) & (pd.isna(df_lab['altura'])) & (pd.isna(df_lab['tfg'])) & \
                                (pd.isna(df_lab['imc']))].index

    df_lab.drop(indexes,inplace=True)
    
    return df_lab


def uniq_pac(df):
    """
    """
    df_exp = df[df['fuente'] != 'NER']
    prop_codigo = df_exp.groupby(['cx_curp','fecha_consulta'], as_index=False)['newid']\
    .count()\
    .rename(columns={'newid': 'count'})
    prop_codigo['prop'] = prop_codigo['count']/np.sum(prop_codigo['count'])
    df_rep = prop_codigo.sort_values(by = ['prop'], ascending = False)
    df_rep = df_rep[df_rep['count']>1]
    
    # Reemplazando 0 por NaN en valores de laboratorio
    cols = ['glucosa', 'colesterol', 'trigliceridos', 'hdl', 'ldl', 'presion_arterial', 'hba1c', 'plaquetas',
        'creatinina', 'acido_urico', 'urea', 'peso', 'altura', 'tfg', 'imc', 'glucosa1', 'glucosa2',
        'sistolica', 'diastolica']
    df_exp[cols] = df_exp[cols].replace({'0':np.nan, 0:np.nan})
    
    # Eliminando duplicados
    df_exp = df_exp.drop_duplicates()
    
    
    return df_exp


def transform(df, path_save):
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
    df = clean_data_dates(df)
    
    # Limpiando CIE-10
    df['codigos_cie'] = df['codigos_cie'].replace(' ', '', regex=True)
    
    # Normalizando nombre de columnas
    df = utils.clean_column(df)
    
    # Cambio de tipo de datos
    df['sexo'] = df['sexo'].astype('category')
    df['fecha_consulta']= pd.to_datetime(df['fecha_consulta'])
    df['fecha_nacimiento']= pd.to_datetime(df['fecha_nacimiento'])
    
    # Creación de variables
    df = creation_vars(df)
    
    # Únicos laboratorios
    df_lab = unique_labs(df)
    
    # Pacientes únicos por fuente
    df_exp = uniq_pac(df)
    

    # Se guarda pkl
    utils.save_df(df, path_save)
    print("Finalizó proceso:  Transformación y limpieza")
    
    return df