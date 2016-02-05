def decoratorFunction(f):

    def newFunc():
        print "inside decorator function"
        print "entering", f.__name__
        f()
        print "exited", f.__name__

    return newFunc

class decoratorWithoutArguments(object):

    '''
    If there are no decorator arguments, the function to be decorated is passed
    to the constructor.
    '''
    def __init__(self, f):
        self.f = f
        print "decoratorWithoutArguments.__init__"

    '''
    Note:
    1. The major constraint on the result of a decorator is that it be callable.
    The __call__ method here achieves that.
    2. __call__ is called every time the decorated function is called;
    __init__is called only once during the 'construction' of the decorated
    function.

    '''
    '''
    The __call__ method is not called until the decorated function is called.
    '''
    def __call__(self, *args):
        print "decoratorWithoutArguments.__call__"
        print "entering", self.f.__name__
        self.f(*args)
        print "exited", self.f.__name__

@decoratorWithoutArguments
def func1(a1, a2, a3):
    print "inside function 1"
    print "spell args: ", a1, a2, a3

@decoratorWithoutArguments
def func2():
    print "inside function 2"
    print "no args"

@decoratorFunction
def func3():
    print "inside function 3"


if __name__ == "__main__":

    func1("test", "multiple", "args")
    print '\n'
    func1("another", "round", "of args")
    print '\n'
    func2()
    print '\n'
    func3()

    print '\n'
    print "end of example"
