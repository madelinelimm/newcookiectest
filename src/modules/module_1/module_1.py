from logs import logDecorator as lD 
import jsonref, pprint
import pandas as pd

config = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.modules.module_1.module_1'


@lD.log(logBase + '.doRemoveNA')
def doRemoveNA(logger, data):
    '''print a line
    
    This function simply removes missing values in the data
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    data : {DataFrame}
        DataFrame consisting dataset to be trained and tested
    '''
    curdata = data.loc[~data['bmi'].isna()]
    curdata1 = curdata.loc[:,list(data.columns)[1:]]

    return curdata1

@lD.log(logBase + '.doFactorise')
def doFactorise(logger, data):
    '''print a line
    
    This function factorises categorical information in the data
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    data : {DataFrame}
        DataFrame consisting dataset to be trained and tested
    '''
    cols = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']

    curdata = data.loc[:,list(data.columns)]
    for col in cols:
        curdata.loc[:,col] = pd.factorize(data.loc[:,col])[0]

    return curdata

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
        A dictionary containing information about the 
        command line arguments. These can be used for
        overwriting command line arguments as needed.
    '''

    print('='*30)
    print('Main function of module_1')
    print('='*30)

    database = pd.read_csv('../data/raw_data/healthcare-dataset-stroke-data.csv')
    cur = doRemoveNA(database)
    result = doFactorise(cur)
    result.to_csv('../data/intermediate/cleaned-dataset.csv', index = False)

    print('Cleaned data has been generated')
    print(' ')

    return 

