export GUILE_AUTO_COMPILE=0

for N in 600
do
python make_dataset.py $N
bash load_dgraph.sh
cd time_check
python run_atomspace.py > atomspace_${N}.txt
python run_dgraph_50x50.py > dgraph_${N}.txt
python run_dgraph_50x50_p7.py > dgraph_p7_${N}.txt
cd ..
done
