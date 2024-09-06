#include <stdio.h>
#include <stdlib.h>
#include "LatexSolver.h"
#include "NumericalSolver.h"
#include "FileHandler.h"

int main() {
    // Prompt the user for the equation in LaTeX format
    char latex_input[256];
    printf("Enter the differential equation in LaTeX format (e.g., Eq(Derivative(y(t), t), t + y(t))):\n");
    fgets(latex_input, sizeof(latex_input), stdin);

    // Call the Python script to solve the equation symbolically
    solve_latex_equation(latex_input);

    // Prompt the user for numerical solving method and parameters
    double t0, y0, h;
    int steps, method_choice;

    printf("Enter the initial time (t0): ");
    scanf("%lf", &t0);
    printf("Enter the initial value (y0): ");
    scanf("%lf", &y0);
    printf("Enter the step size (h): ");
    scanf("%lf", &h);
    printf("Enter the number of steps: ");
    scanf("%d", &steps);
    
    // Output file
    const char *filename = "output.csv";
    initialize_file(filename);

    printf("Choose a numerical method (1: Euler, 2: Runge-Kutta): ");
    scanf("%d", &method_choice);

    // Solve using the chosen method
    if (method_choice == 1) {
        printf("Solving using Euler's Method...\n");
        euler(t0, y0, h, steps, filename);
    } else if (method_choice == 2) {
        printf("Solving using Runge-Kutta Method...\n");
        runge_kutta(t0, y0, h, steps, filename);
    }

    printf("Results have been saved to %s\n", filename);
    
    return 0;
}