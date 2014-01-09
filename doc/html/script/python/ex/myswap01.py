#!/usr/bin/env python 

def change(arg1, arg2):
    print "arg1: ", arg1, "arg2: ", arg2 
    (arg1, arg2) = (arg2 ,arg1) 
    print "arg1: ", arg1, "arg2: ", arg2 
    return (arg1, arg2)

if __name__ == "__main__":
    change("A", "B") 