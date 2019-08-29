import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('N_reserv', type=int)
args = parser.parse_args()

# number of possible object that person could like
N_likes = 100

# probability of like each of objects
prob_likes = 0.1

N_persons = 10000

N_reserv = args.N_reserv
N_rest   = 100

# maximal number of persons in each of reservations
max_N_reserv = 5

out_atomspace = open("atomspace.scm", "w")
out_dgraph    = open("dgraph.txt", "w")

def name_person(pid):
    return "person-%06i"%pid

def name_rest(rest_id):
    return "restaurant-%06i"%rest_id

def name_likeobj(oid):
    return "obj-%06i"%oid

def name_reserv(reserv_id):
    return "reservation-%06i"%reserv_id

def print_person_likes(pid, oid):
    person = name_person(pid)
    name_obj = name_likeobj(oid)
    out_atomspace.write('(EvaluationLink (PredicateNode "Likes") (ListLink (ConceptNode "%s") (ConceptNode "%s")))\n'%(person, name_obj))
    
    elink    = "evlink_%s_%s"%(person, name_obj)
    listlink = "listlink_%s_%s"%(person, name_obj)
    cn_person = "ConceptNode_%s"%person
    cn_object = "ConceptNode_%s"%name_obj
    out_dgraph.write('_:%s <EvaluationLinkLink1> _:%s .\n'%(elink, "PredicateNode_Likes"))
    out_dgraph.write('_:%s <name_of_predicate> "%s" .\n'%("PredicateNode_Likes", "Likes"))
    out_dgraph.write('_:%s <EvaluationLinkLink2> _:%s .\n'%(elink, listlink))
    out_dgraph.write('_:%s <ListLinkLink1> _:%s .\n'%(listlink, cn_person))
    out_dgraph.write('_:%s <ListLinkLink2> _:%s .\n'%(listlink, cn_object))
    out_dgraph.write('_:%s <name_of_concept> "%s" .\n'%(cn_person, person))
    out_dgraph.write('_:%s <name_of_concept> "%s" .\n'%(cn_object, name_obj))
    
    
def print_person(pid):
    for oid in range(N_likes):
        if np.random.rand() < prob_likes:
            print_person_likes(pid, oid)            

    person = name_person(pid)        

def print_reserv(reserv_id):
    n_reserv = np.random.randint(1, max_N_reserv + 1)
    pids = sorted(np.random.choice(range(N_persons), n_reserv, replace=False))
    rest = name_rest(np.random.randint(N_rest))
    reserv = name_reserv(reserv_id)
    
    rez_persons = " ".join(['(ConceptNode "%s")'%name_person(pid) for pid in pids])
    rez_as = '(EvaluationLink (PredicateNode "%s") (ListLink (ConceptNode "%s") %s))'% (reserv, rest, rez_persons)
    out_atomspace.write(rez_as + "\n")

    
    elink    = "evlink_%s"%(reserv)
    listlink = "listlink_%s"%(reserv)
    setlink  = "setlink_%s"%(reserv)
    pnode = "PredicateNode_%s"%(reserv)
    cn_rest = "ConceptNode_%s"%rest
    
    
    out_dgraph.write('_:%s <EvaluationLinkLink1> _:%s .\n'%(elink, pnode))
    out_dgraph.write('_:%s <name_of_predicate> "%s" .\n'%(pnode, reserv))
    out_dgraph.write('_:%s <EvaluationLinkLink2> _:%s .\n'%(elink, listlink))
    out_dgraph.write('_:%s <ListLinkLink1> _:%s .\n'%(listlink, cn_rest))
    out_dgraph.write('_:%s <ListLinkLink2> _:%s .\n'%(listlink, setlink))
    out_dgraph.write('_:%s <name_of_concept> "%s" .\n'%(cn_rest, rest))
    for pid in pids:
        cn_person = "ConceptNode_%s"%name_person(pid)
        
        out_dgraph.write('_:%s <SetLinkLink> _:%s .\n'%(setlink, cn_person))
        out_dgraph.write('_:%s <name_of_concept> "%s" .\n'%(cn_person, name_person(pid)))
                    
    
for pid in range(N_persons):
    print_person(pid)

for reserv_id in range(N_reserv):
    print_reserv(reserv_id)

#out_dgraph.write("} \n } \n")    
