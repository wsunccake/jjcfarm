#!/usr/bin/env python 

def change(arg1, arg2): 
    print "arg1: ", arg1, "arg2: ", arg2 
    (arg1, arg2) = (arg2 ,arg1) 
    print "arg1: ", arg1, "arg2: ", arg2 
    return (arg1, arg2) 

if __name__ == "__main__": 
    import sys 
    import getopt 

    for a in sys.argv: 
        print a 

    def usage(): 
        print "Usage: swap -a 'A' -b 'b'" 
        print "-h: help" 

    try: 
        opt_list, args = getopt.getopt(sys.argv[1:], 'a:b:hv') 
     
    except getopt.GetoptError, err: 
        print str(err) 
        usage() 
        sys.exit(2) 

    Aarg_flag = False 
    Barg_flag = False 
    help_flag = False 
    verbose_flag = False 

    for o, a in opt_list: 
        if o in ('-a'): 
            Aarg_flag = True 
            Aarg = a 
        elif o in ("-b"): 
            Barg_flag = True 
            Barg = a 
        elif o in ("-v"): 
            verbose_flag = True 
        elif o in ("-h"): 
            help_flag = True 

    if help_flag or not Aarg_flag or not Barg_flag: 
        usage() 
        sys.exit(2) 

    if verbose_flag: print ("Initial: Aarg: %s, Barg: %s" %(Aarg, Barg)) 
    change(Aarg, Barg) 
    if verbose_flag: print ("Final: Aarg: %s, Barg: %s" %(Aarg, Barg))