from logs import logDecorator as lD 
import jsonref, pprint
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline

config = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.modules.module_2.module_2'


@lD.log(logBase + '.doTrainTestSplit')
def doTrainTestSplit(logger, data):
    '''print a line
    
    This function splits data into train and test sets
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    data : {DataFrame}
        DataFrame consisting dataset to be trained and tested
    '''
    train_X, test_X, train_Y, test_Y = train_test_split(data.drop(columns = ['stroke']), data['stroke'], test_size = 0.2, random_state = 1)

    print("Train dataset has {} patients.".format(len(train_X)))
    print("Test dataset has {} patients.".format(len(test_X)))

    train_dataset = train_X.join(train_Y)
    test_dataset = test_X.join(test_Y)

    return train_dataset, test_dataset

@lD.log(logBase + '.doSMOTE')
def doSMOTE(logger, data):
    '''print a line
    
    This function will use SMOTE to oversample the train dataset to prevent skewed dataset with majority class = 0
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    data : {DataFrame}
        DataFrame consisting dataset to be oversampled
    '''
    train_X = data.drop(columns = ['stroke'])
    train_Y = data.loc[:, 'stroke']

    over = SMOTE(sampling_strategy=0.9)

    steps = [('o', over)]
    pipeline = Pipeline(steps=steps)

    train_Xres, train_Yres = pipeline.fit_resample(train_X, train_Y)

    training_dataset = train_Xres.join(train_Yres)

    return training_dataset

    
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
    print('Main function of module_2')
    print('='*30)

    database = pd.read_csv('../data/intermediate/cleaned-dataset.csv')
    train_cur, test_cur = doTrainTestSplit(database)
    train_result = doSMOTE(train_cur)

    train_result.to_csv('../data/final/train.csv', index = False)
    test_cur.to_csv('../data/final/test.csv', index = False)
    
    print('Train and Test data has been generated')
    print(' ')

    return

