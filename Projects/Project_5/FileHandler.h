#ifndef FILEHANDLER_H
#define FILEHANDLER_H

#include <stdio.h>

void save_to_file(double t, double y, const char *filename) {
    FILE *file = fopen(filename, "a");  // Append mode
    if (file == NULL) {
        printf("Error opening file!\n");
        return;
    }
    fprintf(file, "%lf, %lf\n", t, y);  // Write t and y values
    fclose(file);
}

void initialize_file(const char *filename) {
    FILE *file = fopen(filename, "w");  // Write mode
    if (file == NULL) {
        printf("Error creating file!\n");
        return;
    }
    fprintf(file, "Time, Value\n");  // CSV header
    fclose(file);
}

#endif