
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
		     (EvaluationLink
		        (Predicate "Participant")
		        (ListLink
		 	   (Variable "$reservation")
			   (Variable "$person")))
		     (EvaluationLink
		            (PredicateNode "Likes")
		            (ListLink
				(VariableNode "$person")
				(ConceptNode "obj-000005"))))
		(ListLink (VariableNode "$reservation") (VariableNode "$person"))))


