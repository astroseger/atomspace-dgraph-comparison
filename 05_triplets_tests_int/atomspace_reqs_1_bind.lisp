
; one guy who likes obj-000005 and made reservation in restaurant-00002

(cog-execute! (BindLink (VariableList  
			  (TypedVariable 
			     (Variable "$x") 
			     (TypeNode "ConceptNode"))			  
			  )
		    ( EvaluationLink
		       (PredicateNode "predicate-000000")
		       (ListLink
			  (ConceptNode "subject-000000")
			  (VariableNode "$x")
			  )
		       )
		  (VariableNode "$x"))
		 )


