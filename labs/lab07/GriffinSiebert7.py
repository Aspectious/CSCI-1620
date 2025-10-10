# Authored by Aspectious for code review purposes.

# Power function simply splits the problem up into repeated multiplication.
# When the power is exhausted to the power of one, we return last x value.
def power(x,y):
    if (y <= 1):
        return x * y;
    else:
        return x * power(x,y-1)

# A simple function, it really is just a complex way to multiply a number by two.
def cat_ears(n):
    if n == 0:
        return 0
    else:
        return 2 + cat_ears(n-1)

# This function was a lot more complex to handle
# I started by writing my own function that used iteration and used its behaviour to build this function instead. 
# Very cool process. I would have it all in one else, however I thought this should work fine for readability.
# Does python have switch statments?
def alien_ears(n):
    if n < 1:
        return 0;
    if n % 2 == 0:
        return 2 + alien_ears(n-1)
    else:
        return 3 + alien_ears(n-1)


# Tests, should only run if python file is run from main.
def main():
    print(power(2,3))
    print(power(-2,3))
    print(power(1,5))
    print(cat_ears(0))
    print(cat_ears(1))
    print(cat_ears(2))
    print(alien_ears(1))
    print(alien_ears(2))

# The standard.
if __name__ == "__main__":
    main()
