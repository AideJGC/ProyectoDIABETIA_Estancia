
# Functions for CIE 10 and Medicine

import pandas as pd 
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter
import pickle


def imc_calculo_range(imc):
    imc = imc.iloc[0]
    range_imc = np.nan
    #print("imc -> ",imc)
    if (imc < 18.5):
        range_imc = 'Bajo peso'
    elif (imc >= 18.5) & (imc < 25):
        range_imc = 'Peso normal'
    elif (imc >= 25  ) & (imc < 30):
        range_imc = 'Sobrepeso'
    elif (imc >= 30  ):
        range_imc = 'Obesidad'
    return range_imc

def dias_year(date):
    days = np.nan
    p = pd.Period(date)
    if p.is_leap_year:
        days = 366
    else:
        days = 365
        
    return days

def fecha_ini_fin(fecha_ini):
    # Crear variable de ventanas máximas o hacer referencia a la variable años de conuslta
    fecha_ini = pd.to_datetime(fecha_ini)
    fecha_ini = pd.Timestamp(fecha_ini)
    
    a_ini = fecha_ini+pd.to_timedelta(365, unit = 'D')
    a_inter = fecha_ini+pd.to_timedelta(2*365, unit = 'D')
    a_fin = fecha_ini+pd.to_timedelta(3*365, unit = 'D')
    
    i = a_ini.strftime('%Y-%m-%d')
    i_t = a_inter.strftime('%Y-%m-%d')
    f = a_fin.strftime('%Y-%m-%d')
    
    i = dias_year(i)
    i_t = dias_year(i_t)
    f = dias_year(f)    
    
    a_ini = fecha_ini+pd.to_timedelta(i, unit = 'D')
    a_inter = fecha_ini+pd.to_timedelta(i+i_t, unit = 'D')
    a_fin = fecha_ini+pd.to_timedelta(i+i_t+f, unit = 'D')
    
    return a_ini, a_inter, a_fin

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
    df["dm_insulinodep"] = np.where(df["codigos_cie"].str.contains('E10'), 1, 0)
    df["dm_insulinodep_coma"] = np.where(df["codigos_cie"].str.contains('E100'), 1, 0)
    df["dm_insulinodep_ceto"] = np.where(df["codigos_cie"].str.contains('E101'), 1, 0)
    df["dm_insulinodep_c_renal"] = np.where(df["codigos_cie"].str.contains('E102'), 1, 0)
    df["dm_insulinodep_c_oft"] = np.where(df["codigos_cie"].str.contains('E103'), 1, 0)
    df["dm_insulinodep_c_neu"] = np.where(df["codigos_cie"].str.contains('E104'), 1, 0)
    df["dm_insulinodep_c_cirp"] = np.where(df["codigos_cie"].str.contains('E105'), 1, 0)
    df["dm_insulinodep_c_esp"] = np.where(df["codigos_cie"].str.contains('E106'), 1, 0)
    df["dm_insulinodep_c_mult"] = np.where(df["codigos_cie"].str.contains('E107'), 1, 0)
    df["dm_insulinodep_c_ne"] = np.where(df["codigos_cie"].str.contains('E108'), 1, 0)
    df["dm_insulinodep_sin_mc"] = np.where(df["codigos_cie"].str.contains('E109','E10X'), 1, 0)
    # E11
    df["dm_no_insulinodep"] = np.where(df["codigos_cie"].str.contains('E11'), 1, 0)
    df["dm_no_insulinodep_coma"] = np.where(df["codigos_cie"].str.contains('E110'), 1, 0)
    df["dm_no_insulinodep_ceto"] = np.where(df["codigos_cie"].str.contains('E111'), 1, 0)
    df["dm_no_insulinodep_c_renal"] = np.where(df["codigos_cie"].str.contains('E112'), 1, 0)
    df["dm_no_insulinodep_c_oft"] = np.where(df["codigos_cie"].str.contains('E113'), 1, 0)
    df["dm_no_insulinodep_c_neu"] = np.where(df["codigos_cie"].str.contains('E114'), 1, 0)
    df["dm_no_insulinodep_c_cirp"] = np.where(df["codigos_cie"].str.contains('E115'), 1, 0)
    df["dm_no_insulinodep_c_esp"] = np.where(df["codigos_cie"].str.contains('E116'), 1, 0)
    df["dm_no_insulinodep_c_mult"] = np.where(df["codigos_cie"].str.contains('E117'), 1, 0)
    df["dm_no_insulinodep_c_ne"] = np.where(df["codigos_cie"].str.contains('E118'), 1, 0)
    df["dm_no_insulinodep_sin_mc"] = np.where(df["codigos_cie"].str.contains('E119','E11X'), 1, 0)
    # E12
    df["dm_asoc_desnutricion"] = np.where(df["codigos_cie"].str.contains('E12'), 1, 0)
    df["dm_asoc_desnutricion_coma"] = np.where(df["codigos_cie"].str.contains('E120'), 1, 0)
    df["dm_asoc_desnutricion_ceto"] = np.where(df["codigos_cie"].str.contains('E121'), 1, 0)
    df["dm_asoc_desnutricion_c_renal"] = np.where(df["codigos_cie"].str.contains('E122'), 1, 0)
    df["dm_asoc_desnutricion_c_oft"] = np.where(df["codigos_cie"].str.contains('E123'), 1, 0)
    df["dm_asoc_desnutricion_c_neu"] = np.where(df["codigos_cie"].str.contains('E124'), 1, 0)
    df["dm_asoc_desnutricion_c_cirp"] = np.where(df["codigos_cie"].str.contains('E125'), 1, 0)
    df["dm_asoc_desnutricion_c_esp"] = np.where(df["codigos_cie"].str.contains('E126'), 1, 0)
    df["dm_asoc_desnutricion_c_mult"] = np.where(df["codigos_cie"].str.contains('E127'), 1, 0)
    df["dm_asoc_desnutricion_c_ne"] = np.where(df["codigos_cie"].str.contains('E128'), 1, 0)
    df["dm_asoc_desnutricion_sin_mc"] = np.where(df["codigos_cie"].str.contains('E129','E12X'), 1, 0)
    # E13
    df["otras_dm"] = np.where(df["codigos_cie"].str.contains('E13'), 1, 0)
    df["otras_dm_coma"] = np.where(df["codigos_cie"].str.contains('E130'), 1, 0)
    df["otras_dm_ceto"] = np.where(df["codigos_cie"].str.contains('E131'), 1, 0)
    df["otras_dm_c_renal"] = np.where(df["codigos_cie"].str.contains('E132'), 1, 0)
    df["otras_dm_c_oft"] = np.where(df["codigos_cie"].str.contains('E133'), 1, 0)
    df["otras_dm_c_neu"] = np.where(df["codigos_cie"].str.contains('E134'), 1, 0)
    df["otras_dm_c_cirp"] = np.where(df["codigos_cie"].str.contains('E135'), 1, 0)
    df["otras_dm_c_esp"] = np.where(df["codigos_cie"].str.contains('E136'), 1, 0)
    df["otras_dm_c_mult"] = np.where(df["codigos_cie"].str.contains('E137'), 1, 0)
    df["otras_dm_c_ne"] = np.where(df["codigos_cie"].str.contains('E138'), 1, 0)
    df["otras_dm_sin_mc"] = np.where(df["codigos_cie"].str.contains('E139','E13X'), 1, 0)
    # E14
    df["dm_no_especificada"] = np.where(df["codigos_cie"].str.contains('E14'), 1, 0)
    df["dm_no_especificada_coma"] = np.where(df["codigos_cie"].str.contains('E140'), 1, 0)
    df["dm_no_especificada_ceto"] = np.where(df["codigos_cie"].str.contains('E141'), 1, 0)
    df["dm_no_especificada_c_renal"] = np.where(df["codigos_cie"].str.contains('E142'), 1, 0)
    df["dm_no_especificada_c_oft"] = np.where(df["codigos_cie"].str.contains('E143'), 1, 0)
    df["dm_no_especificada_c_neu"] = np.where(df["codigos_cie"].str.contains('E144'), 1, 0)
    df["dm_no_especificada_c_cirp"] = np.where(df["codigos_cie"].str.contains('E145'), 1, 0)
    df["dm_no_especificada_c_esp"] = np.where(df["codigos_cie"].str.contains('E146'), 1, 0)
    df["dm_no_especificada_c_mult"] = np.where(df["codigos_cie"].str.contains('E147'), 1, 0)
    df["dm_no_especificada_c_ne"] = np.where(df["codigos_cie"].str.contains('E148'), 1, 0)
    df["dm_no_especificada_sin_mc"] = np.where(df["codigos_cie"].str.contains('E149','E14X'), 1, 0)
    
    # Enfermedades del sistema genitourinario
    df['sind_nefritico_ag'] = np.where(df['codigos_cie'].str.contains('N00'), 1, 0)
    df['sind_nefritico_progr'] = np.where(df['codigos_cie'].str.contains('N01'), 1, 0)
    df['hematuria_recur_persist'] = np.where(df['codigos_cie'].str.contains('N02'), 1, 0)
    df['sind_nefritico_cron'] = np.where(df['codigos_cie'].str.contains('N03'), 1, 0)
    df['sind_nefrotico'] = np.where(df['codigos_cie'].str.contains('N04'), 1, 0)
    df['sind_nefritico_ne'] = np.where(df['codigos_cie'].str.contains('N05'), 1, 0)
    df['proteinuria_aislada_lesion_morfo_esp'] = np.where(df['codigos_cie'].str.contains('N06'), 1, 0)
    df['nefropatia_hereditaria_no_c_ot_part'] = np.where(df['codigos_cie'].str.contains('N07'), 1, 0)
    df['trast_glomerulares_enf_c_ot_part'] = np.where(df['codigos_cie'].str.contains('N08'), 1, 0)
    df['nefritis_tubuloint_aguda'] = np.where(df['codigos_cie'].str.contains('N10'), 1, 0)
    df['nefritis_tubuloint_cronica'] = np.where(df['codigos_cie'].str.contains('N11'), 1, 0)
    df['nefritis_tubuloint_ne_aguda_cronica'] = np.where(df['codigos_cie'].str.contains('N12'), 1, 0)
    df['uropatia_obstructiva_por_reflujo'] = np.where(df['codigos_cie'].str.contains('N13'), 1, 0)
    df['afecc_tub_tubuloint_drog_metp'] = np.where(df['codigos_cie'].str.contains('N14'), 1, 0)
    df['otras_enf_renales_tubuloint'] = np.where(df['codigos_cie'].str.contains('N15'), 1, 0)
    df['trast_renales_tubuloint_enf_c_ot_part'] = np.where(df['codigos_cie'].str.contains('N16'), 1, 0)
    df['insuficiencia_renal_aguda'] = np.where(df['codigos_cie'].str.contains('N17'), 1, 0)
    df['insuficiencia_renal_cronica'] = np.where(df['codigos_cie'].str.contains('N18'), 1, 0)
    df['insuficiencia_renal_ne'] = np.where(df['codigos_cie'].str.contains('N19'), 1, 0)
    df['calculo_riñon_ureter'] = np.where(df['codigos_cie'].str.contains('N20'), 1, 0)
    df['calculo_vias_urinarias_inferiores'] = np.where(df['codigos_cie'].str.contains('N21'), 1, 0)
    df['calculo_vias_urinarias_enf_c_ot_part'] = np.where(df['codigos_cie'].str.contains('N22'), 1, 0)
    df['colico_renal_ne'] = np.where(df['codigos_cie'].str.contains('N23'), 1, 0)
    df['trast_resul_fun_tub_renal_alt'] = np.where(df['codigos_cie'].str.contains('N25'), 1, 0)
    df['riñon_contraido_ne'] = np.where(df['codigos_cie'].str.contains('N26'), 1, 0)
    df['riñon_pequeño_causa_desconocida'] = np.where(df['codigos_cie'].str.contains('N27'), 1, 0)
    df['ot_trast_riñon_ureter_no_c_ot_part'] = np.where(df['codigos_cie'].str.contains('N28'), 1, 0)
    df['ot_trast_riñon_ureter_enf_c_ot_part'] = np.where(df['codigos_cie'].str.contains('N29'), 1, 0)
    df['cistitis'] = np.where(df['codigos_cie'].str.contains('N30'), 1, 0)
    df['disf_neuromusc_vejiga_no_c_ot_part'] = np.where(df['codigos_cie'].str.contains('N31'), 1, 0)
    df['ot_trast_vejiga'] = np.where(df['codigos_cie'].str.contains('N32'), 1, 0)
    df['trast_vejiga_enf_c_ot_part'] = np.where(df['codigos_cie'].str.contains('N33'), 1, 0)
    df['uretritis_sind_uretral'] = np.where(df['codigos_cie'].str.contains('N34'), 1, 0)
    df['estrechez_uretral'] = np.where(df['codigos_cie'].str.contains('N35'), 1, 0)
    df['ot_trast_uretra'] = np.where(df['codigos_cie'].str.contains('N36'), 1, 0)
    df['trast_uretra_enf_c_ot_part'] = np.where(df['codigos_cie'].str.contains('N37'), 1, 0)
    df['ot_trast_sistema_urinario'] = np.where(df['codigos_cie'].str.contains('N39'), 1, 0) 
    
    # ENFERMEDADES DEL HIGADO
    df['enf_alcoholica_higado'] = np.where(df['codigos_cie'].str.contains('K70'), 1, 0)
    df['enf_toxica_higado'] = np.where(df['codigos_cie'].str.contains('K71'), 1, 0)
    df['insuficiencia_hepatica_no_c_ot_part'] = np.where(df['codigos_cie'].str.contains('K72'), 1, 0)
    df['hepatitis_cronica_no_c_ot_part'] = np.where(df['codigos_cie'].str.contains('K73'), 1, 0)
    df['fibrosis_cirrosis_higado'] = np.where(df['codigos_cie'].str.contains('K74'), 1, 0)
    df['absceso_higado'] = np.where(df['codigos_cie'].str.contains('K750'), 1, 0)
    df['flebitis_de_la_vena_porta'] = np.where(df['codigos_cie'].str.contains('K751'), 1, 0)
    df['hepatitis_reactiva_no_especifica'] = np.where(df['codigos_cie'].str.contains('K752'), 1, 0)
    df['hepatitis_granulomatosa_no_c_ot_part'] = np.where(df['codigos_cie'].str.contains('K753'), 1, 0)
    df['hepatitis_autoinmune'] = np.where(df['codigos_cie'].str.contains('K754'), 1, 0)
    df['otras_enfes_inflamatorias_higado_esp'] = np.where(df['codigos_cie'].str.contains('K758'), 1, 0)
    df['enf_inflamatoria_higado_ne'] = np.where(df['codigos_cie'].str.contains('K759'), 1, 0)
    df['degeneracion_grasa_higado_no_c_ot_part'] = np.where(df['codigos_cie'].str.contains('K760'), 1, 0)
    df['congestion_pasiva_cronica_higado'] = np.where(df['codigos_cie'].str.contains('K761'), 1, 0)
    df['necrosis_hemorragica_central_higado'] = np.where(df['codigos_cie'].str.contains('K762'), 1, 0)
    df['infarto_higado'] = np.where(df['codigos_cie'].str.contains('K763'), 1, 0)
    df['peliosis_hepatica'] = np.where(df['codigos_cie'].str.contains('K764'), 1, 0)
    df['enf_veno_oclus_higado'] = np.where(df['codigos_cie'].str.contains('K765'), 1, 0)
    df['hipertension_portal'] = np.where(df['codigos_cie'].str.contains('K766'), 1, 0)
    df['sindrome_hepatorrenal'] = np.where(df['codigos_cie'].str.contains('K767'), 1, 0)
    df['otras_enfes_esp_higado'] = np.where(df['codigos_cie'].str.contains('K768'), 1, 0)
    df['enf_higado_ne'] = np.where(df['codigos_cie'].str.contains('K769'), 1, 0)
    
    # OBESIDAD
    df['adiposidad_localizada'] = np.where(df['codigos_cie'].str.contains('E65'), 1, 0)
    df['obesidad'] = np.where(df['codigos_cie'].str.contains('E66'), 1, 0)
    df['obesidad_exceso_calorias'] = np.where(df['codigos_cie'].str.contains('E660'), 1, 0)
    df['obesidad_por_drogas'] = np.where(df['codigos_cie'].str.contains('E661'), 1, 0)
    df['obesidad_extrema_hipov_alveolar'] = np.where(df['codigos_cie'].str.contains('E662'), 1, 0)
    df['obesidad_morbida'] = np.where(df['codigos_cie'].str.contains('E668'), 1, 0)
    df['obesidad_simple'] = np.where(df['codigos_cie'].str.contains('E669'), 1, 0)
    df['otra_hiperalimentacion'] = np.where(df['codigos_cie'].str.contains('E67'), 1, 0)
    df['hipervitaminosis_a'] = np.where(df['codigos_cie'].str.contains('E670'), 1, 0)
    df['hipercarotinemia'] = np.where(df['codigos_cie'].str.contains('E671'), 1, 0)
    df['sindrome_de_megavitamina_b6'] = np.where(df['codigos_cie'].str.contains('E672'), 1, 0)
    df['hipervitaminosis_d'] = np.where(df['codigos_cie'].str.contains('E673'), 1, 0)
    df['ot_hiperalimentacion_esp'] = np.where(df['codigos_cie'].str.contains('E678'), 1, 0)
    df['secuelas_hiperalimentacion'] = np.where(df['codigos_cie'].str.contains('E68'), 1, 0)
    df['hiperalimentacion'] = np.where(df['codigos_cie'].str.contains('R632'), 1, 0)
    df['aumento_anormal_peso'] = np.where(df['codigos_cie'].str.contains('R635'), 1, 0)
    df['aumento_excesivo_peso_embarazo'] = np.where(df['codigos_cie'].str.contains('O260'), 1, 0)
    
    # ENFERMEDADES HIPERTENSIVAS
    df['I10'] = np.where(df['codigos_cie'].str.contains('I10'), 1, 0)
    df['I110'] = np.where(df['codigos_cie'].str.contains('I110'), 1, 0)
    df['I119'] = np.where(df['codigos_cie'].str.contains('I119'), 1, 0)
    df['I120'] = np.where(df['codigos_cie'].str.contains('I120'), 1, 0)
    df['I129'] = np.where(df['codigos_cie'].str.contains('I129'), 1, 0)
    df['I130'] = np.where(df['codigos_cie'].str.contains('I130'), 1, 0)
    df['I131'] = np.where(df['codigos_cie'].str.contains('I131'), 1, 0)
    df['I132'] = np.where(df['codigos_cie'].str.contains('I132'), 1, 0)
    df['I139'] = np.where(df['codigos_cie'].str.contains('I139'), 1, 0)
    df['I151'] = np.where(df['codigos_cie'].str.contains('I151'), 1, 0)
    df['I152'] = np.where(df['codigos_cie'].str.contains('I152'), 1, 0)
    df['I158'] = np.where(df['codigos_cie'].str.contains('I158'), 1, 0)
    df['I159'] = np.where(df['codigos_cie'].str.contains('I159'), 1, 0)
    # ARTERIOESCLEROSIS
    df['Y526'] = np.where(df['codigos_cie'].str.contains('Y526'), 1, 0)
    df['I700'] = np.where(df['codigos_cie'].str.contains('I700'), 1, 0)
    df['I701'] = np.where(df['codigos_cie'].str.contains('I701'), 1, 0)
    df['I702'] = np.where(df['codigos_cie'].str.contains('I702'), 1, 0)
    df['I708'] = np.where(df['codigos_cie'].str.contains('I708'), 1, 0)
    df['I709'] = np.where(df['codigos_cie'].str.contains('I709'), 1, 0)
    df['T466'] = np.where(df['codigos_cie'].str.contains('T466'), 1, 0)
    
    # Trastornos metabólicos: DISLIPIDEMIAS y ALTERACIONES METÁBOLICAS
    df['E700'] = np.where(df['codigos_cie'].str.contains('E700'), 1, 0)
    df['E701'] = np.where(df['codigos_cie'].str.contains('E701'), 1, 0)
    df['E702'] = np.where(df['codigos_cie'].str.contains('E702'), 1, 0)
    df['E703'] = np.where(df['codigos_cie'].str.contains('E703'), 1, 0)
    df['E708'] = np.where(df['codigos_cie'].str.contains('E708'), 1, 0)
    df['E709'] = np.where(df['codigos_cie'].str.contains('E709'), 1, 0)
    df['E710'] = np.where(df['codigos_cie'].str.contains('E710'), 1, 0)
    df['E711'] = np.where(df['codigos_cie'].str.contains('E711'), 1, 0)
    df['E712'] = np.where(df['codigos_cie'].str.contains('E712'), 1, 0)
    df['E713'] = np.where(df['codigos_cie'].str.contains('E713'), 1, 0)
    df['E720'] = np.where(df['codigos_cie'].str.contains('E720'), 1, 0)
    df['E721'] = np.where(df['codigos_cie'].str.contains('E721'), 1, 0)
    df['E722'] = np.where(df['codigos_cie'].str.contains('E722'), 1, 0)
    df['E723'] = np.where(df['codigos_cie'].str.contains('E723'), 1, 0)
    df['E724'] = np.where(df['codigos_cie'].str.contains('E724'), 1, 0)
    df['E725'] = np.where(df['codigos_cie'].str.contains('E725'), 1, 0)
    df['E728'] = np.where(df['codigos_cie'].str.contains('E728'), 1, 0)
    df['E729'] = np.where(df['codigos_cie'].str.contains('E729'), 1, 0)
    df['E730'] = np.where(df['codigos_cie'].str.contains('E730'), 1, 0)
    df['E731'] = np.where(df['codigos_cie'].str.contains('E731'), 1, 0)
    df['E738'] = np.where(df['codigos_cie'].str.contains('E738'), 1, 0)
    df['E739'] = np.where(df['codigos_cie'].str.contains('E739'), 1, 0)
    df['E740'] = np.where(df['codigos_cie'].str.contains('E740'), 1, 0)
    df['E741'] = np.where(df['codigos_cie'].str.contains('E741'), 1, 0)
    df['E742'] = np.where(df['codigos_cie'].str.contains('E742'), 1, 0)
    df['E743'] = np.where(df['codigos_cie'].str.contains('E743'), 1, 0)
    df['E744'] = np.where(df['codigos_cie'].str.contains('E744'), 1, 0)
    df['E748'] = np.where(df['codigos_cie'].str.contains('E748'), 1, 0)
    df['E749'] = np.where(df['codigos_cie'].str.contains('E749'), 1, 0)
    df['E750'] = np.where(df['codigos_cie'].str.contains('E750'), 1, 0)
    df['E751'] = np.where(df['codigos_cie'].str.contains('E751'), 1, 0)
    df['E752'] = np.where(df['codigos_cie'].str.contains('E752'), 1, 0)
    df['E753'] = np.where(df['codigos_cie'].str.contains('E753'), 1, 0)
    df['E754'] = np.where(df['codigos_cie'].str.contains('E754'), 1, 0)
    df['E755'] = np.where(df['codigos_cie'].str.contains('E755'), 1, 0)
    df['E756'] = np.where(df['codigos_cie'].str.contains('E756'), 1, 0)
    df['E760'] = np.where(df['codigos_cie'].str.contains('E760'), 1, 0)
    df['E761'] = np.where(df['codigos_cie'].str.contains('E761'), 1, 0)
    df['E762'] = np.where(df['codigos_cie'].str.contains('E762'), 1, 0)
    df['E763'] = np.where(df['codigos_cie'].str.contains('E763'), 1, 0)
    df['E768'] = np.where(df['codigos_cie'].str.contains('E768'), 1, 0)
    df['E769'] = np.where(df['codigos_cie'].str.contains('E769'), 1, 0)
    df['E770'] = np.where(df['codigos_cie'].str.contains('E770'), 1, 0)
    df['E771'] = np.where(df['codigos_cie'].str.contains('E771'), 1, 0)
    df['E778'] = np.where(df['codigos_cie'].str.contains('E778'), 1, 0)
    df['E779'] = np.where(df['codigos_cie'].str.contains('E779'), 1, 0)
    df['E780'] = np.where(df['codigos_cie'].str.contains('E780'), 1, 0)
    df['E781'] = np.where(df['codigos_cie'].str.contains('E781'), 1, 0)
    df['E782'] = np.where(df['codigos_cie'].str.contains('E782'), 1, 0)
    df['E783'] = np.where(df['codigos_cie'].str.contains('E783'), 1, 0)
    df['E784'] = np.where(df['codigos_cie'].str.contains('E784'), 1, 0)
    df['E785'] = np.where(df['codigos_cie'].str.contains('E785'), 1, 0)
    df['E786'] = np.where(df['codigos_cie'].str.contains('E786'), 1, 0)
    df['E788'] = np.where(df['codigos_cie'].str.contains('E788'), 1, 0)
    df['E789'] = np.where(df['codigos_cie'].str.contains('E789'), 1, 0)
    df['E790'] = np.where(df['codigos_cie'].str.contains('E790'), 1, 0)
    df['E791'] = np.where(df['codigos_cie'].str.contains('E791'), 1, 0)
    df['E798'] = np.where(df['codigos_cie'].str.contains('E798'), 1, 0)
    df['E799'] = np.where(df['codigos_cie'].str.contains('E799'), 1, 0)
    df['E800'] = np.where(df['codigos_cie'].str.contains('E800'), 1, 0)
    df['E801'] = np.where(df['codigos_cie'].str.contains('E801'), 1, 0)
    df['E802'] = np.where(df['codigos_cie'].str.contains('E802'), 1, 0)
    df['E803'] = np.where(df['codigos_cie'].str.contains('E803'), 1, 0)
    df['E804'] = np.where(df['codigos_cie'].str.contains('E804'), 1, 0)
    df['E805'] = np.where(df['codigos_cie'].str.contains('E805'), 1, 0)
    df['E806'] = np.where(df['codigos_cie'].str.contains('E806'), 1, 0)
    df['E807'] = np.where(df['codigos_cie'].str.contains('E807'), 1, 0)
    df['E830'] = np.where(df['codigos_cie'].str.contains('E830'), 1, 0)
    df['E831'] = np.where(df['codigos_cie'].str.contains('E831'), 1, 0)
    df['E832'] = np.where(df['codigos_cie'].str.contains('E832'), 1, 0)
    df['E833'] = np.where(df['codigos_cie'].str.contains('E833'), 1, 0)
    df['E834'] = np.where(df['codigos_cie'].str.contains('E834'), 1, 0)
    df['E835'] = np.where(df['codigos_cie'].str.contains('E835'), 1, 0)
    df['E838'] = np.where(df['codigos_cie'].str.contains('E838'), 1, 0)
    df['E839'] = np.where(df['codigos_cie'].str.contains('E839'), 1, 0)
    df['E840'] = np.where(df['codigos_cie'].str.contains('E840'), 1, 0)
    df['E841'] = np.where(df['codigos_cie'].str.contains('E841'), 1, 0)
    df['E848'] = np.where(df['codigos_cie'].str.contains('E848'), 1, 0)
    df['E849'] = np.where(df['codigos_cie'].str.contains('E849'), 1, 0)
    df['E850'] = np.where(df['codigos_cie'].str.contains('E850'), 1, 0)
    df['E851'] = np.where(df['codigos_cie'].str.contains('E851'), 1, 0)
    df['E852'] = np.where(df['codigos_cie'].str.contains('E852'), 1, 0)
    df['E853'] = np.where(df['codigos_cie'].str.contains('E853'), 1, 0)
    df['E854'] = np.where(df['codigos_cie'].str.contains('E854'), 1, 0)
    df['E858'] = np.where(df['codigos_cie'].str.contains('E858'), 1, 0)
    df['E859'] = np.where(df['codigos_cie'].str.contains('E859'), 1, 0)
    df['E86'] = np.where(df['codigos_cie'].str.contains('E86'), 1, 0)
    df['E87'] = np.where(df['codigos_cie'].str.contains('E87'), 1, 0)
    df['E870'] = np.where(df['codigos_cie'].str.contains('E870'), 1, 0)
    df['E871'] = np.where(df['codigos_cie'].str.contains('E871'), 1, 0)
    df['E872'] = np.where(df['codigos_cie'].str.contains('E872'), 1, 0)
    df['E873'] = np.where(df['codigos_cie'].str.contains('E873'), 1, 0)
    df['E874'] = np.where(df['codigos_cie'].str.contains('E874'), 1, 0)
    df['E875'] = np.where(df['codigos_cie'].str.contains('E875'), 1, 0)
    df['E876'] = np.where(df['codigos_cie'].str.contains('E876'), 1, 0)
    df['E877'] = np.where(df['codigos_cie'].str.contains('E877'), 1, 0)
    df['E878'] = np.where(df['codigos_cie'].str.contains('E878'), 1, 0)
    df['E880'] = np.where(df['codigos_cie'].str.contains('E880'), 1, 0)
    df['E881'] = np.where(df['codigos_cie'].str.contains('E881'), 1, 0)
    df['E882'] = np.where(df['codigos_cie'].str.contains('E882'), 1, 0)
    df['E888'] = np.where(df['codigos_cie'].str.contains('E888'), 1, 0)
    df['E889'] = np.where(df['codigos_cie'].str.contains('E889'), 1, 0)
    df['E89'] = np.where(df['codigos_cie'].str.contains('E89'), 1, 0)
    df['E90'] = np.where(df['codigos_cie'].str.contains('E90'), 1, 0)
    
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
    df["dm_insulinodep"] = df['dm_insulinodep'].astype('category')
    df["dm_insulinodep_coma"] = df['dm_insulinodep_coma'].astype('category')
    df["dm_insulinodep_ceto"] = df['dm_insulinodep_ceto'].astype('category')
    df["dm_insulinodep_c_renal"] = df['dm_insulinodep_c_renal'].astype('category')
    df["dm_insulinodep_c_oft"] = df['dm_insulinodep_c_oft'].astype('category')
    df["dm_insulinodep_c_neu"] = df['dm_insulinodep_c_neu'].astype('category')
    df["dm_insulinodep_c_cirp"] = df['dm_insulinodep_c_cirp'].astype('category')
    df["dm_insulinodep_c_esp"] = df['dm_insulinodep_c_esp'].astype('category')
    df["dm_insulinodep_c_mult"] = df['dm_insulinodep_c_mult'].astype('category')
    df["dm_insulinodep_c_ne"] = df['dm_insulinodep_c_ne'].astype('category')
    df["dm_insulinodep_sin_mc"] = df['dm_insulinodep_sin_mc'].astype('category')
    # E11
    df["dm_no_insulinodep"] = df['dm_no_insulinodep'].astype('category')
    df["dm_no_insulinodep_coma"] = df['dm_no_insulinodep_coma'].astype('category')
    df["dm_no_insulinodep_ceto"] = df['dm_no_insulinodep_ceto'].astype('category')
    df["dm_no_insulinodep_c_renal"] = df['dm_no_insulinodep_c_renal'].astype('category')
    df["dm_no_insulinodep_c_oft"] = df['dm_no_insulinodep_c_oft'].astype('category')
    df["dm_no_insulinodep_c_neu"] = df['dm_no_insulinodep_c_neu'].astype('category')
    df["dm_no_insulinodep_c_cirp"] = df['dm_no_insulinodep_c_cirp'].astype('category')
    df["dm_no_insulinodep_c_esp"] = df['dm_no_insulinodep_c_esp'].astype('category')
    df["dm_no_insulinodep_c_mult"] = df['dm_no_insulinodep_c_mult'].astype('category')
    df["dm_no_insulinodep_c_ne"] = df['dm_no_insulinodep_c_ne'].astype('category')
    df["dm_no_insulinodep_sin_mc"] = df['dm_no_insulinodep_sin_mc'].astype('category')
    # E12
    df["dm_asoc_desnutricion"] = df['dm_asoc_desnutricion'].astype('category')
    df["dm_asoc_desnutricion_coma"] = df['dm_asoc_desnutricion_coma'].astype('category')
    df["dm_asoc_desnutricion_ceto"] = df['dm_asoc_desnutricion_ceto'].astype('category')
    df["dm_asoc_desnutricion_c_renal"] = df['dm_asoc_desnutricion_c_renal'].astype('category')
    df["dm_asoc_desnutricion_c_oft"] = df['dm_asoc_desnutricion_c_oft'].astype('category')
    df["dm_asoc_desnutricion_c_neu"] = df['dm_asoc_desnutricion_c_neu'].astype('category')
    df["dm_asoc_desnutricion_c_cirp"] = df['dm_asoc_desnutricion_c_cirp'].astype('category')
    df["dm_asoc_desnutricion_c_esp"] = df['dm_asoc_desnutricion_c_esp'].astype('category')
    df["dm_asoc_desnutricion_c_mult"] = df['dm_asoc_desnutricion_c_mult'].astype('category')
    df["dm_asoc_desnutricion_c_ne"] = df['dm_asoc_desnutricion_c_ne'].astype('category')
    df["dm_asoc_desnutricion_sin_mc"] = df['dm_asoc_desnutricion_sin_mc'].astype('category')
    # E13
    df["otras_dm"] = df['otras_dm'].astype('category')
    df["otras_dm_coma"] = df['otras_dm_coma'].astype('category')
    df["otras_dm_ceto"] = df['otras_dm_ceto'].astype('category')
    df["otras_dm_c_renal"] = df['otras_dm_c_renal'].astype('category')
    df["otras_dm_c_oft"] = df['otras_dm_c_oft'].astype('category')
    df["otras_dm_c_neu"] = df['otras_dm_c_neu'].astype('category')
    df["otras_dm_c_cirp"] = df['otras_dm_c_cirp'].astype('category')
    df["otras_dm_c_esp"] = df['otras_dm_c_esp'].astype('category')
    df["otras_dm_c_mult"] = df['otras_dm_c_mult'].astype('category')
    df["otras_dm_c_ne"] = df['otras_dm_c_ne'].astype('category')
    df["otras_dm_sin_mc"] = df['otras_dm_sin_mc'].astype('category')
    # E14
    df["dm_no_especificada"] = df['dm_no_especificada'].astype('category')
    df["dm_no_especificada_coma"] = df['dm_no_especificada_coma'].astype('category')
    df["dm_no_especificada_ceto"] = df['dm_no_especificada_ceto'].astype('category')
    df["dm_no_especificada_c_renal"] = df['dm_no_especificada_c_renal'].astype('category')
    df["dm_no_especificada_c_oft"] = df['dm_no_especificada_c_oft'].astype('category')
    df["dm_no_especificada_c_neu"] = df['dm_no_especificada_c_neu'].astype('category')
    df["dm_no_especificada_c_cirp"] = df['dm_no_especificada_c_cirp'].astype('category')
    df["dm_no_especificada_c_esp"] = df['dm_no_especificada_c_esp'].astype('category')
    df["dm_no_especificada_c_mult"] = df['dm_no_especificada_c_mult'].astype('category')
    df["dm_no_especificada_c_ne"] = df['dm_no_especificada_c_ne'].astype('category')
    df["dm_no_especificada_sin_mc"] = df['dm_no_especificada_sin_mc'].astype('category')
    
    # Enf renales
    df['sind_nefritico_ag'] = df['sind_nefritico_ag'].astype('category')
    df['sind_nefritico_progr'] = df['sind_nefritico_progr'].astype('category')
    df['hematuria_recur_persist'] = df['hematuria_recur_persist'].astype('category')
    df['sind_nefritico_cron'] = df['sind_nefritico_cron'].astype('category')
    df['sind_nefrotico'] = df['sind_nefrotico'].astype('category')
    df['sind_nefritico_ne'] = df['sind_nefritico_ne'].astype('category')
    df['proteinuria_aislada_lesion_morfo_esp'] = df['proteinuria_aislada_lesion_morfo_esp'].astype('category')
    df['nefropatia_hereditaria_no_c_ot_part'] = df['nefropatia_hereditaria_no_c_ot_part'].astype('category')
    df['trast_glomerulares_enf_c_ot_part'] = df['trast_glomerulares_enf_c_ot_part'].astype('category')
    df['nefritis_tubuloint_aguda'] = df['nefritis_tubuloint_aguda'].astype('category')
    df['nefritis_tubuloint_cronica'] = df['nefritis_tubuloint_cronica'].astype('category')
    df['nefritis_tubuloint_ne_aguda_cronica'] = df['nefritis_tubuloint_ne_aguda_cronica'].astype('category')
    df['uropatia_obstructiva_por_reflujo'] = df['uropatia_obstructiva_por_reflujo'].astype('category')
    df['afecc_tub_tubuloint_drog_metp'] = df['afecc_tub_tubuloint_drog_metp'].astype('category')
    df['otras_enf_renales_tubuloint'] = df['otras_enf_renales_tubuloint'].astype('category')
    df['trast_renales_tubuloint_enf_c_ot_part'] = df['trast_renales_tubuloint_enf_c_ot_part'].astype('category')
    df['insuficiencia_renal_aguda'] = df['insuficiencia_renal_aguda'].astype('category')
    df['insuficiencia_renal_cronica'] = df['insuficiencia_renal_cronica'].astype('category')
    df['insuficiencia_renal_ne'] = df['insuficiencia_renal_ne'].astype('category')
    df['calculo_riñon_ureter'] = df['calculo_riñon_ureter'].astype('category')
    df['calculo_vias_urinarias_inferiores'] = df['calculo_vias_urinarias_inferiores'].astype('category')
    df['calculo_vias_urinarias_enf_c_ot_part'] = df['calculo_vias_urinarias_enf_c_ot_part'].astype('category')
    df['colico_renal_ne'] = df['colico_renal_ne'].astype('category')
    df['trast_resul_fun_tub_renal_alt'] = df['trast_resul_fun_tub_renal_alt'].astype('category')
    df['riñon_contraido_ne'] = df['riñon_contraido_ne'].astype('category')
    df['riñon_pequeño_causa_desconocida'] = df['riñon_pequeño_causa_desconocida'].astype('category')
    df['ot_trast_riñon_ureter_no_c_ot_part'] = df['ot_trast_riñon_ureter_no_c_ot_part'].astype('category')
    df['ot_trast_riñon_ureter_enf_c_ot_part'] = df['ot_trast_riñon_ureter_enf_c_ot_part'].astype('category')
    df['cistitis'] = df['cistitis'].astype('category')
    df['disf_neuromusc_vejiga_no_c_ot_part'] = df['disf_neuromusc_vejiga_no_c_ot_part'].astype('category')
    df['ot_trast_vejiga'] = df['ot_trast_vejiga'].astype('category')
    df['trast_vejiga_enf_c_ot_part'] = df['trast_vejiga_enf_c_ot_part'].astype('category')
    df['uretritis_sind_uretral'] = df['uretritis_sind_uretral'].astype('category')
    df['estrechez_uretral'] = df['estrechez_uretral'].astype('category')
    df['ot_trast_uretra'] = df['ot_trast_uretra'].astype('category')
    df['trast_uretra_enf_c_ot_part'] = df['trast_uretra_enf_c_ot_part'].astype('category')
    df['ot_trast_sistema_urinario'] = df['ot_trast_sistema_urinario'].astype('category')
    
    # enf hígado
    df['enf_alcoholica_higado'] = df['enf_alcoholica_higado'].astype('category')
    df['enf_toxica_higado'] = df['enf_toxica_higado'].astype('category')
    df['insuficiencia_hepatica_no_c_ot_part'] = df['insuficiencia_hepatica_no_c_ot_part'].astype('category')
    df['hepatitis_cronica_no_c_ot_part'] = df['hepatitis_cronica_no_c_ot_part'].astype('category')
    df['fibrosis_cirrosis_higado'] = df['fibrosis_cirrosis_higado'].astype('category')
    df['absceso_higado'] = df['absceso_higado'].astype('category')
    df['flebitis_de_la_vena_porta'] = df['flebitis_de_la_vena_porta'].astype('category')
    df['hepatitis_reactiva_no_especifica'] = df['hepatitis_reactiva_no_especifica'].astype('category')
    df['hepatitis_granulomatosa_no_c_ot_part'] = df['hepatitis_granulomatosa_no_c_ot_part'].astype('category')
    df['hepatitis_autoinmune'] = df['hepatitis_autoinmune'].astype('category')
    df['otras_enfes_inflamatorias_higado_esp'] = df['otras_enfes_inflamatorias_higado_esp'].astype('category')
    df['enf_inflamatoria_higado_ne'] = df['enf_inflamatoria_higado_ne'].astype('category')
    df['degeneracion_grasa_higado_no_c_ot_part'] = df['degeneracion_grasa_higado_no_c_ot_part'].astype('category')
    df['congestion_pasiva_cronica_higado'] = df['congestion_pasiva_cronica_higado'].astype('category')
    df['necrosis_hemorragica_central_higado'] = df['necrosis_hemorragica_central_higado'].astype('category')
    df['infarto_higado'] = df['infarto_higado'].astype('category')
    df['peliosis_hepatica'] = df['peliosis_hepatica'].astype('category')
    df['enf_veno_oclus_higado'] = df['enf_veno_oclus_higado'].astype('category')
    df['hipertension_portal'] = df['hipertension_portal'].astype('category')
    df['sindrome_hepatorrenal'] = df['sindrome_hepatorrenal'].astype('category')
    df['otras_enfes_esp_higado'] = df['otras_enfes_esp_higado'].astype('category')
    df['enf_higado_ne'] = df['enf_higado_ne'].astype('category')
    
    #obses
    df['adiposidad_localizada'] = df['adiposidad_localizada'].astype('category')
    df['obesidad'] = df['obesidad'].astype('category')
    df['obesidad_exceso_calorias'] = df['obesidad_exceso_calorias'].astype('category')
    df['obesidad_por_drogas'] = df['obesidad_por_drogas'].astype('category')
    df['obesidad_extrema_hipov_alveolar'] = df['obesidad_extrema_hipov_alveolar'].astype('category')
    df['obesidad_morbida'] = df['obesidad_morbida'].astype('category')
    df['obesidad_simple'] = df['obesidad_simple'].astype('category')
    df['otra_hiperalimentacion'] = df['otra_hiperalimentacion'].astype('category')
    df['hipervitaminosis_a'] = df['hipervitaminosis_a'].astype('category')
    df['hipercarotinemia'] = df['hipercarotinemia'].astype('category')
    df['sindrome_de_megavitamina_b6'] = df['sindrome_de_megavitamina_b6'].astype('category')
    df['hipervitaminosis_d'] = df['hipervitaminosis_d'].astype('category')
    df['ot_hiperalimentacion_esp'] = df['ot_hiperalimentacion_esp'].astype('category')
    df['secuelas_hiperalimentacion'] = df['secuelas_hiperalimentacion'].astype('category')
    df['hiperalimentacion'] = df['hiperalimentacion'].astype('category')
    df['aumento_anormal_peso'] = df['aumento_anormal_peso'].astype('category')
    df['aumento_excesivo_peso_embarazo'] = df['aumento_excesivo_peso_embarazo'].astype('category')
    
    # enf hipertensivas
    df['I10'] = df['I10'].astype('category')
    df['I110'] = df['I110'].astype('category')
    df['I119'] = df['I119'].astype('category')
    df['I120'] = df['I120'].astype('category')
    df['I129'] = df['I129'].astype('category')
    df['I130'] = df['I130'].astype('category')
    df['I131'] = df['I131'].astype('category')
    df['I132'] = df['I132'].astype('category')
    df['I139'] = df['I139'].astype('category')
    df['I151'] = df['I151'].astype('category')
    df['I152'] = df['I152'].astype('category')
    df['I158'] = df['I158'].astype('category')
    df['I159'] = df['I159'].astype('category')
    # arteriosc
    df['Y526'] = df['Y526'].astype('category')
    df['I700'] = df['I700'].astype('category')
    df['I701'] = df['I701'].astype('category')
    df['I702'] = df['I702'].astype('category')
    df['I708'] = df['I708'].astype('category')
    df['I709'] = df['I709'].astype('category')
    df['T466'] = df['T466'].astype('category')
    
    # enf metab
    df['E700'] = df['E700'].astype('category')
    df['E701'] = df['E701'].astype('category')
    df['E702'] = df['E702'].astype('category')
    df['E703'] = df['E703'].astype('category')
    df['E708'] = df['E708'].astype('category')
    df['E709'] = df['E709'].astype('category')
    df['E710'] = df['E710'].astype('category')
    df['E711'] = df['E711'].astype('category')
    df['E712'] = df['E712'].astype('category')
    df['E713'] = df['E713'].astype('category')
    df['E720'] = df['E720'].astype('category')
    df['E721'] = df['E721'].astype('category')
    df['E722'] = df['E722'].astype('category')
    df['E723'] = df['E723'].astype('category')
    df['E724'] = df['E724'].astype('category')
    df['E725'] = df['E725'].astype('category')
    df['E728'] = df['E728'].astype('category')
    df['E729'] = df['E729'].astype('category')
    df['E730'] = df['E730'].astype('category')
    df['E731'] = df['E731'].astype('category')
    df['E738'] = df['E738'].astype('category')
    df['E739'] = df['E739'].astype('category')
    df['E740'] = df['E740'].astype('category')
    df['E741'] = df['E741'].astype('category')
    df['E742'] = df['E742'].astype('category')
    df['E743'] = df['E743'].astype('category')
    df['E744'] = df['E744'].astype('category')
    df['E748'] = df['E748'].astype('category')
    df['E749'] = df['E749'].astype('category')
    df['E750'] = df['E750'].astype('category')
    df['E751'] = df['E751'].astype('category')
    df['E752'] = df['E752'].astype('category')
    df['E753'] = df['E753'].astype('category')
    df['E754'] = df['E754'].astype('category')
    df['E755'] = df['E755'].astype('category')
    df['E756'] = df['E756'].astype('category')
    df['E760'] = df['E760'].astype('category')
    df['E761'] = df['E761'].astype('category')
    df['E762'] = df['E762'].astype('category')
    df['E763'] = df['E763'].astype('category')
    df['E768'] = df['E768'].astype('category')
    df['E769'] = df['E769'].astype('category')
    df['E770'] = df['E770'].astype('category')
    df['E771'] = df['E771'].astype('category')
    df['E778'] = df['E778'].astype('category')
    df['E779'] = df['E779'].astype('category')
    df['E780'] = df['E780'].astype('category')
    df['E781'] = df['E781'].astype('category')
    df['E782'] = df['E782'].astype('category')
    df['E783'] = df['E783'].astype('category')
    df['E784'] = df['E784'].astype('category')
    df['E785'] = df['E785'].astype('category')
    df['E786'] = df['E786'].astype('category')
    df['E788'] = df['E788'].astype('category')
    df['E789'] = df['E789'].astype('category')
    df['E790'] = df['E790'].astype('category')
    df['E791'] = df['E791'].astype('category')
    df['E798'] = df['E798'].astype('category')
    df['E799'] = df['E799'].astype('category')
    df['E800'] = df['E800'].astype('category')
    df['E801'] = df['E801'].astype('category')
    df['E802'] = df['E802'].astype('category')
    df['E803'] = df['E803'].astype('category')
    df['E804'] = df['E804'].astype('category')
    df['E805'] = df['E805'].astype('category')
    df['E806'] = df['E806'].astype('category')
    df['E807'] = df['E807'].astype('category')
    df['E830'] = df['E830'].astype('category')
    df['E831'] = df['E831'].astype('category')
    df['E832'] = df['E832'].astype('category')
    df['E833'] = df['E833'].astype('category')
    df['E834'] = df['E834'].astype('category')
    df['E835'] = df['E835'].astype('category')
    df['E838'] = df['E838'].astype('category')
    df['E839'] = df['E839'].astype('category')
    df['E840'] = df['E840'].astype('category')
    df['E841'] = df['E841'].astype('category')
    df['E848'] = df['E848'].astype('category')
    df['E849'] = df['E849'].astype('category')
    df['E850'] = df['E850'].astype('category')
    df['E851'] = df['E851'].astype('category')
    df['E852'] = df['E852'].astype('category')
    df['E853'] = df['E853'].astype('category')
    df['E854'] = df['E854'].astype('category')
    df['E858'] = df['E858'].astype('category')
    df['E859'] = df['E859'].astype('category')
    df['E86'] = df['E86'].astype('category')
    df['E87'] = df['E87'].astype('category')
    df['E870'] = df['E870'].astype('category')
    df['E871'] = df['E871'].astype('category')
    df['E872'] = df['E872'].astype('category')
    df['E873'] = df['E873'].astype('category')
    df['E874'] = df['E874'].astype('category')
    df['E875'] = df['E875'].astype('category')
    df['E876'] = df['E876'].astype('category')
    df['E877'] = df['E877'].astype('category')
    df['E878'] = df['E878'].astype('category')
    df['E880'] = df['E880'].astype('category')
    df['E881'] = df['E881'].astype('category')
    df['E882'] = df['E882'].astype('category')
    df['E888'] = df['E888'].astype('category')
    df['E889'] = df['E889'].astype('category')
    df['E89'] = df['E89'].astype('category')
    df['E90'] = df['E90'].astype('category')
    
    return df


