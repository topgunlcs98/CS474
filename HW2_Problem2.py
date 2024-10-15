from z3 import *

p = Bool("p")
q = Bool("q")
r = Bool("r")

## encoding the original formula
original = And(
    Or(q, Not(r)),
    Or(Not(p), r),
    Or(Not(q), r, p),
    Or(p, q, Not(q)),
    Or(Not(r), q),
)

## encoding the resolustion
resolution = And(
    Or(q, Not(r)),
    Or(Not(p), r),
    Or(Not(q), r, p),
    Or(q, Not(p)),
    Or(Not(q), r),
)


s = Solver()
s.add(original)
print("Original formula:")
print(s.check())


s.reset()
s.add(resolution)
print("Resolution:")
print(s.check())
