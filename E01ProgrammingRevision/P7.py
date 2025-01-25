"""
Teerapong Kunasit
Problem 7: SIR Model Disease Spread Calculator
"""

if __name__ == "__main__":
    S, I, R = input("Initial S, I, R: ").split()
    c, r = input("c, r: ").split()
    S = float(S)
    I = float(I)
    R = float(R)
    c = float(c)
    r = float(r)
    periods = int(input("periods: "))

    if any(x < 0 for x in [S, I, R, c, r, periods]):
        raise ValueError("All values must be non-negative")

    if c * S > r:
        print("--> It is spreading!")
    else:
        print("--> It is contained!")

    with open("epidemic.txt", "w") as f:
        m = "0: S = {:.0f}; I = {:.0f}; R = {:.0f}\n".format(S, I, R)
        f.write(m)
        for n in range(periods):
            dS = -c * S * I
            dI = c * S * I - r * I
            dR = r * I

            S += dS
            I += dI
            R += dR

            m = "{}: S = {:.0f}; I = {:.0f}; R = {:.0f}\n".format(n+1, S, I, R)
            f.write(m)