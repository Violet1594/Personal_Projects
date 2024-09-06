#ifdef _WIN32
    #define popen _popen
    #define pclose _pclose
#endif

#include <stdio.h>
#include <stdlib.h>

// Function to call the Python script and get the symbolic solution
void solve_latex_equation(const char *latex_input) {
    char command[256];
    
    // Build the command to call the Python script with the LaTeX input
    snprintf(command, sizeof(command), "python LatexSolver.py \"%s\"", latex_input);
    
    // Open a pipe to the Python process and capture its output
    FILE *fp = popen(command, "r");
    if (fp == NULL) {
        printf("Error executing Python script.\n");
        return;
    }
    
    // Read the output (the solution)
    char result[1024];
    if (fgets(result, sizeof(result), fp) != NULL) {
        printf("Symbolic Solution: %s\n", result);
    } else {
        printf("No solution received.\n");
    }
    
    // Close the pipe
    pclose(fp);
}