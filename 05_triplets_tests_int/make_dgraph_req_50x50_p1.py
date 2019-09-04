


print("{")
for p in range(50):
    for s in range(50):
        name_func = "name%i_%i"%(p,s)
        name_subject   = "subject-%06i"%(s)
        name_predicate = "predicate-%06i"%(p)
        print(
"""
name_%s(func: eq(name_of_concept, %i)) @cascade {  
uid
}
"""%(name_func, s))
print("}")
				   
