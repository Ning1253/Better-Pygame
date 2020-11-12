#include <math.h>
#include "equations.c"

#define EXPORT __declspec(dllexport)
#define absc(x, y) sqrt(x * x + y * y)
#define PI 3.14159265358979
#define len(x) (sizeof(x) / sizeof(x[0]))

//rect: {topleft, topright, bottomleft, bottomright};
//circ: {x, y, rad};

double max(double array[], int size) {
    double biggest = array[0];
    for (int i = 1; i < size; i++) {
        if (array[i] > biggest) {
            biggest = array[i];
        }
    }
    return biggest;   
}

double min(double array[], int size) {
    double smallest = array[0];
    for (int i = 1; i < size; i++) {
        if (array[i] < smallest) {
            smallest = array[i];
        }
    }
    return smallest;    
}



EXPORT bool rect_collision(double a[4][2], double b[4][2]) {
    
    if (a[1][0] != a[0][0] && a[1][1] != a[0][1]) {
        double m1 = (a[1][1] - a[0][1]) / (a[1][0] - a[0][0]); // dy / dx
        double m2 = -1 / m1; // 90 degrees off, -1/m.

        double p1[] = {(m1 * a[0][1] + a[0][0]) / (m1 * m1 + 1), 
                       (m1 * a[1][1] + a[1][0]) / (m1 * m1 + 1), 
                       (m1 * a[2][1] + a[2][0]) / (m1 * m1 + 1), 
                       (m1 * a[3][1] + a[3][0]) / (m1 * m1 + 1)};

        double p2[] = {(m1 * b[0][1] + b[0][0]) / (m1 * m1 + 1), 
                       (m1 * b[1][1] + b[1][0]) / (m1 * m1 + 1), 
                       (m1 * b[2][1] + b[2][0]) / (m1 * m1 + 1), 
                       (m1 * b[3][1] + b[3][0]) / (m1 * m1 + 1)};
        
        double A = min(p1, 4), B = min(p2, 4), C = max(p1, 4), D = max(p2, 4);

        
        if ( !( ( (A <= B) && (B <= C) ) || 
                ( (A <= D) && (D <= C) ) ||
                ( (B <= A) && (A <= D) ) || 
                ( (B <= C) && (C <= D) ) ) ) {
            
            return False;
        }

        double p3[] = {(m2 * a[0][1] + a[0][0]) / (m2 * m2 + 1), 
                       (m2 * a[1][1] + a[1][0]) / (m2 * m2 + 1), 
                       (m2 * a[2][1] + a[2][0]) / (m2 * m2 + 1), 
                       (m2 * a[3][1] + a[3][0]) / (m2 * m2 + 1)};
        
        double p4[] = {(m2 * b[0][1] + b[0][0]) / (m2 * m2 + 1), 
                       (m2 * b[1][1] + b[1][0]) / (m2 * m2 + 1), 
                       (m2 * b[2][1] + b[2][0]) / (m2 * m2 + 1), 
                       (m2 * b[3][1] + b[3][0]) / (m2 * m2 + 1)};
        
        A = min(p3, 4), B = min(p4, 4), C = max(p3, 4), D = max(p4, 4);

        
        if ( !( ( (A <= B) && (B <= C) ) || 
                ( (A <= D) && (D <= C) ) ||
                ( (B <= A) && (A <= D) ) || 
                ( (B <= C) && (C <= D) ) ) ) {
            
            return False;
        }
    }

    else {
        double p1[] = {a[0][0], a[1][0], a[2][0], a[3][0]};
        double p2[] = {b[0][0], b[1][0], b[2][0], b[3][0]};

        double A = min(p1, 4), B = min(p2, 4), C = max(p1, 4), D = max(p2, 4);
        
        if ( !( ( (A <= B) && (B <= C) ) || 
                ( (A <= D) && (D <= C) ) ||
                ( (B <= A) && (A <= D) ) || 
                ( (B <= C) && (C <= D) ) ) ) {
            
            return False;
        }

        double p3[] = {a[0][1], a[1][1], a[2][1], a[3][1]};
        double p4[] = {b[0][1], b[1][1], b[2][1], b[3][1]};

        A = min(p3, 4), B = min(p4, 4), C = max(p3, 4), D = max(p4, 4);
        
        if ( !( ( (A <= B) && (B <= C) ) || 
                ( (A <= D) && (D <= C) ) ||
                ( (B <= A) && (A <= D) ) || 
                ( (B <= C) && (C <= D) ) ) ) {
            
            return False;
        }
    }

    if (b[1][0] != b[0][0] && b[1][1] != b[0][1]) {
        double m1 = (b[1][1] - b[0][1]) / (b[1][0] - b[0][0]); // dy / dx
        double m2 = -1 / m1; // 90 degrees off, -1/m.

        double p1[] = {(m1 * a[0][1] + a[0][0]) / (m1 * m1 + 1), 
                       (m1 * a[1][1] + a[1][0]) / (m1 * m1 + 1), 
                       (m1 * a[2][1] + a[2][0]) / (m1 * m1 + 1), 
                       (m1 * a[3][1] + a[3][0]) / (m1 * m1 + 1)};
        
        double p2[] = {(m1 * b[0][1] + b[0][0]) / (m1 * m1 + 1), 
                       (m1 * b[1][1] + b[1][0]) / (m1 * m1 + 1), 
                       (m1 * b[2][1] + b[2][0]) / (m1 * m1 + 1), 
                       (m1 * b[3][1] + b[3][0]) / (m1 * m1 + 1)};
        
        double A = min(p1, 4), B = min(p2, 4), C = max(p1, 4), D = max(p2, 4);
        
        if ( !( ( (A <= B) && (B <= C) ) || 
                ( (A <= D) && (D <= C) ) ||
                ( (B <= A) && (A <= D) ) || 
                ( (B <= C) && (C <= D) ) ) ) {
            
            return False;
        }

        double p3[] = {(m2 * a[0][1] + a[0][0]) / (m2 * m2 + 1), 
                       (m2 * a[1][1] + a[1][0]) / (m2 * m2 + 1), 
                       (m2 * a[2][1] + a[2][0]) / (m2 * m2 + 1), 
                       (m2 * a[3][1] + a[3][0]) / (m2 * m2 + 1)};
        
        double p4[] = {(m2 * b[0][1] + b[0][0]) / (m2 * m2 + 1), 
                       (m2 * b[1][1] + b[1][0]) / (m2 * m2 + 1), 
                       (m2 * b[2][1] + b[2][0]) / (m2 * m2 + 1), 
                       (m2 * b[3][1] + b[3][0]) / (m2 * m2 + 1)};
        
        A = min(p3, 4), B = min(p4, 4), C = max(p3, 4), D = max(p4, 4);
        
        if ( !( ( (A <= B) && (B <= C) ) || 
                ( (A <= D) && (D <= C) ) ||
                ( (B <= A) && (A <= D) ) || 
                ( (B <= C) && (C <= D) ) ) ) {
            
            return False;
        }
    }

    else {
        double p1[] = {a[0][0], a[1][0], a[2][0], a[3][0]};
        double p2[] = {b[0][0], b[1][0], b[2][0], b[3][0]};

        double A = min(p1, 4), B = min(p2, 4), C = max(p1, 4), D = max(p2, 4);
        
        if ( !( ( (A <= B) && (B <= C) ) || 
                ( (A <= D) && (D <= C) ) ||
                ( (B <= A) && (A <= D) ) || 
                ( (B <= C) && (C <= D) ) ) ) {
            
            return False;
        }

        double p3[] = {a[0][1], a[1][1], a[2][1], a[3][1]};
        double p4[] = {b[0][1], b[1][1], b[2][1], b[3][1]};

        A = min(p3, 4), B = min(p4, 4), C = max(p3, 4), D = max(p4, 4);
        
        if ( !( ( (A <= B) && (B <= C) ) || 
                ( (A <= D) && (D <= C) ) ||
                ( (B <= A) && (A <= D) ) || 
                ( (B <= C) && (C <= D) ) ) ) {
            
            return False;
        }
    }

    return True;
}


