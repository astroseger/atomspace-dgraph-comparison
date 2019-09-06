
; one guy who likes obj-000005 and made reservation in restaurant-00002

(cog-execute! (BindLink (VariableList  
			  (TypedVariable 
			     (Variable "$reservation") 
			     (TypeNode "ConceptNode"))			  
			  (TypedVariable 
			     (Variable "$person") 
			     (TypeNode "ConceptNode")))
		(AndLink
		     (EvaluationLink
		        (Predicate "Reservation")
		        (ListLink
		 	   (Variable "$reservation")
			   (ConceptNode "restaurant-000002")))
		     (MemberLink (Variable "$person") (Variable "$reservation"))
		     (EvaluationLink
		            (PredicateNode "Likes")
		            (ListLink
				(VariableNode "$person")
				(ConceptNode "obj-000005"))))
		(ListLink (VariableNode "$reservation") (VariableNode "$person"))))


