


print("{")
for p in range(50):
    for s in range(50):
        name_func = "name%i_%i"%(p,s)
        name_subject   = "subject-%06i"%(s)
        name_predicate = "predicate-%06i"%(p)
        print(
"""
name_%s(func: eq(name_of_predicate, %i)) @cascade { 
~EvaluationLinkLink1
{
EvaluationLinkLink2
{
ListLinkLink1 @filter (eq(name_of_concept, %i))
ListLinkLink2
{
name_of_concept}}}}
"""%(name_func, p,s))
print("}")
				   
