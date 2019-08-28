## Motivations of this experiment

The general target of this study is to assess the possibility of using DGraph in Opencog as a part of the episodic memory.
This particular experiment is a first step in which we generate relatively simply dataset for the comparison of the performance of dgraph and atomspace for different queries.

### Dataset

In this dataset we have set of people who like different objects. We have different restaurants and we have set of reservations in these restaurants.
The sample dataset in atomspace looks like this
```scheme
(EvaluationLink (PredicateNode "Likes") 
   (ListLink 
        (ConceptNode "person-000000") 
        (ConceptNode "obj-000000")))
(EvaluationLink (PredicateNode "Likes") 
   (ListLink 
        (ConceptNode "person-000001") 
        (ConceptNode "obj-000001")))
(EvaluationLink (PredicateNode "Likes") 
   (ListLink 
        (ConceptNode "person-000002") 
        (ConceptNode "obj-000003")))
(EvaluationLink (PredicateNode "Likes") 
   (ListLink 
        (ConceptNode "person-000004") 
        (ConceptNode "obj-000000")))
(EvaluationLink (PredicateNode "reservation-000000") 
    (ListLink 
         (ConceptNode "restaurant-000000") 
         (ConceptNode "person-000003")))
(EvaluationLink (PredicateNode "reservation-000001") 
    (ListLink 
         (ConceptNode "restaurant-000001") 
         (ConceptNode "person-000000") 
         (ConceptNode "person-000001") 
         (ConceptNode "person-000002") 
         (ConceptNode "person-000003") 
         (ConceptNode "person-000004")))
``` 

We assume that list of people is sorted in the reservation, however it will not be important here.

In dgraph we use the following schema

```
<likes>: uid @reverse .
<name_of_object>: string @index(hash) .
<name_of_person>: string @index(hash) .
<name_of_reservation>: string @index(hash) .
<name_of_restaurant>: string @index(hash) .
<participant>: uid @reverse .
``` 

and out sample dataset will look as following:

```
_:obj-000000 <name_of_object> "obj-000000" .
_:person-000000 <likes> _:obj-000000 .
_:person-000000 <name_of_person>  "person-000000" .
_:obj-000001 <name_of_object> "obj-000001" .
_:person-000001 <likes> _:obj-000001 .
_:person-000001 <name_of_person>  "person-000001" .
_:obj-000003 <name_of_object> "obj-000003" .
_:person-000002 <likes> _:obj-000003 .
_:person-000002 <name_of_person>  "person-000002" .
_:person-000003 <name_of_person>  "person-000003" .
_:obj-000000 <name_of_object> "obj-000000" .
_:person-000004 <likes> _:obj-000000 .
_:person-000004 <name_of_person>  "person-000004" .
_:reservation-000000 <name_of_reservation> "reservation-000000" .
_:reservation-000000 <name_of_restaurant> "restaurant-000000" .
_:reservation-000000 <participant> _:person-000003 .
_:reservation-000001 <name_of_reservation> "reservation-000001" .
_:reservation-000001 <name_of_restaurant> "restaurant-000001" .
_:reservation-000001 <participant> _:person-000000 .
_:reservation-000001 <participant> _:person-000001 .
_:reservation-000001 <participant> _:person-000002 .
_:reservation-000001 <participant> _:person-000003 .
_:reservation-000001 <participant> _:person-000004 .
```

### Queries and the comparison of speed

We will consider two queries here:

1. Find all reservations for restaurant X with person who likes Y
2. Find all reservations with at least two persons who likes X.

#### Query 1 (restaurant X with person who likes Y)

In dgraph we should explicitly specify how we make graph traversal. So there are at least two variants:

variant-1 we start from the given restaurant 
```
{
name(func: eq(name_of_restaurant,"restaurant-000002")) @cascade {
   name_of_reservation
   name_of_restaurant
   participant {
     name_of_person
     likes @filter (eq (name_of_object, "obj-000005"))
     }
   }
}

```

variant-2 we start from the given object
```
name(func: eq(name_of_object, "obj-000005")) @cascade {
   ~likes {
     name_of_person
     ~participant @filter (eq (name_of_restaurant, "restaurant-000002")) {
         name_of_reservation  
         name_of_restaurant
         }     
     }
   }
}
```
 
Which variant is faster depends on relative number of different records in dataset.

Query in atomspace was as following: [atomspace_reqs_1_bind.lisp](atomspace_reqs_1_bind.lisp)

#### Query-2 (reservations with two persons who like given object)

query in dgraph:
```
{
var(func: eq(name_of_object,"obj-000005"))
{
  person_likes_obj as ~likes
  {
   good_reservations as ~participant
    {
      num_count as count(participant @filter (uid(person_likes_obj)))
    }
 }
}
name2(func: uid(good_reservations)) @filter(ge(val(num_count), 2))
    {
      name_of_reservation
      count(participant @filter (uid(person_likes_obj)))
    }
  
}
```

query in atomspace [atomspace_reqs_2_bind.lisp](atomspace_reqs_2_bind.lisp)

You can see that queries in dgrapn and atomspace are very different.  
In dgraph we simply count the number of participant who likes given object for each of reservation.

###Comparison of the execution time

In order to compare execution time we've generated different datasets with fixed number of objects and persons but with different number of reservations. We wanted to see how execution time depends on number of reservations.

results for query-1
[results-query-1]()

results for query-2
[results-query-2]()

You can see that time for query-1 is linear for both atomspace and dgraph (for dgraph time is given for variant-1, for variant-2 time would be smaller). For query-2 dgraph is linear but for atomspace is O(N^2).  

### Discussion

* For this particular task we can successfully represent data in both atomspace and dgraph. 
* In dgraph we have much more control how exactly we traverse graph. However it is a disadvantage, because in query-1 atomspace manage to choose optimal traverse, however it might not be a case in the general case
* It is not clear how automatically translate request from atomspace to dgraph

