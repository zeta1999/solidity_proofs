from z3 import *
from rule import Rule

"""
SHR(B, SHL(A, X)) -> AND(SH[L/R]([B - A / A - B], X), Mask)
"""

rule = Rule()

n_bits = 64

# Input vars
x = BitVec('x', n_bits)
a = BitVec('a', n_bits)
b = BitVec('b', n_bits)

# Constants
bv_n = BitVecVal(n_bits, n_bits)

# Requirements
rule.require(ULT(a, bv_n))
rule.require(ULT(b, bv_n))

# Non optimized result
nonopt = LShR(x << a, b)

# Optimized result
mask = (LShR(Int2BV(IntVal(-1), n_bits) << a, b))
opt = If(
	UGT(a, b),
	(x << (a - b)) & mask,
		If(
			UGT(b, a),
			LShR(x, b - a) & mask,
			x & mask
		)
	)

rule.check(nonopt, opt)
