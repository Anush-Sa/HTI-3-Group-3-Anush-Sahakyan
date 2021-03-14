from time import time, sleep

def warn_slaw(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        dur = end - start

        if dur > 2:
            print(f"Execution of {func.__name__} with {', '.join(map(str, args))} arguments took more than 2 seconds ({dur} seconds)")
            return f"Result = {res}"
        else:
            print(f"Execution of {func.__name__} with {', '.join(map(str, args))} arguments took {dur} seconds")
            return f"Result = {res}"
    return wrapper

@warn_slaw
def fast_sum(x, y):
    return x + y


@warn_slaw
def slow_sum(x, y):
    sleep(3)
    return x + y

print(fast_sum(1234, 12345))
print(slow_sum(1234, 12345))
