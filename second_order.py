import matplotlib.pyplot as plt
import cmath

def solve_second_order():
    a = float(input("Enter coefficient 'a' of the quadratic equation: "))
    b = float(input("Enter coefficient 'b' of the quadratic equation: "))
    c = float(input("Enter coefficient 'c' of the quadratic equation: "))
    
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    print('discriminant(delta): ',discriminant)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
    
    equation = f"y = {a}x^2 + {b}x + {c}"
    draw_quadratic_curve(a, b, c, equation)

def draw_quadratic_curve(a, b, c, equation):
    x = range(-10, 11)
    y = [a * xi**2 + b * xi + c for xi in x]
    
    plt.plot(x, y, label=equation)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Quadratic Equation Plot")
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    solve_second_order()

