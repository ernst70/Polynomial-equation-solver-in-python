import first_order
import second_order
import third_order

def main():
    degree = int(input('Enter the degree of the algebraic equation (1, 2, or 3): '))
    
    if degree == 1:
        first_order.solve_first_order()
    elif degree == 2:
        second_order.solve_second_order()
    elif degree == 3:
        third_order.plot_third_order()
    else:
        print("Unsupported degree. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


