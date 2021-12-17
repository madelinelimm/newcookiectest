from logs import logDecorator as lD 
import jsonref, pprint

config = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.modules.module2.module2'

@lD.log(logBase + '.doFirstthing')
def doFirstthing(logger):
    """[summary]
    This function simply prints a single line
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information

    """
    print('Are we in module 2 ?')

    return


@lD.log(logBase + '.doSomething')
def doSomething(logger):
    '''print a line
    
    This function simply prints a single line
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    '''


    print('We are in module 2')
    print('#'*100)
    configModule2 = jsonref.load(open('../config/modules2.json'))
    print(configModule2)
    value1 = configModule2['value1']
    value2 = configModule2['value2']
    print(value1)
    print(value2)


    print('#'*100)
    return


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
    print('Main function of module 2')
    print('='*30)
    print('We get a copy of the result dictionary over here ...')
    pprint.pprint(resultsDict)

    doFirstthing()
    doSomething()

    print('Getting out of Module 2')
    print('-'*30)

    return

