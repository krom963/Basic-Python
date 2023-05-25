improt cmath
def solve_quadratic(a, b, c):
    D = cmath.sqrt(b**2 - 4*a*c)

    x1 = (-b + D) / (2*a)
    x2 = (-b - D) / (2*a)
    return x1, x2   

a = float(input("係数a："))
b = float(input("係数b："))
c = float(input("係数c："))
x1, x2 = solve_quadratic(a, b, c)
print("x1=",x1,"x2=:",x2)

