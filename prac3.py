#nested function
def outer():

    def inner():

        return "hello"
    return inner()    


print(outer())