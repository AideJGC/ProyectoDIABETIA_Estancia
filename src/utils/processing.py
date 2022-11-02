
# Functions for CIE 10 and Medicine

import pandas as pd 
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter
import pickle

def laboratories(df):
    """
    """
    df['lab_colesterol'] = np.where(pd.isna(df['colesterol']),0,1)
    df['lab_trigliceridos'] = np.where(pd.isna(df['trigliceridos']),0,1)
    df['lab_hdl'] = np.where(pd.isna(df['hdl']),0,1)
    df['lab_ldl'] = np.where(pd.isna(df['ldl']),0,1)
    df['lab_hba1c'] = np.where(pd.isna(df['hba1c']),0,1)
    df['lab_plaquetas'] = np.where(pd.isna(df['plaquetas']),0,1)
    df['lab_creatinina'] = np.where(pd.isna(df['creatinina']),0,1)
    df['lab_acido_urico'] = np.where(pd.isna(df['acido_urico']),0,1)
    df['lab_urea'] = np.where(pd.isna(df['urea']),0,1)
    df['lab_tfg'] = np.where(pd.isna(df['tfg']),0,1)
    
    return df

def cod_medicamento(df_m,df):
    """
    """
    df['cod_med'] = np.nan

    for i in range(len(df['cx_curp'])):
        x = df['medicamentos'][i]
        if(~pd.isna(x) and x!= 'nan'):
            for j in range(len(df_m['DESCRIPCION_ARTICULO'])):
                y = df_m['DESCRIPCION_ARTICULO'][j]
                m = df_m['ID_PRODUCTO'][j]
                if y in str(x):
                    df['cod_med'][i] = str(df['cod_med'][i]) + ',' + str(m)
                    
    df['cod_med'] = df['cod_med'].str.replace('nan,','')
    
    return df
    
    
def num_medicamentos(df):
    df['num_med'] = df['cod_med'].apply(lambda x : len(str(x).split(',')))
    df["num_med"] = np.where(pd.isna(df["cod_med"]), 0, df["num_med"])
    return df
    
    
def edad_range(df):
    df["edad_range"] = np.nan
    df.loc[(df['edad'] <  11), 'edad_range'] = 1#'hasta 10 años'
    df.loc[(df['edad'] > 10) & (df['edad'] <= 20), 'edad_range'] = 2#'11-20'
    df.loc[(df['edad'] > 20) & (df['edad'] <= 30), 'edad_range'] = 3#'21-30'
    df.loc[(df['edad'] > 30) & (df['edad'] <= 40), 'edad_range'] = 4#'31-40'
    df.loc[(df['edad'] > 40) & (df['edad'] <= 50), 'edad_range'] = 5#'41-50'
    df.loc[(df['edad'] > 50) & (df['edad'] <= 60), 'edad_range'] = 6#'51-60'
    df.loc[(df['edad'] > 60) & (df['edad'] <= 70), 'edad_range'] = 7#'61-70'
    df.loc[(df['edad'] > 70) & (df['edad'] <= 80), 'edad_range'] = 8#'71-80'
    df.loc[(df['edad'] > 80) & (df['edad'] <= 90), 'edad_range'] = 9#'81-90'
    df.loc[(df['edad'] > 90  ), 'edad_range'] = 10#'91 y más'
    return df
    
    
def edad_range_e(edad):
    e_r = np.nan
    if (edad <  11): 
        e_r = 1 #'hasta 10 años'
    elif (edad > 10) & (edad <= 20):
        e_r = 2 #'11-20'
    elif (edad > 20) & (edad <= 30): 
        e_r = 3 #'21-30'
    elif (edad > 30) & (edad <= 40): 
        e_r = 4 #'31-40'
    elif (edad > 40) & (edad <= 50): 
        e_r = 5 #'41-50'
    elif (edad > 50) & (edad <= 60): 
        e_r = 6 #'51-60'
    elif (edad > 60) & (edad <= 70): 
        e_r = 7 #'61-70'
    elif (edad > 70) & (edad <= 80): 
        e_r = 8 #'71-80'
    elif (edad > 80) & (edad <= 90): 
        e_r = 9 #'81-90'
    elif (edad > 90  ): 
        e_r = 10 #'91 y más'
 
    return e_r
    
    
def epoca_nac(df):
    df["year_nac"] = pd.DatetimeIndex(df['fecha_nacimiento']).year
    df["epoca_nac"] = np.nan
    pd.DatetimeIndex(df['fecha_nacimiento']).year.unique()

    for i in range(len(df['cx_curp'])):
        x = df["year_nac"][i]
        if(~pd.isna(x)):
            if(x<=1910):
                df["epoca_nac"][i] = 0
            elif(x>1910 and x<= 1920):
                df["epoca_nac"][i] = 1
            elif(x>1920 and x<= 1930):
                df["epoca_nac"][i] = 2
            elif(x>1930 and x<= 1940):
                df["epoca_nac"][i] = 3
            elif(x>1940 and x<= 1950):
                df["epoca_nac"][i] = 4
            elif(x>1950 and x<= 1960):
                df["epoca_nac"][i] = 5
            elif(x>1960 and x<= 1970):
                df["epoca_nac"][i] = 6
            elif(x>1970 and x<= 1980):
                df["epoca_nac"][i] = 7
            elif(x>1980 and x<= 1990):
                df["epoca_nac"][i] = 8
            elif(x>1990 and x<= 2000):
                df["epoca_nac"][i] = 9
            else:
                df["epoca_nac"][i] = 10
        
    return df



def epoca_nac_a(anio):
    e_a = np.nan
    if(anio<=1910):
        e_a = 0
    elif(anio>1910 and anio<= 1920):
        e_a = 1
    elif(anio>1920 and anio<= 1930):
        e_a = 2
    elif(anio>1930 and anio<= 1940):
        e_a = 3
    elif(anio>1940 and anio<= 1950):
        e_a = 4
    elif(anio>1950 and anio<= 1960):
        e_a = 5
    elif(anio>1960 and anio<= 1970):
        e_a = 6
    elif(anio>1970 and anio<= 1980):
        e_a = 7
    elif(anio>1980 and anio<= 1990):
        e_a = 8
    elif(anio>1990 and anio<= 2000):
        e_a = 9
    else:
        e_a = 10
        
    return e_a

def imc_calculo_range(df):
    df["imc_range"] = np.nan
    df.loc[(df['imc_calculado'] <  18.5), 'imc_range'] = 1#'Bajo peso'
    df.loc[(df['imc_calculado'] >= 18.5) & (df['imc_calculado'] < 25), 'imc_range'] = 2#'Peso normal'
    df.loc[(df['imc_calculado'] >= 25  ) & (df['imc_calculado'] < 30), 'imc_range'] = 3#'Sobrepeso'
    df.loc[(df['imc_calculado'] >= 30  ), 'imc_range'] = 4#'Obesidad'
    return df


def imc_calculo_range_imc(imc):
    #imc = imc.iloc[0]
    range_imc = np.nan
    #print("imc -> ",imc)
    if (imc < 18.5):
        range_imc = 1#'Bajo peso'
    elif (imc >= 18.5) & (imc < 25):
        range_imc = 2#'Peso normal'
    elif (imc >= 25  ) & (imc < 30):
        range_imc = 3#'Sobrepeso'
    elif (imc >= 30  ):
        range_imc = 4#'Obesidad Grado 3'
        
    return range_imc


def dias_year(date):
    days = np.nan
    p = pd.Period(date)
    if p.is_leap_year:
        days = 366
    else:
        days = 365
        
    return days



def fecha_ini_fin(fecha_ini,periodo):
    # Crear variable de ventanas máximas o hacer referencia a la variable años de conuslta
    fecha_ini = pd.to_datetime(fecha_ini)
    fecha_ini = pd.Timestamp(fecha_ini)
    
    # 1-Año; 2 - 3 meses
    i = 0
    i_t = 0
    f = 0
    #print("periodo: ", periodo)
    
    if(periodo == "1"):        
        a_ini = fecha_ini+pd.to_timedelta(365, unit = 'D')
        a_inter = fecha_ini+pd.to_timedelta(2*365, unit = 'D')
        a_fin = fecha_ini+pd.to_timedelta(3*365, unit = 'D')
        
        i = a_ini.strftime('%Y-%m-%d')
        i_t = a_inter.strftime('%Y-%m-%d')
        f = a_fin.strftime('%Y-%m-%d')

        i = dias_year(i)
        i_t = dias_year(i_t)
        f = dias_year(f)  
    
    elif(periodo == "2"):   
        a_ini = fecha_ini+pd.to_timedelta(45, unit = 'D')
        a_inter = fecha_ini+pd.to_timedelta(90, unit = 'D')
        a_fin = fecha_ini+pd.to_timedelta(120, unit = 'D')
        
        i = 45
        i_t = 90
        f = 30 
    
    
    a_ini = fecha_ini+pd.to_timedelta(i, unit = 'D')
    a_inter = fecha_ini+pd.to_timedelta(i+i_t, unit = 'D')
    a_fin = fecha_ini+pd.to_timedelta(i+i_t+f, unit = 'D')
    
    return a_ini, a_inter, a_fin


def ventana_ini_consulta(df):
    df["vent_ini_aux"] = np.nan
    grp = df.groupby('cx_curp')['fecha_consulta']
    for i, group in grp:  
        df["vent_ini_aux"][df.index.isin(group.index)] = group.sub(group.iloc[0])

    df['vent_ini_consul'] = df['vent_ini_aux'].dt.days.abs() 
    print(df['vent_ini_aux'])
    df["vent_entre_consul"] = df.groupby(["cx_curp"])["fecha_consulta"].diff().dt.days
    return df


def ventana_entre_consultas(df):
    df["vent_ini_aux"] = np.nan
    grp = df.groupby('cx_curp')['fecha_consulta']
    for i, group in grp:  
        df["vent_ini_aux"][df.index.isin(group.index)] = group.sub(group.iloc[0])

    df['vent_years_consul'] = (df['vent_ini_aux'].dt.days.abs() / 365).astype('int')
    return df


def ventana_ini_lab(df):
    df["vent_ini_aux"] = np.nan
    grp = df.groupby('cx_curp')['fecha_laboratorio']
    for i, group in grp:  
        df["vent_ini_aux"][df.index.isin(group.index)] = group.sub(group.iloc[0])

    df['vent_ini_lab'] = df['vent_ini_aux'].dt.days.abs() 
    df["vent_entre_lab"] = df.groupby(["cx_curp"])["fecha_laboratorio"].diff().dt.days
    df.drop(['vent_ini_aux'], axis=1)
    return df

"""
def ventana_entre_lab(df):# pendiente si se quita
    df["vent_ini_aux"] = np.nan
    grp = df.groupby('cx_curp')['fecha_laboratorio']
    for i, group in grp:  
        df["vent_ini_aux"][df.index.isin(group.index)] = group.sub(group.iloc[0])

    df['vent_years_lab'] = (df['vent_ini_aux'].dt.days.abs() / 365).astype('int')
    return df
"""    



