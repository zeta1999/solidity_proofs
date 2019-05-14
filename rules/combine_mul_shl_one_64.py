from z3 import *
from rule import Rule

"""
Rule:
MUL(X, SHL(Y, 1)) -> SHL(Y, X)
MUL(SHL(X, 1), Y) -> SHL(X, Y)
Requirements:
"""

rule = Rule()

n_bits = 64

# Input vars
x = BitVec('x', n_bits)
y = BitVec('y', n_bits)

# Constants
bv_one = BitVecVal(1, n_bits)

# Requirements

# Non optimized result
nonopt_1 = x * (bv_one << y)
nonopt_2 = (bv_one << x) * y;

# Optimized result
opt_1 = x << y;
opt_2 = y << x;

rule.check(nonopt_1, opt_1)
rule.check(nonopt_2, opt_2)