EXPORT bool circle_collision(double a[3], double b[3]) {
    double len2 = (b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1]); // a^2 + b^2
    double rad2 = (a[2] + b[2]) * (a[2] + b[2]); //Sum of radiuses squared

    if (len2 <= rad2) {
        return True;
    }

    else {
        return False;
    }
}

EXPORT bool rect_circle_collision(double r[4][2], double c[3]) {
    //Centre to 0, 0
    double rad = c[2];
    // Translate rect by - circle coords, to shift to 0, 0.
    for (int i = 0; i < 4; i++) {
        r[i][0] -= c[0];
        r[i][1] -= c[1];
    };

    c[0] = 0;
    c[1] = 0;

    if (absc(r[0][0], r[0][1]) <= rad &&
        absc(r[1][0], r[1][1]) <= rad &&
        absc(r[2][0], r[2][1]) <= rad &&
        absc(r[3][0], r[3][1]) <= rad) {
        return True;
    }

    // Get both gradients of rectangle, as in rect_collision. 
    if (r[1][0] != r[0][0] && r[1][1] != r[0][1]) {
        double m1 = (r[1][1] - r[0][1]) / (r[1][0] - r[0][0]); // dy / dx
        double m2 = -1 / m1; // 90 degrees off, -1/m.

        double c1 = r[0][1] - m1 * r[0][0], c2 = r[3][1] - m1 * r[3][0];
        double c3 = r[0][1] - m2 * r[0][0], c4 = r[3][1] - m2 * r[3][0];

        if ( ((c1 >= 0 && c2 <= 0) || (c1 <= 0 && c2 >= 0)) &&
             ((c3 >= 0 && c4 <= 0) || (c3 <= 0 && c4 >= 0))) {return True;}
        
        struct Solutions a = quadratic(m1 * m1 + 1, 2 * m1 * c1, c1 * c1 - rad * rad), 
                         b = quadratic(m2 * m2 + 1, 2 * m2 * c3, c3 * c3 - rad * rad), 
                         c = quadratic(m1 * m1 + 1, 2 * m1 * c2, c2 * c2 - rad * rad), 
                         d = quadratic(m2 * m2 + 1, 2 * m2 * c4, c4 * c4 - rad * rad);

        if (a.is_empty && b.is_empty && c.is_empty && d.is_empty) {return False;}
        
            if (!a.is_empty) {
            if (r[0][0] <= a.sol1 && a.sol1 <= r[1][0]) {return True;}
            if (r[0][0] <= a.sol2 && a.sol2 <= r[1][0]) {return True;}
            if (r[0][0] >= a.sol1 && a.sol1 >= r[1][0]) {return True;}
            if (r[0][0] >= a.sol2 && a.sol2 >= r[1][0]) {return True;}
        }
        if (!b.is_empty) {
            if (r[0][0] <= b.sol1 && b.sol1 <= r[2][0]) {return True;}
            if (r[0][0] <= b.sol2 && b.sol2 <= r[2][0]) {return True;}
            if (r[0][0] >= b.sol1 && b.sol1 >= r[2][0]) {return True;}
            if (r[0][0] >= b.sol2 && b.sol2 >= r[2][0]) {return True;}
        }
        if (!c.is_empty) {
            if (r[2][0] <= c.sol1 && c.sol1 <= r[3][0]) {return True;}
            if (r[2][0] <= c.sol2 && c.sol2 <= r[3][0]) {return True;}
            if (r[2][0] >= c.sol1 && c.sol1 >= r[3][0]) {return True;}
            if (r[2][0] >= c.sol2 && c.sol2 >= r[3][0]) {return True;}
        }
        if (!d.is_empty) {
            if (r[1][0] <= d.sol1 && d.sol1 <= r[3][0]) {return True;}
            if (r[1][0] <= d.sol2 && d.sol2 <= r[3][0]) {return True;}
            if (r[1][0] >= d.sol1 && d.sol1 >= r[3][0]) {return True;}
            if (r[1][0] >= d.sol2 && d.sol2 >= r[3][0]) {return True;}
        }

        return False;
        
    }

    else {
        if ( (( r[0][0] <= 0 && r[3][0] >= 0 ) || ( r[0][0] >= 0 && r[3][0] <= 0 )) && 
             (( r[0][1] <= 0 && r[3][1] >= 0 ) || ( r[0][1] >= 0 && r[3][1] <= 0 ))) {
            return True;
        }
        
        else {
            struct Solutions a = quadratic(1, 0, r[0][0] * r[0][0] - rad * rad),
                             b = quadratic(1, 0, r[3][0] * r[3][0] - rad * rad),
                             c = quadratic(1, 0, r[0][1] * r[0][1] - rad * rad), 
                             d = quadratic(1, 0, r[3][1] * r[3][1] - rad * rad);

            if (a.is_empty && b.is_empty && c.is_empty && d.is_empty) {return False;}
            
            if (!a.is_empty) {
                if (r[0][1] <= a.sol1 && a.sol1 <= r[3][1]) {return True;}
                if (r[0][1] <= a.sol2 && a.sol2 <= r[3][1]) {return True;}
                if (r[0][1] >= a.sol1 && a.sol1 >= r[3][1]) {return True;}
                if (r[0][1] >= a.sol2 && a.sol2 >= r[3][1]) {return True;}
            }
            if (!b.is_empty) {
                if (r[0][1] <= b.sol1 && b.sol1 <= r[3][1]) {return True;}
                if (r[0][1] <= b.sol2 && b.sol2 <= r[3][1]) {return True;}
                if (r[0][1] >= b.sol1 && b.sol1 >= r[3][1]) {return True;}
                if (r[0][1] >= b.sol2 && b.sol2 >= r[3][1]) {return True;}
            }
            if (!c.is_empty) {
                if (r[0][0] <= c.sol1 && c.sol1 <= r[3][0]) {return True;}
                if (r[0][0] <= c.sol2 && c.sol2 <= r[3][0]) {return True;}
                if (r[0][0] >= c.sol1 && c.sol1 >= r[3][0]) {return True;}
                if (r[0][0] >= c.sol2 && c.sol2 >= r[3][0]) {return True;}
            }
            if (!d.is_empty) {
                if (r[0][0] <= d.sol1 && d.sol1 <= r[3][0]) {return True;}
                if (r[0][0] <= d.sol2 && d.sol2 <= r[3][0]) {return True;}
                if (r[0][0] >= d.sol1 && d.sol1 >= r[3][0]) {return True;}
                if (r[0][0] >= d.sol2 && d.sol2 >= r[3][0]) {return True;}
            }

            return False;
        }
        
    }

    return False;
}

