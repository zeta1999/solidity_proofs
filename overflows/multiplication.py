from z3 import *
from rule import Rule
from opcodes import *

"""
Multiplication Overflow condition:
AND(ISZERO(ISZERO(x)), LT(DIV(<mask>, x), y))
"""

n_bits = 32
setOpcodeBits(n_bits)

for type_size in [8, 16]:
	rule = Rule()

	# Input vars
	x = BitVec('x', n_bits)
	y = BitVec('y', n_bits)

	# Constants
	bv_one = BitVecVal(1, n_bits)
	bv_zero = BitVecVal(0, n_bits)
	mask = (bv_one << type_size) - bv_one

	# Requirements
	rule.require(ULT(x,mask))
	rule.require(ULT(y,mask))

	code_condition = AND(ISZERO(ISZERO(x)), LT(DIV(mask, x), y))
	overflow = If(ULT(mask, x * y), bv_one, bv_zero)

	rule.check(code_condition, overflow)
