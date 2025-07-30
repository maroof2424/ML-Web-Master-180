import time
def main():
    #Task1 
    def log_function_call(func):
        def wrapper(*args, **kwargs):
            print(f"Calling: {func.__name__}")
            return func(*args,**kwargs)
        return wrapper
    
    @log_function_call
    def greet(name):
        print(f"Hello {name}")

    greet("Maroof")
    # Task 2
    def timer(func):
        def wrapper(*args,**kwargs):
            start = time.time()
            result = func(*args,**kwargs)
            end = time.time()
            print(f"{func.__name__} took {end - start} seconds")
            return result
        return wrapper
    @log_function_call
    def add(x,y):
        return x+y
    print(5+7)
    
    # Task 3
    def number_generator(limit):
        for number in range(limit+1):
            yield number
    for n in number_generator(50):
        print(n)
    #Task 4
    def fibonacci_generator(limit):
        a,b = 0,1
        while a <= limit:
            yield a
            a,b = b,a+b
    
    for fib in fibonacci_generator(21):
        print(fib, end=" ")
if __name__ == "__main__":
    main()