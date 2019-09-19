# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine

#create the Turing machine
adder = TuringMachine( 
    { 
        #Write your transition rules here as entries to a Python dictionary
        #For example, the key will be a pair (state, character)
        #The value will be the triple (next state, character to write, move head L or R)
        #such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        #then transition to state q1, write a 0 and move head right.
        
        ('q0', '1'): ('q0','1','R'),
        

        
        ('q0', '0'): ('q0','','R'),
        ('q0', ''): ('qa', '', 'R')
        
    }
)


print("Input:",'110111')
print("Accepted?", adder.accepts('110111'))
adder.debug('110111')

print("Input:",'11101111')
print("Accepted?", adder.accepts('11101111'))

adder.debug('11101111')
