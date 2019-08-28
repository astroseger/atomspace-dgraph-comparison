curl localhost:8080/query -XPOST -d '
{
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
' 
#| python -m json.tool | less
				   
