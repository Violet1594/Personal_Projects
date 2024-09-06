from sympy import *
from sympy.abc import t, y

def solve_differential(latex_input):
    # Convert LaTeX input into SymPy equation
    equation = sympify(latex_input)
    
    # Solve the differential equation symbolically
    solution = dsolve(equation, y(t))
    
    return solution

if __name__ == "__main__":
    import sys
    latex_input = sys.argv[1]
    result = solve_differential(latex_input)
    print(result)