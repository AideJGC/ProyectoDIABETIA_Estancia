import sys
import os
import time
from os.path import dirname
import warnings
warnings.filterwarnings('ignore')
sys.path.append(dirname('../src'))
from diabetia_hta.pipeline import ingestion, transformation, feature_engineering, modeling

# RUN
# python diabetia_hta.py 1 "aide.csv"
# python diabetia_hta.py 2 "aide.csv"

# Argumentos
# 1 entrenamiento o predicci�n 
# archivo de datos
# ventana

ent_pred = sys.argv[1]
file_data = sys.argv[2]


def main():
    # Entrenamiento
    if (ent_pred == "1"):
        print("Iniciando entrenamiento---------------------------------------------------------------")
        start_time = time.time()
        df = ingestion.ingesta_data(file_data, "../data/data.pkl")
        df = transformation.transform(df, "../data/transformation.pkl")
        df = feature_engineering.feature_engineering(df, "../data/feature_eng.pkl")
        df_m = df.loc[:, df.columns != 'cx_curp']
        #df_curp = df[["cx_curp"]]
        model_and_features, X_test, y_test = modeling.training(df_m)
        model = modeling.best_model(model_and_features, X_test, y_test, "../data/best_model.pkl")
        print("Finaliza entrenamiento en ", time.time() - start_time, " segundos")
        print("--------------------------------------------------------------------------------------")
        
    # Predicci�n
    elif (ent_pred == "2"):
        print("Comenzando predicci�n ----------------------------------------------------------------")
        start_time = time.time()
        df = ingestion.ingesta_data(file_data, "../data/new_data.pkl")
        df['hba1c'] = df['hba1c'].astype(str)
        df = transformation.transform(df, "../data/new_transformation.pkl")
        df = feature_engineering.feature_engineering(df, "../data/new_data_fe.pkl")
        df = modeling.predict(df, "../data/best_model.pkl", "../data/save_new_predict.pkl")
        print("Fin predicci�n en ", time.time() - start_time, " segundos")
        print("--------------------------------------------------------------------------------------")
    else:
        print("Argumentos incorrectos")
    pass


if __name__ == '__main__':
    main()
