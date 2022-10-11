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
from sklearn.model_selection import train_test_split, TimeSeriesSplit, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

def train_test(df): 
    """
    Recibe el data frame del cual se elegiran muestran de test y train
    """
    print('Se inicia el proceso de muestreo:train/test')   
    X = df.loc[:, df.columns != 'label']
    Y = df[["label"]]
    
    np.random.seed(2021)
    X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.3,random_state=4)
    print('Muestreo estratificado train/test completado satisfactoriamente')   
    return (X_train_id, X_test_id, y_train, y_test)

    
def auto_selection_variables (X_train_id, y_train):
    
    # Parámetros para la mejor selección de variables
    grid_param = {
        'n_estimators': [100, 150],
        'min_samples_split': [2, 5, 7, 10,15]
    }

    #classifier = RandomForestClassifier()
    classifier = RandomForestClassifier(oob_score=True, random_state=1234)

    #Prepareción del GridSearch
    gd_sr = GridSearchCV(estimator=classifier,
                         param_grid=grid_param,
                         scoring='precision',
                         cv=2)
    
    gd_sr.fit(X_train, y_train)
    best_e = gs.best_estimator_
    cols= X_train.columns

    feature_importance = pd.DataFrame({'importance': best_e.feature_importances_,
                                       'feature': list(cols)}).sort_values(by="importance", ascending=False)

    auto_selection_variables = feature_importance[feature_importance.importance > 0]['feature'].unique()
    
    return (auto_selection_variables)


def magic_loop(algorithms, features, labels, scoring_met):
    best_estimators = []
    for algorithm in algorithms:
        estimator = estimators_dict[algorithm]
        grid_search_to_look = algorithms_dict[algorithm]
        grid_params = grid_search_dict[grid_search_to_look]
        #tscv = TimeSeriesSplit(n_splits=5)
        
        #gs = GridSearchCV(estimator, grid_params, scoring='precision', cv=5, n_jobs=-1)
        gs = GridSearchCV(estimator, grid_params, scoring = scoring_met, cv=5, n_jobs=-1)
        
        #train
        gs.fit(features, labels)
        best_estimators.append(gs)        
        
    return best_estimators
    
    
def train_models(X_train_id, y_train, auto_variables):

    X_train = X_train_id[auto_variables]

    algorithms_dict = {'tree': 'tree_grid_search',
                       'random_forest': 'rf_grid_search',
                       'logistic': 'logistic_grid_search',
                       'xgboost': 'xgboost_grid_search'}

    grid_search_dict = {
                            'tree_grid_search': {
                                'max_depth': [5, 10, 15],
                                'min_samples_leaf': [3, 5, 7]
                            },
                            'rf_grid_search': {
                                'n_estimators': [30, 50, 100],
                                'max_depth': [5, 10, 15],
                                'min_samples_leaf': [3, 5, 10]
                            },
                            'logistic_grid_search':{
                                'C':np.logspace(-3,3,7),
                                'penalty':['l2']
                            },
                            'xgboost_grid_search':{
                                'max_depth': range (2, 10, 1),
                                'n_estimators': range(60, 220, 40),
                                'learning_rate': [0.1, 0.01, 0.05]
                            }
                        }

    estimators_dict = {'tree': DecisionTreeClassifier(random_state=1111),
                       'random_forest': RandomForestClassifier(oob_score=True, random_state=2222),
                       'logistic': LogisticRegression(random_state=3333),
                       'xgboost': XGBClassifier(objective= 'binary:logistic',nthread=4,seed=42)
                      } 
    
    scoring_met = 'roc_auc' #'recall'
    algorithms = ['tree', 'random_forest','logistic','xgboost']
    models = []
    start_time = time.time()
    models_list = []
   
    models = magic_loop(algorithms, X_train, y_train)
    return (models)


def training(df_fe):
    
    print("Inicia proceso de entrenamiento de modelos")
    start_time = time.time()
    
    X_train_id, X_test_id, y_train, y_test = train_test(df_fe)
    auto_variables = auto_selection_variables(X_train_id, y_train)
    models = train_models(X_train_id, y_train, auto_variables)
    print("Se concluye proceso de entrenamiento con datos completos en  ", time.time() - start_time, ' segundos')
    model_and_features = {'models': models, 'features': auto_variables}        
    return model_and_features


def get_best_model()



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
    df_f = create_window(df, 3)
        
    # Se guarda pkl
    utils.save_df(df_f, path_save)
    print("Finalizó proceso: Feature_engineering")
    
    return df_f