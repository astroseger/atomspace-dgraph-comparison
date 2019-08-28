curl localhost:8080/query -XPOST -d '

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

' 
#| python -m json.tool | less
				   
