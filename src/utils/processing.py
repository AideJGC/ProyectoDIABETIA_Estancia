
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
    df["**Data**
    # A00-A09
    df["enf_inf_intestinales"] = np.where(df["codigos_cie"].str.contains('A0'), 1, 0)
    # A15-A19
    df["tuberculosis"] = np.where(df["codigos_cie"].str.contains('A15')|
                                          df["codigos_cie"].str.contains('A16')|
                                          df["codigos_cie"].str.contains('A17')|
                                          df["codigos_cie"].str.contains('A18')|
                                          df["codigos_cie"].str.contains('A19'), 1, 0)
    # A20-A32, A35-A49
    df["ot_enf_bacterianas"] = np.where(df["codigos_cie"].str.contains('A2')
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
    df["ot_enf_inf_y_paras_y_efec_tardios
    df["enf_viricas
    df["rickettsiosis_y_ot_enf__protozoarios
    df["tumores_malig_labio_bucal_faringe 
    df["tumores_malig_organos
    df["tumores_malig_org_respiratorios_intratoracicos
    df["tumores_malig_huesos_articulares_conjuntivo_piel_mama
    df["tumores_malig_org_genitourinarios
    df["tumores_malig_otros_sitios_ne
    df["tumores_malig_tejido_linf_org_hematop
    df["tumores_malig_sitios_mul_indep
    df["tumores_insitu
    df["tumores_benignos
    df["tumores_comp_incierto_desc
    df["enf_sangre_org_hematop
    df["enf_endocrinas
    df["desnutricion_ot_deficiencias
    df["trastornos_mentales
    df["enf_sist_nervioso
    df["enf_ojo_anexos
    df["enf_oido_apofisis_mastoides
    df["fiebre_y_enf_cardiacas_reumaticas
    df["enf_hipertensivas
    df["enf_isquemicas_corazon
    df["enf_circulacion_pulmonar_enf_corazon
    df["enf_cerebrovasculares
    df["otras_enf_aparato_vasc
    df["inf_y_enf_vias_respiratorias_sup
    df["otras_enf_aparato_resp
    df["enf_cavidad_bucal_glandulas_salivales
    df["enf_ot_partes_aparato_digestivo
    df["enf_piel_tejido_subcutaneo
    df["enf_sist_osteomuscular_y_tejido
    df["enf_aparato_urinario
    df["enf_org_genitales_masculinos
    df["trastornos_mama
    df["enf_org_genitales_femeninos
    df["trastornos_sist_genitourinario_consec_proced
    df["causas_obstetricas_directas
    df["parto
    df["causas_obstetricas_indirectas
#
    df["Ciertas afecciones originadas en el período perinatal
#
    df["malformaciones_congenitas
    df["sintomas_signos_hallazgos_anormales_clin_lab_no_clasif
    df["fracturas
    df["luxaciones_esguinces_torceduras
    df["traumatismos_int_intracraneales_y_otr
    df["heridas
    df["efec_cuerpos_extr_pen_orificios_naturales
    df["quemaduras_corrosiones
    df["envenenamiento_efectos_tox
    df["sindrome_maltrato
    df["comp_precoces_traumatismos
    df["comp_aten_med_qx_no_clasif
    df["sec_traumatismos_envenenamiento_causas_ext
    df["ot_efec_causas_ext_comp_traumatismos

    
    return df

# Función number_formater

def medicine_cat(df):
    """Convert a number into a human readable format."""
    
    return df

