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
    df['fecha_laboratorio']= pd.to_datetime(df['fecha_laboratorio'])
    #display(df.info())
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
    
    prop_codigo = df_exp.groupby(['cx_curp','fecha_consulta'], as_index=False)['newid']\
    .count()\
    .rename(columns={'newid': 'count'})
    prop_codigo['prop'] = prop_codigo['count']/np.sum(prop_codigo['count'])
    df_rep_exp = prop_codigo.sort_values(by = ['prop'], ascending = False)
    df_rep_exp = df_rep_exp[df_rep_exp['count']>1]
    
    df_u_exp = pd.merge(df_exp,df_rep_exp, on = ['cx_curp','fecha_consulta'])
    
    df_ug = df_u_exp[~pd.isna(df_u_exp['glucosa'])]
    
    prop_codigo = df_ug.groupby(['cx_curp','fecha_consulta'], as_index=False)['newid']\
    .count()\
    .rename(columns={'newid': 'count'})
    prop_codigo['prop'] = prop_codigo['count']/np.sum(prop_codigo['count'])
    df_rep_val0 = prop_codigo.sort_values(by = ['prop'], ascending = False)
    df_rep_val0 = df_rep_val0[df_rep_val0['count']>1]
    
    #prop_codigo = df_u_exp.groupby(['fuente'], as_index=False)['newid']\
    #.count()\
    #.rename(columns={'newid': 'count'})
    #prop_codigo['prop'] = prop_codigo['count']/np.sum(prop_codigo['count'])
    #prop_codigo.sort_values(by = ['prop'], ascending = False)
    
    # Colapse information
    df_collapse = df_u_exp.groupby(['cx_curp','fecha_consulta']).first().reset_index()
    df_collapse["fuente"] = "corhis_somatometria/exphis_hc_diabetes"
    prop_codigo = df_collapse.groupby(['fuente'], as_index=False)['newid']\
    .count()\
    .rename(columns={'newid': 'count'})
    prop_codigo['prop'] = prop_codigo['count']/np.sum(prop_codigo['count'])
    #prop_codigo.sort_values(by = ['prop'], ascending = False)
    
    prop_codigo = df_exp.groupby(['cx_curp','fecha_consulta'], as_index=False)['newid']\
    .count()\
    .rename(columns={'newid': 'count'})
    prop_codigo['prop'] = prop_codigo['count']/np.sum(prop_codigo['count'])
    df_unic_exp = prop_codigo.sort_values(by = ['prop'], ascending = False)
    df_unic_exp = df_unic_exp[df_unic_exp['count']==1]
    #df_unic_exp

    df_u1_exp = pd.merge(df_exp,df_unic_exp, on = ['cx_curp','fecha_consulta'])
    #df_u1_exp
    
    # Uniendo datos consulta unicos y collapsados
    df_exp_his_u = pd.concat([df_u1_exp, df_collapse])
    
    return df_exp_his_u


