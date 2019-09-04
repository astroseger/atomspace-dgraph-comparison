


print("{")
for p in range(50):
    for s in range(50):
        name_func = "name%i_%i"%(p,s)
        name_subject   = "subject-%06i"%(s)
        name_predicate = "predicate-%06i"%(p)
        print(
"""
name_%s(func: eq(name_of_concept, %i)) @cascade {  
~ListLinkLink1
{
~EvaluationLinkLink2
{
EvaluationLinkLink1 @filter (eq(name_of_predicate, %i))
}
ListLinkLink2{
uid
}

}}
"""%(name_func, s, p))
print("}")
				   
