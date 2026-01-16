#genrators
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1

x = count_up(10)

print(x.__next__())
print(x.__next__())

for i in x:
    print(i)


# <generator object gen at 0x000001C75FD45480>   its giving this output


#List (stores everything in memory) memory issue 

#when u are fetching 1000 records all that records will be loaded in the memory we want one value at a time thats why we use genrator