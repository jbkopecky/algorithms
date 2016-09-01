import time

def timeit(f):
    def timed(*args, **kwargs):
        ts = time.time()
        result = f(*args, **kwargs)
        te = time.time()
        print('%r (%r, %r) %2.4f sec' % (f.__name__, args, kwargs, te-ts))
        return result
    return timed
