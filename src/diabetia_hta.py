import sys
import os
from os.path import dirname
import warnings
warnings.filterwarnings('ignore')
sys.path.append(dirname('../src'))
from pipeline import ingestion, transformation, feature_engineering, modeling

# RUN
# python diabetia_hta.py 1 "aide.csv"
# python diabetia_hta.py 2 "aide.csv"

# Argumentos
# 1 entrenamiento o predicción 
# archivo de datos
# ventana

ent_pred = sys.argv[1]
file_data = sys.argv[2]


def main ():
    #print("ent_pred: ",type(ent_pred))
    #print("file_data :", file_data)
    # Entrenamiento
    if (ent_pred == "1"):
        print("Iniciando entrenamiento--------------------------------------------------------------")
        #df = ingestion.ingesta_data(file_data, "../Data/data.pkl")
        #df = transformation.transform(df, "../Data/transformation.pkl")
        #df = feature_engineering.feature_engineering(df, "../Data/feature_eng.pkl")
        #df_m = df.loc[:, df.columns != 'cx_curp']
        #df_curp = df[["cx_curp"]]
        #model_and_features, X_test, y_test = modeling.training(df_m)
        #model = modeling.best_model(model_and_features, X_test, y_test, "../Data/best_model.pkl")
        print("Finaliza entrenamiento ---------------------------------------------------------------")
        
    # Predicción
    elif (ent_pred == "2"):
        print("Comenzando predicción ----------------------------------------------------------------")
        #df = ingestion.ingesta_data(file_data, "../Data/data_new.pkl")
        #df = transformation.transform(df, "../Data/transformation_new.pkl")
        ## dejar en ventanas
        #df = feature_engineering.feature_engineering(df, "../Data/feature_eng_new.pkl")
        #df_m = df.loc[:, df.columns != 'cx_curp']
        #df_curp = df[["cx_curp"]]
        #modeling.predict()
        
    else:
        print("Argumentos incorrectos")
        
    print("FIN")
    
    pass


if __name__ == '__main__':
    main()