def dm_unic(df):
    
    d_dx_dm = df[df['dm_cie']==1][['cx_curp','fecha_consulta','dm_cie']].\
                              sort_values(by = ['cx_curp','fecha_consulta'])
    d_dx_dm_u = d_dx_dm.groupby('cx_curp').first()
    
    df_dx_dm = df.drop_duplicates(subset=['cx_curp','año_dx_dm'])[['cx_curp','año_dx_dm']]
    df_dx_dm = df_dx_dm.loc[df_dx_dm['año_dx_dm'].notnull()]
    df_dx_dm.sort_values(by=['cx_curp','año_dx_dm'])
    
    pru2 = pd.merge(d_dx_dm_u, df_dx_dm, on = ["cx_curp"], how="left")
    pru2["año_dx_dm2"] = pru2["año_dx_dm"]
    
    pru2['año_dx_dm3'] = pd.DatetimeIndex(pru2['fecha_consulta']).year

    for i in range(len(pru2['cx_curp'])):
        x = pru2['año_dx_dm'][i]
        y = pru2['año_dx_dm3'][i]

        if (pd.isna(x)):
            pru2['año_dx_dm'][i] = pru2['año_dx_dm3'][i]
        elif x < y:
            pru2['año_dx_dm'][i] = pru2['año_dx_dm'][i]

    pru2 = pru2.drop(['año_dx_dm2','año_dx_dm3'], axis=1)

    pru = df.copy()
    pru = pd.merge(pru, pru2, on = ["cx_curp",'fecha_consulta'], how="left")
    pru[~pd.isna(pru["dm_cie_y"])][["cx_curp",'fecha_consulta',\
                                    'dm_cie_x','año_dx_dm_x','dm_cie_y','año_dx_dm_y']]
    
    pru.rename(columns = {'dm_cie_x':'dm_cie','dm_cie_y':'dm_cie_unic'}, inplace = True)
    
    pru = pd.merge(pru, pru2, on = ["cx_curp"], how="left")
    
    pru = pru.drop(['año_dx_dm_y'], axis=1)
    
    # Actualiza dm seguimiento
    pru['dm_cie_unic'] = np.where((pru['year_consulta']>=pru['año_dx_dm_x'])|
                                  ((pd.isna(pru['dm_cie_unic']))&(pru['fecha_consulta_x']>=pru['fecha_consulta_y'])),\
                                 1, pru['dm_cie_unic'])
    pru.sort_values(by=['cx_curp','fecha_consulta_x'])[['cx_curp','dm_cie_x','dm_cie_y','dm_cie_unic',\
                                                        'fecha_consulta_x','fecha_consulta_y','año_dx_dm_x',\
                                                        'year_consulta']]

    pru[pru['año_dx_dm_x']==pru['year_consulta']][['cx_curp','dm_cie_x','dm_cie_y','dm_cie_unic',\
                                                        'fecha_consulta_x','fecha_consulta_y','año_dx_dm_x',\
                                                        'year_consulta']]
    
    
    
    pru[pru['año_dx_dm_x']==pru['year_consulta']][['cx_curp','dm_cie_x','dm_cie_y','dm_cie_unic',\
                                                    'fecha_consulta_x','fecha_consulta_y','año_dx_dm_x',\
                                                    'year_consulta']]
    
    
    pru['año_dx_dm'] = np.where((pd.isna(pru['dm_cie_unic'])),\
                             np.nan, 
                             pru['año_dx_dm'])
    pru['año_dx_dm'] = np.where(pru['fecha_consulta_x']<pru['fecha_consulta_y'],\
                             np.nan, 
                             pru['año_dx_dm'])
    pru['dm_cie_unic'] = np.where(pru['fecha_consulta_x']<pru['fecha_consulta_y'],\
                             np.nan, 
                             pru['dm_cie_unic'])
    pru['año_dx_dm'] = np.where((pd.isna(pru['dm_cie_unic']))&(pru['año_dx_dm_x']<pru['year_consulta']),\
                             pru['año_dx_dm_x'], 
                             pru['año_dx_dm'])
    pru['dm_cie_unic'] = np.where((pd.isna(pru['dm_cie_unic']))&(pru['año_dx_dm_x']<pru['year_consulta']),\
                             1, 
                             pru['dm_cie_unic'] )
    
    # Calcula años con dx
    pru['dm_años_int'] = np.where((~pd.isna(pru['dm_cie_unic'])),\
                             (pru.year_consulta - pru.año_dx_dm),
                             np.nan)
    
    
    pru = pru.drop(['dm_cie_y','año_dx_dm_x'], axis=1)
    pru.rename(columns = {'dm_cie_x':'dm_cie'}, inplace = True)
    
    
    # Calcula años con dx desde el primer dx en base de datos
    pru['dm_años_flt_ini_db_dx'] = np.where((~pd.isna(pru['dm_cie_unic'])),\
                             (pru['fecha_consulta_x'] - pru['fecha_consulta_y']) / np.timedelta64(1, 'Y'), 
                             np.nan)
    # Calcula años con dx desde el primer dx en base de datos
    pru['dm_años_int_ini_db_dx'] = np.where((~pd.isna(pru['dm_cie_unic'])),\
                             (pru.fecha_consulta_x - pru.fecha_consulta_y).astype('timedelta64[Y]').astype('int'),
                             np.nan)

    pru['dm_años_flt_ini_db_dx'] = np.where(pru['dm_años_flt_ini_db_dx']<0,\
                             np.nan, 
                             pru['dm_años_flt_ini_db_dx'])
    pru['dm_años_int_ini_db_dx'] = np.where(pru['dm_años_int_ini_db_dx']<0,\
                             np.nan, 
                             pru['dm_años_int_ini_db_dx'])
    
    
    pru.rename(columns = {'fecha_consulta_x':'fecha_consulta','fecha_consulta_y':'fecha_dm_dx'}, inplace = True)
    pru['fecha_dm_dx'] = np.where(pd.isna(pru['dm_años_int_ini_db_dx']), np.datetime64('NaT'), pru['fecha_dm_dx'])
    
    df = pru.copy()
    
    return df


def hta_unic(df):
    
    d_dx_hta = df[df['hta_cie']==1][['cx_curp','fecha_consulta','hta_cie']].\
                              sort_values(by = ['cx_curp','fecha_consulta'])
    d_dx_hta_u = d_dx_hta.groupby('cx_curp').first()
    
    df_dx_hta = df.drop_duplicates(subset=['cx_curp','año_dx_hta'])[['cx_curp','año_dx_hta']]
    df_dx_hta = df_dx_hta.loc[df_dx_hta['año_dx_hta'].notnull()]
    df_dx_hta.sort_values(by=['cx_curp','año_dx_hta'])
    
    pru2 = pd.merge(d_dx_hta_u, df_dx_hta, on = ["cx_curp"], how="left")
    pru2["año_dx_hta2"] = pru2["año_dx_hta"]
    
    pru2['año_dx_hta3'] = pd.DatetimeIndex(pru2['fecha_consulta']).year
    
    for i in range(len(pru2['cx_curp'])):
        x = pru2['año_dx_hta'][i]
        y = pru2['año_dx_hta3'][i]

        if (pd.isna(x)):
            pru2['año_dx_hta'][i] = pru2['año_dx_hta3'][i]
        elif x < y:
            pru2['año_dx_hta'][i] = pru2['año_dx_hta'][i]

    pru2 = pru2.drop(['año_dx_hta2','año_dx_hta3'], axis=1)
    
    pru = df.copy()
    pru = pd.merge(pru, pru2, on = ["cx_curp",'fecha_consulta'], how="left")
    
    pru.rename(columns = {'hta_cie_x':'hta_cie','hta_cie_y':'hta_cie_unic'}, inplace = True)
    
    pru = pd.merge(pru, pru2, on = ["cx_curp"], how="left")
    
    pru = pru.drop(['año_dx_hta_y'], axis=1)
    
    # Actualiza hta seguimiento
    pru['hta_cie_unic'] = np.where((pru['year_consulta']>=pru['año_dx_hta_x'])|
                                  ((pd.isna(pru['hta_cie_unic']))&(pru['fecha_consulta_x']>=pru['fecha_consulta_y'])),\
                                 1, pru['hta_cie_unic'])
    pru.sort_values(by=['cx_curp','fecha_consulta_x'])[['cx_curp','hta_cie_x','hta_cie_y','hta_cie_unic',\
                                                        'fecha_consulta_x','fecha_consulta_y','año_dx_hta_x',\
                                                        'year_consulta']]

    pru[pru['año_dx_hta_x']==pru['year_consulta']][['cx_curp','hta_cie_x','hta_cie_y','hta_cie_unic',\
                                                        'fecha_consulta_x','fecha_consulta_y','año_dx_hta_x',\
                                                        'year_consulta']]
    
    
    pru['año_dx_hta'] = np.where((pd.isna(pru['hta_cie_unic'])),\
                             np.nan, 
                             pru['año_dx_hta'])
    pru['año_dx_hta'] = np.where(pru['fecha_consulta_x']<pru['fecha_consulta_y'],\
                             np.nan, 
                             pru['año_dx_hta'])
    pru['hta_cie_unic'] = np.where(pru['fecha_consulta_x']<pru['fecha_consulta_y'],\
                             np.nan, 
                             pru['hta_cie_unic'])
    pru['año_dx_hta'] = np.where((pd.isna(pru['hta_cie_unic']))&(pru['año_dx_hta_x']<pru['year_consulta']),\
                             pru['año_dx_hta_x'], 
                             pru['año_dx_hta'])
    pru['hta_cie_unic'] = np.where((pd.isna(pru['hta_cie_unic']))&(pru['año_dx_hta_x']<pru['year_consulta']),\
                             1, 
                             pru['hta_cie_unic'] )
    
    
    pru = pru.drop(['hta_cie_y','año_dx_hta_x'], axis=1)
    pru.rename(columns = {'hta_cie_x':'hta_cie'}, inplace = True)
    
    # Calcula años con dx desde el primer dx en base de datos
    pru['hta_años_flt_ini_db_dx'] = np.where((~pd.isna(pru['hta_cie_unic'])),\
                             (pru['fecha_consulta_x'] - pru['fecha_consulta_y']) / np.timedelta64(1, 'Y'), 
                             np.nan)
    # Calcula años con dx desde el primer dx en base de datos
    pru['hta_años_int_ini_db_dx'] = np.where((~pd.isna(pru['hta_cie_unic'])),\
                             (pru.fecha_consulta_x - pru.fecha_consulta_y).astype('timedelta64[Y]').astype('int'),
                             np.nan)

    pru['hta_años_flt_ini_db_dx'] = np.where(pru['hta_años_flt_ini_db_dx']<0,\
                             np.nan, 
                             pru['hta_años_flt_ini_db_dx'])
    pru['hta_años_int_ini_db_dx'] = np.where(pru['hta_años_int_ini_db_dx']<0,\
                             np.nan, 
                             pru['hta_años_int_ini_db_dx'])  
    
    # Calcula años con dx
    pru['hta_años_int'] = np.where((~pd.isna(pru['hta_cie_unic'])),\
                             (pru.year_consulta - pru.año_dx_hta),
                             np.nan)
    
    pru.rename(columns = {'fecha_consulta_x':'fecha_consulta','fecha_consulta_y':'fecha_hta_dx'}, inplace = True)
    
    pru['fecha_hta_dx'] = np.where(pd.isna(pru['hta_años_int_ini_db_dx']), np.datetime64('NaT'), pru['fecha_hta_dx'])

    
    df = pru.copy()
    df['fecha_consulta']= pd.to_datetime(df['fecha_consulta'])
    df['FechaNuevaHipertension']= pd.to_datetime(df['FechaNuevaHipertension'])

    
    df['hta_nvo_ce'] = np.where(df['fecha_consulta']>=df['FechaNuevaHipertension'],1,0)
    df['fecha_hta_nvo'] = np.where(df['fecha_consulta']>=df['FechaNuevaHipertension'],df['FechaNuevaHipertension'],\
                                   np.datetime64('NaT'))
    df['año_hta_nvo'] = pd.DatetimeIndex(df['FechaNuevaHipertension']).year

    # Calcula años con dx desde el primer dx en base de datos
    df['hta_años_flt'] = np.where((~pd.isna(df['año_hta_nvo'])),\
                             (df['fecha_consulta'] - df['FechaNuevaHipertension']) / np.timedelta64(1, 'Y'), 
                             np.nan)
    # Calcula años con dx desde el primer dx en base de datos
    df['hta_años_int'] = np.where((~pd.isna(df['año_hta_nvo'])),\
                             (df.fecha_consulta - df.FechaNuevaHipertension).astype('timedelta64[Y]').astype('int'),
                             np.nan)

    df['año_hta_nvo'] = np.where(df['hta_años_int']<0,np.nan,df['año_hta_nvo'])
    df['hta_años_flt'] = np.where(df['hta_años_int']<0,np.nan,df['hta_años_flt'])
    df['hta_años_int'] = np.where(df['hta_años_int']<0,np.nan,df['hta_años_int'])

    df.drop('FechaNuevaHipertension', inplace=True, axis=1)  
    
    return df, d_dx_hta_u


def renal_unic(df):
    
    d_dx_renal = df[df['renal_cie']==1][['cx_curp','fecha_consulta','renal_cie']].\
                              sort_values(by = ['cx_curp','fecha_consulta'])
    d_dx_renal_u = d_dx_renal.groupby('cx_curp').first()
    
    df = pd.merge(df, d_dx_renal_u, on = ["cx_curp",'fecha_consulta'], how="left")
    df.rename(columns = {'renal_cie_x':'renal_cie','renal_cie_y':'renal_cie_unic'}, inplace = True)
    df = pd.merge(df, d_dx_renal_u, on = ["cx_curp"], how="left")
    # Actualiza renal seguimiento
    df['renal_cie_unic'] = np.where((pd.isna(df['renal_cie_unic']))&(df['fecha_consulta_x']>=df['fecha_consulta_y']),\
                                 1, df['renal_cie_unic'])
    # Calcula años con dx
    df['renal_años_flt'] = np.where((~pd.isna(df['renal_cie_unic'])),\
                             (df['fecha_consulta_x'] - df['fecha_consulta_y']) / np.timedelta64(1, 'Y'), 
                             np.nan)
    
    df['renal_años_flt'] = df['renal_años_flt'].fillna(0) 
    df['renal_años_int'] = df['renal_años_flt'].astype('int')
    
    df.rename(columns = {'renal_cie_x':'renal_cie','fecha_consulta_x':'fecha_consulta'}, inplace = True)
    df.drop('fecha_consulta_y', inplace=True, axis=1)
    df.drop('renal_cie_y', inplace=True, axis=1)
    
    return df


