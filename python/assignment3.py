from learning import *
import pdb
import math
import random
import os
import sys
import numpy as np
# import scipy as sp
# import matplotlib.pyplot as plt


def testNeuralNetLearner(data, iterations=1000, learn_rate=0.5, momentum=0.1):

	if data == "xor":
	    ds = DataSet(name='../data/xor')
	    num_input = 2
	    num_output = 2
	    num_hl = 1 # number of hidden layers
	elif data == "semeion":
	    ds = DataSet(name='../data/semeion')
	    num_input = 256
	    num_output = 10
	    num_hl = 1 # number of hidden layers
	 
	# create the learner with the matrix
	NNlearner = createNeuralNetLearner(ds, num_input, num_output, num_hl, iterations, learn_rate, momentum)
 
	# test the learner (cross validation)
		 

def createNeuralNetLearner(ds, num_input, num_output, num_hl, iterations, learn_rate, momentum):
 	# create a neural net learner

 	# transform the ds to matrix of inputs 	
 	obs = np.matrix(ds.examples)
 	inputs = np.delete(obs,len(ds.examples) - 2,1)
 	target = obs[:,num_input]
	mxi = np.matrix(inputs)
	mxt = np.matrix(target)

 	# create input weights
 	mwi = np.random.random((num_input + 1, num_input + 1))

 	# create output weights
 	mwo = np.random.random((num_input + 1, num_output))
 	
	# call forward propogation
	for i in range(len(mxi)):

		# add in bias column of 1's
		input_row_with_bias = np.append(1,mxi[i])	

		# call forward prop
		ai, mnh, mno = forwardProp(np.matrix(input_row_with_bias),np.matrix(mwi),np.matrix(mwo))

		# grab target values
		target_value = mxt[i]

		# call backward prop
		backwardProp(np.matrix(target_value), mno)

 		# update weights
 	

def forwardProp(row, mwi, mwo):
	# takes a list of node values and the associated weights
	# returns a matrix of updated input and output activations 	

	# 1 dimensional input activation matrix
	ai = row * mwi

	# initialize matrix to store hidden node values
	mnh = np.matrix(ai)

	# loop through all of ai and update with sigmoid
	for i in range(ai.shape[1]):	
		mnh[0,i] = sigmoid(ai[0,i])

	# 1 dimensional output activation matrix
	ao = mnh * mwo

	# initialize matrix to store output node values
	mno = np.matrix(ao)

	# loop through all of ao and update with sigmoid
	for i in range(ao.shape[1]):	
		mno[0,i] = sigmoid(ao[0,i])

	return ai, mnh, mno


def sigmoid(a):
	# takes in a value in the activation matrix
	# returns the result of the sigmoid function performed on it

	return 1/(1 + math.pow(math.e, -a))


def _create_weights(m):
	pass


if __name__ == "__main__":

	testNeuralNetLearner("xor",1000,0.5,0.1)

	# some stuff
	# 
	# testNeuralNetLearner()

