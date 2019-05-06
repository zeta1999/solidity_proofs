from z3 import *
from rule import Rule

"""
Shift left workaround that Solidity implements
due to a bug in Boost.
"""

rule = Rule()

n_bits = 8
bigint_bits = 16

# Input vars
x = BitVec('x', n_bits)
a = BitVec('a', n_bits)
b = BitVec('r', bigint_bits)

# Compute workaround
workaround = Int2BV(
	BV2Int(
		(Int2BV(BV2Int(x), bigint_bits) << Int2BV(BV2Int(a), bigint_bits)) &
		Int2BV(BV2Int(Int2BV(IntVal(-1), n_bits)), bigint_bits)
	), n_bits
)

rule.check(workaround, x << a)
