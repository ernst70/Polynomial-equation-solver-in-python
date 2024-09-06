import matplotlib.pyplot as plt

def solve_first_order():
    a = float(input("Enter coefficient 'a' of the linear equation: "))
    b = float(input("Enter coefficient 'b' of the linear equation: "))
    
    if a == 0:
        if b == 0:
            print("Infinite solutions")
        else:
            print("No solutions")
    else:
        root = -b / a
        width_from_origin = abs(root)
        
        print(f"x: {root} | y: {width_from_origin}")
        print(f"")
        
        equation = f"y = {a}x + {b}"
        draw_linear_curve(a, b, equation)

def draw_linear_curve(a, b, equation):
    x = range(-10, 11)
    y = [a * xi + b for xi in x]
    
    plt.plot(x, y, label=equation)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear Equation")
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    solve_first_order()
