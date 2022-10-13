import pandas as pd
import numpy as np
import sys
import os
import time
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
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.metrics import accuracy_score, precision_recall_curve, precision_score, recall_score
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
import matplotlib.pyplot as plt

def train_test(df): 
    """
    Recibe el data frame del cual se elegiran muestran de test y train
    """
    print('Se inicia el proceso de muestreo:train/test')   
    X = df.loc[:, df.columns != 'label']
    Y = df[["label"]]
    
    np.random.seed(2021)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3,random_state=4)
    print('Muestreo estratificado train/test completado satisfactoriamente')   
    return (X_train, X_test, y_train, y_test)

    
def auto_selection_variables (X_train, y_train):
    
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
    best_e = gd_sr.best_estimator_
    cols= X_train.columns

    feature_importance = pd.DataFrame({'importance': best_e.feature_importances_,
                                       'feature': list(cols)}).sort_values(by="importance", ascending=False)

    auto_selection_variables = feature_importance[feature_importance.importance > 0]['feature'].unique()
    
    return (auto_selection_variables)


def magic_loop(estimators_dict, algorithms_dict, grid_search_dict, algorithms, features, labels, scoring_met):
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
   
    models = magic_loop(estimators_dict, algorithms_dict, grid_search_dict, algorithms, X_train, y_train, scoring_met)
    return (models)


def training(df_fe):
    
    print("Inicia proceso de entrenamiento de modelos")
    start_time = time.time()
    
    X_train, X_test, y_train, y_test = train_test(df_fe)
    auto_variables = auto_selection_variables(X_train, y_train)
    models = train_models(X_train, y_train, auto_variables)
    print("Se concluye proceso de entrenamiento con datos completos en  ", time.time() - start_time, ' segundos')
    model_and_features = {'models': models, 'features': auto_variables}  
    
    return model_and_features, X_test, y_test


def param_graf(y_true, y_scores):
    k_values = np.linspace(0, 0.99, 100)
    lista = []

    for k in k_values:
        p_k = precision_at_k(y_true, pd.DataFrame(y_scores)[1], k)
        r_k = recall_at_k(y_true, pd.DataFrame(y_scores)[1], k)
        lista = lista + [[p_k, r_k, k]]

    p_r_g = pd.DataFrame(lista, columns=["p_k", "r_k", "k"])

    return p_r_g

def precision_at_k(y_true, y_scores, k):
    threshold = np.sort(y_scores)[::-1][int(k * len(y_scores))]
    y_pred = np.asarray([1 if i >= threshold else 0 for i in y_scores])

    return precision_score(y_true, y_pred)

def recall_at_k(y_true, y_scores, k):
    threshold = np.sort(y_scores)[::-1][int(k * len(y_scores))]
    y_pred = np.asarray([1 if i >= threshold else 0 for i in y_scores])

    return recall_score(y_true, y_pred)


def print_results_model(X_test, y_test, model):
    """
    """
    predicted_labels = model.predict(X_test)
    predicted_scores = model.predict_proba(X_test)
    
    ### Curva ROC
    plt.figure()
    fpr, tpr, thresholds = roc_curve(y_test, predicted_scores[:, 1], pos_label=1)
    plt.clf()
    plt.plot([0, 1], [0, 1], 'k--', c="red")
    plt.plot(fpr, tpr)
    plt.title("ROC best RF, AUC: {}".format(roc_auc_score(y_test, predicted_labels)))
    plt.xlabel("fpr")
    plt.ylabel("tpr")
    plt.savefig('../output/ROC_curve.png', bbox_inches='tight')
    #plt.show()
    cm = plot_confusion_matrix(model, X_test, y_test, cmap=plt.cm.Blues)  
    cm.figure_.savefig('../output/confusion_matrix.png',dpi=300)
    
    # Precision and recall at k%
    data_junta = pd.concat([X_test, y_test], axis=1)
    data_filtrada = data_junta
    datos_finales_X = pd.DataFrame(data_filtrada.drop(['label'], axis=1))
    y_true = data_filtrada.label
    y_scores = model1.predict_proba(datos_finales_X)
    
    p_r_g = param_graf(y_true, y_scores)

    plt.figure()
    plt.plot(p_r_g["k"], p_r_g["p_k"], label="P")
    plt.plot(p_r_g["k"], p_r_g["r_k"], label="R")
    plt.title("Precision and recall at k%: PA")
    plt.axvline(x=0.037, c='red', linestyle='--')
    plt.ylabel("Mejor valor")
    plt.legend(['Precision', 'Recall'])
    plt.xlabel("%k")
    plt.savefig('../output/recall_precision_k.png', bbox_inches='tight')
    #plt.show()


