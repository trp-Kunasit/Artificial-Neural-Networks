import math

def power(v):
    return 5*v - 3*(1 - math.log(3.8 - v)) - 1

if __name__ == "__main__":
    v = 2.8
    p = power(v)
    print('power=', p)
