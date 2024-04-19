def max_of_two(x,y):
    if (x>y):
        return x 
    else: (y>x)
    return y
maxtwo= max_of_two(5,1)
print(maxtwo)

def max_of_three(x, y, z):
    if x>z and x>y:
        return x
    elif x<y and y>z:
        return y
    else: x<z and y<z
    return z
maxthree= max_of_three(100,70,4)
print(maxthree)
