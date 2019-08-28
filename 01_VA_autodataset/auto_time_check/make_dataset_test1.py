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
    
    out_dgraph.write('_:%s <name_of_object> "%s" .\n'%(name_obj, name_obj))
    out_dgraph.write('_:%s <likes> _:%s .\n'%(person, name_obj))
    
    
def print_person(pid):
    for oid in range(N_likes):
        if np.random.rand() < prob_likes:
            print_person_likes(pid, oid)            

    person = name_person(pid)        
    out_dgraph.write('_:%s <name_of_person>  "%s" .\n'%(person, person))

def print_reserv(reserv_id):
    n_reserv = np.random.randint(1, max_N_reserv + 1)
    pids = sorted(np.random.choice(range(N_persons), n_reserv, replace=False))
    rest = name_rest(np.random.randint(N_rest))
    reserv = name_reserv(reserv_id)
    
    rez_persons = " ".join(['(ConceptNode "%s")'%name_person(pid) for pid in pids])
    rez_as = '(EvaluationLink (PredicateNode "%s") (ListLink (ConceptNode "%s") %s))'% (reserv, rest, rez_persons)
    out_atomspace.write(rez_as + "\n")

    
    out_dgraph.write('_:%s <name_of_reservation> "%s" .\n'%(reserv, reserv))
    out_dgraph.write('_:%s <name_of_restaurant> "%s" .\n'%(reserv, rest))
    
    for pid in pids:
        out_dgraph.write('_:%s <participant> _:%s .\n'%(reserv, name_person(pid)))
            
#out_dgraph.write("{\n set { \n")    
    
for pid in range(N_persons):
    print_person(pid)

for reserv_id in range(N_reserv):
    print_reserv(reserv_id)

#out_dgraph.write("} \n } \n")    
