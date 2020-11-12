#include<math.h>

typedef enum {False, True} bool;
#define EXPORT __declspec(dllexport)

struct Solutions {
    double sol1;
    double sol2;
    bool is_empty;
};

// Simple - return the result.
EXPORT double linear(double a, double b) {
    return (-b / a);
};

EXPORT struct Solutions quadratic(double a, double b, double c) {
    struct Solutions solutions;

    if (a != 0) {
        if (b * b - 4 * a * c >= 0) {
            solutions.sol1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a);
            solutions.sol2 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a);
            solutions.is_empty = False;
        }
    }

    else {
        solutions.is_empty = True;
    }

    return solutions;
};