

; two guy who both likes obj-000005 in the same restaurant

(cog-execute! (BindLink (VariableList  
			  (TypedVariable 
			     (Variable "$x_reserv") 
			     (TypeNode "ConceptNode"))			  
			  (TypedVariable 
			     (Variable "$x_rest") 
			     (TypeNode "ConceptNode"))			  
			  (TypedVariable 
			     (Variable "$xp1") 
			     (TypeNode "ConceptNode"))			  
			  (TypedVariable 
			     (Variable "$xp2") 
			     (TypeNode "ConceptNode")))
	    (AndLink
		    (EvaluationLink
		       (PredicateNode "Reservation")
		        (ListLink
			  (Variable "$x_reserv")
			  (Variable "$x_rest")))
		    (EvaluationLink
		       (PredicateNode "Participant")
		        (ListLink
			  (Variable "$x_reserv")
			  (Variable "$xp1")))
		    (EvaluationLink
		       (PredicateNode "Participant")
		        (ListLink
			  (Variable "$x_reserv")
			  (Variable "$xp2")))	       
		    (EvaluationLink
		       (PredicateNode "Likes")
		        (ListLink
			  (VariableNode "$xp1")
			  (ConceptNode "obj-000005")))
		    (EvaluationLink
		       (PredicateNode "Likes")
		        (ListLink
			  (VariableNode "$xp2")
			  (ConceptNode "obj-000005")))
                    (NotLink (Identical (Variable "$xp1") (Variable "$xp2"))))
            (ListLink (VariableNode "$x_reserv") (VariableNode "$xp1") (VariableNode "$xp2"))))
