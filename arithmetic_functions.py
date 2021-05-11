def zero(function=None):
    return function(0) if function else 0
def one(function=None):
    return function(1) if function else 1
def two(function=None):
    return function(2) if function else 2
def three(function=None):
    return function(3) if function else 3
def four(function=None):
    return function(4) if function else 4
def five(function=None):
    return function(5) if function else 5
def six(function=None):
    return function(6) if function else 6
def seven(function=None):
    return function(7) if function else 7
def eight(function=None):
    return function(8) if function else 8
def nine(function=None):
    return function(9) if function else 9
    
def plus(p):
    plus = lambda a: a + p
    return plus
def minus(m):
    minus = lambda a: a - m
    return minus
def times(n_times):
    times = lambda y: y * n_times
    return times
def divided_by(div):
    divided_by = lambda y: y / div
    return divided_by
    
print(four(times(five())))   
print(one(plus(eight())))
print(seven(minus(three())))
print(nine(divided_by(three())))

print(nine(divided_by(two())))
print(zero(divided_by(two())))

