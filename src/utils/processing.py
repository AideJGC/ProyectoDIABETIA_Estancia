
# Functions for CIE 10 and Medicine

import pandas as pd 
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter
import pickle


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

    
    return df

# Función number_formater

def medicine_cat(df):
    """Convert a number into a human readable format."""
    
    return df
7