def proporciones(df):
    
    df_aux = df.copy()
    df_aux['sexo_n'] = ""
    df_aux['edad_c'] = ""

    for i in range(len(df_aux['newid'])):  

        if pd.isna(df_aux['glucosa1'][i]):        
            df_aux['glucosa1'][i] = 'NaN'        
        else:        
            df_aux['glucosa1'][i] = 'Value'

        if pd.isna(df_aux['glucosa2'][i]):
            df_aux['glucosa2'][i] = 'NaN'        
        else:        
            df_aux['glucosa2'][i] = 'Value'

        if pd.isna(df_aux['sistolica'][i]):        
            df_aux['sistolica'][i] = 'NaN'        
        else:        
            df_aux['sistolica'][i] = 'Value'

        if pd.isna(df_aux['diastolica'][i]):
            df_aux['diastolica'][i] = 'NaN'        
        else:        
            df_aux['diastolica'][i] = 'Value'

        if pd.isna(df_aux['colesterol'][i]):        
            df_aux['colesterol'][i] = 'NaN'        
        else:        
            df_aux['colesterol'][i] = 'Value'

        if pd.isna(df_aux['trigliceridos'][i]):
            df_aux['trigliceridos'][i] = 'NaN'        
        else:        
            df_aux['trigliceridos'][i] = 'Value'

        if pd.isna(df_aux['hdl'][i]):        
            df_aux['hdl'][i] = 'NaN'        
        else:        
            df_aux['hdl'][i] = 'Value'

        if pd.isna(df_aux['ldl'][i]):
            df_aux['ldl'][i] = 'NaN'        
        else:        
            df_aux['ldl'][i] = 'Value'

        if pd.isna(df_aux['hba1c'][i]):        
            df_aux['hba1c'][i] = 'NaN'        
        else:        
            df_aux['hba1c'][i] = 'Value'

        if pd.isna(df_aux['plaquetas'][i]):
            df_aux['plaquetas'][i] = 'NaN'        
        else:        
            df_aux['plaquetas'][i] = 'Value'

        if pd.isna(df_aux['creatinina'][i]):        
            df_aux['creatinina'][i] = 'NaN'        
        else:        
            df_aux['creatinina'][i] = 'Value'

        if pd.isna(df_aux['acido_urico'][i]):
            df_aux['acido_urico'][i] = 'NaN'        
        else:        
            df_aux['acido_urico'][i] = 'Value'

        if pd.isna(df_aux['urea'][i]):        
            df_aux['urea'][i] = 'NaN'        
        else:        
            df_aux['urea'][i] = 'Value'

        if pd.isna(df_aux['peso'][i]):
            df_aux['peso'][i] = 'NaN'        
        else:        
            df_aux['peso'][i] = 'Value'

        if pd.isna(df_aux['altura'][i]):        
            df_aux['altura'][i] = 'NaN'        
        else:        
            df_aux['altura'][i] = 'Value'

        if pd.isna(df_aux['tfg'][i]):
            df_aux['tfg'][i] = 'NaN'        
        else:        
            df_aux['tfg'][i] = 'Value'

        if pd.isna(df_aux['imc'][i]):        
            df_aux['imc'][i] = 'NaN'        
        else:        
            df_aux['imc'][i] = 'Value'

        if pd.isna(df_aux['in_consulta'][i]):
            df_aux['in_consulta'][i] = 'NaN'        
        else:        
            df_aux['in_consulta'][i] = 'Value'

        if pd.isna(df_aux['fecha_nacimiento'][i]):        
            df_aux['fecha_nacimiento'][i] = 'NaN'        
        else:        
            df_aux['fecha_nacimiento'][i] = 'Value'

        if pd.isna(df_aux['sexo'][i]):
            df_aux['sexo_n'][i] = 'NaN'        
        else:        
            df_aux['sexo_n'][i] = 'Value'

        if pd.isna(df_aux['edad'][i]):
            df_aux['edad_c'][i] = 'NaN'        
        else:        
            df_aux['edad_c'][i] = 'Value'

        if pd.isna(df_aux['año_dx_dm'][i]):
            df_aux['año_dx_dm'][i] = 'NaN'        
        else:        
            df_aux['año_dx_dm'][i] = 'Value'

        if pd.isna(df_aux['año_dx_hta'][i]):        
            df_aux['año_dx_hta'][i] = 'NaN'        
        else:        
            df_aux['año_dx_hta'][i] = 'Value'

        if pd.isna(df_aux['year_consulta'][i]):        
            df_aux['year_consulta'][i] = 'NaN'        
        else:        
            df_aux['year_consulta'][i] = 'Value'
        
    return df_aux


