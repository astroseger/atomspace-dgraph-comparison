curl -X POST localhost:8080/alter -d '{"drop_all": true}'
rm -f ~/dgraph/dgraph.txt ~/dgraph/dgraph_schema.txt
cp  dgraph.txt ~/dgraph/
cp  dgraph_schema.txt ~/dgraph/
docker exec -it dgraph dgraph live -r dgraph.txt -s dgraph_schema.txt --zero localhost:5080 -c 1

#curl localhost:8080/alter -XPOST --data-binary "@dgraph_schema.txt" 
#curl localhost:8080/mutate -XPOST -H 'X-Dgraph-CommitNow: true' --data-binary "@dgraph.txt"
