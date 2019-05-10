from z3 import *
from rule import Rule

"""
Rule:
SHR(B, AND(X, A)) -> AND(SHR(B, X), A >> B)
SHR(B, AND(A, X)) -> AND(SHR(B, X), A >> B)
Requirements:
B < BitWidth
"""

rule = Rule()

n_bits = 128

# Input vars
x = BitVec('x', n_bits)
a = BitVec('a', n_bits)
b = BitVec('b', n_bits)

# Constants
bv_n = BitVecVal(n_bits, n_bits)

# Requirements
rule.require(ULT(b, bv_n))

# Non optimized result
nonopt_1 = LShR((x & a), b);
nonopt_2 = LShR((a & x), b);

# Optimized result
mask = LShR(a, b);
opt = LShR(x, b) & mask;

rule.check(nonopt_1, opt)
rule.check(nonopt_2, opt)