def lista_mex_enf(df):
    """
    Agrupa dx de acuerdo a lista mexicana
    """
    # A00-A09
    df["enf_inf_intestinales"] = np.where(df["codigos_cie"].str.contains('A0'), 1, 0)
    # A15-A19
    df["tuberculosis"] = np.where(df["codigos_cie"].str.contains('A15')|
                                          df["codigos_cie"].str.contains('A16')|
                                          df["codigos_cie"].str.contains('A17')|
                                          df["codigos_cie"].str.contains('A18')|
                                          df["codigos_cie"].str.contains('A19'), 1, 0)
    # A20-A32, A35-A49
    df["ot_enf_bacterianas"] = np.where(df["codigos_cie"].str.contains('A2')|
                                          df["codigos_cie"].str.contains('A30')|
                                          df["codigos_cie"].str.contains('A31')|
                                          df["codigos_cie"].str.contains('A32')|
                                          df["codigos_cie"].str.contains('A35')|
                                          df["codigos_cie"].str.contains('A36')|
                                          df["codigos_cie"].str.contains('A37')|
                                          df["codigos_cie"].str.contains('A38')|
                                          df["codigos_cie"].str.contains('A39')|
                                          df["codigos_cie"].str.contains('A4'), 1, 0)
    # A50-A64
    df["inf_trans_pred_sexual"] = np.where(df["codigos_cie"].str.contains('A5')|
                                          df["codigos_cie"].str.contains('A60')|
                                          df["codigos_cie"].str.contains('A61')|
                                          df["codigos_cie"].str.contains('A62')|
                                          df["codigos_cie"].str.contains('A63')|
                                          df["codigos_cie"].str.contains('A64'), 1, 0)
    # A65-A69,B35-B49,B58-B99
    df["ot_enf_inf_y_paras_y_efec_tardios"] = np.where(df["codigos_cie"].str.contains('A65')|
                                          df["codigos_cie"].str.contains('A66')|
                                          df["codigos_cie"].str.contains('A67')|
                                          df["codigos_cie"].str.contains('A68')|
                                          df["codigos_cie"].str.contains('A69')|
                                          df["codigos_cie"].str.contains('B35')|
                                          df["codigos_cie"].str.contains('B36')|
                                          df["codigos_cie"].str.contains('B37')|
                                          df["codigos_cie"].str.contains('B38')|
                                          df["codigos_cie"].str.contains('B39')|
                                          df["codigos_cie"].str.contains('B4')|
                                          df["codigos_cie"].str.contains('B58')|
                                          df["codigos_cie"].str.contains('B59')|
                                          df["codigos_cie"].str.contains('B6')|
                                          df["codigos_cie"].str.contains('B7')|
                                          df["codigos_cie"].str.contains('B8')|
                                          df["codigos_cie"].str.contains('B9'), 1, 0)
    # A70-A74,A80-B34
    df["enf_viricas"] = np.where(df["codigos_cie"].str.contains('A70')|
                                          df["codigos_cie"].str.contains('A71')|
                                          df["codigos_cie"].str.contains('A72')|
                                          df["codigos_cie"].str.contains('A73')|
                                          df["codigos_cie"].str.contains('A74')|
                                          df["codigos_cie"].str.contains('A75')|
                                          df["codigos_cie"].str.contains('A8')|
                                          df["codigos_cie"].str.contains('A9')|
                                          df["codigos_cie"].str.contains('B0')|
                                          df["codigos_cie"].str.contains('B1')|
                                          df["codigos_cie"].str.contains('B2')|
                                          df["codigos_cie"].str.contains('B30')|
                                          df["codigos_cie"].str.contains('B31')|
                                          df["codigos_cie"].str.contains('B32')|
                                          df["codigos_cie"].str.contains('B33')|
                                          df["codigos_cie"].str.contains('B34'), 1, 0)
    # A75-A79,B50-B57
    df["rickettsiosis_y_ot_enf__protozoarios"] = np.where(df["codigos_cie"].str.contains('A75')|
                                          df["codigos_cie"].str.contains('A76')|
                                          df["codigos_cie"].str.contains('A77')|
                                          df["codigos_cie"].str.contains('A78')|
                                          df["codigos_cie"].str.contains('A79')|
                                          df["codigos_cie"].str.contains('B50')|
                                          df["codigos_cie"].str.contains('B51')|
                                          df["codigos_cie"].str.contains('B52')|
                                          df["codigos_cie"].str.contains('B53')|
                                          df["codigos_cie"].str.contains('B54')|
                                          df["codigos_cie"].str.contains('B55')|
                                          df["codigos_cie"].str.contains('B56')|
                                          df["codigos_cie"].str.contains('B57'), 1, 0)
    # C00-C14
    df["tumores_malig_labio_bucal_faringe"] = np.where(df["codigos_cie"].str.contains('C0')|
                                          df["codigos_cie"].str.contains('C10')|
                                          df["codigos_cie"].str.contains('C11')|
                                          df["codigos_cie"].str.contains('C12')|
                                          df["codigos_cie"].str.contains('C13')|
                                          df["codigos_cie"].str.contains('C14'), 1, 0) 
    # C15-C26
    df["tumores_malig_organos"] = np.where(df["codigos_cie"].str.contains('C15')|
                                          df["codigos_cie"].str.contains('C16')|
                                          df["codigos_cie"].str.contains('C17')|
                                          df["codigos_cie"].str.contains('C18')|
                                          df["codigos_cie"].str.contains('C19')|
                                          df["codigos_cie"].str.contains('C20')|
                                          df["codigos_cie"].str.contains('C21')|
                                          df["codigos_cie"].str.contains('C22')|
                                          df["codigos_cie"].str.contains('C23')|
                                          df["codigos_cie"].str.contains('C24')|
                                          df["codigos_cie"].str.contains('C25')|
                                          df["codigos_cie"].str.contains('C26'), 1, 0) 
    # C30-C39
    df["tumores_malig_org_respiratorios_intratoracicos"] = np.where(df["codigos_cie"].str.contains('C3'), 1, 0) 
    # C40-C50
    df["tumores_malig_huesos_articulares_conjuntivo_piel_mama"] = np.where(df["codigos_cie"].str.contains('C4')|
                                          df["codigos_cie"].str.contains('C50'), 1, 0) 
    # C51-C68
    df["tumores_malig_org_genitourinarios"] = np.where(df["codigos_cie"].str.contains('C51')|
                                          df["codigos_cie"].str.contains('C52')|
                                          df["codigos_cie"].str.contains('C53')|
                                          df["codigos_cie"].str.contains('C54')|
                                          df["codigos_cie"].str.contains('C55')|
                                          df["codigos_cie"].str.contains('C56')|
                                          df["codigos_cie"].str.contains('C57')|
                                          df["codigos_cie"].str.contains('C58')|
                                          df["codigos_cie"].str.contains('C59')|
                                          df["codigos_cie"].str.contains('C60')|
                                          df["codigos_cie"].str.contains('C61')|
                                          df["codigos_cie"].str.contains('C62')|
                                          df["codigos_cie"].str.contains('C63')|
                                          df["codigos_cie"].str.contains('C64')|
                                          df["codigos_cie"].str.contains('C65')|
                                          df["codigos_cie"].str.contains('C66')|
                                          df["codigos_cie"].str.contains('C67')|
                                          df["codigos_cie"].str.contains('C68'), 1, 0) 
    # C69-C80
    df["tumores_malig_otros_sitios_ne"] = np.where(df["codigos_cie"].str.contains('C69')|
                                          df["codigos_cie"].str.contains('C7')|
                                          df["codigos_cie"].str.contains('C80'), 1, 0)
    # C81-C96
    df["tumores_malig_tejido_linf_org_hematop"] = np.where(df["codigos_cie"].str.contains('C81')|
                                          df["codigos_cie"].str.contains('C82')|
                                          df["codigos_cie"].str.contains('C83')|
                                          df["codigos_cie"].str.contains('C84')|
                                          df["codigos_cie"].str.contains('C85')|
                                          df["codigos_cie"].str.contains('C86')|
                                          df["codigos_cie"].str.contains('C87')|
                                          df["codigos_cie"].str.contains('C88')|
                                          df["codigos_cie"].str.contains('C89')|
                                          df["codigos_cie"].str.contains('C90')|
                                          df["codigos_cie"].str.contains('C91')|
                                          df["codigos_cie"].str.contains('C92')|
                                          df["codigos_cie"].str.contains('C93')|
                                          df["codigos_cie"].str.contains('C94')|
                                          df["codigos_cie"].str.contains('C95')|
                                          df["codigos_cie"].str.contains('C96'), 1, 0)
    # C97
    df["tumores_malig_sitios_mul_indep"] = np.where(df["codigos_cie"].str.contains('C97'), 1, 0)
    # D00-D09
    df["tumores_insitu"] = np.where(df["codigos_cie"].str.contains('CD0'), 1, 0)
    # D10-D36
    df["tumores_benignos"] = np.where(df["codigos_cie"].str.contains('D1')|
                                          df["codigos_cie"].str.contains('D2')|
                                          df["codigos_cie"].str.contains('D30')|
                                          df["codigos_cie"].str.contains('D31')|
                                          df["codigos_cie"].str.contains('D32')|
                                          df["codigos_cie"].str.contains('D33')|
                                          df["codigos_cie"].str.contains('D34')|
                                          df["codigos_cie"].str.contains('D35')|
                                          df["codigos_cie"].str.contains('D36'), 1, 0)
    # D37-D48
    df["tumores_comp_incierto_desc"] = np.where(df["codigos_cie"].str.contains('D37')|
                                          df["codigos_cie"].str.contains('D38')|
                                          df["codigos_cie"].str.contains('D39')|
                                          df["codigos_cie"].str.contains('D40')|
                                          df["codigos_cie"].str.contains('D41')|
                                          df["codigos_cie"].str.contains('D42')|
                                          df["codigos_cie"].str.contains('D43')|
                                          df["codigos_cie"].str.contains('D44')|
                                          df["codigos_cie"].str.contains('D45')|
                                          df["codigos_cie"].str.contains('D46')|
                                          df["codigos_cie"].str.contains('D47')|
                                          df["codigos_cie"].str.contains('D48'), 1, 0)
    # D50-D76, D80-D89
    df["enf_sangre_org_hematop"] = np.where(df["codigos_cie"].str.contains('D5')|
                                          df["codigos_cie"].str.contains('D6')|
                                          df["codigos_cie"].str.contains('D70')|
                                          df["codigos_cie"].str.contains('D71')|
                                          df["codigos_cie"].str.contains('D72')|
                                          df["codigos_cie"].str.contains('D73')|
                                          df["codigos_cie"].str.contains('D74')|
                                          df["codigos_cie"].str.contains('D75')|
                                          df["codigos_cie"].str.contains('D76')|
                                          df["codigos_cie"].str.contains('D8'), 1, 0)
    # E00-E34,E65-E89
    df["enf_endocrinas"] = np.where(df["codigos_cie"].str.contains('E0')|
                                          df["codigos_cie"].str.contains('E1')|
                                          df["codigos_cie"].str.contains('E2')|
                                          df["codigos_cie"].str.contains('E30')|
                                          df["codigos_cie"].str.contains('E31')|
                                          df["codigos_cie"].str.contains('E32')|
                                          df["codigos_cie"].str.contains('E33')|
                                          df["codigos_cie"].str.contains('E65')|
                                          df["codigos_cie"].str.contains('E66')|
                                          df["codigos_cie"].str.contains('E67')|
                                          df["codigos_cie"].str.contains('E68')|
                                          df["codigos_cie"].str.contains('E69')|
                                          df["codigos_cie"].str.contains('E7')|
                                          df["codigos_cie"].str.contains('E8'), 1, 0)
    # E40-E64
    df["desnutricion_ot_deficiencias"] = np.where(df["codigos_cie"].str.contains('E4')|
                                          df["codigos_cie"].str.contains('E5')|
                                          df["codigos_cie"].str.contains('E60')|
                                          df["codigos_cie"].str.contains('E61')|
                                          df["codigos_cie"].str.contains('E62')|
                                          df["codigos_cie"].str.contains('E63')|
                                          df["codigos_cie"].str.contains('E64'), 1, 0)
    # F00-F52, F54-F99
    df["trastornos_mentales"] = np.where(df["codigos_cie"].str.contains('F0')|
                                          df["codigos_cie"].str.contains('F1')|
                                          df["codigos_cie"].str.contains('F2')|
                                          df["codigos_cie"].str.contains('F3')|
                                          df["codigos_cie"].str.contains('F4')|
                                          df["codigos_cie"].str.contains('F51')|
                                          df["codigos_cie"].str.contains('F52')|
                                          df["codigos_cie"].str.contains('F54')|
                                          df["codigos_cie"].str.contains('F55')|
                                          df["codigos_cie"].str.contains('F56')|
                                          df["codigos_cie"].str.contains('F57')|
                                          df["codigos_cie"].str.contains('F58')|
                                          df["codigos_cie"].str.contains('F59')|
                                          df["codigos_cie"].str.contains('F6')|
                                          df["codigos_cie"].str.contains('F7')|
                                          df["codigos_cie"].str.contains('F8')|
                                          df["codigos_cie"].str.contains('F9'), 1, 0)
    # G00-G99
    df["enf_sist_nervioso"] = np.where(df["codigos_cie"].str.contains('G0'), 1, 0)
    # H00-H59
    df["enf_ojo_anexos"] = np.where(df["codigos_cie"].str.contains('H0')|
                                          df["codigos_cie"].str.contains('H1')|
                                          df["codigos_cie"].str.contains('H2')|
                                          df["codigos_cie"].str.contains('H3')|
                                          df["codigos_cie"].str.contains('H4')|
                                          df["codigos_cie"].str.contains('H5'), 1, 0)
    # H60-H93,H95
    df["enf_oido_apofisis_mastoides"] = np.where(df["codigos_cie"].str.contains('H6')|
                                          df["codigos_cie"].str.contains('H7')|
                                          df["codigos_cie"].str.contains('H8')|
                                          df["codigos_cie"].str.contains('H90')|
                                          df["codigos_cie"].str.contains('H91')|
                                          df["codigos_cie"].str.contains('H92')|
                                          df["codigos_cie"].str.contains('H93')|
                                          df["codigos_cie"].str.contains('H95'), 1, 0)
    # I00-I09
    df["fiebre_y_enf_cardiacas_reumaticas"] = np.where(df["codigos_cie"].str.contains('I0'), 1, 0)
    # I10-I13 y (I15 sólo para morbilidad)
    df["enf_hipertensivas"] = np.where(df["codigos_cie"].str.contains('I10')|
                                          df["codigos_cie"].str.contains('I11')|
                                          df["codigos_cie"].str.contains('I12')|
                                          df["codigos_cie"].str.contains('I13')|
                                          df["codigos_cie"].str.contains('I15'), 1, 0)
    # I20-I25
    df["enf_isquemicas_corazon"] = np.where(df["codigos_cie"].str.contains('I20')|
                                          df["codigos_cie"].str.contains('I21')|
                                          df["codigos_cie"].str.contains('I22')|
                                          df["codigos_cie"].str.contains('I23')|
                                          df["codigos_cie"].str.contains('I24')|
                                          df["codigos_cie"].str.contains('I25'), 1, 0)
    # I26-I51
    df["enf_circulacion_pulmonar_enf_corazon"] = np.where(df["codigos_cie"].str.contains('I26')|
                                          df["codigos_cie"].str.contains('I27')|
                                          df["codigos_cie"].str.contains('I28')|
                                          df["codigos_cie"].str.contains('I29')|
                                          df["codigos_cie"].str.contains('I3')|
                                          df["codigos_cie"].str.contains('I4')|
                                          df["codigos_cie"].str.contains('I50')|
                                          df["codigos_cie"].str.contains('I51'), 1, 0)
    # I60-I69
    df["enf_cerebrovasculares"] = np.where(df["codigos_cie"].str.contains('I6'), 1, 0)
    # I70-I99
    df["otras_enf_aparato_vasc"] = np.where(df["codigos_cie"].str.contains('I7')|
                                          df["codigos_cie"].str.contains('I8')|
                                          df["codigos_cie"].str.contains('I9'), 1, 0)
    # J00-J06,   J30-J39
    df["inf_y_enf_vias_respiratorias_sup"] = np.where(df["codigos_cie"].str.contains('J00')|
                                          df["codigos_cie"].str.contains('J01')|
                                          df["codigos_cie"].str.contains('J02')|
                                          df["codigos_cie"].str.contains('J03')|
                                          df["codigos_cie"].str.contains('J04')|
                                          df["codigos_cie"].str.contains('J05')|
                                          df["codigos_cie"].str.contains('J06')|
                                          df["codigos_cie"].str.contains('J3'), 1, 0)
    # J10-J22, J40-J98
    df["otras_enf_aparato_resp"] = np.where(df["codigos_cie"].str.contains('J1')|
                                          df["codigos_cie"].str.contains('J20')|
                                          df["codigos_cie"].str.contains('J21')|
                                          df["codigos_cie"].str.contains('J22')|
                                          df["codigos_cie"].str.contains('J4')|
                                          df["codigos_cie"].str.contains('J5')|
                                          df["codigos_cie"].str.contains('J6')|
                                          df["codigos_cie"].str.contains('J7')|
                                          df["codigos_cie"].str.contains('J8')|
                                          df["codigos_cie"].str.contains('J90')|
                                          df["codigos_cie"].str.contains('J91')|
                                          df["codigos_cie"].str.contains('J92')|
                                          df["codigos_cie"].str.contains('J93')|
                                          df["codigos_cie"].str.contains('J94')|
                                          df["codigos_cie"].str.contains('J95')|
                                          df["codigos_cie"].str.contains('J96')|
                                          df["codigos_cie"].str.contains('J97')|
                                          df["codigos_cie"].str.contains('J98'), 1, 0)
    # K00-K14
    df["enf_cavidad_bucal_glandulas_salivales"] = np.where(df["codigos_cie"].str.contains('K0')|
                                          df["codigos_cie"].str.contains('K10')|
                                          df["codigos_cie"].str.contains('K11')|
                                          df["codigos_cie"].str.contains('K12')|
                                          df["codigos_cie"].str.contains('K13')|
                                          df["codigos_cie"].str.contains('K14'), 1, 0)
    # K20-K92
    df["enf_ot_partes_aparato_digestivo"] = np.where(df["codigos_cie"].str.contains('K2')|
                                          df["codigos_cie"].str.contains('K3')|
                                          df["codigos_cie"].str.contains('K4')|
                                          df["codigos_cie"].str.contains('K5')|
                                          df["codigos_cie"].str.contains('K6')|
                                          df["codigos_cie"].str.contains('K7')|
                                          df["codigos_cie"].str.contains('K8')|
                                          df["codigos_cie"].str.contains('K90')|
                                          df["codigos_cie"].str.contains('K91')|
                                          df["codigos_cie"].str.contains('K92'), 1, 0)
    # L00-L98
    df["enf_piel_tejido_subcutaneo"] = np.where(df["codigos_cie"].str.contains('L0')|
                                          df["codigos_cie"].str.contains('L1')|
                                          df["codigos_cie"].str.contains('L2')|
                                          df["codigos_cie"].str.contains('L3')|
                                          df["codigos_cie"].str.contains('L4')|
                                          df["codigos_cie"].str.contains('L5')|
                                          df["codigos_cie"].str.contains('L6')|
                                          df["codigos_cie"].str.contains('L7')|
                                          df["codigos_cie"].str.contains('L8')|
                                          df["codigos_cie"].str.contains('L90')|
                                          df["codigos_cie"].str.contains('L91')|
                                          df["codigos_cie"].str.contains('L92')|
                                          df["codigos_cie"].str.contains('L93')|
                                          df["codigos_cie"].str.contains('L94')|
                                          df["codigos_cie"].str.contains('L95')|
                                          df["codigos_cie"].str.contains('L96')|
                                          df["codigos_cie"].str.contains('L97')|
                                          df["codigos_cie"].str.contains('L98'), 1, 0)
    # M00-M82,M83.1-M99
    df["enf_sist_osteomuscular_y_tejido"] = np.where(df["codigos_cie"].str.contains('M0')|
                                          df["codigos_cie"].str.contains('M1')|
                                          df["codigos_cie"].str.contains('M2')|
                                          df["codigos_cie"].str.contains('M3')|
                                          df["codigos_cie"].str.contains('M4')|
                                          df["codigos_cie"].str.contains('M5')|
                                          df["codigos_cie"].str.contains('M6')|
                                          df["codigos_cie"].str.contains('M7')|
                                          df["codigos_cie"].str.contains('M80')|
                                          df["codigos_cie"].str.contains('M81')|
                                          df["codigos_cie"].str.contains('M82')|
                                          df["codigos_cie"].str.contains('M831')|
                                          df["codigos_cie"].str.contains('M832')|
                                          df["codigos_cie"].str.contains('M833')|
                                          df["codigos_cie"].str.contains('M834')|
                                          df["codigos_cie"].str.contains('M835')|
                                          df["codigos_cie"].str.contains('M836')|
                                          df["codigos_cie"].str.contains('M837')|
                                          df["codigos_cie"].str.contains('M838')|
                                          df["codigos_cie"].str.contains('M839')|
                                          df["codigos_cie"].str.contains('M84')|
                                          df["codigos_cie"].str.contains('M85')|
                                          df["codigos_cie"].str.contains('M86')|
                                          df["codigos_cie"].str.contains('M87')|
                                          df["codigos_cie"].str.contains('M88')|
                                          df["codigos_cie"].str.contains('M89')|
                                          df["codigos_cie"].str.contains('M9'), 1, 0)
    # N00-N39
    df["enf_aparato_urinario"] = np.where(df["codigos_cie"].str.contains('N0')|
                                          df["codigos_cie"].str.contains('N1')|
                                          df["codigos_cie"].str.contains('N2')|
                                          df["codigos_cie"].str.contains('N3'), 1, 0)
    # N40-N50
    df["enf_org_genitales_masculinos"] = np.where(df["codigos_cie"].str.contains('N4')|
                                          df["codigos_cie"].str.contains('N50'), 1, 0)
    # N60-N64
    df["trastornos_mama"] = np.where(df["codigos_cie"].str.contains('N60')|
                                          df["codigos_cie"].str.contains('N61')|
                                          df["codigos_cie"].str.contains('N62')|
                                          df["codigos_cie"].str.contains('N63')|
                                          df["codigos_cie"].str.contains('N64'), 1, 0)
    # N70-N98
    df["enf_org_genitales_femeninos"] = np.where(df["codigos_cie"].str.contains('N7')|
                                          df["codigos_cie"].str.contains('N8')|
                                          df["codigos_cie"].str.contains('N90')|
                                          df["codigos_cie"].str.contains('N91')|
                                          df["codigos_cie"].str.contains('N92')|
                                          df["codigos_cie"].str.contains('N93')|
                                          df["codigos_cie"].str.contains('N94')|
                                          df["codigos_cie"].str.contains('N95')|
                                          df["codigos_cie"].str.contains('N96')|
                                          df["codigos_cie"].str.contains('N97')|
                                          df["codigos_cie"].str.contains('N98'), 1, 0)
    # N99 (solo para morbilidad)
    df["trastornos_sist_genitourinario_consec_proced"] = np.where(df["codigos_cie"].str.contains('N99'), 1, 0)
    # O00-O07,  (O08 no es causa de muerte), O10-O75, O85-O97,A34,F53,M83.0
    df["causas_obstetricas_directas"] = np.where(df["codigos_cie"].str.contains('O00')|
                                          df["codigos_cie"].str.contains('O01')|
                                          df["codigos_cie"].str.contains('O02')|
                                          df["codigos_cie"].str.contains('O03')|
                                          df["codigos_cie"].str.contains('O04')|
                                          df["codigos_cie"].str.contains('O05')|
                                          df["codigos_cie"].str.contains('O06')|
                                          df["codigos_cie"].str.contains('O07')|
                                          df["codigos_cie"].str.contains('O1')|
                                          df["codigos_cie"].str.contains('O2')|
                                          df["codigos_cie"].str.contains('O3')|
                                          df["codigos_cie"].str.contains('O4')|
                                          df["codigos_cie"].str.contains('O5')|
                                          df["codigos_cie"].str.contains('O6')|
                                          df["codigos_cie"].str.contains('O70')|
                                          df["codigos_cie"].str.contains('O71')|
                                          df["codigos_cie"].str.contains('O72')|
                                          df["codigos_cie"].str.contains('O73')|
                                          df["codigos_cie"].str.contains('O74')|
                                          df["codigos_cie"].str.contains('O75')|
                                          df["codigos_cie"].str.contains('O85')|
                                          df["codigos_cie"].str.contains('O86')|
                                          df["codigos_cie"].str.contains('O87')|
                                          df["codigos_cie"].str.contains('O88')|
                                          df["codigos_cie"].str.contains('O89')|
                                          df["codigos_cie"].str.contains('O90')|
                                          df["codigos_cie"].str.contains('O91')|
                                          df["codigos_cie"].str.contains('O92')|
                                          df["codigos_cie"].str.contains('O93')|
                                          df["codigos_cie"].str.contains('O94')|
                                          df["codigos_cie"].str.contains('O95')|
                                          df["codigos_cie"].str.contains('O96')|
                                          df["codigos_cie"].str.contains('O97')|
                                          df["codigos_cie"].str.contains('A34')|
                                          df["codigos_cie"].str.contains('F53')|
                                          df["codigos_cie"].str.contains('M830'), 1, 0)
    # O80 -O84
    df["parto"] = np.where(df["codigos_cie"].str.contains('O80')|
                                          df["codigos_cie"].str.contains('O81')|
                                          df["codigos_cie"].str.contains('O82')|
                                          df["codigos_cie"].str.contains('O83')|
                                          df["codigos_cie"].str.contains('O84'), 1, 0)
    # O98-O99
    df["causas_obstetricas_indirectas"] = np.where(df["codigos_cie"].str.contains('O98')|
                                          df["codigos_cie"].str.contains('O99'), 1, 0)
    # P00-P96, A33
    # df["Ciertas afecciones originadas en el período perinatal
    # Q00 - Q99
    df["malformaciones_congenitas"] = np.where(df["codigos_cie"].str.contains('Q'), 1, 0)
    # R00-R99 --> quitar en una prueba
    df["sintomas_signos_hallazgos_anormales_clin_lab_no_clasif"] = np.where(df["codigos_cie"].str.contains('R'), 1, 0)
    # S02,S12,S22,S32,S42,S52,S62,S72,S82, S92,T02,T08,T10,T12,T14.2
    df["fracturas"] = np.where(df["codigos_cie"].str.contains('S02')|
                                          df["codigos_cie"].str.contains('S12')|
                                          df["codigos_cie"].str.contains('S22')|
                                          df["codigos_cie"].str.contains('S32')|
                                          df["codigos_cie"].str.contains('S42')|
                                          df["codigos_cie"].str.contains('S52')|
                                          df["codigos_cie"].str.contains('S62')|
                                          df["codigos_cie"].str.contains('S72')|
                                          df["codigos_cie"].str.contains('S82')|
                                          df["codigos_cie"].str.contains('S92')|
                                          df["codigos_cie"].str.contains('T02')|
                                          df["codigos_cie"].str.contains('T08')|
                                          df["codigos_cie"].str.contains('T10')|
                                          df["codigos_cie"].str.contains('T12')|
                                          df["codigos_cie"].str.contains('T142'), 1, 0)
    # S03, S13, S23, S33, S43, S53, S63, S73,S83,S93,T03, T09.2, T11.2,T13.2,T14.3
    df["luxaciones_esguinces_torceduras"] = np.where(df["codigos_cie"].str.contains('S03')|
                                          df["codigos_cie"].str.contains('S13')|
                                          df["codigos_cie"].str.contains('S23')|
                                          df["codigos_cie"].str.contains('S33')|
                                          df["codigos_cie"].str.contains('S43')|
                                          df["codigos_cie"].str.contains('S53')|
                                          df["codigos_cie"].str.contains('S63')|
                                          df["codigos_cie"].str.contains('S73')|
                                          df["codigos_cie"].str.contains('S83')|
                                          df["codigos_cie"].str.contains('S93')|
                                          df["codigos_cie"].str.contains('T03')|
                                          df["codigos_cie"].str.contains('T092')|
                                          df["codigos_cie"].str.contains('T112')|
                                          df["codigos_cie"].str.contains('T132')|
                                          df["codigos_cie"].str.contains('T143'), 1, 0)
    # S90,S94-T00,T04-T07, T09,T11,T13,T14
    df["traumatismos_int_intracraneales_y_otr"] = np.where(df["codigos_cie"].str.contains('S90')|
                                          df["codigos_cie"].str.contains('S94')|
                                          df["codigos_cie"].str.contains('S95')|
                                          df["codigos_cie"].str.contains('S96')|
                                          df["codigos_cie"].str.contains('S97')|
                                          df["codigos_cie"].str.contains('S98')|
                                          df["codigos_cie"].str.contains('S99')|
                                          df["codigos_cie"].str.contains('T00')|
                                          df["codigos_cie"].str.contains('T04')|
                                          df["codigos_cie"].str.contains('T05')|
                                          df["codigos_cie"].str.contains('T06')|
                                          df["codigos_cie"].str.contains('T07')|
                                          df["codigos_cie"].str.contains('T09')|
                                          df["codigos_cie"].str.contains('T11')|
                                          df["codigos_cie"].str.contains('T13')|
                                          df["codigos_cie"].str.contains('T14'), 1, 0)
    # S01,S11,S21,S31,S41,S51,S61,S71,S81,S91,T01, T09.1,T11.1,T13.1,T14.1
    df["heridas"] = np.where(df["codigos_cie"].str.contains('S01')|
                                          df["codigos_cie"].str.contains('S11')|
                                          df["codigos_cie"].str.contains('S21')|
                                          df["codigos_cie"].str.contains('S31')|
                                          df["codigos_cie"].str.contains('S41')|
                                          df["codigos_cie"].str.contains('S51')|
                                          df["codigos_cie"].str.contains('S61')|
                                          df["codigos_cie"].str.contains('S71')|
                                          df["codigos_cie"].str.contains('S81')|
                                          df["codigos_cie"].str.contains('S91')|
                                          df["codigos_cie"].str.contains('T01')|
                                          df["codigos_cie"].str.contains('T091')|
                                          df["codigos_cie"].str.contains('T111')|
                                          df["codigos_cie"].str.contains('T131')|
                                          df["codigos_cie"].str.contains('T141'), 1, 0)
    # T15-T19
    df["efec_cuerpos_extr_pen_orificios_naturales"] = np.where(df["codigos_cie"].str.contains('T15')|
                                          df["codigos_cie"].str.contains('T16')|
                                          df["codigos_cie"].str.contains('T17')|
                                          df["codigos_cie"].str.contains('T18')|
                                          df["codigos_cie"].str.contains('T19'), 1, 0)
    # T20-T32
    df["quemaduras_corrosiones"] = np.where(df["codigos_cie"].str.contains('T2')|
                                          df["codigos_cie"].str.contains('T30')|
                                          df["codigos_cie"].str.contains('T31')|
                                          df["codigos_cie"].str.contains('T32'), 1, 0)
    # T36-T65
    df["envenenamiento_efectos_tox"] = np.where(df["codigos_cie"].str.contains('T36')|
                                          df["codigos_cie"].str.contains('T37')|
                                          df["codigos_cie"].str.contains('T38')|
                                          df["codigos_cie"].str.contains('T39')|
                                          df["codigos_cie"].str.contains('T4')|
                                          df["codigos_cie"].str.contains('T5')|
                                          df["codigos_cie"].str.contains('T60')|
                                          df["codigos_cie"].str.contains('T61')|
                                          df["codigos_cie"].str.contains('T62')|
                                          df["codigos_cie"].str.contains('T63')|
                                          df["codigos_cie"].str.contains('T64')|
                                          df["codigos_cie"].str.contains('T65'), 1, 0)
    # T74
    df["sindrome_maltrato"] = np.where(df["codigos_cie"].str.contains('T74'), 1, 0)
    # T79
    df["comp_precoces_traumatismos"] = np.where(df["codigos_cie"].str.contains('T79'), 1, 0)
    # T80-T88
    df["comp_aten_med_qx_no_clasif"] = np.where(df["codigos_cie"].str.contains('T80')|
                                          df["codigos_cie"].str.contains('T81')|
                                          df["codigos_cie"].str.contains('T82')|
                                          df["codigos_cie"].str.contains('T83')|
                                          df["codigos_cie"].str.contains('T84')|
                                          df["codigos_cie"].str.contains('T85')|
                                          df["codigos_cie"].str.contains('T86')|
                                          df["codigos_cie"].str.contains('T87')|
                                          df["codigos_cie"].str.contains('T88'), 1, 0)
    # T90-T98
    df["sec_traumatismos_envenenamiento_causas_ext"] = np.where(df["codigos_cie"].str.contains('T90')|
                                          df["codigos_cie"].str.contains('T91')|
                                          df["codigos_cie"].str.contains('T92')|
                                          df["codigos_cie"].str.contains('T93')|
                                          df["codigos_cie"].str.contains('T94')|
                                          df["codigos_cie"].str.contains('T95')|
                                          df["codigos_cie"].str.contains('T96')|
                                          df["codigos_cie"].str.contains('T97')|
                                          df["codigos_cie"].str.contains('T98'), 1, 0)
    # T33-T35,T66-T73,T75-T78
    df["ot_efec_causas_ext_comp_traumatismos"] = np.where(df["codigos_cie"].str.contains('T33')|
                                          df["codigos_cie"].str.contains('T34')|
                                          df["codigos_cie"].str.contains('T35')|
                                          df["codigos_cie"].str.contains('T66')|
                                          df["codigos_cie"].str.contains('T67')|
                                          df["codigos_cie"].str.contains('T68')|
                                          df["codigos_cie"].str.contains('T69')|
                                          df["codigos_cie"].str.contains('T70')|
                                          df["codigos_cie"].str.contains('T71')|
                                          df["codigos_cie"].str.contains('T72')|
                                          df["codigos_cie"].str.contains('T73')|
                                          df["codigos_cie"].str.contains('T75')|
                                          df["codigos_cie"].str.contains('T76')|
                                          df["codigos_cie"].str.contains('T77')|
                                          df["codigos_cie"].str.contains('T78'), 1, 0)
    
    # DIABETES
    # E10
    df["E10"] = np.where(df["codigos_cie"].str.contains('E10'), 1, 0)
    # E11
    df["E11"] = np.where(df["codigos_cie"].str.contains('E11'), 1, 0)
    # E12
    df["E12"] = np.where(df["codigos_cie"].str.contains('E12'), 1, 0)
    # E13
    df["E13"] = np.where(df["codigos_cie"].str.contains('E13'), 1, 0)
    # E14
    df["E14"] = np.where(df["codigos_cie"].str.contains('E14'), 1, 0)
        
    # ENFERMEDADES DEL HIGADO
    df['K70_K77'] = np.where(df['codigos_cie'].str.contains('K70')|
                             df['codigos_cie'].str.contains('K71')|
                             df['codigos_cie'].str.contains('K72')|
                             df['codigos_cie'].str.contains('K73')|
                             df['codigos_cie'].str.contains('K74')|
                             df['codigos_cie'].str.contains('K75')|
                             df['codigos_cie'].str.contains('K76')|
                             df['codigos_cie'].str.contains('K77'), 1, 0)
    
    # enfermedades endocrinas, nutricionales y metabolicas
    df['E0_E64'] = np.where(df['codigos_cie'].str.contains('E0')|
                            df["codigos_cie"].str.contains('E15')|
                            df["codigos_cie"].str.contains('E16')|
                            df["codigos_cie"].str.contains('E2')|
                            df["codigos_cie"].str.contains('E30')|
                            df["codigos_cie"].str.contains('E31')|
                            df["codigos_cie"].str.contains('E32')|
                            df["codigos_cie"].str.contains('E33')|
                            df["codigos_cie"].str.contains('E34')|
                            df["codigos_cie"].str.contains('E35')|
                            df["codigos_cie"].str.contains('E40')|
                            df["codigos_cie"].str.contains('E41')|
                            df["codigos_cie"].str.contains('E42')|
                            df["codigos_cie"].str.contains('E43')|
                            df["codigos_cie"].str.contains('E44')|
                            df["codigos_cie"].str.contains('E45')|
                            df["codigos_cie"].str.contains('E46')|
                            df["codigos_cie"].str.contains('E5')|
                            df["codigos_cie"].str.contains('E60')|
                            df["codigos_cie"].str.contains('E61')|
                            df["codigos_cie"].str.contains('E62')|
                            df["codigos_cie"].str.contains('E63')|
                            df["codigos_cie"].str.contains('E64'), 1, 0) 
    
    # OBESIDAD
    df['E65_E68'] = np.where(df['codigos_cie'].str.contains('E65')|
                             df["codigos_cie"].str.contains('E66')|
                             df["codigos_cie"].str.contains('E67')|
                             df["codigos_cie"].str.contains('E68'), 1, 0)
    #df['R635'] = np.where(df['codigos_cie'].str.contains('R635'), 1, 0)
                                                            
    # TRASTORNOS METABOLICOS
    df['E70_E90'] = np.where(df['codigos_cie'].str.contains('E7')|
                             df['codigos_cie'].str.contains('E8')|
                             df['codigos_cie'].str.contains('E9'), 1, 0)    
    
    # EMBARAZO
    df['O10_O16'] = np.where(df['codigos_cie'].str.contains('O10')|
                             df['codigos_cie'].str.contains('O11')|
                             df['codigos_cie'].str.contains('O12')|
                             df['codigos_cie'].str.contains('O13')|
                             df['codigos_cie'].str.contains('O14')|
                             df['codigos_cie'].str.contains('O15')|
                             df['codigos_cie'].str.contains('O16'), 1, 0)
    
    df['O22'] = np.where(df['codigos_cie'].str.contains('O22'), 1, 0)  
    df['O24'] = np.where(df['codigos_cie'].str.contains('O24'), 1, 0)  
    
    # ENFERMEDADES HIPERTENSIVAS
    df['I10_I15'] = np.where(df['codigos_cie'].str.contains('I10')|
                             df['codigos_cie'].str.contains('I11')|
                             df['codigos_cie'].str.contains('I12')|
                             df['codigos_cie'].str.contains('I13')|
                             df['codigos_cie'].str.contains('I15'), 1, 0)
                                                            
    # ARTERIOESCLEROSIS, ENVENENAMIENTO
    df['Y52_T46'] = np.where(df['codigos_cie'].str.contains('Y52')|
                             df['codigos_cie'].str.contains('T46'), 1, 0)
    # ENFERMEDADES DEL SISTEMA CIRCULATORIO     
    df['I6_I8'] = np.where(df["codigos_cie"].str.contains('I6')|   
                           df["codigos_cie"].str.contains('I7')|   
                           df["codigos_cie"].str.contains('I8'), 1, 0) 
        
    # SIGNOS Y SÍNTOMAS
    df['R0_R4'] = np.where(df["codigos_cie"].str.contains('R0')|   
                           df["codigos_cie"].str.contains('R1')|
                           df["codigos_cie"].str.contains('R2')|
                           df["codigos_cie"].str.contains('R3')|  
                           df["codigos_cie"].str.contains('R4'), 1, 0)
    
    # ----------------------------------------------------------------------------------------------------------
    df["enf_inf_intestinales"] = df['enf_inf_intestinales'].astype('category')
    df["tuberculosis"] = df['tuberculosis'].astype('category')
    df["ot_enf_bacterianas"] = df['ot_enf_bacterianas'].astype('category')
    df["inf_trans_pred_sexual"] = df['inf_trans_pred_sexual'].astype('category')
    df["ot_enf_inf_y_paras_y_efec_tardios"] = df['ot_enf_inf_y_paras_y_efec_tardios'].astype('category')
    df["enf_viricas"] = df['enf_viricas'].astype('category')
    df["rickettsiosis_y_ot_enf__protozoarios"] = df['rickettsiosis_y_ot_enf__protozoarios'].astype('category')
    df["tumores_malig_labio_bucal_faringe "] = df['tumores_malig_labio_bucal_faringe'].astype('category')
    df["tumores_malig_organos"] = df['tumores_malig_organos'].astype('category')
    df["tumores_malig_org_respiratorios_intratoracicos"] = df['tumores_malig_org_respiratorios_intratoracicos'].astype('category')
    df["tumores_malig_huesos_articulares_conjuntivo_piel_mama"] = df['tumores_malig_huesos_articulares_conjuntivo_piel_mama'].astype('category')
    df["tumores_malig_org_genitourinarios"] = df['tumores_malig_org_genitourinarios'].astype('category')
    df["tumores_malig_otros_sitios_ne"] = df['tumores_malig_otros_sitios_ne'].astype('category')
    df["tumores_malig_tejido_linf_org_hematop"] = df['tumores_malig_tejido_linf_org_hematop'].astype('category')
    df["tumores_malig_sitios_mul_indep"] = df['tumores_malig_sitios_mul_indep'].astype('category')
    df["tumores_insitu"] = df['tumores_insitu'].astype('category')
    df["tumores_benignos"] = df['tumores_benignos'].astype('category')
    df["tumores_comp_incierto_desc"] = df['tumores_comp_incierto_desc'].astype('category')
    df["enf_sangre_org_hematop"] = df['enf_sangre_org_hematop'].astype('category')
    df["enf_endocrinas"] = df['enf_endocrinas'].astype('category')
    df["desnutricion_ot_deficiencias"] = df['desnutricion_ot_deficiencias'].astype('category')
    df["trastornos_mentales"] = df['trastornos_mentales'].astype('category')
    df["enf_sist_nervioso"] = df['enf_sist_nervioso'].astype('category')
    df["enf_ojo_anexos"] = df['enf_ojo_anexos'].astype('category')
    df["enf_oido_apofisis_mastoides"] = df['enf_oido_apofisis_mastoides'].astype('category')
    df["fiebre_y_enf_cardiacas_reumaticas"] = df['fiebre_y_enf_cardiacas_reumaticas'].astype('category')
    df["enf_hipertensivas"] = df['enf_hipertensivas'].astype('category')
    df["enf_isquemicas_corazon"] = df['enf_isquemicas_corazon'].astype('category')
    df["enf_circulacion_pulmonar_enf_corazon"] = df['enf_circulacion_pulmonar_enf_corazon'].astype('category')
    df["enf_cerebrovasculares"] = df['enf_cerebrovasculares'].astype('category')
    df["otras_enf_aparato_vasc"] = df['otras_enf_aparato_vasc'].astype('category')
    df["inf_y_enf_vias_respiratorias_sup"] = df['inf_y_enf_vias_respiratorias_sup'].astype('category')
    df["otras_enf_aparato_resp"] = df['otras_enf_aparato_resp'].astype('category')
    df["enf_cavidad_bucal_glandulas_salivales"] = df['enf_cavidad_bucal_glandulas_salivales'].astype('category')
    df["enf_ot_partes_aparato_digestivo"] = df['enf_ot_partes_aparato_digestivo'].astype('category')
    df["enf_piel_tejido_subcutaneo"] = df['enf_piel_tejido_subcutaneo'].astype('category')
    df["enf_sist_osteomuscular_y_tejido"] = df['enf_sist_osteomuscular_y_tejido'].astype('category')
    df["enf_aparato_urinario"] = df['enf_aparato_urinario'].astype('category')
    df["enf_org_genitales_masculinos"] = df['enf_org_genitales_masculinos'].astype('category')
    df["trastornos_mama"] = df['trastornos_mama'].astype('category')
    df["enf_org_genitales_femeninos"] = df['enf_org_genitales_femeninos'].astype('category')
    df["trastornos_sist_genitourinario_consec_proced"] = df['trastornos_sist_genitourinario_consec_proced'].astype('category')
    df["causas_obstetricas_directas"] = df['causas_obstetricas_directas'].astype('category')
    df["parto"] = df['parto'].astype('category')
    df["causas_obstetricas_indirectas"] = df['causas_obstetricas_indirectas'].astype('category')
    #Ciertas afecciones originadas en el período perinatal"] = df['período'].astype('category')
    df["malformaciones_congenitas"] = df['malformaciones_congenitas'].astype('category')
    df["sintomas_signos_hallazgos_anormales_clin_lab_no_clasif"] = df['sintomas_signos_hallazgos_anormales_clin_lab_no_clasif'].astype('category')
    df["fracturas"] = df['fracturas'].astype('category')
    df["luxaciones_esguinces_torceduras"] = df['luxaciones_esguinces_torceduras'].astype('category')
    df["traumatismos_int_intracraneales_y_otr"] = df['traumatismos_int_intracraneales_y_otr'].astype('category')
    df["heridas"] = df['heridas'].astype('category')
    df["efec_cuerpos_extr_pen_orificios_naturales"] = df['efec_cuerpos_extr_pen_orificios_naturales'].astype('category')
    df["quemaduras_corrosiones"] = df['quemaduras_corrosiones'].astype('category')
    df["envenenamiento_efectos_tox"] = df['envenenamiento_efectos_tox'].astype('category')
    df["sindrome_maltrato"] = df['sindrome_maltrato'].astype('category')
    df["comp_precoces_traumatismos"] = df['comp_precoces_traumatismos'].astype('category')
    df["comp_aten_med_qx_no_clasif"] = df['comp_aten_med_qx_no_clasif'].astype('category')
    df["sec_traumatismos_envenenamiento_causas_ext"] = df['sec_traumatismos_envenenamiento_causas_ext'].astype('category')
    df["ot_efec_causas_ext_comp_traumatismos"] = df['ot_efec_causas_ext_comp_traumatismos'].astype('category')

    # E10
    df["E10"] = df['E10'].astype('category')
    # E11
    df["E11"] = df['E11'].astype('category')
    # E12
    df["E12"] = df['E12'].astype('category')
    # E13
    df["E13"] = df['E13'].astype('category')
    # E14
    df["E14"] = df['E14'].astype('category')
    
    # enf hígado
    df['K70_K77'] = df['K70_K77'].astype('category')
                                                            
    # enfermedades endocrinas, nutricionales y metabolicas
    df['E0_E64'] = df['E0_E64'].astype('category')
    
    #obses
    df['E65_E68'] = df['E65_E68'].astype('category')
    #df['R635'] = df['R635'].astype('category')   
                                                            
    # TRASTORNOS METABOLICOS
    df['E70_E90'] = df['E70_E90'].astype('category')
              
    # EMBARAZO
    df['O10_O16'] = df['O10_O16'].astype('category')
    df['O22'] = df['O22'].astype('category')
    df['O24'] = df['O24'].astype('category')                                                        
    
    # enf hipertensivas
    df['I10_I15'] = df['I10_I15'].astype('category')
                                                            
    # arteriosc ENVEN
    df['Y52_T46'] = df['Y52_T46'].astype('category')
                                              
    # CIRCULATORIAS
    df['I6_I8'] = df['I6_I8'].astype('category')    
    
    df['R0_R4'] = df['R0_R4'].astype('category')
    
    return df


