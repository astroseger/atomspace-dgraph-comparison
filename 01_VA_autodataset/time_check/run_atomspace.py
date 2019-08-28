from opencog.type_constructors import *                            
from opencog.utilities import initialize_opencog
from opencog.bindlink import execute_atom
from opencog.atomspace import TruthValue
from opencog.scheme_wrapper import scheme_eval      
import time
atomspace = AtomSpace()

scheme_eval(atomspace, '(load "../atomspace.scm")') 
scheme_eval(atomspace, '(use-modules (opencog exec))')             


N = 5
t1 = time.time()
for i in range(N):
    t11 = time.time()
    rez1 = scheme_eval(atomspace, '(load "../atomspace_reqs_1_bind.lisp")')
    print(time.time() - t11)
rez = (time.time() - t1) / N
print("reqs1 ", (time.time() - t1) / N)


t1 = time.time()
for i in range(N):
    t11 = time.time()
    rez1 = scheme_eval(atomspace, '(load "../atomspace_reqs_2_bind.lisp")') 
    print(time.time() - t11)
rez = (time.time() - t1) / N
print("reqs2 ", (time.time() - t1) / N)

