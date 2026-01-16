# *args and **kwargs

#*for tuples
#** for dict

def f(*name):
    return name

print(f(1, 2, 3)) 

def fun(**roll):
    return roll

print(fun(name="Shaiv", age=21, cgpa=7.5))