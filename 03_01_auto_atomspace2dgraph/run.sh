export GUILE_AUTO_COMPILE=0

for N in 10000 50000 100000 200000 400000 800000 1000000
do
python make_dataset.py $N
bash load_dgraph.sh
cd time_check
python run_atomspace.py > atomspace_${N}.txt
python run_dgraph.py > dgraph_${N}.txt
cd ..
done
