curl localhost:8080/query -XPOST -d '
{
var(func: eq(name_of_concept, "obj-000005")) @cascade {  
~ListLinkLink2
{
~EvaluationLinkLink2
{
EvaluationLinkLink1 @filter (eq(name_of_predicate, "Likes"))
}
ListLinkLink1{
likes5 as uid
}

}
}
name2(func: eq(name_of_concept, "restaurant-000002")) @cascade
{

~ListLinkLink1
{
ListLinkLink2
{
SetLinkLink @filter (uid(likes5))
}
~EvaluationLinkLink2
{
EvaluationLinkLink1
{
name_of_predicate
}
}
}
}
}
' 
#| python -m json.tool | less
				   
