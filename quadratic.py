def roots(a, b, c):
    import math
    discriminant= b**2 - 4*a*c
    if discriminant>0:
        r1 = (-b + math.sqrt(discriminant)) / 2*a
        r2 = (-b - math.sqrt(discriminant)) / 2*a
        return f"({r1}, {r2})"
    elif discriminant == 0:
        r = -b / (2*a)
        return f"({r})"
    else:
        return "( )"

raiz= roots(1,-3,2)
print(raiz)
    
def value_y(a, b, c, x):
    y= a*(x**2) + b*x + c
    return y
cuad= value_y(1,-3,2,0)
print(cuad)

def to_string(a, b, c):
    if a!=0 and b!=0 and c!=0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a==0 and b!=0 and c!=0:
        return f"f(x) = {b} * X + {c}"
    elif a!=0 and b==0 and c!=0:
        return f"f(x) = {a} * X^2 + {c}"
    elif a!=0 and b!=0 and c==0:
        return f"f(x) = {a} * X^2 + {b} * X"
    elif a==0 and b==0 and c!=0:
        return f"f(x) = {c}"
    elif a==0 and b!=0 and c==0:
        return f"f(x) = {b} * X"
    elif a!=0 and b==0 and c==0:
        return f"f(x) = {a} * X^2"
string= to_string(2,-3,1)
print(string)

def derivation(a, b, c):
    if a!=0 and b!=0:
        return f"f'(x) = {2*a} * X + {b}"
    elif a==0 and b!=0:
        return f"f'(x) = {b}"
    elif a!=0 and b==0:
        return f"f'(x) = {2*a} * X"
    elif a==0 and b==0:
        return f"f'(x) = 0"   
deriv=derivation(2,-3,1)
print(deriv)
