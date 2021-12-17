    
import jsonref, argparse

from importlib      import util
from logs           import logDecorator  as lD
from lib.testLib    import simpleLib     as sL
from lib.argParsers import addAllParsers as aP

config   = jsonref.load(open('../config/config.json'))
logBase  = config['logging']['logBase']
logLevel = config['logging']['level']
logSpecs = config['logging']['specs']

# Let us add an argument parser here
parser = argparse.ArgumentParser(description='newcookiectest command line arguments')

modules = jsonref.load(open('../config/modules.json'))
modules = [m['moduleName'] for m in modules]
print(modules)

if True:
    parser.add_argument('-m', '--module', action='append',
        type = str,
        choices = modules,
        help = '''Add modules to run over here. Multiple modules can be run
        simply by adding multiple strings over here. Make sure that the 
        available choices are reflected in the choices section''')

    parser = aP.parsersAdd(parser)
    results = parser.parse_args()
    resultsDict = aP.decodeParsers(results)

    print(results.module)

    # if results.module is not None:
    #     resultsDict['modules'] = results.module
    # else:
    #     resultsDict['modules'] = None
        

    # # ---------------------------------------------------
    # # We need to explicitely define the logging here
    # # rather than as a decorator, bacause we have
    # # fundamentally changed the way in which logging 
    # # is done here
    # # ---------------------------------------------------
    # logSpecs = aP.updateArgs(logSpecs, resultsDict['config']['logging']['specs'])
    # try:
    #     logLevel = resultsDict['config']['logging']['level']
    # except Exception as e:
    #     print('Logging level taking from the config file: {}'.format(logLevel))

    # logInit  = lD.logInit(logBase, logLevel, logSpecs)
    # main     = logInit(main)

    # main(resultsDict)