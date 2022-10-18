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
from sklearn.impute import SimpleImputer


COLUMN_NAMES = ['cx_curp','ventana','fecha_ini','fecha_fin','sexo','sum_num_consultas','avg_num_consultas_by_year',
                'dm', 'año_dx_dm', 'dm_años_int', 
                'renal','renal_años_int',
                'edad_range','epoca_nac', 'imc_range',
                'num_med','avg_num_med','min_num_med','max_num_med',  
                'preglucosa','num_med_preglucosa','avg_preglucosa','min_preglucosa','max_preglucosa',
                'postglucosa','num_med_postglucosa','avg_postglucosa','min_postglucosa','max_postglucosa',
                'colesterol','num_med_colesterol','avg_colesterol','min_colesterol','max_colesterol',
                'trigliceridos','num_med_trigliceridos','avg_trigliceridos','min_trigliceridos','max_trigliceridos',
                'hdl','num_med_hdl','avg_hdl','min_hdl','max_hdl',
                'ldl','num_med_ldl','avg_ldl','min_ldl','max_ldl',
                'presion_arterial','num_med_presion_a',
                'avg_sistolica_a','min_sistolica_a','max_sistolica_a','fn_sistolica_a',
                'avg_diastolica_a','min_diastolica_a','max_diastolica_a','fn_distolica_a',
                'map_g',
                'hba1c','num_med_hba1c','avg_hba1c','min_hba1c','max_hba1c',
                'plaquetas','num_med_plaquetas','avg_plaquetas','min_plaquetas','max_plaquetas',
                'creatinina','num_med_creatinina','avg_creatinina','min_creatinina','max_creatinina',
                'acido_urico','num_med_acido_urico','avg_acido_urico','min_acido_urico','max_acido_urico',
                'urea','num_med_urea','avg_urea','min_urea','max_urea',
                'tfg','num_med_tfg','avg_tfg','min_tfg','max_tfg',
                'enf_inf_intestinales',
                'tuberculosis',
                'ot_enf_bacterianas',
                'inf_trans_pred_sexual',
                'ot_enf_inf_y_paras_y_efec_tardios',
                'enf_viricas',
                'rickettsiosis_y_ot_enf__protozoarios',
                'tumores_malig_labio_bucal_faringe',
                'tumores_malig_organos',
                'tumores_malig_org_respiratorios_intratoracicos',
                'tumores_malig_huesos_articulares_conjuntivo_piel_mama',
                'tumores_malig_org_genitourinarios',
                'tumores_malig_otros_sitios_ne',
                'tumores_malig_tejido_linf_org_hematop',
                'tumores_malig_sitios_mul_indep',
                'tumores_insitu',
                'tumores_benignos',
                'tumores_comp_incierto_desc',
                'enf_sangre_org_hematop',
                'enf_endocrinas',
                'desnutricion_ot_deficiencias',
                'trastornos_mentales',
                'enf_sist_nervioso',
                'enf_ojo_anexos',
                'enf_oido_apofisis_mastoides',
                'fiebre_y_enf_cardiacas_reumaticas',
                'enf_isquemicas_corazon',
                'enf_circulacion_pulmonar_enf_corazon',
                'enf_cerebrovasculares',
                'otras_enf_aparato_vasc',
                'inf_y_enf_vias_respiratorias_sup',
                'otras_enf_aparato_resp',
                'enf_cavidad_bucal_glandulas_salivales',
                'enf_ot_partes_aparato_digestivo',
                'enf_piel_tejido_subcutaneo',
                'enf_sist_osteomuscular_y_tejido',
                'enf_aparato_urinario',
                'enf_org_genitales_masculinos',
                'trastornos_mama',
                'enf_org_genitales_femeninos',
                'trastornos_sist_genitourinario_consec_proced',
                'causas_obstetricas_directas',
                'parto',
                'causas_obstetricas_indirectas',
                'malformaciones_congenitas',
                'sintomas_signos_hallazgos_anormales_clin_lab_no_clasif',
                'fracturas',
                'luxaciones_esguinces_torceduras',
                'traumatismos_int_intracraneales_y_otr',
                'heridas',
                'efec_cuerpos_extr_pen_orificios_naturales',
                'quemaduras_corrosiones',
                'envenenamiento_efectos_tox',
                'sindrome_maltrato',
                'comp_precoces_traumatismos',
                'comp_aten_med_qx_no_clasif',
                'sec_traumatismos_envenenamiento_causas_ext',
                'ot_efec_causas_ext_comp_traumatismos',
                'E10',
                'E11',
                'E12',
                'E13',
                'E14',
                'K70_K77',
                'E0_E64',
                'E65_E68',
                'E70_E90',
                'O10_O16',
                'O22',
                'O24',
                'Y52_T46',
                'I6_I8',
                'R0_R4',              
                'g1',
                'g2',
                'g3',
                'g4',
                'g5',
                'g6',
                'g7',
                'g8',
                'g9',
                'g10',
                'g11',
                'g12',
                'g13',
                'g14',
                'g15',
                'g16',
                'g17',
                'g18',
                'g19',
                'g20',
                'g21',
                'g22',
                'g23',
                'ACIDIFICANTES DE LAS VIAS URINARIAS',
                'ACTIVADORES DEL METABOLISMO NEURONAL',
                'ADRENERGICOS',
                'ADYUVANTES DE LA ANALGESIA',
                'ANALGESICOS',
                'ANALGESICOS ANTIINFLAMATORIOS TOPICOS',
                'ANESTESICOS GENERALES',
                'ANESTESICOS LOCALES',
                'ANSIOLITICOS',
                'ANTAGONISTAS',
                'ANTIACIDOS',
                'ANTIADRENERGICOS',
                'ANTIALCOHOL',
                'ANTIALERGICOS',
                'ANTIAMEBIANOS',
                'ANTIANEMICOS',
                'ANTIARTRITICOS',
                'ANTIASMATICOS',
                'ANTICOAGULANTES',
                'ANTICOLINERGICOS',
                'ANTICONCEPTIVOS',
                'ANTIDEPRESIVOS',
                'ANTIDIABETICOS',
                'ANTIDIARREICOS',
                'ANTIDISFUNCION ERECTIL',
                'ANTIDOTOS',
                'ANTIEMETICOS',
                'ANTIENURESIS',
                'ANTIEPILEPTICOS',
                'ANTIESPASMODICOS',
                'ANTIESPASMODICOS DE VIAS URINARIAS',
                'ANTIESTROGENOS',
                'ANTIFLATULENTOS',
                'ANTIGOTOSOS',
                'ANTIGRIPALES',
                'ANTIHELMINTICOS',
                'ANTIHIPERPROLACTINEMICOS',
                'ANTIHISTAMINICOS',
                'ANTIINFLAMATORIOS',
                'ANTILEPROSOS',
                'ANTIMICOTICOS',
                'ANTIMICROBIANOS',
                'ANTIMICROBIANOS OTICOS',
                'ANTIMIGRANOSOS',
                'ANTINEOPLASICOS',
                'ANTINICOTINICOS',
                'ANTIOBESIDAD',
                'ANTIOSTEOPOROSICOS',
                'ANTIPALUDICOS',
                'ANTIPARASITARIOS VAGINALES',
                'ANTIPARKINSONIANOS',
                'ANTIPROSTATICOS',
                'ANTIPROTOZOARIOS',
                'ANTIPSICOTICOS',
                'ANTIRREUMATICOS',
                'ANTISEPTICOS',
                'ANTISEPTICOS URINARIOS',
                'ANTITABAQUISMO',
                'ANTITIROIDEOS',
                'ANTITUBERCULOSOS',
                'ANTITUSIGENOS',
                'ANTIULCEROSOS',
                'ANTIVIRALES',
                'BRONCODILATADORES',
                'COAGULANTES',
                'COLINERGICOS',
                'CORTICOSTEROIDES',
                'DERMATOLOGICOS',
                'DESINFECTANTES',
                'DIURETICOS',
                'DOPAMINERGICOS',
                'ELECTROLITOS ORALES',
                'ESTIMULANTES DE GRANULOCITOS',
                'ESTIMULANTES DE LA CONTRACTILIDAD UTERINA',
                'ESTIMULANTES DE LA MOTILIDAD UTERINA',
                'EXPECTORANTES',
                'GLUCOSIDOS CARDIACOS',
                'HEMATOPOYETICOS',
                'HIPOCALCEMICOS',
                'HIPOLIPEMIANTES',
                'HORMONAS',
                'INDUCTORES DE LA OVULACION',
                'INMUNODEPRESORES',
                'INMUNOGLOBULINAS',
                'LAXANTES',
                'LITOLITICOS',
                'MINERALES',
                'NEUROPROTECTORES',
                'OFTALMICOS',
                'OTROS INOTROPICOS POSITIVOS',
                'OXITOCICOS',
                'PROCINETICOS GASTROINTESTINALES',
                'RELAJANTES MUSCULARES',
                'RELAJANTES VASCULARES',
                'SEDANTES HIPNOTICOS',
                'SOLUCIONES ELECTROLITICAS',
                'SUEROS INMUNITARIOS',
                'TOXOIDES',
                'TROMBOLITICOS',
                'VACUNAS',
                'VITAMINAS',
                'GAS MEDICINAL',
                'FORMULA POLIMERICA',
                'label']


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
    #df = processing.ventana_ini_consulta(df)
    #df = processing.ventana_entre_consultas(df)
    # Ventanas fecha_laboratorio: desde el primer laboratorio y entre laboratorios
    #df = processing.ventana_ini_lab(df)
    
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
    df_vac = pd.read_csv("../../data/med2.csv", encoding='ISO-8859-1')
    df_vac = df_vac.rename(columns={'ANTIMIGRAÃ\x91OSOS': 'ANTIMIGRANOSOS'})
    df = processing.clas_med(df,df_vac)
    
    return df
    

