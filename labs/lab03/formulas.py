import random; import sys;

def add(values):
    val = 0
    goodvals = []
    for value in values:
        if value < 0:
            goodvals.append(value)
    if len(goodvals) == 0: return 0
    val = goodvals[0]
    for value in goodvals[1:]:
        val += value
    return val

def subtract(values):
    val = 0
    goodvals = []
    for value in values:
        if value > 0:
            goodvals.append(value)
    if len(goodvals) == 0: return 0
    val = goodvals[0]
    for value in goodvals[1:]:
        val -= value
    return val

def multiply(values):
    val = 1
    goodvals = []
    for value in values:
        if not value == 0:
            goodvals.append(value)
    if len(goodvals) == 0: return 0
    val = goodvals[0]
    for value in goodvals[1:]:
        val *= value
    return val

def divide(values):
    val = 1
    if values[0] == 0: return 0
    goodvals = []
    for value in values:
        if not value == 0:
            goodvals.append(value)
        else:
            print("Cannot Divide by Zero")
            sys.exit(0)
    if len(goodvals) == 0: return 0
    val = goodvals[0]
    for value in goodvals[1:]:
        val /= value
    return val

def choose(values): return values[random.randrange(0, len(values))]