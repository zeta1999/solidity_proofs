from z3 import *
from rule import Rule

"""
Rule:
DIV(X, SHL(Y, 1)) -> SHR(Y, X)
Requirements:
"""

rule = Rule()

n_bits = 32

# Input vars
x = BitVec('x', n_bits)
y = BitVec('y', n_bits)

# Constants
bv_one = BitVecVal(1, n_bits)
bv_zero = BitVecVal(0, n_bits)

# Requirements

# Non optimized result
# Division by 0 is undefined for BitVectors, so we define it.
nonopt = If(
			(bv_one << y) == bv_zero,
			bv_zero,
			UDiv(x, bv_one << y)
		)

# Optimized result
opt = LShR(x, y)

rule.check(nonopt, opt)
