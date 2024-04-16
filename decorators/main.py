import time

def delay_decorator(function):
    def wrapper():
        time.sleep(2)
        function()
    return wrapper

@delay_decorator
def say_hi():
    print("hello")

@delay_decorator    
def say_bye():
    print("bye")
    
@delay_decorator
def greet():
    print("How are you?")

say_hi()
say_bye()
greet()