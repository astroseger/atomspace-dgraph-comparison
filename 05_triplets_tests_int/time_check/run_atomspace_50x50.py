from opencog.type_constructors import *                            
from opencog.utilities import initialize_opencog
from opencog.bindlink import execute_atom
from opencog.atomspace import TruthValue
from opencog.scheme_wrapper import scheme_eval      
import time
atomspace = AtomSpace()

scheme_eval(atomspace, '(load "../atomspace.scm")') 
scheme_eval(atomspace, '(use-modules (opencog exec))')             

def exec_50x50():
    for p in range(50):
        for s in range(50):
            name_subject   = "subject-%06i"%(s)
            name_predicate = "predicate-%06i"%(p)
                                        
            req = '''
            (cog-execute! (BindLink (VariableList
            (TypedVariable
            (Variable "$x")
            (TypeNode "ConceptNode"))
            )
            ( EvaluationLink
            (PredicateNode "%s")
            (ListLink
            (ConceptNode "%s")
            (VariableNode "$x")
            )
            )
            (VariableNode "$x"))
            )'''%(name_predicate, name_subject)
            rez = scheme_eval(atomspace, req)
N = 5
t1 = time.time()
for i in range(N):
    t11 = time.time()
    exec_50x50()
    print(time.time() - t11)
rez = (time.time() - t1) / N
print("reqs1 ", (time.time() - t1) / N)


