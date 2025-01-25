import math

def objective(v):
    return 5*v - 3*(1 - math.log(3.8 - v)) - 1

def dPv(v):
    return 5 - 3/(3.8 - v)

def maximizer(v_init, step_size, steps):
    v = v_init
    for _ in range(steps):
        g = dPv(v)
        v = v + step_size*g
    return v

if __name__ == "__main__":
    v = 1.2
    print('objective=', objective(v))
    print('dPv=', dPv(v))
    print('v*=', maximizer(v, 0.001, 100))
    print('v*=', maximizer(v, 0.01, 10))
    print('v*=', maximizer(v, 0.02, 10))
