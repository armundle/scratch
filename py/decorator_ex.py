'''
def decoratorFunc(f):

    print "inside decorator function"
    f(42)

    return

@decoratorFunc
def func1(val):

    print "inside function 1"

    return
'''

class entryExit(object):

    def __init__(self, f):
        self.f = f

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


if __name__ == "__main__":

    pass
    func1()
    func2()
