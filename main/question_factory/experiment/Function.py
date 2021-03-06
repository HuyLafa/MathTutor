from sympy.parsing.sympy_parser import parse_expr
from sympy import *
from sympy.abc import x,y
from mpmath import *

class Function:
	# input: string representation of the function. Variables are marked as "x&" instead of "x"
	# because later "x&" will be replaced with an actual number.
	# isConstant: boolean to indicate if this function is a constant
	# elementary: boolean to indicate if this function is an elementary function.
	def __init__( self, input, isConstant = False, elementary = False ):
		self.func = input
		self.isConstant = isConstant
		self.elementary = elementary
		self.derivative = None
		self.integral = None


	# Return the string currently held
	def getStringFunc( self ):
		if self.elementary or self.isConstant:
			return self.func
		return "(" + self.func + ")"


	# Return the proper representation of this function
	def toString( self ):
		return self.func.replace("x&", "x")


	def constant( self ):
		return self.isConstant


	def isNotElementary( self ):
		return not self.elementary


	def getlatex( self ):
		return latex(parse_expr(self.toString()), inv_trig_style="full")


	def setDerivative( self, derivative ):
		self.derivative = derivative


	def getDerivative( self ):
		return self.derivative


	def getIntegral( self ):
		return self.integral


	def setIntegral( self, integral ):
		self.integral = integral

		
	# Evalute this function given an x-value using SymPy
	@classmethod
	def evaluate(self, funcString, number):
		return N(parse_expr(funcString).subs(symbols("x"),  number))


	@classmethod
	def isAcceptable( cls, expression):
		complexity = 0
		for args in preorder_traversal( expression ):
			# must be integrable
			if isinstance(args, Integral) or str(args) == "zoo" or str(arg) == "inf":
				return False

			# must not be too complex
			complexity += cls.getOperatorComplexity( arg.func )
			if complexity >= complexityBound:
				return False

			# must have valid coefficients


	@classmethod
	def isIntegrable( cls, expression):
		for args in preorder_traversal(expression):
			if isinstance(args, Integral) or str(args) == "zoo":
				return False
		return True

	@classmethod
	def meetsComplexityBound( cls, expression, complexityBound ):
		complexity = 0
		for arg in preorder_traversal(expression):
			complexity += cls.getOperatorComplexity(arg.func)
		return complexity < complexityBound

	@classmethod
	# convert an instance of sympy operator class to a number representing its complexity
	def getOperatorComplexity( cls, operator):
		if str(operator) == "<class 'sympy.core.add.Add'>":
			return 1
		elif str(operator) == "<class 'sympy.core.mul.Mul'>":
			return 2
		elif str(operator) == "<class 'sympy.core.power.Pow'>":
			return 8
		else:
			return 0