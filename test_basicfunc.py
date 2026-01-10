from basicfunc import add, subtract


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10
    function.y = 2


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x
    del function.y


### Run to see failed test
#def test_basicfunc_add():
#    assert add(test_basicfunc_add.x + test_basicfunc_subtract.y) == 11

def test_basicfunc_subtract():
    assert subtract(function.x,function.y) == 8
