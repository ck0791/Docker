from basicfunc import add, subtract


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x


### Run to see failed test
#def test_basicfunc_add():
#    assert add(test_basicfunc_add.x) == 12

def test_basicfunc_subtract():
    assert subtract(test_basicfunc_subtract.x) == 9