def processing_union_cons_lab(df_p):
    """
    """
    # Count repeat
    df_p['occurance_counter'] = df_p.groupby(['cx_curp','fecha_laboratorio_y'])['fecha_laboratorio_y'].\
                                         cumcount().add(1)
    # Dejando unicos laboratorios
    df_p['fecha_laboratorio_y'] = np.where((df_p['occurance_counter'] > 1) & \
                                       (df_p['fecha_laboratorio_y'] != np.datetime64('NaT')), \
                                       np.datetime64('NaT'), 
                                       df_p['fecha_laboratorio_y'])
    
    # Limpiando merge incorrect
    df_p['index_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['index_y'])
    df_p['glucosa_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['glucosa_y'])
    df_p['glucosa1_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['glucosa1_y'])
    df_p['glucosa2_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['glucosa2_y'])
    df_p['colesterol_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['colesterol_y'])
    df_p['trigliceridos_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['trigliceridos_y'])
    df_p['hdl_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['hdl_y'])
    df_p['ldl_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['ldl_y'])
    df_p['presion_arterial_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['presion_arterial_y'])
    df_p['sistolica_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['sistolica_y'])
    df_p['diastolica_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['diastolica_y'])
    df_p['hba1c_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['hba1c_y'])
    df_p['plaquetas_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['plaquetas_y'])
    df_p['creatinina_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['creatinina_y'])
    df_p['acido_urico_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['acido_urico_y'])
    df_p['urea_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['urea_y'])
    df_p['peso_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['peso_y'])
    df_p['altura_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['altura_y'])
    df_p['tfg_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['tfg_y'])
    df_p['imc_y'] = np.where(pd.isna(df_p['fecha_laboratorio_y']), np.nan, df_p['imc_y'])
    
    df_p.reset_index(inplace = True)
    
    # Dejando daos de laboratorios en consulta
    for i in range(len(df_p['newid'])):     
    
        if ~(pd.isna(df_p['fecha_laboratorio_y'][i])):          

            if (((pd.isna(df_p['glucosa_x'][i])) or (df_p['glucosa_x'][i] == 'nan'))) and ~(pd.isna(df_p['glucosa_y'][i])):        
                df_p['glucosa_x'][i] = df_p['glucosa_y'][i]      
                df_p['glucosa1_x'][i] = df_p['glucosa1_y'][i]      
                df_p['glucosa2_x'][i] = df_p['glucosa2_y'][i]

            if (pd.isna(df_p['colesterol_x'][i])) and ~(pd.isna(df_p['colesterol_y'][i])):        
                df_p['colesterol_x'][i] = df_p['colesterol_y'][i]

            if (pd.isna(df_p['trigliceridos_x'][i])) and ~(pd.isna(df_p['trigliceridos_y'][i])):        
                df_p['trigliceridos_x'][i] = df_p['trigliceridos_y'][i]
            if (pd.isna(df_p['hdl_x'][i])) and ~(pd.isna(df_p['hdl_y'][i])):        
                df_p['hdl_x'][i] = df_p['hdl_y'][i]
            if (pd.isna(df_p['ldl_x'][i])) and ~(pd.isna(df_p['ldl_y'][i])):        
                df_p['ldl_x'][i] = df_p['ldl_y'][i]
            if (pd.isna(df_p['presion_arterial_x'][i])) and ~(pd.isna(df_p['presion_arterial_y'][i])): 
                df_p['presion_arterial_x'][i] = df_p['presion_arterial_y'][i]
                df_p['sistolica_x'][i] = df_p['sistolica_y'][i]
                df_p['diastolica_x'][i] = df_p['diastolica_y'][i]
            if (pd.isna(df_p['hba1c_x'][i])) and ~(pd.isna(df_p['hba1c_y'][i])):        
                df_p['hba1c_x'][i] = df_p['hba1c_y'][i]
            if (pd.isna(df_p['plaquetas_x'][i])) and ~(pd.isna(df_p['plaquetas_y'][i])):        
                df_p['plaquetas_x'][i] = df_p['plaquetas_y'][i]
            if (pd.isna(df_p['creatinina_x'][i])) and ~(pd.isna(df_p['creatinina_y'][i])):        
                df_p['creatinina_x'][i] = df_p['creatinina_y'][i]
            if (pd.isna(df_p['acido_urico_x'][i])) and ~(pd.isna(df_p['acido_urico_y'][i])):        
                df_p['acido_urico_x'][i] = df_p['acido_urico_y'][i]
            if (pd.isna(df_p['urea_x'][i])) and ~(pd.isna(df_p['urea_y'][i])):        
                df_p['urea_x'][i] = df_p['urea_y'][i]
            if (pd.isna(df_p['peso_x'][i])) and ~(pd.isna(df_p['peso_y'][i])):        
                df_p['peso_x'][i] = df_p['peso_y'][i]
            if (pd.isna(df_p['altura_x'][i])) and ~(pd.isna(df_p['altura_y'][i])):        
                df_p['altura_x'][i] = df_p['altura_y'][i]
            if (pd.isna(df_p['tfg_x'][i])) and ~(pd.isna(df_p['tfg_y'][i])):        
                df_p['tfg_x'][i] = df_p['tfg_y'][i]
            if (pd.isna(df_p['imc_x'][i])) and ~(pd.isna(df_p['imc_y'][i])):        
                df_p['imc_x'][i] = df_p['imc_y'][i]
            
    # ELIMINANDO COLUMNASNO NECESARIAS
    df_p.drop(columns=['index_x', 'index_y', 'glucosa_y', 'glucosa1_y', 'glucosa2_y', 'fecha_laboratorio_x', 
                       'colesterol_y', 'trigliceridos_y', 'hdl_y', 'ldl_y', 'presion_arterial_y', 
                       'sistolica_y', 'diastolica_y', 'hba1c_y', 'plaquetas_y', 'creatinina_y', 'acido_urico_y', 
                       'urea_y', 'peso_y', 'altura_y', 'tfg_y', 'imc_y', 
                       'index','count','prop'], axis=1, inplace=True)
    # RENOMBRANDOCOLUMNAS RESULTADO DE MERGE
    df_p.rename(columns = {'fecha_laboratorio_y':'fecha_laboratorio', 'glucosa_x':'glucosa', 'glucosa1_x':'glucosa1',\
                         'glucosa2_x':'glucosa2', 'colesterol_x':'colesterol', 'trigliceridos_x':'trigliceridos',\
                         'hdl_x':'hdl', 'ldl_x':'ldl', 'presion_arterial_x':'presion_arterial',\
                         'sistolica_x':'sistolica', 'diastolica_x':'diastolica', 'hba1c_x':'hba1c', \
                         'plaquetas_x':'plaquetas', 'creatinina_x':'creatinina', 'acido_urico_x':'acido_urico', \
                         'urea_x':'urea', 'peso_x':'peso', 'altura_x':'altura', 'tfg_x':'tfg', 'imc_x':'imc', \
                         'in_consulta_x':'in_consulta'}, inplace = True)

    return df_p    


def union_pac_lab(df_exp_his_u, df_lab):
    """
    """
    df_exp_his_u = df_exp_his_u.sort_values(['cx_curp','fecha_consulta']).reset_index()
    df_lab = df_lab.sort_values(['cx_curp','fecha_laboratorio']).reset_index()
    
    # Diferencia entre laboratorios
    df_lab["dif_date_lab"] = np.nan
    grp = df_lab.groupby('cx_curp')['fecha_laboratorio']
    #display(grp)
    for i, group in grp:  
        df_lab["dif_date_lab"][df_lab.index.isin(group.index)] = group.sub(group.iloc[0])

    #df_lab['dif_date_lab_from_ini'] = df_lab['dif_date_lab'].dt.days.abs()   
    #df_lab["dif_date_lab"] = df_lab.groupby(["cx_curp"])["fecha_laboratorio"].diff().dt.days
    
    # Ordenando
    df_exp_his_u = df_exp_his_u.sort_values(['fecha_consulta'])
    df_lab = df_lab.sort_values(['fecha_laboratorio'])
    
    # Unión de datos cosulta - laboratorio
    df_f = pd.merge_asof(df_exp_his_u, df_lab,\
                     left_on='fecha_consulta',\
                     right_on='fecha_laboratorio',\
                     by='cx_curp', \
                     tolerance=pd.Timedelta(days=60),\
                     direction = 'backward')
    
    df_f = processing_union_cons_lab(df_f)    
    
    return df_f


def paste_dm_hta(df_f, df):
    """
    """
    df_a = df[~pd.isna(df['año_de_diagnostico_diabetes'])][['cx_curp','fecha_consulta','año_de_diagnostico_diabetes']].\
              sort_values(['cx_curp','fecha_consulta'])
    
    df_b = df[~pd.isna(df['año_de_diagnostico_hipertension'])][['cx_curp','fecha_consulta','año_de_diagnostico_hipertension']].\
              sort_values(['cx_curp','fecha_consulta'])

    a_dx_dm = df.groupby('cx_curp').agg({'año_de_diagnostico_diabetes': ['min']})
    a_dx_dm = a_dx_dm.reset_index()
    a_dx_dm.columns = ['cx_curp', 'año_dx_dm']
    a_dx_dm = a_dx_dm[~pd.isna(a_dx_dm['año_dx_dm'])][['cx_curp', 'año_dx_dm']]
    a_dx_dm["año_dx_dm"] = a_dx_dm["año_dx_dm"].astype(int)
    #a_dx_dm
    
    a_dx_hta = df.groupby('cx_curp').agg({'año_de_diagnostico_hipertension': ['min']})
    a_dx_hta = a_dx_hta.reset_index()
    a_dx_hta.columns = ['cx_curp', 'año_dx_hta']
    a_dx_hta = a_dx_hta[~pd.isna(a_dx_hta['año_dx_hta'])][['cx_curp', 'año_dx_hta']]
    a_dx_hta["año_dx_hta"] = a_dx_hta["año_dx_hta"].astype(int)
    #a_dx_hta
    
    df_f = pd.merge(df_f, a_dx_dm, on = "cx_curp", how="left")
    df_f = pd.merge(df_f, a_dx_hta, on = "cx_curp", how="left")
    
    df_f['year_consulta'] = pd.DatetimeIndex(df_f['fecha_consulta']).year
    
    df_f['año_dx_dm'] = np.where((~pd.isna(df_f['año_dx_dm'])&(df_f['año_dx_dm']>df_f['year_consulta'])), \
                                  np.nan, 
                                  df_f['año_dx_dm'])
    df_f['año_dx_hta'] = np.where((~pd.isna(df_f['año_dx_hta'])&(df_f['año_dx_hta']>df_f['year_consulta'])), \
                                   np.nan, 
                                   df_f['año_dx_hta'])
    df_f.drop(['nota_medica', 'fecha', 'hipertension', 'año_de_diagnostico_diabetes', \
               'año_de_diagnostico_hipertension','fechas_procesadas','bandera_fechas_procesadas'], axis=1, inplace=True)
        
    return df_f


def paste_dx_hta_med(df_f):
    """
    """
    df_h = pd.read_csv("../../data/NewHypertensionList.csv")
    df_h = df_h[['cx_curp','FechaNuevaHipertension']]
    df_f = pd.merge(df_f, df_h, on = ["cx_curp"], how="left")
    df_f['FechaNuevaHipertension']= pd.to_datetime(df_f['FechaNuevaHipertension'])
    
    return df_f

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
    
    # Uniendo pacientes únicos a laboratorios
    df_f = union_pac_lab(df_exp, df_lab)
    #display(df_union)
    
    # Años DM y HTA
    df_f = paste_dm_hta(df_f, df)
    
    # Pegando DX por Medicamento
    df_f = paste_dx_hta_med(df_f)    

    # Se guarda pkl
    utils.save_df(df_f, path_save)
    print("Finalizó proceso:  Transformación y limpieza")
    
    return df_f
