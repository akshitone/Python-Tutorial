import functools


def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Do something before function')
        result = func(*args, **kwargs)
        print('Do something after function')
        return result
    return wrapper


@start_end_decorator
def add5(x):
    return x+5

# @start_end_decorator
# def print_name():
#     print("Akshit Mithaiwala")


# print_name = start_end_decorator(print_name)

result = add5(10)
print(result)


# print(help(add5))
# print(add5.__name__)

print('-------------------------------------')


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = ''
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


greet("Akshit")

print('--------------- CLASS DECORATOR --------------------')


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_count = 0

    def __call__(self, *args, **kwargs):
        self.num_count += 1
        print(f'This is executed {self.num_count} times')
        return self.func(*args, **kwargs)


# count_calls = CountCalls(None)
# count_calls()

@CountCalls
def say_hello(name):
    greeting = f"Good Morning {name}"
    print(greeting)


say_hello("Akshit")
say_hello("Suru")
say_hello("Viral")
