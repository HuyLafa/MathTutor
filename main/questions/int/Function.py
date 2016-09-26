from sympy.parsing.sympy_parser import parse_expr
from sympy import *
from mpmath import *

class Function:

	# input: string representation of the function. Variables are marked as "x&" instead of "x"
	# because later "x&" will be replaced with an actual number.
	# isConstant: boolean to indicate if this function is a constant
	# elementary: boolean to indicate if this function is an elementary function.
	def __init__( self, input, isConstant = False, elementary = True ):
		self.func = input
		self.isConstant = isConstant
		self.elementary = elementary
		self.integral = None


	# Return the string currently held
	def getStringFunc( self ):
		return self.func


	# Return the proper representation of this function
	def toString( self ):
		return self.func.replace("x&", "x")

	# Evalute this function given an x-value using SymPy
	@classmethod
	def evaluate(self, funcString, number):
		return N(parse_expr(funcString).subs(symbols("x"),  number))


	def constant( self ):
		return self.isConstant


	def isNotElementary( self ):
		return not self.elementary


	def setlatex( self, latex ):
		self.latex = latex


	def getlatex( self ):
		return latex(parse_expr(self.toString()), inv_trig_style="full")


	def getDisplayLatex( self ):
		return self.latex.replace("x&", "x")


	def setDerivative( self, derivative ):
		self.derivative = derivative


	def getDerivative( self ):
		return self.derivative