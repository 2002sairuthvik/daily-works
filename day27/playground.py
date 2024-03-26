# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
    
# def calculate(n, **kwargs):
#     print(kwargs)
    
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
    
# calculate(2, add=3 , multiply=5)

# class Car:
    
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get('model')

# my_car = Car(make="Nissan")   
# print(my_car.model)     

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)