EXPORT bool pixel_collision(double a[][2], int sizea, double b[][2], int sizeb) {
    for (int i = 0; i < sizea; i++) {
        for (int j = 0; j < sizeb; j++) {
            if (a[i][0] == b[j][0] && a[i][1] == b[j][1]) {return True;}
        }
    }
    return False;
}

EXPORT bool pixel_circle_collision(double a[][2], int sizea, double c[3]) {
    for (int i = 0; i < sizea; i++) {
        if ((a[i][0] - c[0]) * (a[i][0] - c[0]) + (a[i][1] - c[1]) * (a[i][1] - c[1]) <= c[3] * c[3]) {
            return True;
        }
    }
    return False;
}


EXPORT bool pixel_rect_collision(double a[][2], int sizea, double r[4][2]) {
    if (r[0][0] != r[1][0] && r[0][1] != r[1][1]) {
        
        double m1 = (r[1][1] - r[0][1]) / (r[1][0] - r[0][0]);
        double m2 = 1 / m1;

        double c1 = r[0][1] - m1 * r[0][0];
        double c2 = r[3][1] - m1 * r[3][0];
        double c3 = r[0][1] - m2 * r[0][0];
        double c4 = r[3][1] - m2 * r[3][0];

        for (int i = 0; i < sizea; i++) {
            double A = a[i][1] - m1 * a[i][0];
            double B = a[i][1] - m2 * a[i][0];

            if ( ( (c1 <= A && A <= c2) ||
                   (c1 >= A && A >= c2) ) &&
                 ( (c3 <= B && B <= c4) ||
                   (c3 >= B && B >= c4) ) ) {
                return True;
            }
        }

        return False;
    }

    else {
        double x1 = r[0][0], x2 = r[3][0], y1 = r[0][1], y2 = r[3][1];

        for (int i = 0; i < sizea; i++) {
            double A = a[i][0], B = a[i][1];

            if ( ( (x1 <= A && A <= x2) ||
                   (x1 >= A && A >= x2) ) &&
                 ( (y1 <= B && B <= y2) ||
                   (y1 >= B && B >= y2) ) ) {
                return True;
            }
        }

        return False;
    }
}