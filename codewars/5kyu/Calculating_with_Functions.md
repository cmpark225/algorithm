# Detail
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

JavaScript:

```
seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3
```
Ruby:

```
seven(times(five)) # must return 35
four(plus(nine)) # must return 13
eight(minus(three)) # must return 5
six(divided_by(two)) # must return 3
```
Requirements:

* There must be a function for each number from 0 ("zero") to 9 ("nine")
* There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby)
* Each calculation consist of exactly one operation and two numbers
* The most outer function represents the left operand, the most inner function represents the right operand
* Divison should be integer division, e.g eight(dividedBy(three()))/eight(divided_by(three)) should return 2, not 2.666666...


# Best Practices
```
def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y
```

=> lambda

# My Solutions
```
def zero(func=None):
    return 0 if not func else func(0)
    
def one(func=None):
    return 1 if not func else func(1)

def two(func=None):
    return 2 if not func else func(2)        

def three(func=None):
    return 3 if not func else func(3)
    
def four(func=None):
    return 4 if not func else func(4)
    
def five(func=None):
    return 5 if not func else func(5)
    
def six(func=None):
    return 6 if not func else func(6)

def seven(func=None): 
    return 7 if not func else func(7)

def eight(func=None): 
    return 8 if not func else func(8)

def nine(func=None): 
    return 9 if not func else func(9)
    

def plus(right_operand): 
    def inner_plus(num):
        return num + right_operand
    return inner_plus
    
def minus(right_operand): 
    def inner_minus(num):
        return num - right_operand
    return inner_minus
    
def times(right_operand): 
    def inner_times(num):
        return num * right_operand
    return inner_times
  
def divided_by(right_operand): 
    def inner_divided_by(num):
        return int(num/right_operand)
    return inner_divided_by
```

# Todo
클로져, lambda