def best_model(models, X_test, y_test, path_save): 
    
    scores = []
    best_estimator = []
    
    print(len(models['models']))
    
    for i in range(len(models['models'])):
            scores.append(models['models'][i].best_score_) 
            best_estimator.append(models['models'][i].best_estimator_) 

    max_score = max(scores)  
    max_score_index = scores.index(max_score)
    best_model = {
        'best_model': best_estimator[max_score_index],
        'features': models['features']
    }    
    
    # Print results best model
    print_results_model(X_test, y_test, best_model['best_model'])
    
    # Se guarda pkl
    utils.save_df(best_model, path_save)
    
    print(best_model)

    return best_model


def predict(df_fe, model):
    """
    Recibe el data frame a predecir, regresa los labesl y scores predichos
    """    
    auto_variables = model["features"]
    best_model = model["best_model"]

    X_train_id, X_test_id, y_train,y_test = train_test(df_fe)
    predicted_labels = best_model.predict(X_test_id[auto_variables])
    predicted_scores = best_model.predict_proba(X_test_id[auto_variables])
    
    # Punto de corte con recall
    fpr, tpr, thresholds_roc = roc_curve(y_test, predicted_scores[:,1], pos_label=1)
    s1=pd.Series(thresholds_roc,name='threshold')
    s2=pd.Series(fpr,name='false_pr')
    s3=pd.Series(tpr ,name='true_pr')
    df_threshold_roc = pd.concat([s1,s2,s3], axis=1)
    recall = 0.8
    threshold_recall = round(df_threshold_roc[df_threshold_roc.false_pr == df_threshold_roc[df_threshold_roc.true_pr >= recall ].false_pr.min()].threshold, 2).max()
    
    # Resultados 
    predict_proba = pd.DataFrame(predicted_scores[:,1])
    terminos_threshold = predict_proba > threshold_recall

    score = terminos_threshold[0]
    score = score.replace(True,1).replace(False,0)
    score = score.to_numpy()

    results = pd.DataFrame(y_test)
    results['score'] = score 
    results['pred_score'] = predict_proba.values
    
    results_confusion_matrix =  pd.DataFrame(results[['label', 'score']].value_counts()).sort_values('label')
    results_confusion_matrix
    
    # Regresando a una sola columna el one hot encoding de la variable tipo de inspección
    X_test_id['type_inspection_limpia'] = X_test_id[['type_canvass','type_license','type_licuor','type_complaint',
                                          'type_reinsp','type_illegal','type_not_ready','type_out_of_buss',
                                          'type_prelicense','type_others']].idxmax(axis=1) 
                                    
    results_conjunto = pd.concat([results,X_test_id], axis=1)
    
    #Leyendo variables de inicio
    if inicial:
         file_name = 'processed-data/clean-historic-inspections-{}.pkl'.format(date_input.strftime('%Y-%m-%d'))
    else:
         file_name = 'processed-data/clean-consecutive-inspections-{}.pkl'.format(date_input.strftime('%Y-%m-%d'))

    
    s3 = get_s3_client(cte.CREDENTIALS)
    s3_object = s3.get_object(Bucket = cte.BUCKET, Key = file_name)
    body = s3_object['Body']
    my_pickle = pickle.loads(body.read())

    df_clean = pd.DataFrame(my_pickle)
    

    df_clean_results = df_clean[['inspection_id', 'dba_name', 'facility_type', 'inspection_type']]
    results_conjunto_original = results_conjunto.merge(df_clean_results, on='inspection_id', how='left')
    
    return results_conjunto_original
