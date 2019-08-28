curl localhost:8080/query -XPOST -d '
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

'

