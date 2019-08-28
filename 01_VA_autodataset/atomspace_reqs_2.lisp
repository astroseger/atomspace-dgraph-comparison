

; two guy who both likes obj-000005 in the same restaurant

(cog-execute! (GetLink (VariableList  
			  (TypedVariable 
			     (Variable "$x_reserv") 
			     (TypeNode "PredicateNode"))			  
			  (TypedVariable 
			     (Variable "$x_rest") 
			     (TypeNode "ConceptNode"))			  
			  (TypedVariable 
			     (Variable "$xp1") 
			     (TypeNode "ConceptNode"))			  
			  (TypedVariable 
			     (Variable "$xp2") 
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
			  (TypedVariable
			     (Glob   "$star3")
			     (TypeSet
				(Interval 
				   ( Number  0)
				   (Number  -1 ))
				(Type "ConceptNode"))
			     )
			  )
			  
		 (AndLink
		    ( EvaluationLink
		       (Variable "$x_reserv")
		       (ListLink
			  (Variable "$x_rest")
			  (GlobNode "$star1")
			  (VariableNode "$xp1")
			  (GlobNode "$star2")
			  (VariableNode "$xp2")
			  (GlobNode "$star3")
			  )
		       )
		    (EvaluationLink
		             (PredicateNode "Likes")
		             (ListLink
				(VariableNode "$xp1")
				(ConceptNode "obj-000005")
				)
			       )
		    (EvaluationLink
		       (PredicateNode "Likes")
		       (ListLink
			  (VariableNode "$xp2")
			  (ConceptNode "obj-000005")
			  )
		       )

		    
		    )
		 
		 )


)
