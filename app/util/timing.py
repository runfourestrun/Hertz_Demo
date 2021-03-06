from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print ('func:%r args:[ %r] took: %2.4f sec' % \
          (f.__name__, kw, te-ts))
        return result
    return wrap