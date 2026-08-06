import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} tool {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function(*args, **kwargs):
    time.sleep(2)
    return "Done"

slow_function()