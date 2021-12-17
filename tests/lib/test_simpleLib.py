from lib.testLib import simpleLib as sL
import jsonref, logging, pytest
config = jsonref.load(open('../config/config.json'))

def test_simpleTest():
    logging.getLogger(config['logging']['logBase'])
    assert sL.simpleTestFunction(1, 2) == 3
    assert sL.simpleTestFunction('1', '2') == '12'
    return

def test_simpleTest_fail1():
    logging.getLogger(config['logging']['logBase'])
    with pytest.raises(Exception) as e:
        sL.simpleTestFunction(1, '2')
    assert 'TypeError' in str(e)


def test_simpleTest1():
    logging.getLogger(config['logging']['logBase'])
    assert sL.simpleTestFunction1('lame', 2) == 'm'
    assert sL.simpleTestFunction1('lame', -1) == 'e'
    return


def test_simpleTest1_fail1():
    logging.getLogger(config['logging']['logBase'])
    with pytest.raises(Exception) as e:
        sL.simpleTestFunction1('mad', 6)
    assert 'IndexError' in str(e)
    