def medicine_cat(df,df_m):
    """Convert a number into a human readable format."""
    
    #df_m = pd.read_csv("../Data/medicamentos.csv", encoding='ISO-8859-1')
    
    #df_m = df_m.drop(['id','Grupo','Producto_Activo','Cve_Med.1','Cve_Med','GPO','GPO1','ESP','DIF',
    #                  'VAR','CUADRO_BASICO_SAI','PROGRAMA_MEDICO','Unidades', 'Medida','GRUPO'], axis=1)
    
    df['ANALGESIACOS_ANTIINFLAMATORIOS_ANTIRREUMATICOS'] = 0    
    df['ANALGESICOS_OPIOIDES___'] = 0
    df['ANALGESICOS_ANTIPIRETICOS'] = 0
    df['ANESTESICOS_GENERATES'] = 0
    df['ANESTESICOS_LOCALES'] = 0
    df['ANSIOLITICOS'] = 0
    df['ANTIACIDOS'] = 0
    df['ANTIAGREGANTE_PLAQUETARIO'] = 0
    df['ANTIANEMICOS'] = 0
    df['ANTIANGINOSO'] = 0
    df['ANTIARRITMICOS'] = 0
    df['ANTIASMATICO__BRONCODILATADOR'] = 0
    df['ANTIBIOTICOS'] = 0
    df['ANTICONCEPTIVO_INTRAUTERINO'] = 0
    df['ANTIDEPRESIVOS'] = 0
    df['ANTIDIABETICOS'] = 0
    df['ANTIDIARREICOS'] = 0
    df['ANTIDOTOS'] = 0
    df['ANTIEMETICOS'] = 0
    df['ANTIEPILEPTICOS'] = 0
    df['ANTIESPASMODICO'] = 0
    df['ANTIFUNGICOS'] = 0
    df['ANTIGOTOSOS'] = 0
    df['ANTIHEMORRAGICOS'] = 0
    df['ANTIHISTAMINICOS'] = 0
    df['ANTIPARKINSONIANO'] = 0
    df['ANTIPSICOTICOS'] = 0
    df['ANTISEPTICOS_DESINFECTANTES'] = 0
    df['ANTITROMBITICO_TROMBOTICO_ANTIAGREGANTE'] = 0
    df['ANTITROMBOTICO_TROMBOLITICO'] = 0
    df['ANTITUSIVOS'] = 0
    df['ANTIULCEROSOS_PROTECTOR_GASTRICO'] = 0
    df['ANTIVIRALES'] = 0
    df['CARDIOTONICOS'] = 0
    df['CORTICOIDES'] = 0
    df['DIURETICOS_ANTIHIPERTENSIVOS'] = 0
    df['FACTOR_VITAMINICO'] = 0
    df['HIPNOTICO_SEDANTE'] = 0
    df['HIPOLIPEMIANTE'] = 0
    df['INDUCTOR_DEL_PARTO'] = 0
    df['INHIBIDOR_DEL_PARTO'] = 0
    df['INMUNOSUPRESORES'] = 0
    df['LAXANTES'] = 0
    df['MUCOLITICOS'] = 0
    df['OTROS_ANTIHIPERTENSIVOS'] = 0
    df['RELAJANTE_MUSCULAR'] = 0
    df['TERAPIA_TIROIDEA'] = 0
    df['TRATAMIENTO_TUBERCULOSIS'] = 0
    df['g1_ANALGESICOS'] = 0
    df['g2_ANESTESIA'] = 0
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
    df['ANALGESICOS_URINARIOS'] = 0
    df['ANTIAGREGANTES_PLAQUETARIOS'] = 0
    df['ANTIALERGICOS'] = 0
    df['ANTIANDROGENICOS'] = 0
    df['ANTIARRITMICOS.1'] = 0
    df['ANTIBIOTICOS.1'] = 0
    df['ANTICOAGULANTES_ORALES'] = 0
    df['ANTIDEPRESIVOS.1'] = 0
    df['ANTIDIABETICOS.1'] = 0
    df['ANTIFLAMATORIOS_ESTEROIDEOS'] = 0
    df['ANTIHIPERTENSIVOS'] = 0
    df['ANTIINFLAMATORIOS_NO_ESTEROIDEOS'] = 0
    df['ANTIMICOTICOS_SISTEMICOS_Y_TOPICOS'] = 0
    df['ANTIMUSCARINICOS'] = 0
    df['ANTINEURITICOS'] = 0
    df['ANTITUSIVOS.1'] = 0
    df['ANTIULCEROSOS_Y_PROTECTORES_DE_LA_MUCOSA_GASTRICA'] = 0
    df['ANTIURICOSURICOS'] = 0
    df['ANTIVERTIGINOSOS'] = 0
    df['BENZODIAZEPINAS'] = 0
    df['BLOQUEADORES_ALFA'] = 0
    df['BRONCODILATADORES_Y_EXPECTORANTES'] = 0
    df['DISFUNCION_ERECTIL'] = 0
    df['ELECTROLITOS_ORALES'] = 0
    df['FARMACOS_INSUFICIENCIA_CARDIACA_Y_ANTIANGINOSOS'] = 0
    df['FARMACOS_MODIFICADORES_DE_LA_ENFERMEDAD'] = 0
    df['FARMACOS_OCULARES'] = 0
    df['FARMACOS_UTILIZADOS_EN_CANCER_DE_MAMA'] = 0
    df['FARMACOS_UTILIZADOS_EN_HIPERTIROIDISMO'] = 0
    df['FARMACOS_UTILIZADOS_EN_HIPOTIROIDISMO'] = 0
    df['FARMACOS_UTILIZADOS_EN_NEFROLOGIA'] = 0
    df['FARMACOS_UTILIZADOS_EN_NEUROLOGIA'] = 0
    df['FARMACOS_UTILIZADOS_EN_OSTEOPOROSIS'] = 0
    df['FARMACOS_UTILIZADOS_EN_PSIQUIATRIA'] = 0
    df['FORMULAS_NUTRICIONALES_COMPLETAS'] = 0
    df['HIPOLIPEMIANTES'] = 0
    df['HORMONALES'] = 0
    df['METILXANTINAS'] = 0
    df['VARIOS'] = 0
    df['VITAMINICOS'] = 0
    
    for i in range(len(df_m['ID_PRODUCTO'])):
        x = str(df_m['ID_PRODUCTO'][i])
        #print(x)
        for j in range(len(df['cx_curp'])):            
            m = str(df['cod_med'][j])
            #print(m)
            if(~pd.isna(m) and m!='nan'):
                if x in str(m):
            
                    df['ANALGESIACOS_ANTIINFLAMATORIOS_ANTIRREUMATICOS'][j] = df_m['ANALGESIACOS_ANTIINFLAMATORIOS_ANTIRREUMATICOS'][i] + df['ANALGESIACOS_ANTIINFLAMATORIOS_ANTIRREUMATICOS'][j]
                    df['ANALGESICOS_OPIOIDES___'][j] = df_m['ANALGESICOS_OPIOIDES___'][i] + df['ANALGESICOS_OPIOIDES___'][j]
                    df['ANALGESICOS_ANTIPIRETICOS'][j] = df_m['ANALGESICOS_ANTIPIRETICOS'][i] + df['ANALGESICOS_ANTIPIRETICOS'][j]
                    df['ANESTESICOS_GENERATES'][j] = df_m['ANESTESICOS_GENERATES'][i] + df['ANESTESICOS_GENERATES'][j]
                    df['ANESTESICOS_LOCALES'][j] = df_m['ANESTESICOS_LOCALES'][i] + df['ANESTESICOS_LOCALES'][j]
                    df['ANSIOLITICOS'][j] = df_m['ANSIOLITICOS'][i] + df['ANSIOLITICOS'][j]
                    df['ANTIACIDOS'][j] = df_m['ANTIACIDOS'][i] + df['ANTIACIDOS'][j]
                    df['ANTIAGREGANTE_PLAQUETARIO'][j] = df_m['ANTIAGREGANTE_PLAQUETARIO'][i] + df['ANTIAGREGANTE_PLAQUETARIO'][j]
                    df['ANTIANEMICOS'][j] = df_m['ANTIANEMICOS'][i] + df['ANTIANEMICOS'][j]
                    df['ANTIANGINOSO'][j] = df_m['ANTIANGINOSO'][i] + df['ANTIANGINOSO'][j]
                    df['ANTIARRITMICOS'][j] = df_m['ANTIARRITMICOS'][i] + df['ANTIARRITMICOS'][j]
                    df['ANTIASMATICO__BRONCODILATADOR'][j] = df_m['ANTIASMATICO__BRONCODILATADOR'][i] + df['ANTIASMATICO__BRONCODILATADOR'][j]
                    df['ANTIBIOTICOS'][j] = df_m['ANTIBIOTICOS'][i] + df['ANTIBIOTICOS'][j]
                    df['ANTICONCEPTIVO_INTRAUTERINO'][j] = df_m['ANTICONCEPTIVO_INTRAUTERINO'][i] + df['ANTICONCEPTIVO_INTRAUTERINO'][j]
                    df['ANTIDEPRESIVOS'][j] = df_m['ANTIDEPRESIVOS'][i] + df['ANTIDEPRESIVOS'][j]
                    df['ANTIDIABETICOS'][j] = df_m['ANTIDIABETICOS'][i] + df['ANTIDIABETICOS'][j]
                    df['ANTIDIARREICOS'][j] = df_m['ANTIDIARREICOS'][i] + df['ANTIDIARREICOS'][j]
                    df['ANTIDOTOS'][j] = df_m['ANTIDOTOS'][i] + df['ANTIDOTOS'][j]
                    df['ANTIEMETICOS'][j] = df_m['ANTIEMETICOS'][i] + df['ANTIEMETICOS'][j]
                    df['ANTIEPILEPTICOS'][j] = df_m['ANTIEPILEPTICOS'][i] + df['ANTIEPILEPTICOS'][j]
                    df['ANTIESPASMODICO'][j] = df_m['ANTIESPASMODICO'][i] + df['ANTIESPASMODICO'][j]
                    df['ANTIFUNGICOS'][j] = df_m['ANTIFUNGICOS'][i] + df['ANTIFUNGICOS'][j]
                    df['ANTIGOTOSOS'][j] = df_m['ANTIGOTOSOS'][i] + df['ANTIGOTOSOS'][j]
                    df['ANTIHEMORRAGICOS'][j] = df_m['ANTIHEMORRAGICOS'][i] + df['ANTIHEMORRAGICOS'][j]
                    df['ANTIHISTAMINICOS'][j] = df_m['ANTIHISTAMINICOS'][i] + df['ANTIHISTAMINICOS'][j]
                    df['ANTIPARKINSONIANO'][j] = df_m['ANTIPARKINSONIANO'][i] + df['ANTIPARKINSONIANO'][j]
                    df['ANTIPSICOTICOS'][j] = df_m['ANTIPSICOTICOS'][i] + df['ANTIPSICOTICOS'][j]
                    df['ANTISEPTICOS_DESINFECTANTES'][j] = df_m['ANTISEPTICOS_DESINFECTANTES'][i] + df['ANTISEPTICOS_DESINFECTANTES'][j]
                    df['ANTITROMBITICO_TROMBOTICO_ANTIAGREGANTE'][j] = df_m['ANTITROMBITICO_TROMBOTICO_ANTIAGREGANTE'][i] + df['ANTITROMBITICO_TROMBOTICO_ANTIAGREGANTE'][j]
                    df['ANTITROMBOTICO_TROMBOLITICO'][j] = df_m['ANTITROMBOTICO_TROMBOLITICO'][i] + df['ANTITROMBOTICO_TROMBOLITICO'][j]
                    df['ANTITUSIVOS'][j] = df_m['ANTITUSIVOS'][i] + df['ANTITUSIVOS'][j]
                    df['ANTIULCEROSOS_PROTECTOR_GASTRICO'][j] = df_m['ANTIULCEROSOS_PROTECTOR_GASTRICO'][i] + df['ANTIULCEROSOS_PROTECTOR_GASTRICO'][j]
                    df['ANTIVIRALES'][j] = df_m['ANTIVIRALES'][i] + df['ANTIVIRALES'][j]
                    df['CARDIOTONICOS'][j] = df_m['CARDIOTONICOS'][i] + df['CARDIOTONICOS'][j]
                    df['CORTICOIDES'][j] = df_m['CORTICOIDES'][i] + df['CORTICOIDES'][j]
                    df['DIURETICOS_ANTIHIPERTENSIVOS'][j] = df_m['DIURETICOS_ANTIHIPERTENSIVOS'][i] + df['DIURETICOS_ANTIHIPERTENSIVOS'][j]
                    df['FACTOR_VITAMINICO'][j] = df_m['FACTOR_VITAMINICO'][i] + df['FACTOR_VITAMINICO'][j]
                    df['HIPNOTICO_SEDANTE'][j] = df_m['HIPNOTICO_SEDANTE'][i] + df['HIPNOTICO_SEDANTE'][j]
                    df['HIPOLIPEMIANTE'][j] = df_m['HIPOLIPEMIANTE'][i] + df['HIPOLIPEMIANTE'][j]
                    df['INDUCTOR_DEL_PARTO'][j] = df_m['INDUCTOR_DEL_PARTO'][i] + df['INDUCTOR_DEL_PARTO'][j]
                    df['INHIBIDOR_DEL_PARTO'][j] = df_m['INHIBIDOR_DEL_PARTO'][i] + df['INHIBIDOR_DEL_PARTO'][j]
                    df['INMUNOSUPRESORES'][j] = df_m['INMUNOSUPRESORES'][i] + df['INMUNOSUPRESORES'][j]
                    df['LAXANTES'][j] = df_m['LAXANTES'][i] + df['LAXANTES'][j]
                    df['MUCOLITICOS'][j] = df_m['MUCOLITICOS'][i] + df['MUCOLITICOS'][j]
                    df['OTROS_ANTIHIPERTENSIVOS'][j] = df_m['OTROS_ANTIHIPERTENSIVOS'][i] + df['OTROS_ANTIHIPERTENSIVOS'][j]
                    df['RELAJANTE_MUSCULAR'][j] = df_m['RELAJANTE_MUSCULAR'][i] + df['RELAJANTE_MUSCULAR'][j]
                    df['TERAPIA_TIROIDEA'][j] = df_m['TERAPIA_TIROIDEA'][i] + df['TERAPIA_TIROIDEA'][j]
                    df['TRATAMIENTO_TUBERCULOSIS'][j] = df_m['TRATAMIENTO_TUBERCULOSIS'][i] + df['TRATAMIENTO_TUBERCULOSIS'][j]
                    df['g1_ANALGESICOS'][j] = df_m['g1_ANALGESICOS'][i] + df['g1_ANALGESICOS'][j]
                    df['g2_ANESTESIA'][j] = df_m['g2_ANESTESIA'][i] + df['g2_ANESTESIA'][j]
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
                    df['ANALGESICOS_URINARIOS'][j] = df_m['ANALGESICOS_URINARIOS'][i] + df['ANALGESICOS_URINARIOS'][j]
                    df['ANTIAGREGANTES_PLAQUETARIOS'][j] = df_m['ANTIAGREGANTES_PLAQUETARIOS'][i] + df['ANTIAGREGANTES_PLAQUETARIOS'][j]
                    df['ANTIALERGICOS'][j] = df_m['ANTIALERGICOS'][i] + df['ANTIALERGICOS'][j]
                    df['ANTIANDROGENICOS'][j] = df_m['ANTIANDROGENICOS'][i] + df['ANTIANDROGENICOS'][j]
                    df['ANTIARRITMICOS.1'][j] = df_m['ANTIARRITMICOS.1'][i] + df['ANTIARRITMICOS.1'][j]
                    df['ANTIBIOTICOS.1'][j] = df_m['ANTIBIOTICOS.1'][i] + df['ANTIBIOTICOS.1'][j]
                    df['ANTICOAGULANTES_ORALES'][j] = df_m['ANTICOAGULANTES_ORALES'][i] + df['ANTICOAGULANTES_ORALES'][j]
                    df['ANTIDEPRESIVOS.1'][j] = df_m['ANTIDEPRESIVOS.1'][i] + df['ANTIDEPRESIVOS.1'][j]
                    df['ANTIDIABETICOS.1'][j] = df_m['ANTIDIABETICOS.1'][i] + df['ANTIDIABETICOS.1'][j]
                    df['ANTIFLAMATORIOS_ESTEROIDEOS'][j] = df_m['ANTIFLAMATORIOS_ESTEROIDEOS'][i] + df['ANTIFLAMATORIOS_ESTEROIDEOS'][j]
                    df['ANTIHIPERTENSIVOS'][j] = df_m['ANTIHIPERTENSIVOS'][i] + df['ANTIHIPERTENSIVOS'][j]
                    df['ANTIINFLAMATORIOS_NO_ESTEROIDEOS'][j] = df_m['ANTIINFLAMATORIOS_NO_ESTEROIDEOS'][i] + df['ANTIINFLAMATORIOS_NO_ESTEROIDEOS'][j]
                    df['ANTIMICOTICOS_SISTEMICOS_Y_TOPICOS'][j] = df_m['ANTIMICOTICOS_SISTEMICOS_Y_TOPICOS'][i] + df['ANTIMICOTICOS_SISTEMICOS_Y_TOPICOS'][j]
                    df['ANTIMUSCARINICOS'][j] = df_m['ANTIMUSCARINICOS'][i] + df['ANTIMUSCARINICOS'][j]
                    df['ANTINEURITICOS'][j] = df_m['ANTINEURITICOS'][i] + df['ANTINEURITICOS'][j]
                    df['ANTITUSIVOS.1'][j] = df_m['ANTITUSIVOS.1'][i] + df['ANTITUSIVOS.1'][j]
                    df['ANTIULCEROSOS_Y_PROTECTORES_DE_LA_MUCOSA_GASTRICA'][j] = df_m['ANTIULCEROSOS_Y_PROTECTORES_DE_LA_MUCOSA_GASTRICA'][i] + df['ANTIULCEROSOS_Y_PROTECTORES_DE_LA_MUCOSA_GASTRICA'][j]
                    df['ANTIURICOSURICOS'][j] = df_m['ANTIURICOSURICOS'][i] + df['ANTIURICOSURICOS'][j]
                    df['ANTIVERTIGINOSOS'][j] = df_m['ANTIVERTIGINOSOS'][i] + df['ANTIVERTIGINOSOS'][j]
                    df['BENZODIAZEPINAS'][j] = df_m['BENZODIAZEPINAS'][i] + df['BENZODIAZEPINAS'][j]
                    df['BLOQUEADORES_ALFA'][j] = df_m['BLOQUEADORES_ALFA'][i] + df['BLOQUEADORES_ALFA'][j]
                    df['BRONCODILATADORES_Y_EXPECTORANTES'][j] = df_m['BRONCODILATADORES_Y_EXPECTORANTES'][i] + df['BRONCODILATADORES_Y_EXPECTORANTES'][j]
                    df['DISFUNCION_ERECTIL'][j] = df_m['DISFUNCION_ERECTIL'][i] + df['DISFUNCION_ERECTIL'][j]
                    df['ELECTROLITOS_ORALES'][j] = df_m['ELECTROLITOS_ORALES'][i] + df['ELECTROLITOS_ORALES'][j]
                    df['FARMACOS_INSUFICIENCIA_CARDIACA_Y_ANTIANGINOSOS'][j] = df_m['FARMACOS_INSUFICIENCIA_CARDIACA_Y_ANTIANGINOSOS'][i] + df['FARMACOS_INSUFICIENCIA_CARDIACA_Y_ANTIANGINOSOS'][j]
                    df['FARMACOS_MODIFICADORES_DE_LA_ENFERMEDAD'][j] = df_m['FARMACOS_MODIFICADORES_DE_LA_ENFERMEDAD'][i] + df['FARMACOS_MODIFICADORES_DE_LA_ENFERMEDAD'][j]
                    df['FARMACOS_OCULARES'][j] = df_m['FARMACOS_OCULARES'][i] + df['FARMACOS_OCULARES'][j]
                    df['FARMACOS_UTILIZADOS_EN_CANCER_DE_MAMA'][j] = df_m['FARMACOS_UTILIZADOS_EN_CANCER_DE_MAMA'][i] + df['FARMACOS_UTILIZADOS_EN_CANCER_DE_MAMA'][j]
                    df['FARMACOS_UTILIZADOS_EN_HIPERTIROIDISMO'][j] = df_m['FARMACOS_UTILIZADOS_EN_HIPERTIROIDISMO'][i] + df['FARMACOS_UTILIZADOS_EN_HIPERTIROIDISMO'][j]
                    df['FARMACOS_UTILIZADOS_EN_HIPOTIROIDISMO'][j] = df_m['FARMACOS_UTILIZADOS_EN_HIPOTIROIDISMO'][i] + df['FARMACOS_UTILIZADOS_EN_HIPOTIROIDISMO'][j]
                    df['FARMACOS_UTILIZADOS_EN_NEFROLOGIA'][j] = df_m['FARMACOS_UTILIZADOS_EN_NEFROLOGIA'][i] + df['FARMACOS_UTILIZADOS_EN_NEFROLOGIA'][j]
                    df['FARMACOS_UTILIZADOS_EN_NEUROLOGIA'][j] = df_m['FARMACOS_UTILIZADOS_EN_NEUROLOGIA'][i] + df['FARMACOS_UTILIZADOS_EN_NEUROLOGIA'][j]
                    df['FARMACOS_UTILIZADOS_EN_OSTEOPOROSIS'][j] = df_m['FARMACOS_UTILIZADOS_EN_OSTEOPOROSIS'][i] + df['FARMACOS_UTILIZADOS_EN_OSTEOPOROSIS'][j]
                    df['FARMACOS_UTILIZADOS_EN_PSIQUIATRIA'][j] = df_m['FARMACOS_UTILIZADOS_EN_PSIQUIATRIA'][i] + df['FARMACOS_UTILIZADOS_EN_PSIQUIATRIA'][j]
                    df['FORMULAS_NUTRICIONALES_COMPLETAS'][j] = df_m['FORMULAS_NUTRICIONALES_COMPLETAS'][i] + df['FORMULAS_NUTRICIONALES_COMPLETAS'][j]
                    df['HIPOLIPEMIANTES'][j] = df_m['HIPOLIPEMIANTES'][i] + df['HIPOLIPEMIANTES'][j]
                    df['HORMONALES'][j] = df_m['HORMONALES'][i] + df['HORMONALES'][j]
                    df['METILXANTINAS'][j] = df_m['METILXANTINAS'][i] + df['METILXANTINAS'][j]
                    df['VARIOS'][j] = df_m['VARIOS'][i] + df['VARIOS'][j]
                    df['VITAMINICOS'][j] = df_m['VITAMINICOS'][i] + df['VITAMINICOS'][j]


            
    
    return df