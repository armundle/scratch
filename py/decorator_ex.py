def entryExitFunc(f):

    def newFunc():
        print "inside decorator function"
        print "entering", f.__name__
        f()
        print "exited", f.__name__

    return newFunc

class entryExit(object):

    def __init__(self, f):
        self.f = f

    '''
    The major constraint on the result of a decorator is that it be callable.
    The __call__ method here achieves that.
    '''
    def __call__(self):
        print "entering", self.f.__name__
        self.f()
        print "exited", self.f.__name__

@entryExit
def func1():
    print "inside function 1"

@entryExit
def func2():
    print "inside function 2"

@entryExitFunc
def func3():
    print "inside function 3"


if __name__ == "__main__":

    func1()
    print '\n'
    func2()
    print '\n'
    func3()
