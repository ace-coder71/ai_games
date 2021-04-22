import numpy as np
import random
import scipy.special
from defs import *

class Nnet:

    def __init__(self, num_input, num_hidden, num_output):
        self.num_input = num_input
        self.num_hidden = num_hidden
        self.output = num_output
        self.weight_input_hidden = np.random.uniform(-0.5, 0.5, size=(self.num_hidden, self.num_input))
        self.weight_hidden_output = np.random.uniform(-0.5, 0.5, size=(self.output, self.num_hidden))
        self.activation_function = lambda x: scipy.special.expit(x)
    def get_output(self, inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T
        #print('inputs', inputs, sep='\n')
        hidden_inputs = np.dot(self.weight_input_hidden, inputs)
        #print('hidden_inputs', hidden_inputs, sep='\n')
        hidden_outputs = self.activation_function(hidden_inputs)
        #print('hidden_outputs', hidden_outputs, sep='\n')
        final_inputs = np.dot(self.weight_hidden_output, hidden_outputs)
        #print('final_inputs', final_inputs, sep='\n')
        final_outputs = self.activation_function(final_inputs)
        #print('final_outputs', final_outputs, sep='\n')

        return final_outputs

    def get_max_value(self, inputs_list):
        final_outputs = self.get_output(inputs_list)
        return np.max(final_outputs)

    def modify_array(a):
        for x in np.nditer(a, op_flags = ['readwrite']):
            if random.random() < MUTATION_WEIGHT_MODIFY_CHANCE:
                x[...] = np.random.random_sample() - 0.5

    def get_mix_from_arrays(ar1, ar2):
        
        total_entries = ar1.size 
        num_rows = ar1.shape[0]
        num_cols = ar1.shape[1]
