#decorater
def outer(func):

    def inner():
        #u can change greet function here
        func()
        return "hello"
    return inner    



def greet():
    print("Hi")

new_func = outer(greet)
print(new_func())