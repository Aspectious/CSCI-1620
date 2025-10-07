def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)





def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def sum(n):
    if n < 1:
        return 1
    else:
        return n + sum(n-1)


print(sum(666))











#print(fib(5))



#print(fact(5))
#mfw secure coding principles is tiring (why is it needed for every python script?)