def gpo_med(df):
    """
    """
    df_m = pd.read_csv("../../data/CBM4.csv", encoding='ISO-8859-1')
    df_m = df_m.drop(['id','Grupo','Producto_Activo','Cve_Med.1','Cve_Med','GPO','GPO1','ESP','DIF',
                      'VAR','CUADRO_BASICO_SAI','PROGRAMA_MEDICO','Unidades', 'Medida','GRUPO'], axis=1)
    df_m = df_m.rename(columns={'g1_ANALGESICOS': 'g1','g2_ANESTESIA': 'g2'})
    df = processing.cod_medicamento(df_m,df)
    
    # Número de medicamentos
    df = processing.num_medicamentos(df)
    
    # Pegando atributos medicamentos
    df = processing.medicine_cat(df,df_m)
    
    return df

def create_window(df, tam_ventana):
    """
    """
    # Process unique cx_curp
    df_time = df.groupby('cx_curp')['fecha_consulta'].min()
    df_time = pd.DataFrame(df_time).sort_values('cx_curp')
    df_time['year_consulta'] = df_time['fecha_consulta'].dt.year
    df_hta = df[~pd.isna(df['fecha_hta_nvo'])].groupby('cx_curp')['fecha_consulta'].min()
    df_hta = pd.DataFrame(df_hta)
    df_hta['año_dx_hta_r'] = pd.to_datetime(df_hta['fecha_consulta'],\
                                                format='%y-%m-%d %H:%M:%S').dt.strftime('%Y')
    df_hta = df_hta.sort_values('cx_curp')
    df_time_hta = pd.merge(df_time, df_hta, on = ["cx_curp"], how="left")
    df_time_hta.rename(columns = {'fecha_consulta_x':'fecha_consulta'}, inplace = True)
    df_time_hta.drop('fecha_consulta_y', inplace=True, axis=1)
    df_time_hta['fecha_consulta'] = pd.to_datetime(df_time_hta['fecha_consulta'],\
                                                format='%y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df_time_hta["descartados"] = np.where((df_time_hta["year_consulta"]==df_time_hta["año_dx_hta_r"]),1,0)
    df_time_hta = df_time_hta[df_time_hta["descartados"]==0]
    df_time_hta= df_time_hta.reset_index()
    df_time_hta = pd.DataFrame(df_time_hta)
    df_time_hta['fecha_consulta']= pd.to_datetime(df_time_hta['fecha_consulta'])    
    
    # Iniciando dataframe de ventanas
    df_window_f = pd.DataFrame(columns = COLUMN_NAMES)

    # Por cada paciente único
    for i in range(len(df_time_hta['cx_curp'])):
        # Inicializando valores
        curp = df_time_hta['cx_curp'][i]
        print(curp,'  --------------------------------------------------------')   
        f_ini = df[(df['cx_curp']==curp)].fecha_consulta.min()
        f_fin = df[(df['cx_curp']==curp)].fecha_consulta.max() 
        print("f_ini - ",f_ini )  
        print("f_fin - ",f_fin)      

        # Ventana por persona    
        f_aux = f_ini
        j = 1
        hta = 0
        dm = 0
        renal = 0
        hta_5 = 0
        # Balance dataframe
        # 1 año
        #hta_val = 3
        # 3 meses
        hta_val = 35

        while (f_aux <= f_fin) and (hta_5 <= hta_val):
            df_window_p = pd.DataFrame(columns = COLUMN_NAMES)  

            a_ini, a_inter, a_fin = processing.fecha_ini_fin(f_aux) 

            d_w1 = df[(df['cx_curp']==curp)&\
                    (df['fecha_consulta'] >= f_aux)&\
                    (df['fecha_consulta'] < a_ini)][['target_hta']]
            w1 = (d_w1[d_w1['target_hta']==1].count()[0])

            d_w2 = df[(df['cx_curp']==curp)&\
                    (df['fecha_consulta'] >= a_ini)&\
                    (df['fecha_consulta'] < a_inter)][['target_hta']]
            w2 = (d_w2[d_w2['target_hta']==1].count()[0])

            d_w3 = df[(df['cx_curp']==curp)&\
                    (df['fecha_consulta'] >= a_inter)&\
                    (df['fecha_consulta'] < a_fin)][['target_hta']]
            w3 = (d_w3[d_w3['target_hta']==1].count()[0])
            a = 0         

            if a==0:

                if(w3 == 0):
                    df_window_p.at[0, 'label'] = 0
                else:
                    df_window_p.at[0, 'label'] = 1
                    hta_5 = hta_5 + 1

                df_aux = df[(df['cx_curp']==curp)&\
                        (df['fecha_consulta'] >= f_aux)&\
                        (df['fecha_consulta'] < a_inter)].sort_values(['cx_curp','fecha_consulta'])

                df_aux['fecha_consulta'] = pd.to_datetime(df_aux['fecha_consulta'],\
                                                          format='%y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
                # if ------------------------------------------------------------------------------------------
                # Listado de variables a generar
                df_window_p.at[0, 'cx_curp'] = curp

                df_window_p.at[0, 'ventana'] = j
                df_window_p.at[0, 'fecha_ini'] = f_ini
                df_window_p.at[0, 'fecha_fin'] = a_inter

                df_window_p.at[0, 'sexo'] = df_aux[~pd.isna(df_aux['sexo'])][['sexo']].mode().values

                df_window_p.at[0, 'sum_num_consultas'] = df_aux.count()[0]
                df_window_p.at[0, 'avg_num_consultas_by_year'] = df_aux.count()[0] / tam_ventana

                #---------  dm            
                if (df_aux.loc[df_aux['dm_cie_unic'] == 1].count()[0] > 0) or (dm == 1):
                    df_window_p.at[0, 'dm'] = 1
                    dm = 1
                else:
                    df_window_p.at[0, 'dm'] = 0

                if(df_aux[~pd.isna(df_aux['año_dx_dm'])].count()[0] > 0):
                    df_window_p.at[0, 'año_dx_dm'] = df_aux[~pd.isna(df_aux['año_dx_dm'])][['año_dx_dm']].mean()[0]
                else:
                    df_window_p.at[0, 'año_dx_dm'] = np.nan

                if(df_aux[~pd.isna(df_aux['dm_años_int_ini_db_dx'])].count()[0] > 0):
                    df_window_p.at[0, 'dm_años_int'] = df_aux[~pd.isna(df_aux['dm_años_int_ini_db_dx'])][['dm_años_int_ini_db_dx']].mean()[0]
                else:
                    df_window_p.at[0, 'dm_años_int'] = np.nan

                #---------  renal      
                if(df_aux.loc[df_aux['renal_cie_unic'] == 1].count()[0] > 0 or renal == 1):
                    df_window_p.at[0, 'renal'] = 1
                    renal = 1
                else:
                    df_window_p.at[0, 'renal'] = 0

                if(df_aux[~pd.isna(df_aux['renal_años_int'])].count()[0] > 0):
                    df_window_p.at[0, 'renal_años_int'] = df_aux[~pd.isna(df_aux['renal_años_int'])][['renal_años_int']].mean()[0]
                else:
                    df_window_p.at[0, 'renal_años_int'] = np.nan 
                #-----------------------------    
                if(df_aux[~pd.isna(df_aux['edad'])].count()[0] > 0):
                    df_window_p.at[0, 'edad_range'] = processing.edad_range_e(df_aux[~pd.isna(df_aux['edad'])]\
                                                                        [['edad']].mean()[0])
                else:
                    df_window_p.at[0, 'edad_range'] = np.nan

                if(df_aux[~pd.isna(df_aux['year_nac'])].count()[0] > 0):
                    df_window_p.at[0, 'epoca_nac'] = processing.epoca_nac_a(df_aux[~pd.isna(df_aux['year_nac'])]\
                                                                      [['year_nac']].mean()[0])
                else:
                    df_window_p.at[0, 'epoca_nac'] = np.nan

                if(df_aux[~pd.isna(df_aux['imc_calculado'])].count()[0] > 0):
                    df_window_p.at[0, 'imc_range'] = processing.imc_calculo_range_imc(df_aux[~pd.isna(df_aux['imc_calculado'])]\
                                                                                [['imc_calculado']].mean()[0])
                else:
                    df_window_p.at[0, 'imc_range'] = np.nan  
                # -------------------------                    
                if(df_aux[~pd.isna(df_aux['num_med'])].count()[0] > 0):
                    df_window_p.at[0, 'num_med'] = df_aux[~pd.isna(df_aux['num_med'])].count()[0]
                    df_window_p.at[0, 'avg_num_med'] = df_aux[~pd.isna(df_aux['num_med'])][['num_med']].mean()[0]
                    df_window_p.at[0, 'min_num_med'] = df_aux[~pd.isna(df_aux['num_med'])][['num_med']].min()[0]
                    df_window_p.at[0, 'max_num_med'] = df_aux[~pd.isna(df_aux['num_med'])][['num_med']].max()[0]
                else:
                    df_window_p.at[0, 'num_med'] = np.nan
                    df_window_p.at[0, 'avg_num_med'] = np.nan
                    df_window_p.at[0, 'min_num_med'] = np.nan
                    df_window_p.at[0, 'max_num_med'] = np.nan 
                #------    
                if(df_aux[~pd.isna(df_aux['glucosa1'])].count()[0] > 0):
                    df_window_p.at[0, 'preglucosa'] = 1
                    df_window_p.at[0, 'num_med_preglucosa'] = df_aux[~pd.isna(df_aux['glucosa1'])].count()[0]
                    df_window_p.at[0, 'avg_preglucosa'] = df_aux[~pd.isna(df_aux['glucosa1'])][['glucosa1']].mean()[0]
                    df_window_p.at[0, 'min_preglucosa'] = df_aux[~pd.isna(df_aux['glucosa1'])][['glucosa1']].min()[0]
                    df_window_p.at[0, 'max_preglucosa'] = df_aux[~pd.isna(df_aux['glucosa1'])][['glucosa1']].max()[0]                
                else:
                    df_window_p.at[0, 'preglucosa'] = 0
                    df_window_p.at[0, 'num_med_preglucosa'] = np.nan
                    df_window_p.at[0, 'avg_preglucosa'] = np.nan
                    df_window_p.at[0, 'min_preglucosa'] = np.nan
                    df_window_p.at[0, 'max_preglucosa'] = np.nan

                if(df_aux[~pd.isna(df_aux['glucosa2'])].count()[0] > 0):
                    df_window_p.at[0, 'postglucosa'] = 1
                    df_window_p.at[0, 'num_med_postglucosa'] = df_aux[~pd.isna(df_aux['glucosa2'])].count()[0]
                    df_window_p.at[0, 'avg_postglucosa'] = df_aux[~pd.isna(df_aux['glucosa2'])][['glucosa2']].mean()[0]
                    df_window_p.at[0, 'min_postglucosa'] = df_aux[~pd.isna(df_aux['glucosa2'])][['glucosa2']].min()[0]
                    df_window_p.at[0, 'max_postglucosa'] = df_aux[~pd.isna(df_aux['glucosa2'])][['glucosa2']].max()[0]
                else:
                    df_window_p.at[0, 'postglucosa'] = 0
                    df_window_p.at[0, 'num_med_postglucosa'] = np.nan
                    df_window_p.at[0, 'avg_postglucosa'] = np.nan
                    df_window_p.at[0, 'min_postglucosa'] = np.nan
                    df_window_p.at[0, 'max_postglucosa'] = np.nan

                if df_aux[df_aux['lab_colesterol']==1].count()[0] > 0:
                    df_window_p.at[0, 'colesterol'] = 1
                    df_window_p.at[0, 'num_med_colesterol'] = df_aux[df_aux['lab_colesterol']==1].count()[0]
                    df_window_p.at[0, 'avg_colesterol'] = df_aux[~pd.isna(df_aux['colesterol'])][['colesterol']].mean()[0]
                    df_window_p.at[0, 'min_colesterol'] = df_aux[~pd.isna(df_aux['colesterol'])][['colesterol']].min()[0]
                    df_window_p.at[0, 'max_colesterol'] = df_aux[~pd.isna(df_aux['colesterol'])][['colesterol']].max()[0]
                else:
                    df_window_p.at[0, 'colesterol'] = 0
                    df_window_p.at[0, 'num_med_colesterol'] = np.nan
                    df_window_p.at[0, 'avg_colesterol'] = np.nan
                    df_window_p.at[0, 'min_colesterol'] = np.nan
                    df_window_p.at[0, 'max_colesterol'] = np.nan

                if df_aux[df_aux['lab_trigliceridos']==1].count()[0] > 0:
                    df_window_p.at[0, 'trigliceridos'] = 1
                    df_window_p.at[0, 'num_med_trigliceridos'] = df_aux[df_aux['lab_trigliceridos']==1].count()[0]
                    df_window_p.at[0, 'avg_trigliceridos'] = df_aux[~pd.isna(df_aux['trigliceridos'])][['trigliceridos']].mean()[0]
                    df_window_p.at[0, 'min_trigliceridos'] = df_aux[~pd.isna(df_aux['trigliceridos'])][['trigliceridos']].min()[0]
                    df_window_p.at[0, 'max_trigliceridos'] = df_aux[~pd.isna(df_aux['trigliceridos'])][['trigliceridos']].max()[0]
                else:
                    df_window_p.at[0, 'trigliceridos'] = 0
                    df_window_p.at[0, 'num_med_trigliceridos'] = np.nan
                    df_window_p.at[0, 'avg_trigliceridos'] = np.nan
                    df_window_p.at[0, 'min_trigliceridos'] = np.nan
                    df_window_p.at[0, 'max_trigliceridos'] = np.nan

                if df_aux[df_aux['lab_hdl']==1].count()[0] > 0:
                    df_window_p.at[0, 'hdl'] = 1
                    df_window_p.at[0, 'num_med_hdl'] = df_aux[df_aux['lab_hdl']==1].count()[0]
                    df_window_p.at[0, 'avg_hdl'] = df_aux[~pd.isna(df_aux['hdl'])][['hdl']].mean()[0]
                    df_window_p.at[0, 'min_hdl'] = df_aux[~pd.isna(df_aux['hdl'])][['hdl']].min()[0]
                    df_window_p.at[0, 'max_hdl'] = df_aux[~pd.isna(df_aux['hdl'])][['hdl']].max()[0]
                else:
                    df_window_p.at[0, 'hdl'] = 0
                    df_window_p.at[0, 'num_med_hdl'] = np.nan
                    df_window_p.at[0, 'avg_hdl'] = np.nan
                    df_window_p.at[0, 'min_hdl'] = np.nan
                    df_window_p.at[0, 'max_hdl'] = np.nan

                if df_aux[df_aux['lab_ldl']==1].count()[0] > 0:
                    df_window_p.at[0, 'ldl'] = 1
                    df_window_p.at[0, 'num_med_ldl'] = df_aux[df_aux['lab_ldl']==1].count()[0]
                    df_window_p.at[0, 'avg_ldl'] = df_aux[~pd.isna(df_aux['ldl'])][['ldl']].mean()[0]
                    df_window_p.at[0, 'min_ldl'] = df_aux[~pd.isna(df_aux['ldl'])][['ldl']].min()[0]
                    df_window_p.at[0, 'max_ldl'] = df_aux[~pd.isna(df_aux['ldl'])][['ldl']].max()[0]
                else:
                    df_window_p.at[0, 'ldl'] = 0
                    df_window_p.at[0, 'num_med_ldl'] = np.nan
                    df_window_p.at[0, 'avg_ldl'] = np.nan
                    df_window_p.at[0, 'min_ldl'] = np.nan
                    df_window_p.at[0, 'max_ldl'] = np.nan

                if (df_aux[~pd.isna(df_aux['presion_arterial'])].count()[0] > 0):
                    df_window_p.at[0, 'presion_arterial'] = 1
                    df_window_p.at[0, 'num_med_presion_a'] = df_aux[~pd.isna(df_aux['presion_arterial'])].count()[0] 
                    if (df_aux[~pd.isna(df_aux['sistolica_a'])].count()[0] > 0):
                        df_window_p.at[0, 'avg_sistolica_a'] = df_aux[~pd.isna(df_aux['sistolica_a'])][['sistolica_a']].mean()[0]
                        df_window_p.at[0, 'min_sistolica_a'] = df_aux[~pd.isna(df_aux['sistolica_a'])][['sistolica_a']].min()[0]
                        df_window_p.at[0, 'max_sistolica_a'] = df_aux[~pd.isna(df_aux['sistolica_a'])][['sistolica_a']].max()[0]
                        df_window_p.at[0, 'fn_sistolica_a'] = df_aux[df_aux['fecha_consulta'] == max(df_aux['fecha_consulta'])][['sistolica_a']].iat[0,0]
                    else:
                        df_window_p.at[0, 'avg_sistolica_a'] = np.nan
                        df_window_p.at[0, 'min_sistolica_a'] = np.nan
                        df_window_p.at[0, 'max_sistolica_a'] = np.nan
                        df_window_p.at[0, 'fn_sistolica_a'] = np.nan

                    if (df_aux[~pd.isna(df_aux['diastolica_a'])].count()[0] > 0):
                        df_window_p.at[0, 'avg_diastolica_a'] = df_aux[~pd.isna(df_aux['diastolica_a'])][['diastolica_a']].mean()[0]
                        df_window_p.at[0, 'min_diastolica_a'] = df_aux[~pd.isna(df_aux['diastolica_a'])][['diastolica_a']].min()[0]
                        df_window_p.at[0, 'max_diastolica_a'] = df_aux[~pd.isna(df_aux['diastolica_a'])][['diastolica_a']].max()[0]
                        df_window_p.at[0, 'fn_diastolica_a'] = df_aux[df_aux['fecha_consulta'] == max(df_aux['fecha_consulta'])][['diastolica_a']].iat[0,0]
                    else:
                        df_window_p.at[0, 'avg_diastolica_a'] = np.nan
                        df_window_p.at[0, 'min_diastolica_a'] = np.nan
                        df_window_p.at[0, 'max_diastolica_a'] = np.nan 
                        df_window_p.at[0, 'fn_diastolica_a'] = np.nan

                    map_v = (df_window_p.at[0, 'avg_sistolica_a']  + (2*df_window_p.at[0, 'avg_diastolica_a']))/3

                    if (map_v <= 107):
                        df_window_p.at[0, 'map_g'] = 1 #grado1
                    elif ((map_v > 107) & (map_v <=120)):
                        df_window_p.at[0, 'map_g'] = 2 #grado2
                    elif ((map_v > 120) & (map_v <=133)):
                        df_window_p.at[0, 'map_g'] = 3 #severa
                    elif (map_v > 133):
                        df_window_p.at[0, 'map_g'] = 4 #crisis hta
                else:
                    df_window_p.at[0, 'presion_arterial'] = 0
                    df_window_p.at[0, 'num_med_presion_a'] = 0
                    df_window_p.at[0, 'avg_sistolica_a'] = np.nan
                    df_window_p.at[0, 'min_sistolica_a'] = np.nan
                    df_window_p.at[0, 'max_sistolica_a'] = np.nan
                    df_window_p.at[0, 'fn_sistolica_a'] = np.nan
                    df_window_p.at[0, 'avg_diastolica_a'] = np.nan
                    df_window_p.at[0, 'min_diastolica_a'] = np.nan
                    df_window_p.at[0, 'max_diastolica_a'] = np.nan 
                    df_window_p.at[0, 'fn_diastolica_a'] = np.nan     
                    df_window_p.at[0, 'map_g'] = 0

                if df_aux[df_aux['lab_hba1c']==1].count()[0] > 0:
                    df_window_p.at[0, 'hba1c'] = 1
                    df_window_p.at[0, 'num_med_hba1c'] = df_aux[df_aux['lab_hba1c']==1].count()[0]
                    df_window_p.at[0, 'avg_hba1c'] = df_aux[~pd.isna(df_aux['hba1c'])][['hba1c']].mean()[0]
                    df_window_p.at[0, 'min_hba1c'] = df_aux[~pd.isna(df_aux['hba1c'])][['hba1c']].min()[0]
                    df_window_p.at[0, 'max_hba1c'] = df_aux[~pd.isna(df_aux['hba1c'])][['hba1c']].max()[0]
                else:
                    df_window_p.at[0, 'hba1c'] = 0
                    df_window_p.at[0, 'num_med_hba1c'] = np.nan
                    df_window_p.at[0, 'avg_hba1c'] = np.nan
                    df_window_p.at[0, 'min_hba1c'] = np.nan
                    df_window_p.at[0, 'max_hba1c'] = np.nan         

                if df_aux[df_aux['lab_plaquetas']==1].count()[0] > 0:
                    df_window_p.at[0, 'plaquetas'] = 1
                    df_window_p.at[0, 'num_med_plaquetas'] = df_aux[df_aux['lab_plaquetas']==1].count()[0]
                    df_window_p.at[0, 'avg_plaquetas'] = df_aux[~pd.isna(df_aux['plaquetas'])][['plaquetas']].mean()[0]
                    df_window_p.at[0, 'min_plaquetas'] = df_aux[~pd.isna(df_aux['plaquetas'])][['plaquetas']].min()[0]
                    df_window_p.at[0, 'max_plaquetas'] = df_aux[~pd.isna(df_aux['plaquetas'])][['plaquetas']].max()[0]
                else:
                    df_window_p.at[0, 'plaquetas'] = 0
                    df_window_p.at[0, 'num_med_plaquetas'] = np.nan
                    df_window_p.at[0, 'avg_plaquetas'] = np.nan
                    df_window_p.at[0, 'min_plaquetas'] = np.nan
                    df_window_p.at[0, 'max_plaquetas'] = np.nan     

                if df_aux[df_aux['lab_creatinina']==1].count()[0] > 0:
                    df_window_p.at[0, 'creatinina'] = 1
                    df_window_p.at[0, 'num_med_creatinina'] = df_aux[df_aux['lab_creatinina']==1].count()[0]
                    df_window_p.at[0, 'avg_creatinina'] = df_aux[~pd.isna(df_aux['creatinina'])][['creatinina']].mean()[0]
                    df_window_p.at[0, 'min_creatinina'] = df_aux[~pd.isna(df_aux['creatinina'])][['creatinina']].min()[0]
                    df_window_p.at[0, 'max_creatinina'] = df_aux[~pd.isna(df_aux['creatinina'])][['creatinina']].max()[0]
                else:
                    df_window_p.at[0, 'creatinina'] = 0
                    df_window_p.at[0, 'num_med_plaquetas'] = np.nan
                    df_window_p.at[0, 'avg_creatinina'] = np.nan
                    df_window_p.at[0, 'min_creatinina'] = np.nan
                    df_window_p.at[0, 'max_creatinina'] = np.nan   

                if df_aux[df_aux['lab_acido_urico']==1].count()[0] > 0:
                    df_window_p.at[0, 'acido_urico'] = 1
                    df_window_p.at[0, 'num_med_acido_urico'] = df_aux[df_aux['lab_acido_urico']==1].count()[0]
                    df_window_p.at[0, 'avg_acido_urico'] = df_aux[~pd.isna(df_aux['acido_urico'])][['acido_urico']].mean()[0]
                    df_window_p.at[0, 'min_acido_urico'] = df_aux[~pd.isna(df_aux['acido_urico'])][['acido_urico']].min()[0]
                    df_window_p.at[0, 'max_acido_urico'] = df_aux[~pd.isna(df_aux['acido_urico'])][['acido_urico']].max()[0]
                else:
                    df_window_p.at[0, 'acido_urico'] = 0
                    df_window_p.at[0, 'num_med_acido_urico'] = np.nan
                    df_window_p.at[0, 'avg_acido_urico'] = np.nan
                    df_window_p.at[0, 'min_acido_urico'] = np.nan
                    df_window_p.at[0, 'max_acido_urico'] = np.nan

                if df_aux[df_aux['lab_urea']==1].count()[0] > 0:
                    df_window_p.at[0, 'urea'] = 1
                    df_window_p.at[0, 'num_med_urea'] = df_aux[df_aux['lab_urea']==1].count()[0]
                    df_window_p.at[0, 'avg_urea'] = df_aux[~pd.isna(df_aux['urea'])][['urea']].mean()[0]
                    df_window_p.at[0, 'min_urea'] = df_aux[~pd.isna(df_aux['urea'])][['urea']].min()[0]
                    df_window_p.at[0, 'max_urea'] = df_aux[~pd.isna(df_aux['urea'])][['urea']].max()[0]
                else:
                    df_window_p.at[0, 'urea'] = 0
                    df_window_p.at[0, 'num_med_urea'] = np.nan
                    df_window_p.at[0, 'avg_urea'] = np.nan
                    df_window_p.at[0, 'min_urea'] = np.nan
                    df_window_p.at[0, 'max_urea'] = np.nan

                if df_aux[df_aux['lab_tfg']==1].count()[0] > 0:
                    df_window_p.at[0, 'tfg'] = 1
                    df_window_p.at[0, 'num_med_tfg'] = df_aux[df_aux['lab_tfg']==1].count()[0]
                    df_window_p.at[0, 'avg_tfg'] = df_aux[~pd.isna(df_aux['tfg'])][['tfg']].mean()[0]
                    df_window_p.at[0, 'min_tfg'] = df_aux[~pd.isna(df_aux['tfg'])][['tfg']].min()[0]
                    df_window_p.at[0, 'max_tfg'] = df_aux[~pd.isna(df_aux['tfg'])][['tfg']].max()[0]
                else:
                    df_window_p.at[0, 'tfg'] = 0
                    df_window_p.at[0, 'num_med_tfg'] = np.nan
                    df_window_p.at[0, 'avg_tfg'] = np.nan
                    df_window_p.at[0, 'min_tfg'] = np.nan
                    df_window_p.at[0, 'max_tfg'] = np.nan
                # --------------------------------------------------------
                if df_aux[df_aux['enf_inf_intestinales']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_inf_intestinales'] = 1
                else:
                    df_window_p.at[0, 'enf_inf_intestinales'] = 0

                if df_aux[df_aux['tuberculosis']==1].count()[0] > 0:
                    df_window_p.at[0, 'tuberculosis'] = 1
                else:
                    df_window_p.at[0, 'tuberculosis'] = 0

                if df_aux[df_aux['ot_enf_bacterianas']==1].count()[0] > 0:
                    df_window_p.at[0, 'ot_enf_bacterianas'] = 1
                else:
                    df_window_p.at[0, 'ot_enf_bacterianas'] = 0

                if df_aux[df_aux['inf_trans_pred_sexual']==1].count()[0] > 0:
                    df_window_p.at[0, 'inf_trans_pred_sexual'] = 1
                else:
                    df_window_p.at[0, 'inf_trans_pred_sexual'] = 0

                if df_aux[df_aux['ot_enf_inf_y_paras_y_efec_tardios']==1].count()[0] > 0:
                    df_window_p.at[0, 'ot_enf_inf_y_paras_y_efec_tardios'] = 1
                else:
                    df_window_p.at[0, 'ot_enf_inf_y_paras_y_efec_tardios'] = 0

                if df_aux[df_aux['enf_viricas']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_viricas'] = 1
                else:
                    df_window_p.at[0, 'enf_viricas'] = 0

                if df_aux[df_aux['rickettsiosis_y_ot_enf__protozoarios']==1].count()[0] > 0:
                    df_window_p.at[0, 'rickettsiosis_y_ot_enf__protozoarios'] = 1
                else:
                    df_window_p.at[0, 'rickettsiosis_y_ot_enf__protozoarios'] = 0

                if df_aux[df_aux['tumores_malig_labio_bucal_faringe']==1].count()[0] > 0:
                    df_window_p.at[0, 'tumores_malig_labio_bucal_faringe'] = 1
                else:
                    df_window_p.at[0, 'tumores_malig_labio_bucal_faringe'] = 0

                if df_aux[df_aux['tumores_malig_organos']==1].count()[0] > 0:
                    df_window_p.at[0, 'tumores_malig_organos'] = 1
                else:
                    df_window_p.at[0, 'tumores_malig_organos'] = 0

                if df_aux[df_aux['tumores_malig_org_respiratorios_intratoracicos']==1].count()[0] > 0:
                    df_window_p.at[0, 'tumores_malig_org_respiratorios_intratoracicos'] = 1
                else:
                    df_window_p.at[0, 'tumores_malig_org_respiratorios_intratoracicos'] = 0  

                if df_aux[df_aux['tumores_malig_huesos_articulares_conjuntivo_piel_mama']==1].count()[0] > 0:
                    df_window_p.at[0, 'tumores_malig_huesos_articulares_conjuntivo_piel_mama'] = 1
                else:
                    df_window_p.at[0, 'tumores_malig_huesos_articulares_conjuntivo_piel_mama'] = 0

                if df_aux[df_aux['tumores_malig_org_genitourinarios']==1].count()[0] > 0:
                    df_window_p.at[0, 'tumores_malig_org_genitourinarios'] = 1
                else:
                    df_window_p.at[0, 'tumores_malig_org_genitourinarios'] = 0

                if df_aux[df_aux['tumores_malig_otros_sitios_ne']==1].count()[0] > 0:
                    df_window_p.at[0, 'tumores_malig_otros_sitios_ne'] = 1
                else:
                    df_window_p.at[0, 'tumores_malig_otros_sitios_ne'] = 0 

                if df_aux[df_aux['tumores_malig_tejido_linf_org_hematop']==1].count()[0] > 0:
                    df_window_p.at[0, 'tumores_malig_tejido_linf_org_hematop'] = 1
                else:
                    df_window_p.at[0, 'tumores_malig_tejido_linf_org_hematop'] = 0

                if df_aux[df_aux['tumores_malig_sitios_mul_indep']==1].count()[0] > 0:
                    df_window_p.at[0, 'tumores_malig_sitios_mul_indep'] = 1
                else:
                    df_window_p.at[0, 'tumores_malig_sitios_mul_indep'] = 0

                if df_aux[df_aux['tumores_insitu']==1].count()[0] > 0:
                    df_window_p.at[0, 'tumores_insitu'] = 1
                else:
                    df_window_p.at[0, 'tumores_insitu'] = 0

                if df_aux[df_aux['tumores_benignos']==1].count()[0] > 0:
                    df_window_p.at[0, 'tumores_benignos'] = 1
                else:
                    df_window_p.at[0, 'tumores_benignos'] = 0

                if df_aux[df_aux['tumores_comp_incierto_desc']==1].count()[0] > 0:
                    df_window_p.at[0, 'tumores_comp_incierto_desc'] = 1
                else:
                    df_window_p.at[0, 'tumores_comp_incierto_desc'] = 0

                if df_aux[df_aux['enf_sangre_org_hematop']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_sangre_org_hematop'] = 1
                else:
                    df_window_p.at[0, 'enf_sangre_org_hematop'] = 0

                if df_aux[df_aux['enf_endocrinas']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_endocrinas'] = 1
                else:
                    df_window_p.at[0, 'enf_endocrinas'] = 0

                if df_aux[df_aux['desnutricion_ot_deficiencias']==1].count()[0] > 0:
                    df_window_p.at[0, 'desnutricion_ot_deficiencias'] = 1
                else:
                    df_window_p.at[0, 'desnutricion_ot_deficiencias'] = 0

                if df_aux[df_aux['trastornos_mentales']==1].count()[0] > 0:
                    df_window_p.at[0, 'trastornos_mentales'] = 1
                else:
                    df_window_p.at[0, 'trastornos_mentales'] = 0

                if df_aux[df_aux['enf_sist_nervioso']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_sist_nervioso'] = 1
                else:
                    df_window_p.at[0, 'enf_sist_nervioso'] = 0

                if df_aux[df_aux['enf_ojo_anexos']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_ojo_anexos'] = 1
                else:
                    df_window_p.at[0, 'enf_ojo_anexos'] = 0

                if df_aux[df_aux['enf_oido_apofisis_mastoides']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_oido_apofisis_mastoides'] = 1
                else:
                    df_window_p.at[0, 'enf_oido_apofisis_mastoides'] = 0

                if df_aux[df_aux['fiebre_y_enf_cardiacas_reumaticas']==1].count()[0] > 0:
                    df_window_p.at[0, 'fiebre_y_enf_cardiacas_reumaticas'] = 1
                else:
                    df_window_p.at[0, 'fiebre_y_enf_cardiacas_reumaticas'] = 0

                if df_aux[df_aux['enf_isquemicas_corazon']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_isquemicas_corazon'] = 1
                else:
                    df_window_p.at[0, 'enf_isquemicas_corazon'] = 0

                if df_aux[df_aux['enf_circulacion_pulmonar_enf_corazon']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_circulacion_pulmonar_enf_corazon'] = 1
                else:
                    df_window_p.at[0, 'enf_circulacion_pulmonar_enf_corazon'] = 0

                if df_aux[df_aux['enf_cerebrovasculares']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_cerebrovasculares'] = 1
                else:
                    df_window_p.at[0, 'enf_cerebrovasculares'] = 0

                if df_aux[df_aux['otras_enf_aparato_vasc']==1].count()[0] > 0:
                    df_window_p.at[0, 'otras_enf_aparato_vasc'] = 1
                else:
                    df_window_p.at[0, 'otras_enf_aparato_vasc'] = 0
                    
                if df_aux[df_aux['inf_y_enf_vias_respiratorias_sup']==1].count()[0] > 0:
                    df_window_p.at[0, 'inf_y_enf_vias_respiratorias_sup'] = 1
                else:
                    df_window_p.at[0, 'inf_y_enf_vias_respiratorias_sup'] = 0

                if df_aux[df_aux['otras_enf_aparato_resp']==1].count()[0] > 0:
                    df_window_p.at[0, 'otras_enf_aparato_resp'] = 1
                else:
                    df_window_p.at[0, 'otras_enf_aparato_resp'] = 0

                if df_aux[df_aux['enf_cavidad_bucal_glandulas_salivales']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_cavidad_bucal_glandulas_salivales'] = 1
                else:
                    df_window_p.at[0, 'enf_cavidad_bucal_glandulas_salivales'] = 0

                if df_aux[df_aux['enf_ot_partes_aparato_digestivo']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_ot_partes_aparato_digestivo'] = 1
                else:
                    df_window_p.at[0, 'enf_ot_partes_aparato_digestivo'] = 0

                if df_aux[df_aux['enf_piel_tejido_subcutaneo']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_piel_tejido_subcutaneo'] = 1
                else:
                    df_window_p.at[0, 'enf_piel_tejido_subcutaneo'] = 0

                if df_aux[df_aux['enf_sist_osteomuscular_y_tejido']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_sist_osteomuscular_y_tejido'] = 1
                else:
                    df_window_p.at[0, 'enf_sist_osteomuscular_y_tejido'] = 0

                if df_aux[df_aux['enf_aparato_urinario']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_aparato_urinario'] = 1
                else:
                    df_window_p.at[0, 'enf_aparato_urinario'] = 0

                if df_aux[df_aux['enf_org_genitales_masculinos']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_org_genitales_masculinos'] = 1
                else:
                    df_window_p.at[0, 'enf_org_genitales_masculinos'] = 0

                if df_aux[df_aux['trastornos_mama']==1].count()[0] > 0:
                    df_window_p.at[0, 'trastornos_mama'] = 1
                else:
                    df_window_p.at[0, 'trastornos_mama'] = 0  

                if df_aux[df_aux['enf_org_genitales_femeninos']==1].count()[0] > 0:
                    df_window_p.at[0, 'enf_org_genitales_femeninos'] = 1
                else:
                    df_window_p.at[0, 'enf_org_genitales_femeninos'] = 0   

                if df_aux[df_aux['trastornos_sist_genitourinario_consec_proced']==1].count()[0] > 0:
                    df_window_p.at[0, 'trastornos_sist_genitourinario_consec_proced'] = 1
                else:
                    df_window_p.at[0, 'trastornos_sist_genitourinario_consec_proced'] = 0   

                if df_aux[df_aux['causas_obstetricas_directas']==1].count()[0] > 0:
                    df_window_p.at[0, 'causas_obstetricas_directas'] = 1
                else:
                    df_window_p.at[0, 'causas_obstetricas_directas'] = 0     

                if df_aux[df_aux['parto']==1].count()[0] > 0:
                    df_window_p.at[0, 'parto'] = 1
                else:
                    df_window_p.at[0, 'parto'] = 0   

                if df_aux[df_aux['causas_obstetricas_indirectas']==1].count()[0] > 0:
                    df_window_p.at[0, 'causas_obstetricas_indirectas'] = 1
                else:
                    df_window_p.at[0, 'causas_obstetricas_indirectas'] = 0

                if df_aux[df_aux['malformaciones_congenitas']==1].count()[0] > 0:
                    df_window_p.at[0, 'malformaciones_congenitas'] = 1
                else:
                    df_window_p.at[0, 'malformaciones_congenitas'] = 0

                if df_aux[df_aux['sintomas_signos_hallazgos_anormales_clin_lab_no_clasif']==1].count()[0] > 0:
                    df_window_p.at[0, 'sintomas_signos_hallazgos_anormales_clin_lab_no_clasif'] = 1
                else:
                    df_window_p.at[0, 'sintomas_signos_hallazgos_anormales_clin_lab_no_clasif'] = 0 

                if df_aux[df_aux['fracturas']==1].count()[0] > 0:
                    df_window_p.at[0, 'fracturas'] = 1
                else:
                    df_window_p.at[0, 'fracturas'] = 0

                if df_aux[df_aux['luxaciones_esguinces_torceduras']==1].count()[0] > 0:
                    df_window_p.at[0, 'luxaciones_esguinces_torceduras'] = 1
                else:
                    df_window_p.at[0, 'luxaciones_esguinces_torceduras'] = 0

                if df_aux[df_aux['traumatismos_int_intracraneales_y_otr']==1].count()[0] > 0:
                    df_window_p.at[0, 'traumatismos_int_intracraneales_y_otr'] = 1
                else:
                    df_window_p.at[0, 'traumatismos_int_intracraneales_y_otr'] = 0

                if df_aux[df_aux['heridas']==1].count()[0] > 0:
                    df_window_p.at[0, 'heridas'] = 1
                else:
                    df_window_p.at[0, 'heridas'] = 0

                if df_aux[df_aux['efec_cuerpos_extr_pen_orificios_naturales']==1].count()[0] > 0:
                    df_window_p.at[0, 'efec_cuerpos_extr_pen_orificios_naturales'] = 1
                else:
                    df_window_p.at[0, 'efec_cuerpos_extr_pen_orificios_naturales'] = 0

                if df_aux[df_aux['quemaduras_corrosiones']==1].count()[0] > 0:
                    df_window_p.at[0, 'quemaduras_corrosiones'] = 1
                else:
                    df_window_p.at[0, 'quemaduras_corrosiones'] = 0

                if df_aux[df_aux['envenenamiento_efectos_tox']==1].count()[0] > 0:
                    df_window_p.at[0, 'envenenamiento_efectos_tox'] = 1
                else:
                    df_window_p.at[0, 'envenenamiento_efectos_tox'] = 0

                if df_aux[df_aux['sindrome_maltrato']==1].count()[0] > 0:
                    df_window_p.at[0, 'sindrome_maltrato'] = 1
                else:
                    df_window_p.at[0, 'sindrome_maltrato'] = 0

                if df_aux[df_aux['comp_precoces_traumatismos']==1].count()[0] > 0:
                    df_window_p.at[0, 'comp_precoces_traumatismos'] = 1
                else:
                    df_window_p.at[0, 'comp_precoces_traumatismos'] = 0

                if df_aux[df_aux['comp_aten_med_qx_no_clasif']==1].count()[0] > 0:
                    df_window_p.at[0, 'comp_aten_med_qx_no_clasif'] = 1
                else:
                    df_window_p.at[0, 'comp_aten_med_qx_no_clasif'] = 0

                if df_aux[df_aux['sec_traumatismos_envenenamiento_causas_ext']==1].count()[0] > 0:
                    df_window_p.at[0, 'sec_traumatismos_envenenamiento_causas_ext'] = 1
                else:
                    df_window_p.at[0, 'sec_traumatismos_envenenamiento_causas_ext'] = 0

                if df_aux[df_aux['ot_efec_causas_ext_comp_traumatismos']==1].count()[0] > 0:
                    df_window_p.at[0, 'ot_efec_causas_ext_comp_traumatismos'] = 1
                else:
                    df_window_p.at[0, 'ot_efec_causas_ext_comp_traumatismos'] = 0

                # DIABETES
                if df_aux[df_aux['E10']==1].count()[0] > 0:
                    df_window_p.at[0, 'E10'] = 1
                else:
                    df_window_p.at[0, 'E10'] = 0

                if df_aux[df_aux['E11']==1].count()[0] > 0:
                    df_window_p.at[0, 'E11'] = 1
                else:
                    df_window_p.at[0, 'E11'] = 0

                if df_aux[df_aux['E12']==1].count()[0] > 0:
                    df_window_p.at[0, 'E12'] = 1
                else:
                    df_window_p.at[0, 'E12'] = 0

                if df_aux[df_aux['E13']==1].count()[0] > 0:
                    df_window_p.at[0, 'E13'] = 1
                else:
                    df_window_p.at[0, 'E13'] = 0

                if df_aux[df_aux['E14']==1].count()[0] > 0:
                    df_window_p.at[0, 'E14'] = 1
                else:
                    df_window_p.at[0, 'E14'] = 0
                #-----------------------
                if df_aux[df_aux['K70_K77']==1].count()[0] > 0:
                    df_window_p.at[0, 'K70_K77'] = 1
                else:
                    df_window_p.at[0, 'K70_K77'] = 0
                #-------------------     
                if df_aux[df_aux['E0_E64']==1].count()[0] > 0:
                    df_window_p.at[0, 'E0_E64'] = 1
                else:
                    df_window_p.at[0, 'E0_E64'] = 0
                #-------------------------------------  
                if df_aux[df_aux['E65_E68']==1].count()[0] > 0:
                    df_window_p.at[0, 'E65_E68'] = 1
                else:
                    df_window_p.at[0, 'E65_E68'] = 0
                # --------------------------------
                if df_aux[df_aux['E70_E90']==1].count()[0] > 0:
                    df_window_p.at[0, 'E70_E90'] = 1
                else:
                    df_window_p.at[0, 'E70_E90'] = 0
                #-------------------
                if df_aux[df_aux['O10_O16']==1].count()[0] > 0:
                    df_window_p.at[0, 'O10_O16'] = 1
                else:
                    df_window_p.at[0, 'O10_O16'] = 0

                if df_aux[df_aux['O22']==1].count()[0] > 0:
                    df_window_p.at[0, 'O22'] = 1
                else:
                    df_window_p.at[0, 'O22'] = 0

                if df_aux[df_aux['O24']==1].count()[0] > 0:
                    df_window_p.at[0, 'O24'] = 1
                else:
                    df_window_p.at[0, 'O24'] = 0
                # -----------------------------
                if df_aux[df_aux['Y52_T46']==1].count()[0] > 0:
                    df_window_p.at[0, 'Y52_T46'] = 1
                else:
                    df_window_p.at[0, 'Y52_T46'] = 0
                #---------    
                if df_aux[df_aux['I6_I8']==1].count()[0] > 0:
                    df_window_p.at[0, 'I6_I8'] = 1
                else:
                    df_window_p.at[0, 'I6_I8'] = 0
                #-------------------
                if df_aux[df_aux['R0_R4']==1].count()[0] > 0:
                    df_window_p.at[0, 'R0_R4'] = 1
                else:
                    df_window_p.at[0, 'R0_R4'] = 0
                #--------------
                if df_aux[df_aux['g1']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g1'] = 1                             
                else:                 
                    df_window_p.at[0, 'g1'] = 0             

                if df_aux[df_aux['g2']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g2'] = 1                            
                else:                 
                    df_window_p.at[0, 'g2'] = 0             

                if df_aux[df_aux['g3']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g3'] = 1                            
                else:                 
                    df_window_p.at[0, 'g3'] = 0            

                if df_aux[df_aux['g4']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g4'] = 1                          
                else:                 
                    df_window_p.at[0, 'g4'] = 0           

                if df_aux[df_aux['g5']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g5'] = 1                             
                else:                 
                    df_window_p.at[0, 'g5'] = 0             

                if df_aux[df_aux['g6']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g6'] = 1                           
                else:                 
                    df_window_p.at[0, 'g6'] = 0            

                if df_aux[df_aux['g7']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g7'] = 1                           
                else:                 
                    df_window_p.at[0, 'g7'] = 0              

                if df_aux[df_aux['g8']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g8'] = 1                            
                else:                 
                    df_window_p.at[0, 'g8'] = 0              

                if df_aux[df_aux['g9']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g9'] = 1                            
                else:                 
                    df_window_p.at[0, 'g9'] = 0            

                if df_aux[df_aux['g10']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g10'] = 1                             
                else:                 
                    df_window_p.at[0, 'g10'] = 0            

                if df_aux[df_aux['g11']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g11'] = 1                            
                else:                 
                    df_window_p.at[0, 'g11'] = 0             

                if df_aux[df_aux['g12']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g12'] = 1                            
                else:                 
                    df_window_p.at[0, 'g12'] = 0            

                if df_aux[df_aux['g13']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g13'] = 1                          
                else:                 
                    df_window_p.at[0, 'g13'] = 0            

                if df_aux[df_aux['g14']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g14'] = 1                            
                else:                 
                    df_window_p.at[0, 'g14'] = 0            

                if df_aux[df_aux['g15']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g15'] = 1                             
                else:                 
                    df_window_p.at[0, 'g15'] = 0            

                if df_aux[df_aux['g16']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g16'] = 1                            
                else:                 
                    df_window_p.at[0, 'g16'] = 0           

                if df_aux[df_aux['g17']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g17'] = 1                           
                else:                 
                    df_window_p.at[0, 'g17'] = 0            

                if df_aux[df_aux['g18']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g18'] = 1                            
                else:                 
                    df_window_p.at[0, 'g18'] = 0            

                if df_aux[df_aux['g19']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g19'] = 1                          
                else:                 
                    df_window_p.at[0, 'g19'] = 0             

                if df_aux[df_aux['g20']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g20'] = 1                          
                else:                 
                    df_window_p.at[0, 'g20'] = 0            

                if df_aux[df_aux['g21']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g21'] = 1                            
                else:                 
                    df_window_p.at[0, 'g21'] = 0             

                if df_aux[df_aux['g22']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g22'] = 1                           
                else:                 
                    df_window_p.at[0, 'g22'] = 0               

                if df_aux[df_aux['g23']==1].count()[0] > 0:                 
                    df_window_p.at[0, 'g23'] = 1                           
                else:                 
                    df_window_p.at[0, 'g23'] = 0            
                #-----------------------------------------
                if df_aux[df_aux['ACIDIFICANTES DE LAS VIAS URINARIAS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ACIDIFICANTES DE LAS VIAS URINARIAS'] = 1
                else:
                    df_window_p.at[0, 'ACIDIFICANTES DE LAS VIAS URINARIAS'] = 0
                    
                if df_aux[df_aux['ACTIVADORES DEL METABOLISMO NEURONAL']==1].count()[0] > 0:
                    df_window_p.at[0, 'ACTIVADORES DEL METABOLISMO NEURONAL'] = 1
                else:
                    df_window_p.at[0, 'ACTIVADORES DEL METABOLISMO NEURONAL'] = 0
                    
                if df_aux[df_aux['ADRENERGICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ADRENERGICOS'] = 1
                else:
                    df_window_p.at[0, 'ADRENERGICOS'] = 0
                    
                if df_aux[df_aux['ADYUVANTES DE LA ANALGESIA']==1].count()[0] > 0:
                    df_window_p.at[0, 'ADYUVANTES DE LA ANALGESIA'] = 1
                else:
                    df_window_p.at[0, 'ADYUVANTES DE LA ANALGESIA'] = 0
                    
                if df_aux[df_aux['ANALGESICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANALGESICOS'] = 1
                else:
                    df_window_p.at[0, 'ANALGESICOS'] = 0
                    
                if df_aux[df_aux['ANALGESICOS ANTIINFLAMATORIOS TOPICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANALGESICOS ANTIINFLAMATORIOS TOPICOS'] = 1
                else:
                    df_window_p.at[0, 'ANALGESICOS ANTIINFLAMATORIOS TOPICOS'] = 0
                    
                if df_aux[df_aux['ANESTESICOS GENERALES']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANESTESICOS GENERALES'] = 1
                else:
                    df_window_p.at[0, 'ANESTESICOS GENERALES'] = 0
                    
                if df_aux[df_aux['ANESTESICOS LOCALES']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANESTESICOS LOCALES'] = 1
                else:
                    df_window_p.at[0, 'ANESTESICOS LOCALES'] = 0
                    
                if df_aux[df_aux['ANSIOLITICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANSIOLITICOS'] = 1
                else:
                    df_window_p.at[0, 'ANSIOLITICOS'] = 0
                    
                if df_aux[df_aux['ANTAGONISTAS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTAGONISTAS'] = 1
                else:
                    df_window_p.at[0, 'ANTAGONISTAS'] = 0
                    
                if df_aux[df_aux['ANTIACIDOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIACIDOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIACIDOS'] = 0
                    
                if df_aux[df_aux['ANTIADRENERGICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIADRENERGICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIADRENERGICOS'] = 0
                    
                if df_aux[df_aux['ANTIALCOHOL']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIALCOHOL'] = 1
                else:
                    df_window_p.at[0, 'ANTIALCOHOL'] = 0
                    
                if df_aux[df_aux['ANTIALERGICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIALERGICOS'] = 1
                    
                else:
                    df_window_p.at[0, 'ANTIALERGICOS'] = 0
                    
                if df_aux[df_aux['ANTIAMEBIANOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIAMEBIANOS'] = 1
                    
                else:
                    df_window_p.at[0, 'ANTIAMEBIANOS'] = 0
                    
                if df_aux[df_aux['ANTIANEMICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIANEMICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIANEMICOS'] = 0
                    
                if df_aux[df_aux['ANTIARTRITICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIARTRITICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIARTRITICOS'] = 0
                    
                if df_aux[df_aux['ANTIASMATICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIASMATICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIASMATICOS'] = 0
                    
                if df_aux[df_aux['ANTICOAGULANTES']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTICOAGULANTES'] = 1
                else:
                    df_window_p.at[0, 'ANTICOAGULANTES'] = 0
                    
                if df_aux[df_aux['ANTICOLINERGICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTICOLINERGICOS'] = 1                    
                else:
                    df_window_p.at[0, 'ANTICOLINERGICOS'] = 0
                    
                if df_aux[df_aux['ANTICONCEPTIVOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTICONCEPTIVOS'] = 1
                else:
                    df_window_p.at[0, 'ANTICONCEPTIVOS'] = 0
                    
                if df_aux[df_aux['ANTIDEPRESIVOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIDEPRESIVOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIDEPRESIVOS'] = 0
                    
                if df_aux[df_aux['ANTIDIABETICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIDIABETICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIDIABETICOS'] = 0
                    
                if df_aux[df_aux['ANTIDIARREICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIDIARREICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIDIARREICOS'] = 0
                    
                if df_aux[df_aux['ANTIDISFUNCION ERECTIL']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIDISFUNCION ERECTIL'] = 1
                else:
                    df_window_p.at[0, 'ANTIDISFUNCION ERECTIL'] = 0
                    
                if df_aux[df_aux['ANTIDOTOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIDOTOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIDOTOS'] = 0
                    
                if df_aux[df_aux['ANTIEMETICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIEMETICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIEMETICOS'] = 0
                    
                if df_aux[df_aux['ANTIENURESIS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIENURESIS'] = 1
                else:
                    df_window_p.at[0, 'ANTIENURESIS'] = 0
                    
                if df_aux[df_aux['ANTIEPILEPTICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIEPILEPTICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIEPILEPTICOS'] = 0
                    
                if df_aux[df_aux['ANTIESPASMODICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIESPASMODICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIESPASMODICOS'] = 0
                    
                if df_aux[df_aux['ANTIESPASMODICOS DE VIAS URINARIAS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIESPASMODICOS DE VIAS URINARIAS'] = 1
                else:
                    df_window_p.at[0, 'ANTIESPASMODICOS DE VIAS URINARIAS'] = 0
                    
                if df_aux[df_aux['ANTIESTROGENOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIESTROGENOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIESTROGENOS'] = 0
                    
                if df_aux[df_aux['ANTIFLATULENTOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIFLATULENTOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIFLATULENTOS'] = 0
                    
                if df_aux[df_aux['ANTIGOTOSOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIGOTOSOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIGOTOSOS'] = 0
                    
                if df_aux[df_aux['ANTIGRIPALES']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIGRIPALES'] = 1                    
                else:
                    df_window_p.at[0, 'ANTIGRIPALES'] = 0
                    
                if df_aux[df_aux['ANTIHELMINTICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIHELMINTICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIHELMINTICOS'] = 0
                    
                if df_aux[df_aux['ANTIHIPERPROLACTINEMICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIHIPERPROLACTINEMICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIHIPERPROLACTINEMICOS'] = 0
                    
                if df_aux[df_aux['ANTIHISTAMINICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIHISTAMINICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIHISTAMINICOS'] = 0
                    
                if df_aux[df_aux['ANTIINFLAMATORIOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIINFLAMATORIOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIINFLAMATORIOS'] = 0
                    
                if df_aux[df_aux['ANTILEPROSOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTILEPROSOS'] = 1
                else:
                    df_window_p.at[0, 'ANTILEPROSOS'] = 0
                    
                if df_aux[df_aux['ANTIMICOTICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIMICOTICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIMICOTICOS'] = 0
                    
                if df_aux[df_aux['ANTIMICROBIANOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIMICROBIANOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIMICROBIANOS'] = 0
                    
                if df_aux[df_aux['ANTIMICROBIANOS OTICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIMICROBIANOS OTICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIMICROBIANOS OTICOS'] = 0
                    
                if df_aux[df_aux['ANTIMIGRANOSOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIMIGRANOSOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIMIGRANOSOS'] = 0
                    
                if df_aux[df_aux['ANTINEOPLASICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTINEOPLASICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTINEOPLASICOS'] = 0
                    
                if df_aux[df_aux['ANTINICOTINICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTINICOTINICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTINICOTINICOS'] = 0
                    
                if df_aux[df_aux['ANTIOBESIDAD']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIOBESIDAD'] = 1
                else:
                    df_window_p.at[0, 'ANTIOBESIDAD'] = 0
                    
                if df_aux[df_aux['ANTIOSTEOPOROSICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIOSTEOPOROSICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIOSTEOPOROSICOS'] = 0
                    
                if df_aux[df_aux['ANTIPALUDICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIPALUDICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIPALUDICOS'] = 0
                    
                if df_aux[df_aux['ANTIPARASITARIOS VAGINALES']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIPARASITARIOS VAGINALES'] = 1
                else:
                    df_window_p.at[0, 'ANTIPARASITARIOS VAGINALES'] = 0
                    
                if df_aux[df_aux['ANTIPARKINSONIANOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIPARKINSONIANOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIPARKINSONIANOS'] = 0
                    
                if df_aux[df_aux['ANTIPROSTATICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIPROSTATICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIPROSTATICOS'] = 0
                    
                if df_aux[df_aux['ANTIPROTOZOARIOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIPROTOZOARIOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIPROTOZOARIOS'] = 0
                    
                if df_aux[df_aux['ANTIPSICOTICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIPSICOTICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIPSICOTICOS'] = 0
                    
                if df_aux[df_aux['ANTIRREUMATICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIRREUMATICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIRREUMATICOS'] = 0
                    
                if df_aux[df_aux['ANTISEPTICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTISEPTICOS'] = 1
                else:
                    df_window_p.at[0, 'ANTISEPTICOS'] = 0
                    
                if df_aux[df_aux['ANTISEPTICOS URINARIOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTISEPTICOS URINARIOS'] = 1
                else:
                    df_window_p.at[0, 'ANTISEPTICOS URINARIOS'] = 0
                    
                if df_aux[df_aux['ANTITABAQUISMO']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTITABAQUISMO'] = 1
                else:
                    df_window_p.at[0, 'ANTITABAQUISMO'] = 0
                    
                if df_aux[df_aux['ANTITIROIDEOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTITIROIDEOS'] = 1
                else:
                    df_window_p.at[0, 'ANTITIROIDEOS'] = 0
                    
                if df_aux[df_aux['ANTITUBERCULOSOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTITUBERCULOSOS'] = 1
                else:
                    df_window_p.at[0, 'ANTITUBERCULOSOS'] = 0
                    
                if df_aux[df_aux['ANTITUSIGENOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTITUSIGENOS'] = 1
                else:
                    df_window_p.at[0, 'ANTITUSIGENOS'] = 0
                    
                if df_aux[df_aux['ANTIULCEROSOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIULCEROSOS'] = 1
                else:
                    df_window_p.at[0, 'ANTIULCEROSOS'] = 0
                    
                if df_aux[df_aux['ANTIVIRALES']==1].count()[0] > 0:
                    df_window_p.at[0, 'ANTIVIRALES'] = 1
                else:
                    df_window_p.at[0, 'ANTIVIRALES'] = 0
                    
                if df_aux[df_aux['BRONCODILATADORES']==1].count()[0] > 0:
                    df_window_p.at[0, 'BRONCODILATADORES'] = 1
                else:
                    df_window_p.at[0, 'BRONCODILATADORES'] = 0
                    
                if df_aux[df_aux['COAGULANTES']==1].count()[0] > 0:
                    df_window_p.at[0, 'COAGULANTES'] = 1
                else:
                    df_window_p.at[0, 'COAGULANTES'] = 0
                    
                if df_aux[df_aux['COLINERGICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'COLINERGICOS'] = 1
                else:
                    df_window_p.at[0, 'COLINERGICOS'] = 0
                    
                if df_aux[df_aux['CORTICOSTEROIDES']==1].count()[0] > 0:
                    df_window_p.at[0, 'CORTICOSTEROIDES'] = 1
                else:
                    df_window_p.at[0, 'CORTICOSTEROIDES'] = 0
                    
                if df_aux[df_aux['DERMATOLOGICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'DERMATOLOGICOS'] = 1
                else:
                    df_window_p.at[0, 'DERMATOLOGICOS'] = 0
                    
                if df_aux[df_aux['DESINFECTANTES']==1].count()[0] > 0:
                    df_window_p.at[0, 'DESINFECTANTES'] = 1
                else:
                    df_window_p.at[0, 'DESINFECTANTES'] = 0
                    
                if df_aux[df_aux['DIURETICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'DIURETICOS'] = 1
                else:
                    df_window_p.at[0, 'DIURETICOS'] = 0
                    
                if df_aux[df_aux['DOPAMINERGICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'DOPAMINERGICOS'] = 1
                else:
                    df_window_p.at[0, 'DOPAMINERGICOS'] = 0
                    
                if df_aux[df_aux['ELECTROLITOS ORALES']==1].count()[0] > 0:
                    df_window_p.at[0, 'ELECTROLITOS ORALES'] = 1
                else:
                    df_window_p.at[0, 'ELECTROLITOS ORALES'] = 0
                    
                if df_aux[df_aux['ESTIMULANTES DE GRANULOCITOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'ESTIMULANTES DE GRANULOCITOS'] = 1
                    
                else:
                    df_window_p.at[0, 'ESTIMULANTES DE GRANULOCITOS'] = 0
                    
                if df_aux[df_aux['ESTIMULANTES DE LA CONTRACTILIDAD UTERINA']==1].count()[0] > 0:
                    df_window_p.at[0, 'ESTIMULANTES DE LA CONTRACTILIDAD UTERINA'] = 1
                else:
                    df_window_p.at[0, 'ESTIMULANTES DE LA CONTRACTILIDAD UTERINA'] = 0
                    
                if df_aux[df_aux['ESTIMULANTES DE LA MOTILIDAD UTERINA']==1].count()[0] > 0:
                    df_window_p.at[0, 'ESTIMULANTES DE LA MOTILIDAD UTERINA'] = 1
                else:
                    df_window_p.at[0, 'ESTIMULANTES DE LA MOTILIDAD UTERINA'] = 0
                    
                if df_aux[df_aux['EXPECTORANTES']==1].count()[0] > 0:
                    df_window_p.at[0, 'EXPECTORANTES'] = 1
                else:
                    df_window_p.at[0, 'EXPECTORANTES'] = 0
                    
                if df_aux[df_aux['GLUCOSIDOS CARDIACOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'GLUCOSIDOS CARDIACOS'] = 1
                else:
                    df_window_p.at[0, 'GLUCOSIDOS CARDIACOS'] = 0
                    
                if df_aux[df_aux['HEMATOPOYETICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'HEMATOPOYETICOS'] = 1
                else:
                    df_window_p.at[0, 'HEMATOPOYETICOS'] = 0
                    
                if df_aux[df_aux['HIPOCALCEMICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'HIPOCALCEMICOS'] = 1
                else:
                    df_window_p.at[0, 'HIPOCALCEMICOS'] = 0
                    
                if df_aux[df_aux['HIPOLIPEMIANTES']==1].count()[0] > 0:
                    df_window_p.at[0, 'HIPOLIPEMIANTES'] = 1
                else:
                    df_window_p.at[0, 'HIPOLIPEMIANTES'] = 0
                    
                if df_aux[df_aux['HORMONAS']==1].count()[0] > 0:
                    df_window_p.at[0, 'HORMONAS'] = 1
                else:
                    df_window_p.at[0, 'HORMONAS'] = 0
                    
                if df_aux[df_aux['INDUCTORES DE LA OVULACION']==1].count()[0] > 0:
                    df_window_p.at[0, 'INDUCTORES DE LA OVULACION'] = 1
                else:
                    df_window_p.at[0, 'INDUCTORES DE LA OVULACION'] = 0
                    
                if df_aux[df_aux['INMUNODEPRESORES']==1].count()[0] > 0:
                    df_window_p.at[0, 'INMUNODEPRESORES'] = 1
                else:
                    df_window_p.at[0, 'INMUNODEPRESORES'] = 0
                    
                if df_aux[df_aux['INMUNOGLOBULINAS']==1].count()[0] > 0:
                    df_window_p.at[0, 'INMUNOGLOBULINAS'] = 1
                else:
                    df_window_p.at[0, 'INMUNOGLOBULINAS'] = 0
                    
                if df_aux[df_aux['LAXANTES']==1].count()[0] > 0:
                    df_window_p.at[0, 'LAXANTES'] = 1
                else:
                    df_window_p.at[0, 'LAXANTES'] = 0
                    
                if df_aux[df_aux['LITOLITICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'LITOLITICOS'] = 1
                else:
                    df_window_p.at[0, 'LITOLITICOS'] = 0
                    
                if df_aux[df_aux['MINERALES']==1].count()[0] > 0:
                    df_window_p.at[0, 'MINERALES'] = 1
                else:
                    df_window_p.at[0, 'MINERALES'] = 0
                    
                if df_aux[df_aux['NEUROPROTECTORES']==1].count()[0] > 0:
                    df_window_p.at[0, 'NEUROPROTECTORES'] = 1
                else:
                    df_window_p.at[0, 'NEUROPROTECTORES'] = 0
                    
                if df_aux[df_aux['OFTALMICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'OFTALMICOS'] = 1
                else:
                    df_window_p.at[0, 'OFTALMICOS'] = 0
                    
                if df_aux[df_aux['OTROS INOTROPICOS POSITIVOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'OTROS INOTROPICOS POSITIVOS'] = 1
                else:
                    df_window_p.at[0, 'OTROS INOTROPICOS POSITIVOS'] = 0
                    
                if df_aux[df_aux['OXITOCICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'OXITOCICOS'] = 1
                else:
                    df_window_p.at[0, 'OXITOCICOS'] = 0
                    
                if df_aux[df_aux['PROCINETICOS GASTROINTESTINALES']==1].count()[0] > 0:
                    df_window_p.at[0, 'PROCINETICOS GASTROINTESTINALES'] = 1
                else:
                    df_window_p.at[0, 'PROCINETICOS GASTROINTESTINALES'] = 0
                    
                if df_aux[df_aux['RELAJANTES MUSCULARES']==1].count()[0] > 0:
                    df_window_p.at[0, 'RELAJANTES MUSCULARES'] = 1
                else:
                    df_window_p.at[0, 'RELAJANTES MUSCULARES'] = 0
                    
                if df_aux[df_aux['RELAJANTES VASCULARES']==1].count()[0] > 0:
                    df_window_p.at[0, 'RELAJANTES VASCULARES'] = 1
                else:
                    df_window_p.at[0, 'RELAJANTES VASCULARES'] = 0
                    
                if df_aux[df_aux['SEDANTES HIPNOTICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'SEDANTES HIPNOTICOS'] = 1
                else:
                    df_window_p.at[0, 'SEDANTES HIPNOTICOS'] = 0
                    
                if df_aux[df_aux['SOLUCIONES ELECTROLITICAS']==1].count()[0] > 0:
                    df_window_p.at[0, 'SOLUCIONES ELECTROLITICAS'] = 1
                else:
                    df_window_p.at[0, 'SOLUCIONES ELECTROLITICAS'] = 0
                    
                if df_aux[df_aux['SUEROS INMUNITARIOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'SUEROS INMUNITARIOS'] = 1
                else:
                    df_window_p.at[0, 'SUEROS INMUNITARIOS'] = 0
                    
                if df_aux[df_aux['TOXOIDES']==1].count()[0] > 0:
                    df_window_p.at[0, 'TOXOIDES'] = 1
                else:
                    df_window_p.at[0, 'TOXOIDES'] = 0
                    
                if df_aux[df_aux['TROMBOLITICOS']==1].count()[0] > 0:
                    df_window_p.at[0, 'TROMBOLITICOS'] = 1
                else:
                    df_window_p.at[0, 'TROMBOLITICOS'] = 0
                    
                if df_aux[df_aux['VACUNAS']==1].count()[0] > 0:
                    df_window_p.at[0, 'VACUNAS'] = 1
                else:
                    df_window_p.at[0, 'VACUNAS'] = 0
                    
                if df_aux[df_aux['VITAMINAS']==1].count()[0] > 0:
                    df_window_p.at[0, 'VITAMINAS'] = 1
                else:
                    df_window_p.at[0, 'VITAMINAS'] = 0

                if df_aux[df_aux['GAS MEDICINAL']==1].count()[0] > 0:
                    df_window_p.at[0, 'GAS MEDICINAL'] = 1
                else:
                    df_window_p.at[0, 'GAS MEDICINAL'] = 0

                if df_aux[df_aux['FORMULA POLIMERICA']==1].count()[0] > 0:
                    df_window_p.at[0, 'FORMULA POLIMERICA'] = 1
                else:
                    df_window_p.at[0, 'FORMULA POLIMERICA'] = 0

                f_aux = a_ini
                f_ini = a_ini
                j = j+1

                df_window_f = pd.concat([df_window_f, df_window_p]) 

    
        
    # Clean sexo
    df_window_f['sexo'] = df_window_f['sexo'].astype(str).str.replace(r'\[|\]|\'', '')
    df_window_f.loc[(df_window_f['sexo'] == 'M'), 'sexo'] = 1
    df_window_f.loc[(df_window_f['sexo'] == 'F'), 'sexo'] = 2
    df_window_f.reset_index(inplace=True)
    df_window_f.drop('index', inplace=True, axis=1)
    df_window_f.drop(['fecha_ini', 'fecha_fin'], inplace=True, axis=1)
                
    return df_window_f

def change_datatype(df_1):
    """
    """   
    c = list(df_1.columns)
    
    for var in c:
        #print(var)
        df_1[var] = pd.to_numeric(df_1[var])
        
    return df_1
        

def imputation(df_1):
    """
    """   
    # Imputaciones
    col = list(df_1.columns)
    col    
    my_imputer = SimpleImputer()
    d_inp = pd.DataFrame(my_imputer.fit_transform(df_1))
    d_inp.columns = col
    
    return d_inp  
   

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
    
    # Label
    df['target_hta'] = df['hta_nvo_ce']
    
    # Creación de ventanas
    # 1 año
    #df_f = create_window(df, 2)
    # 3 meses
    df_f = create_window(df, 3)
    
    # Eliminando filas que no aportan información
    df_f = df_f[df_f['sum_num_consultas']>0]
    df_f = df_f.reset_index()
    df_f = df_f.drop(columns=['index'])
    
    # Eliminando columnas que no aportan información
    subset_df = df_f.loc[:, df_f.isnull().all()]
    col_null = list(subset_df.columns)
    df_f.drop(col_null, axis=1, inplace=True)
    
    # Cambiando tipo de dato
    df_1 = df_f.loc[:, df_f.columns != 'cx_curp']
    df_1 = change_datatype(df_1)
    
    # Imputaciones
    df_i = imputation(df_1)
    
    result = pd.concat([df_f[['cx_curp']], df_i], axis=1)
        
    # Se guarda pkl
    utils.save_df(result, path_save)
    print("Finalizó proceso: Feature_engineering")
    
    return result
