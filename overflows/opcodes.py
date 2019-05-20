from z3 import *

__constants = [BitVecVal(0, 256), BitVecVal(1, 256)]

def setOpcodeBits(bits):
	__constants[0] = BitVecVal(0, bits)
	__constants[1] = BitVecVal(1, bits)

def ISZERO(x):
	return If(x == 0, __constants[1], __constants[0])

def ADD(x, y):
	return x + y

def MUL(x, y):
	return x * y

def SUB(x, y):
	return x - y

def DIV(x, y):
	return If(y == 0, __constants[0], UDiv(x, y))

def SDIV(x, y):
	return If(y == 0,  __constants[0], x / y)

def MOD(x, y):
	return If(y == 0, __constants[0], URem(x, y))

def SMOD(x, y):
	return If(y == 0, __constants[0], x % y)

def LT(x, y):
	return If(ULT(x, y), __constants[1], __constants[0])

def GT(x, y):
	return If(UGT(x, y), __constants[1], __constants[0])

def SLT(x, y):
	return If(x < y, __constants[1], __constants[0])

def SGT(x, y):
	return If(x > y, __constants[1], __constants[0])

def AND(x, y):
	return x & y

def SHL(x, y):
	return y << x

def SHR(x, y):
	return LShR(y, x)

def SAR(x, y):
	return y >> x
