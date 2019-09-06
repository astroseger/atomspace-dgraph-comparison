## Experiment

The same as in [02_VA_withmemberlinks](../02_VA_withmemberlinks/), but with inverse member link. See results in [02.v3_VA_withmemberlinks_predicate](../02.v3_VA_withmemberlinks_predicate/).

### Dataset

The same small sample dataset as in [01_VA_autodataset](../01_VA_autodataset)  will look like this (MemberLinks are inverted in comparison to [02_VA_withmemberlinks](../02_VA_withmemberlinks/)):

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

(EvaluationLink (PredicateNode "Reservation")
   (ListLink
        (ConceptNode "reservation-000000")
        (ConceptNode "restaurant-000000")))
(MemberLink (ConceptNode "person-000000") (ConceptNode "reservation-000000"))
(MemberLink (ConceptNode "person-000001") (ConceptNode "reservation-000000"))
(MemberLink (ConceptNode "person-000002") (ConceptNode "reservation-000000"))
(MemberLink (ConceptNode "person-000003") (ConceptNode "reservation-000000"))
(MemberLink (ConceptNode "person-000004") (ConceptNode "reservation-000000"))
```

