#ifndef NUMERICALSOLVER_H
#define NUMERICALSOLVER_H

#include "FileHandler.h"

// Define the differential equation dy/dt = f(t, y)
double f(double t, double y) {
    return t + y;  // Example: dy/dt = t + y
}

// Euler's method for solving ODEs
void euler(double t0, double y0, double h, int steps, const char *filename) {
    double t = t0;
    double y = y0;

    save_to_file(t, y, filename);  // Save initial condition

    for (int i = 0; i < steps; i++) {
        y = y + h * f(t, y);  // Euler's method formula
        t = t + h;
        save_to_file(t, y, filename);  // Save to file
    }
}

// Runge-Kutta 4th order method for solving ODEs
void runge_kutta(double t0, double y0, double h, int steps, const char *filename) {
    double t = t0;
    double y = y0;

    save_to_file(t, y, filename);  // Save initial condition

    for (int i = 0; i < steps; i++) {
        double k1 = h * f(t, y);
        double k2 = h * f(t + h / 2.0, y + k1 / 2.0);
        double k3 = h * f(t + h / 2.0, y + k2 / 2.0);
        double k4 = h * f(t + h, y + k3);

        y = y + (1.0 / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4);
        t = t + h;
        save_to_file(t, y, filename);  // Save to file
    }
}

#endif