def medicine_cat(df,df_m):
    """Convert a number into a human readable format."""
      
    df['g1'] = 0
    df['g2'] = 0
    df['g3'] = 0
    df['g4'] = 0
    df['g5'] = 0
    df['g6'] = 0
    df['g7'] = 0
    df['g8'] = 0
    df['g9'] = 0
    df['g10'] = 0
    df['g11'] = 0
    df['g12'] = 0
    df['g13'] = 0
    df['g14'] = 0
    df['g15'] = 0
    df['g16'] = 0
    df['g17'] = 0
    df['g18'] = 0
    df['g19'] = 0
    df['g20'] = 0
    df['g21'] = 0
    df['g22'] = 0
    df['g23'] = 0
    
    for i in range(len(df_m['ID_PRODUCTO'])):
        x = str(df_m['ID_PRODUCTO'][i])
        #print(x)
        for j in range(len(df['cx_curp'])):            
            m = str(df['cod_med'][j])
            #print(m)
            if(~pd.isna(m) and m!='nan'):
                if x in str(m):
                    
                    df['g1'][j] = df_m['g1'][i] + df['g1'][j]
                    df['g2'][j] = df_m['g2'][i] + df['g2'][j]
                    df['g3'][j] = df_m['g3'][i] + df['g3'][j]
                    df['g4'][j] = df_m['g4'][i] + df['g4'][j]
                    df['g5'][j] = df_m['g5'][i] + df['g5'][j]
                    df['g6'][j] = df_m['g6'][i] + df['g6'][j]
                    df['g7'][j] = df_m['g7'][i] + df['g7'][j]
                    df['g8'][j] = df_m['g8'][i] + df['g8'][j]
                    df['g9'][j] = df_m['g9'][i] + df['g9'][j]
                    df['g10'][j] = df_m['g10'][i] + df['g10'][j]
                    df['g11'][j] = df_m['g11'][i] + df['g11'][j]
                    df['g12'][j] = df_m['g12'][i] + df['g12'][j]
                    df['g13'][j] = df_m['g13'][i] + df['g13'][j]
                    df['g14'][j] = df_m['g14'][i] + df['g14'][j]
                    df['g15'][j] = df_m['g15'][i] + df['g15'][j]
                    df['g16'][j] = df_m['g16'][i] + df['g16'][j]
                    df['g17'][j] = df_m['g17'][i] + df['g17'][j]
                    df['g18'][j] = df_m['g18'][i] + df['g18'][j]
                    df['g19'][j] = df_m['g19'][i] + df['g19'][j]
                    df['g20'][j] = df_m['g20'][i] + df['g20'][j]
                    df['g21'][j] = df_m['g21'][i] + df['g21'][j]
                    df['g22'][j] = df_m['g22'][i] + df['g22'][j]
                    df['g23'][j] = df_m['g23'][i] + df['g23'][j]
    return df


