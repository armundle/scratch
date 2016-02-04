def entryExit(f):

    print "entryExit decorator"
    f(2)

    return

@entryExit
def func1(val):

    print "Inside func1"
    print val

    return None

if __name__ == "__main__":
    func1
