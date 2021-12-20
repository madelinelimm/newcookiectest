from logs import logDecorator as lD 
import jsonref, pprint
import pandas as pd
import xgboost as xgb
from sklearn.metrics import confusion_matrix, roc_auc_score

config = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.modules.module_3.module_3'


@lD.log(logBase + '.doXGBoostFit')
def doXGBoostFit(logger, train_data, test_data):
    '''print a line
    
    This function simply prints a single line
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    train_data : {DataFrame}
        DataFrame consisting dataset to be trained and predicted
    test_data : {DataFrame}
        DataFrame consisting dataset to be predicted
    '''
    train_X = train_data.drop(columns = ['stroke'])
    train_Y = train_data.loc[:, 'stroke']

    test_X = test_data.drop(columns = ['stroke'])
    test_Y = test_data.loc[:, 'stroke']

    xgb_model = xgb.XGBClassifier(random_state = 90,
                             objective='binary:logistic',
                             learning_rate = 0.005,
                             gamma = 0.1,
                             max_depth = 3,
                             min_child_weight = 10,
                             scale_pos_weight = 0.9,
                             use_label_encoder = False,
                             eval_metric = 'logloss')   

    xgb_model.fit(train_X, train_Y)

    train_pred = xgb_model.predict(train_X)
    test_pred = xgb_model.predict(test_X)

    return train_pred, test_pred

@lD.log(logBase + '.doConfusionMatrix')
def doConfusionMatrx(logger, pred_data, true_data):
    '''print a line
    
    This function computes the confusion matrix of predicted and actual response
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    pred_data : {list}
        DataFrame consisting predicted response
    true_data : {list}
        DataFrame consisting actual response
    '''
    XGBcm = pd.DataFrame(confusion_matrix(pred_data, true_data))
    XGBcm.columns = ['True Y=0','True Y=1']
    XGBcm.index = ['Predicted Y=0','Predicted Y=1']

    return XGBcm

@lD.log(logBase + '.main')
def main(logger, resultsDict):
    '''main function for module1
    
    This function finishes all the tasks for the
    main function. This is a way in which a 
    particular module is going to be executed. 
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    resultsDict: {dict}
        A dintionary containing information about the 
        command line arguments. These can be used for
        overwriting command line arguments as needed.
    '''

    print('='*30)
    print('Main function of module_3')
    print('='*30)

    train = pd.read_csv('../data/final/train.csv')
    test = pd.read_csv('../data/final/test.csv')
    train_Y = train.loc[:, 'stroke']
    test_Y = test.loc[:, 'stroke']
    train_pred, test_pred = doXGBoostFit(train_data = train, test_data = test)
    print('Done fitting and predicting with XGBoost')
    print(' ')


    print('-'*40)
    print('Confusion Matrix for Train Predictions')
    print('-'*40)
    XGBcm1 = doConfusionMatrx(train_pred, train_Y)
    print(XGBcm1)
    print(' ')

    print('-'*40)
    print('Confusion Matrix for Test Predictions')
    print('-'*40)
    XGBcm2 = doConfusionMatrx(test_pred, test_Y)
    print(XGBcm2)
    print(' ')

    print('Training AUC:',roc_auc_score(train_Y, train_pred))
    print('Test AUC:',roc_auc_score(test_Y, test_pred))

    return