def clas_med(df,df_vac):
    
    df['ACIDIFICANTES DE LAS VIAS URINARIAS'] = 0
    df['ACTIVADORES DEL METABOLISMO NEURONAL'] = 0
    df['ADRENERGICOS'] = 0
    df['ADYUVANTES DE LA ANALGESIA'] = 0
    df['ANALGESICOS'] = 0
    df['ANALGESICOS ANTIINFLAMATORIOS TOPICOS'] = 0
    df['ANESTESICOS GENERALES'] = 0
    df['ANESTESICOS LOCALES'] = 0
    df['ANSIOLITICOS'] = 0
    df['ANTAGONISTAS'] = 0
    df['ANTIACIDOS'] = 0
    df['ANTIADRENERGICOS'] = 0
    df['ANTIALCOHOL'] = 0
    df['ANTIALERGICOS'] = 0
    df['ANTIAMEBIANOS'] = 0
    df['ANTIANEMICOS'] = 0
    df['ANTIANGINOSOS'] = 0
    df['ANTIARRITMICOS'] = 0
    df['ANTIARTRITICOS'] = 0
    df['ANTIASMATICOS'] = 0
    df['ANTICOAGULANTES'] = 0
    df['ANTICOLINERGICOS'] = 0
    df['ANTICONCEPTIVOS'] = 0
    df['ANTIDEPRESIVOS'] = 0
    df['ANTIDIABETICOS'] = 0
    df['ANTIDIARREICOS'] = 0
    df['ANTIDISFUNCION ERECTIL'] = 0
    df['ANTIDOTOS'] = 0
    df['ANTIEMETICOS'] = 0
    df['ANTIEMETICOS Y ANTIVERTIGINOSOS'] = 0
    df['ANTIENURESIS'] = 0
    df['ANTIEPILEPTICOS'] = 0
    df['ANTIESPASMODICOS'] = 0
    df['ANTIESPASMODICOS DE VIAS URINARIAS'] = 0
    df['ANTIESTROGENOS'] = 0
    df['ANTIFLATULENTOS'] = 0
    df['ANTIGOTOSOS'] = 0
    df['ANTIGRIPALES'] = 0
    df['ANTIHELMINTICOS'] = 0
    df['ANTIHIPERPROLACTINEMICOS'] = 0
    df['ANTIHIPERTENSIVOS'] = 0
    df['ANTIHISTAMINICOS'] = 0
    df['ANTIINFLAMATORIOS'] = 0
    df['ANTILEPROSOS'] = 0
    df['ANTIMICOTICOS'] = 0
    df['ANTIMICROBIANOS'] = 0
    df['ANTIMICROBIANOS OTICOS'] = 0
    df['ANTIMIGRANOSOS'] = 0
    df['ANTINEOPLASICOS'] = 0
    df['ANTINICOTINICOS'] = 0
    df['ANTIOBESIDAD'] = 0
    df['ANTIOSTEOPOROSICOS'] = 0
    df['ANTIPALUDICOS'] = 0
    df['ANTIPARASITARIOS VAGINALES'] = 0
    df['ANTIPARKINSONIANOS'] = 0
    df['ANTIPROSTATICOS'] = 0
    df['ANTIPROTOZOARIOS'] = 0
    df['ANTIPSICOTICOS'] = 0
    df['ANTIRREUMATICOS'] = 0
    df['ANTISEPTICOS'] = 0
    df['ANTISEPTICOS URINARIOS'] = 0
    df['ANTITABAQUISMO'] = 0
    df['ANTITIROIDEOS'] = 0
    df['ANTITUBERCULOSOS'] = 0
    df['ANTITUSIGENOS'] = 0
    df['ANTIULCEROSOS'] = 0
    df['ANTIVERTIGINOSOS'] = 0
    df['ANTIVIRALES'] = 0
    df['BRONCODILATADORES'] = 0
    df['COAGULANTES'] = 0
    df['COLINERGICOS'] = 0
    df['CORTICOSTEROIDES'] = 0
    df['DERMATOLOGICOS'] = 0
    df['DESINFECTANTES'] = 0
    df['DIURETICOS'] = 0
    df['DOPAMINERGICOS'] = 0
    df['ELECTROLITOS ORALES'] = 0
    df['ESTIMULANTES DE GRANULOCITOS'] = 0
    df['ESTIMULANTES DE LA CONTRACTILIDAD UTERINA'] = 0
    df['ESTIMULANTES DE LA MOTILIDAD UTERINA'] = 0
    df['EXPECTORANTES'] = 0
    df['GLUCOSIDOS CARDIACOS'] = 0
    df['HEMATOPOYETICOS'] = 0
    df['HIPOCALCEMICOS'] = 0
    df['HIPOLIPEMIANTES'] = 0
    df['HORMONAS'] = 0
    df['INDUCTORES DE LA OVULACION'] = 0
    df['INMUNODEPRESORES'] = 0
    df['INMUNOGLOBULINAS'] = 0
    df['LAXANTES'] = 0
    df['LITOLITICOS'] = 0
    df['MINERALES'] = 0
    df['NEUROPROTECTORES'] = 0
    df['OFTALMICOS'] = 0
    df['OTROS INOTROPICOS POSITIVOS'] = 0
    df['OXITOCICOS'] = 0
    df['PROCINETICOS GASTROINTESTINALES'] = 0
    df['RELAJANTES MUSCULARES'] = 0
    df['RELAJANTES VASCULARES'] = 0
    df['SEDANTES HIPNOTICOS'] = 0
    df['SOLUCIONES ELECTROLITICAS'] = 0
    df['SUEROS INMUNITARIOS'] = 0
    df['TOXOIDES'] = 0
    df['TROMBOLITICOS'] = 0
    df['VACUNAS'] = 0
    df['VASOPRESORES'] = 0
    df['VITAMINAS'] = 0
    df['GAS MEDICINAL'] = 0
    df['FORMULA POLIMERICA'] = 0

    for i in range(len(df['medicamentos'])):
        x = str(df['medicamentos'][i])
        
        for j in range(len(df_vac['med1'])):            
            num_m = df_vac['num_med'][j]
            m1 = str(df_vac['med1'][j])
            m2 = str(df_vac['med2'][j])
            m3 = str(df_vac['med3'][j])
            #m4 = str(df_vac['med4'][j])          
            """
            print('m1: ',m1)
            print('m2: ',m2)
            print('m3: ',m3)
            print('x1: ', x.find(m1))
            print('x2: ', x.find(m2))
            print('x3: ', x.find(m3))
            """
            flag = 0
            
            if(num_m == 1 and (x.find(m1) != -1) and (~pd.isna(m1))):
                #df[str(df_vac['med1'])] = 1
                flag = 1
                
            if(num_m == 2 and (x.find(m1) != -1) and (~pd.isna(m1)) and \
               (x.find(m2) != -1) and (~pd.isna(m2))):                
                #df[str(df_vac['med1'])] = 1
                #df[str(df_vac['med2'])] = 1
                flag = 1
                
            if(num_m == 3 and (x.find(m1) != -1) and (~pd.isna(m1)) and \
               (x.find(m2) != -1) and (~pd.isna(m2)) and \
               (x.find(m3) != -1) and (~pd.isna(m3))):                   
                #df[str(df_vac['med1'])] = 1
                #df[str(df_vac['med2'])] = 1
                #df[str(df_vac['med3'])] = 1
                flag = 1
            
            if (flag == 1):
                if(df['ACIDIFICANTES DE LAS VIAS URINARIAS'][i] ==0): 
                    df['ACIDIFICANTES DE LAS VIAS URINARIAS'][i] = df_vac['ACIDIFICANTES DE LAS VIAS URINARIAS'][j]
                if(df['ACTIVADORES DEL METABOLISMO NEURONAL'][i] ==0): 
                    df['ACTIVADORES DEL METABOLISMO NEURONAL'][i] = df_vac['ACTIVADORES DEL METABOLISMO NEURONAL'][j]
                if(df['ADRENERGICOS'][i] ==0): 
                    df['ADRENERGICOS'][i] = df_vac['ADRENERGICOS'][j]
                if(df['ADYUVANTES DE LA ANALGESIA'][i] ==0): 
                    df['ADYUVANTES DE LA ANALGESIA'][i] = df_vac['ADYUVANTES DE LA ANALGESIA'][j]
                if(df['ANALGESICOS'][i] ==0): 
                    df['ANALGESICOS'][i] = df_vac['ANALGESICOS'][j]
                if(df['ANALGESICOS ANTIINFLAMATORIOS TOPICOS'][i] ==0): 
                    df['ANALGESICOS ANTIINFLAMATORIOS TOPICOS'][i] = df_vac['ANALGESICOS ANTIINFLAMATORIOS TOPICOS'][j]
                if(df['ANESTESICOS GENERALES'][i] ==0): 
                    df['ANESTESICOS GENERALES'][i] = df_vac['ANESTESICOS GENERALES'][j]
                if(df['ANESTESICOS LOCALES'][i] ==0): 
                    df['ANESTESICOS LOCALES'][i] = df_vac['ANESTESICOS LOCALES'][j]
                if(df['ANSIOLITICOS'][i] ==0): 
                    df['ANSIOLITICOS'][i] = df_vac['ANSIOLITICOS'][j]
                if(df['ANTAGONISTAS'][i] ==0): 
                    df['ANTAGONISTAS'][i] = df_vac['ANTAGONISTAS'][j]
                if(df['ANTIACIDOS'][i] ==0): 
                    df['ANTIACIDOS'][i] = df_vac['ANTIACIDOS'][j]
                if(df['ANTIADRENERGICOS'][i] ==0): 
                    df['ANTIADRENERGICOS'][i] = df_vac['ANTIADRENERGICOS'][j]
                if(df['ANTIALCOHOL'][i] ==0): 
                    df['ANTIALCOHOL'][i] = df_vac['ANTIALCOHOL'][j]
                if(df['ANTIALERGICOS'][i] ==0): 
                    df['ANTIALERGICOS'][i] = df_vac['ANTIALERGICOS'][j]
                if(df['ANTIAMEBIANOS'][i] ==0): 
                    df['ANTIAMEBIANOS'][i] = df_vac['ANTIAMEBIANOS'][j]
                if(df['ANTIANEMICOS'][i] ==0): 
                    df['ANTIANEMICOS'][i] = df_vac['ANTIANEMICOS'][j]
                if(df['ANTIANGINOSOS'][i] ==0): 
                    df['ANTIANGINOSOS'][i] = df_vac['ANTIANGINOSOS'][j]
                if(df['ANTIARRITMICOS'][i] ==0): 
                    df['ANTIARRITMICOS'][i] = df_vac['ANTIARRITMICOS'][j]
                if(df['ANTIARTRITICOS'][i] ==0): 
                    df['ANTIARTRITICOS'][i] = df_vac['ANTIARTRITICOS'][j]
                if(df['ANTIASMATICOS'][i] ==0): 
                    df['ANTIASMATICOS'][i] = df_vac['ANTIASMATICOS'][j]
                if(df['ANTICOAGULANTES'][i] ==0): 
                    df['ANTICOAGULANTES'][i] = df_vac['ANTICOAGULANTES'][j]
                if(df['ANTICOLINERGICOS'][i] ==0): 
                    df['ANTICOLINERGICOS'][i] = df_vac['ANTICOLINERGICOS'][j]
                if(df['ANTICONCEPTIVOS'][i] ==0): 
                    df['ANTICONCEPTIVOS'][i] = df_vac['ANTICONCEPTIVOS'][j]
                if(df['ANTIDEPRESIVOS'][i] ==0): 
                    df['ANTIDEPRESIVOS'][i] = df_vac['ANTIDEPRESIVOS'][j]
                if(df['ANTIDIABETICOS'][i] ==0): 
                    df['ANTIDIABETICOS'][i] = df_vac['ANTIDIABETICOS'][j]
                if(df['ANTIDIARREICOS'][i] ==0): 
                    df['ANTIDIARREICOS'][i] = df_vac['ANTIDIARREICOS'][j]
                if(df['ANTIDISFUNCION ERECTIL'][i] ==0): 
                    df['ANTIDISFUNCION ERECTIL'][i] = df_vac['ANTIDISFUNCION ERECTIL'][j]
                if(df['ANTIDOTOS'][i] ==0): 
                    df['ANTIDOTOS'][i] = df_vac['ANTIDOTOS'][j]
                if(df['ANTIEMETICOS'][i] ==0): 
                    df['ANTIEMETICOS'][i] = df_vac['ANTIEMETICOS'][j]
                if(df['ANTIEMETICOS Y ANTIVERTIGINOSOS'][i] ==0): 
                    df['ANTIEMETICOS Y ANTIVERTIGINOSOS'][i] = df_vac['ANTIEMETICOS Y ANTIVERTIGINOSOS'][j]
                if(df['ANTIENURESIS'][i] ==0): 
                    df['ANTIENURESIS'][i] = df_vac['ANTIENURESIS'][j]
                if(df['ANTIEPILEPTICOS'][i] ==0): 
                    df['ANTIEPILEPTICOS'][i] = df_vac['ANTIEPILEPTICOS'][j]
                if(df['ANTIESPASMODICOS'][i] ==0): 
                    df['ANTIESPASMODICOS'][i] = df_vac['ANTIESPASMODICOS'][j]
                if(df['ANTIESPASMODICOS DE VIAS URINARIAS'][i] ==0): 
                    df['ANTIESPASMODICOS DE VIAS URINARIAS'][i] = df_vac['ANTIESPASMODICOS DE VIAS URINARIAS'][j]
                if(df['ANTIESTROGENOS'][i] ==0): 
                    df['ANTIESTROGENOS'][i] = df_vac['ANTIESTROGENOS'][j]
                if(df['ANTIFLATULENTOS'][i] ==0): 
                    df['ANTIFLATULENTOS'][i] = df_vac['ANTIFLATULENTOS'][j]
                if(df['ANTIGOTOSOS'][i] ==0): 
                    df['ANTIGOTOSOS'][i] = df_vac['ANTIGOTOSOS'][j]
                if(df['ANTIGRIPALES'][i] ==0): 
                    df['ANTIGRIPALES'][i] = df_vac['ANTIGRIPALES'][j]
                if(df['ANTIHELMINTICOS'][i] ==0): 
                    df['ANTIHELMINTICOS'][i] = df_vac['ANTIHELMINTICOS'][j]
                if(df['ANTIHIPERPROLACTINEMICOS'][i] ==0): 
                    df['ANTIHIPERPROLACTINEMICOS'][i] = df_vac['ANTIHIPERPROLACTINEMICOS'][j]
                if(df['ANTIHIPERTENSIVOS'][i] ==0): 
                    df['ANTIHIPERTENSIVOS'][i] = df_vac['ANTIHIPERTENSIVOS'][j]
                if(df['ANTIHISTAMINICOS'][i] ==0): 
                    df['ANTIHISTAMINICOS'][i] = df_vac['ANTIHISTAMINICOS'][j]
                if(df['ANTIINFLAMATORIOS'][i] ==0): 
                    df['ANTIINFLAMATORIOS'][i] = df_vac['ANTIINFLAMATORIOS'][j]
                if(df['ANTILEPROSOS'][i] ==0): 
                    df['ANTILEPROSOS'][i] = df_vac['ANTILEPROSOS'][j]
                if(df['ANTIMICOTICOS'][i] ==0): 
                    df['ANTIMICOTICOS'][i] = df_vac['ANTIMICOTICOS'][j]
                if(df['ANTIMICROBIANOS'][i] ==0): 
                    df['ANTIMICROBIANOS'][i] = df_vac['ANTIMICROBIANOS'][j]
                if(df['ANTIMICROBIANOS OTICOS'][i] ==0): 
                    df['ANTIMICROBIANOS OTICOS'][i] = df_vac['ANTIMICROBIANOS OTICOS'][j]
                if(df['ANTIMIGRANOSOS'][i] ==0): 
                    df['ANTIMIGRANOSOS'][i] = df_vac['ANTIMIGRANOSOS'][j]
                if(df['ANTINEOPLASICOS'][i] ==0): 
                    df['ANTINEOPLASICOS'][i] = df_vac['ANTINEOPLASICOS'][j]
                if(df['ANTINICOTINICOS'][i] ==0): 
                    df['ANTINICOTINICOS'][i] = df_vac['ANTINICOTINICOS'][j]
                if(df['ANTIOBESIDAD'][i] ==0): 
                    df['ANTIOBESIDAD'][i] = df_vac['ANTIOBESIDAD'][j]
                if(df['ANTIOSTEOPOROSICOS'][i] ==0): 
                    df['ANTIOSTEOPOROSICOS'][i] = df_vac['ANTIOSTEOPOROSICOS'][j]
                if(df['ANTIPALUDICOS'][i] ==0): 
                    df['ANTIPALUDICOS'][i] = df_vac['ANTIPALUDICOS'][j]
                if(df['ANTIPARASITARIOS VAGINALES'][i] ==0): 
                    df['ANTIPARASITARIOS VAGINALES'][i] = df_vac['ANTIPARASITARIOS VAGINALES'][j]
                if(df['ANTIPARKINSONIANOS'][i] ==0): 
                    df['ANTIPARKINSONIANOS'][i] = df_vac['ANTIPARKINSONIANOS'][j]
                if(df['ANTIPROSTATICOS'][i] ==0): 
                    df['ANTIPROSTATICOS'][i] = df_vac['ANTIPROSTATICOS'][j]
                if(df['ANTIPROTOZOARIOS'][i] ==0): 
                    df['ANTIPROTOZOARIOS'][i] = df_vac['ANTIPROTOZOARIOS'][j]
                if(df['ANTIPSICOTICOS'][i] ==0): 
                    df['ANTIPSICOTICOS'][i] = df_vac['ANTIPSICOTICOS'][j]
                if(df['ANTIRREUMATICOS'][i] ==0): 
                    df['ANTIRREUMATICOS'][i] = df_vac['ANTIRREUMATICOS'][j]
                if(df['ANTISEPTICOS'][i] ==0): 
                    df['ANTISEPTICOS'][i] = df_vac['ANTISEPTICOS'][j]
                if(df['ANTISEPTICOS URINARIOS'][i] ==0): 
                    df['ANTISEPTICOS URINARIOS'][i] = df_vac['ANTISEPTICOS URINARIOS'][j]
                if(df['ANTITABAQUISMO'][i] ==0): 
                    df['ANTITABAQUISMO'][i] = df_vac['ANTITABAQUISMO'][j]
                if(df['ANTITIROIDEOS'][i] ==0): 
                    df['ANTITIROIDEOS'][i] = df_vac['ANTITIROIDEOS'][j]
                if(df['ANTITUBERCULOSOS'][i] ==0): 
                    df['ANTITUBERCULOSOS'][i] = df_vac['ANTITUBERCULOSOS'][j]
                if(df['ANTITUSIGENOS'][i] ==0): 
                    df['ANTITUSIGENOS'][i] = df_vac['ANTITUSIGENOS'][j]
                if(df['ANTIULCEROSOS'][i] ==0): 
                    df['ANTIULCEROSOS'][i] = df_vac['ANTIULCEROSOS'][j]
                if(df['ANTIVERTIGINOSOS'][i] ==0): 
                    df['ANTIVERTIGINOSOS'][i] = df_vac['ANTIVERTIGINOSOS'][j]
                if(df['ANTIVIRALES'][i] ==0): 
                    df['ANTIVIRALES'][i] = df_vac['ANTIVIRALES'][j]
                if(df['BRONCODILATADORES'][i] ==0): 
                    df['BRONCODILATADORES'][i] = df_vac['BRONCODILATADORES'][j]
                if(df['COAGULANTES'][i] ==0): 
                    df['COAGULANTES'][i] = df_vac['COAGULANTES'][j]
                if(df['COLINERGICOS'][i] ==0): 
                    df['COLINERGICOS'][i] = df_vac['COLINERGICOS'][j]
                if(df['CORTICOSTEROIDES'][i] ==0): 
                    df['CORTICOSTEROIDES'][i] = df_vac['CORTICOSTEROIDES'][j]
                if(df['DERMATOLOGICOS'][i] ==0): 
                    df['DERMATOLOGICOS'][i] = df_vac['DERMATOLOGICOS'][j]
                if(df['DESINFECTANTES'][i] ==0): 
                    df['DESINFECTANTES'][i] = df_vac['DESINFECTANTES'][j]
                if(df['DIURETICOS'][i] ==0): 
                    df['DIURETICOS'][i] = df_vac['DIURETICOS'][j]
                if(df['DOPAMINERGICOS'][i] ==0): 
                    df['DOPAMINERGICOS'][i] = df_vac['DOPAMINERGICOS'][j]
                if(df['ELECTROLITOS ORALES'][i] ==0): 
                    df['ELECTROLITOS ORALES'][i] = df_vac['ELECTROLITOS ORALES'][j]
                if(df['ESTIMULANTES DE GRANULOCITOS'][i] ==0): 
                    df['ESTIMULANTES DE GRANULOCITOS'][i] = df_vac['ESTIMULANTES DE GRANULOCITOS'][j]
                if(df['ESTIMULANTES DE LA CONTRACTILIDAD UTERINA'][i] ==0): 
                    df['ESTIMULANTES DE LA CONTRACTILIDAD UTERINA'][i] = df_vac['ESTIMULANTES DE LA CONTRACTILIDAD UTERINA'][j]
                if(df['ESTIMULANTES DE LA MOTILIDAD UTERINA'][i] ==0): 
                    df['ESTIMULANTES DE LA MOTILIDAD UTERINA'][i] = df_vac['ESTIMULANTES DE LA MOTILIDAD UTERINA'][j]
                if(df['EXPECTORANTES'][i] ==0): 
                    df['EXPECTORANTES'][i] = df_vac['EXPECTORANTES'][j]
                if(df['GLUCOSIDOS CARDIACOS'][i] ==0): 
                    df['GLUCOSIDOS CARDIACOS'][i] = df_vac['GLUCOSIDOS CARDIACOS'][j]
                if(df['HEMATOPOYETICOS'][i] ==0): 
                    df['HEMATOPOYETICOS'][i] = df_vac['HEMATOPOYETICOS'][j]
                if(df['HIPOCALCEMICOS'][i] ==0): 
                    df['HIPOCALCEMICOS'][i] = df_vac['HIPOCALCEMICOS'][j]
                if(df['HIPOLIPEMIANTES'][i] ==0): 
                    df['HIPOLIPEMIANTES'][i] = df_vac['HIPOLIPEMIANTES'][j]
                if(df['HORMONAS'][i] ==0): 
                    df['HORMONAS'][i] = df_vac['HORMONAS'][j]
                if(df['INDUCTORES DE LA OVULACION'][i] ==0): 
                    df['INDUCTORES DE LA OVULACION'][i] = df_vac['INDUCTORES DE LA OVULACION'][j]
                if(df['INMUNODEPRESORES'][i] ==0): 
                    df['INMUNODEPRESORES'][i] = df_vac['INMUNODEPRESORES'][j]
                if(df['INMUNOGLOBULINAS'][i] ==0): 
                    df['INMUNOGLOBULINAS'][i] = df_vac['INMUNOGLOBULINAS'][j]
                if(df['LAXANTES'][i] ==0): 
                    df['LAXANTES'][i] = df_vac['LAXANTES'][j]
                if(df['LITOLITICOS'][i] ==0): 
                    df['LITOLITICOS'][i] = df_vac['LITOLITICOS'][j]
                if(df['MINERALES'][i] ==0): 
                    df['MINERALES'][i] = df_vac['MINERALES'][j]
                if(df['NEUROPROTECTORES'][i] ==0): 
                    df['NEUROPROTECTORES'][i] = df_vac['NEUROPROTECTORES'][j]
                if(df['OFTALMICOS'][i] ==0): 
                    df['OFTALMICOS'][i] = df_vac['OFTALMICOS'][j]
                if(df['OTROS INOTROPICOS POSITIVOS'][i] ==0): 
                    df['OTROS INOTROPICOS POSITIVOS'][i] = df_vac['OTROS INOTROPICOS POSITIVOS'][j]
                if(df['OXITOCICOS'][i] ==0): 
                    df['OXITOCICOS'][i] = df_vac['OXITOCICOS'][j]
                if(df['PROCINETICOS GASTROINTESTINALES'][i] ==0): 
                    df['PROCINETICOS GASTROINTESTINALES'][i] = df_vac['PROCINETICOS GASTROINTESTINALES'][j]
                if(df['RELAJANTES MUSCULARES'][i] ==0): 
                    df['RELAJANTES MUSCULARES'][i] = df_vac['RELAJANTES MUSCULARES'][j]
                if(df['RELAJANTES VASCULARES'][i] ==0): 
                    df['RELAJANTES VASCULARES'][i] = df_vac['RELAJANTES VASCULARES'][j]
                if(df['SEDANTES HIPNOTICOS'][i] ==0): 
                    df['SEDANTES HIPNOTICOS'][i] = df_vac['SEDANTES HIPNOTICOS'][j]
                if(df['SOLUCIONES ELECTROLITICAS'][i] ==0): 
                    df['SOLUCIONES ELECTROLITICAS'][i] = df_vac['SOLUCIONES ELECTROLITICAS'][j]
                if(df['SUEROS INMUNITARIOS'][i] ==0): 
                    df['SUEROS INMUNITARIOS'][i] = df_vac['SUEROS INMUNITARIOS'][j]
                if(df['TOXOIDES'][i] ==0): 
                    df['TOXOIDES'][i] = df_vac['TOXOIDES'][j]
                if(df['TROMBOLITICOS'][i] ==0): 
                    df['TROMBOLITICOS'][i] = df_vac['TROMBOLITICOS'][j]
                if(df['VACUNAS'][i] ==0): 
                    df['VACUNAS'][i] = df_vac['VACUNAS'][j]
                if(df['VASOPRESORES'][i] ==0): 
                    df['VASOPRESORES'][i] = df_vac['VASOPRESORES'][j]
                if(df['VITAMINAS'][i] ==0): 
                    df['VITAMINAS'][i] = df_vac['VITAMINAS'][j]                    
                if(df['GAS MEDICINAL'][i] ==0): 
                    df['GAS MEDICINAL'][i] = df_vac['GAS MEDICINAL'][j]
                if(df['FORMULA POLIMERICA'][i] ==0): 
                    df['FORMULA POLIMERICA'][i] = df_vac['FORMULA POLIMERICA'][j]

                
                
    return df

