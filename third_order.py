import matplotlib.pyplot as plt
import numpy as np

def plot_third_order():
    a = float(input("Enter coefficient 'a': "))
    b = float(input("Enter coefficient 'b': "))
    c = float(input("Enter coefficient 'c': "))
    d = float(input("Enter coefficient 'd': "))

    x = range(-10, 11)
    y = [a*x**3 + b*x**2 + c*x + d for x in x]

    roots = np.roots([a, b, c, d])  # Calculate the roots

    for i, root in enumerate(roots, 1):
        print(f"Root{i}: {root}")

    equation = f"y = {a}x^3 + {b}x^2 + {c}x + {d}"

    plt.plot(x, y, label=equation)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Third-Order Equation Solver")
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_third_order()

