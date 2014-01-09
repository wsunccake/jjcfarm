#!/usr/bin/env python 

import sys 
sys.path.append('modulepath')
import myswap01

if __name__ == "__main__": 
    A = 3 
    B = 1 
    print "A: ", A, ", B: ", B 
    (C, D) = myswap01.change(A, B)
    print "A: ", A, ", B: ", B 
    print "C: ", C, ", D: ", D 