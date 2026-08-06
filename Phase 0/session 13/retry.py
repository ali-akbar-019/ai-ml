def retry(max_attempts=3):
    def decorator(func):
        def wrapper():
            for attempt in range(max_attempts):
                try:
                    return func()
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt == max_attempts - 1:
                        raise
            return None
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable_connection():
    import random
    if random.random() < 0.7:
        raise Exception("Connection failed!")
    return "Connected!"

# Try running it
print(unstable_connection())