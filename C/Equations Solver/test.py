from ctypes import *

double = c_double

class Solutions(Structure):
    _fields_ = [("sol1", c_double), 
                ("sol2", c_double), 
                ("is_empty", c_bool)]


file = CDLL("C:/Users/aslas/Desktop/EPQ/C/Equations Solver/equations.dll")

def wrap_function(file, func, argtypes = None, restype = None):
    func = file.__getattr__(func)
    if argtypes: func.argtypes = argtypes
    if restype: func.restype = restype
    return func


quadratic = wrap_function(file, "quadratic", argtypes=(double, double, double), restype = Solutions)

def quadratics(a, b, c):
    sols = quadratic(a, b, c)
    if sols.is_empty: return None
    return sols.sol1, sols.sol2

a, b, c = float(input("Enter co-efficient of x ** 2: ")), float(input("Enter the co-efficient of x: ")), float(input("Enter the constant: "))
if quadratics(a, b, c):
    print(f"{a} * x ** 2 + {b} * x + {c} = 0 provides solutions {quadratics(a, b, c)}. ")
else:
    print(f"{a} * x ** 2 + {b} * x + {c} = 0 provides no valid solutions. ")

input()
