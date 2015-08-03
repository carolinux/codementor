
def dec(func): 
    """ Only used for debugging"""

    def bla():
         print "im in the wrapped function"

    def wrapped(*args, **kwargs):

        wrapped.foo = bla
        wrapped.f = "aaa"
        func.wontwork ="bbb" # this doesnt work
        return func(*args, **kwargs)

    return wrapped
    
    
def dec2(func): 
  
    def wrapped(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapped


@dec
@dec2
def bar():
    this = bar
    this.a = "a"
    print dir(bar)
    print this.f
    bar.foo()




