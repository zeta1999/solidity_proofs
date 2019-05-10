from z3 import *
from rule import Rule

"""
Rule:
SHL(B, AND(X, A)) -> AND(SHL(B, X), A << B)
SHL(B, AND(A, X)) -> AND(SHL(B, X), A << B)
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
nonopt_1 = (x & a) << b;
nonopt_2 = (a & x) << b;

# Optimized result
mask = a << b;
opt = (x << b) & mask;

rule.check(nonopt_1, opt)
rule.check(nonopt_2, opt)
