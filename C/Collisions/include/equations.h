#define EXPORT __declspec(dllexport)
typedef enum {False, True} bool;

struct Solutions;
EXPORT double linear(double, double);
EXPORT struct Solutions quadratic(double, double, double);