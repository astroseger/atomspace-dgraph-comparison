from opencog.type_constructors import *                            
from opencog.utilities import initialize_opencog
from opencog.bindlink import execute_atom
from opencog.atomspace import TruthValue
from opencog.scheme_wrapper import scheme_eval      
atomspace = AtomSpace()

scheme_eval(atomspace, '(load "../atomspace.scm")') 
scheme_eval(atomspace, '(use-modules (opencog exec))')             


rez1 = scheme_eval(atomspace, '(load "../atomspace_reqs_1_bind.lisp")')      

f1 = open("atomspace_reqs_1_rez.txt", 'wb')
f1.write(rez1)


rez2 = scheme_eval(atomspace, '(load "../atomspace_reqs_2_bind.lisp")') 
f2 = open("atomspace_reqs_2_rez.txt", 'wb')
f2.write(rez2)
