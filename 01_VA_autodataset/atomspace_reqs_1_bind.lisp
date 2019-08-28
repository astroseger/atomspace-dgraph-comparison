
; one guy who likes obj-000005 and made reservation in restaurant-00002

(cog-execute! (BindLink (VariableList  
			  (TypedVariable 
			     (Variable "$x1") 
			     (TypeNode "PredicateNode"))			  
			  (TypedVariable 
			     (Variable "$x2") 
			     (TypeNode "ConceptNode"))			  
			  (TypedVariable
			     (Glob   "$star1")
			     (TypeSet
				(Interval 
				   ( Number  0)
				   (Number  -1 ))
				(Type "ConceptNode")))
			  (TypedVariable
			     (Glob   "$star2")
			     (TypeSet
				(Interval 
				   ( Number  0)
				   (Number  -1 ))
				(Type "ConceptNode")))
			  )
		 (AndLink
		    ( EvaluationLink
		       (Variable "$x1")
		       (ListLink
			  (ConceptNode "restaurant-000002")
			  (GlobNode "$star1")
			  (VariableNode "$x2")
			  (GlobNode "$star2")
			  )
		       )
		    (EvaluationLink
		             (PredicateNode "Likes")
		             (ListLink
				(VariableNode "$x2")
				(ConceptNode "obj-000005")
				)
		          )
		    
		    )

		  (ListLink (VariableNode "$x1") (VariableNode "$x2"))
		 )
   
   )


