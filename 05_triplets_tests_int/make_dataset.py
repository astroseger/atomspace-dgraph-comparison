import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('N', type=int)
args = parser.parse_args()

N_objects = args.N

N_subjects = args.N

N_pred = args.N // 2

N_eval_for_subject = args.N // 4

out_dgraph    = open("dgraph.txt", "w")

def generate_triplets_for_subject(subject_id):
    triplets = set()
    while(len(triplets) < N_eval_for_subject):
        s = subject_id
        p = np.random.randint(N_pred)
        o = np.random.randint(N_objects)
        triplets.add((s,p,o))
    return triplets

def generate_triplets():
    triplets = []
    for subject_id in range(N_subjects):
        triplets += list(generate_triplets_for_subject(subject_id))
    return triplets


def write_triplets(triplets):
    out_atomspace = open("atomspace.scm", "w")
    out_dgraph    = open("dgraph.txt", "w")
    for s,p,o in triplets:
        name_subject   = "subject-%06i"%(s)
        name_predicate = "predicate-%06i"%(p)
        name_object    = "object-%06i"%(o)
        out_atomspace.write('(EvaluationLink (PredicateNode "%s") (ListLink (ConceptNode "%s") (ConceptNode "%s")))\n'%(name_predicate, name_subject, name_object))
        
        elink      = "evlink_s%i_p%i_o%i"%(s,p,o)
        listlink   = "listlink_s%i_o%i"%(s,o)
        pn         = "PredicateNode_%s"%name_predicate
        cn_subject = "ConceptNode_%s"%name_subject
        cn_object  = "ConceptNode_%s"%name_object
        out_dgraph.write('_:%s <EvaluationLinkLink1> _:%s .\n'%(elink, pn))
        out_dgraph.write('_:%s <name_of_predicate> "%i" .\n'%(pn, p))
        out_dgraph.write('_:%s <EvaluationLinkLink2> _:%s .\n'%(elink, listlink))
        out_dgraph.write('_:%s <ListLinkLink1> _:%s .\n'%(listlink, cn_subject))
        out_dgraph.write('_:%s <ListLinkLink2> _:%s .\n'%(listlink, cn_object))
        out_dgraph.write('_:%s <name_of_concept> "%i" .\n'%(cn_subject, s))
        out_dgraph.write('_:%s <name_of_concept> "%i" .\n'%(cn_object,  o))

        
triplets = generate_triplets()
write_triplets(triplets)

        

