import pickle
import numpy as np
import types
import sys, os

from sympy import *
from random import choice, randint, uniform

sys.path.append(os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../../")))
from main.question_factory.DiffProd import FunctionTree, Production, Function
from main.question_factory.QuestionData import QuestionData

"""

Parameters for generating questions

"""
questions_num = 20
difficulty = 4
dirname = "generated_questions"

"""

Helper functions

"""

def generateFunction():
	global domain, tree, funcString, derivString, eval_table
	tree = FunctionTree.buildTreeWithMaxComplexity(difficulty)
	#tree.printTree()
	funcString = tree.getOutputFunction().toString()
	derivString = tree.getOutputDerivative().toString()
	generateEvalTable()

def generateEvalTable() :
	global domain, tree, funcString, derivString, eval_table
	domain = 2*np.random.random(60)
	eval_table = np.array([(x, Function.evaluate(derivString, x)) for x in domain if isinstance(Function.evaluate(derivString, x), Float)]).astype(float)

def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


"""

Generate question files

"""

print ""
print "##############################################"
print "Generating questions of difficulty " + str(difficulty)
print "Questions will be saved in '" + dirname + "'"
print "##############################################"
print ""

for i in range(questions_num):
	generateFunction()
	while len(eval_table) < 10:
		generateFunction()
	question_data = QuestionData(tree, funcString, derivString, domain, eval_table)
	filename = dirname + "/difficulty" + str(difficulty) + "_" + str(i) + ".question"
	save_object(question_data, filename)
	print "Generated Question #" + str(i) + " : " + funcString

print ""
print "Finished generating " + str(questions_num) + " question(s)."

