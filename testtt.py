import math

def P(v):
    # Define the power function
    return 5*v - 3*(1 - math.log(3.8 - v)) - 1
    # or equivalently: return 5*v - 4 + 3*math.log(3.8 - v)

# Solve for v* directly (no need for sympy):
v_star = 3.2  # from the algebraic solution
p_star = P(v_star)

print(f"Optimal operating voltage: v* = {v_star} V")
print(f"Maximum power delivered: P(v*) = {p_star:.4f}")


5-1/(3.8-v)=0
print(v)
