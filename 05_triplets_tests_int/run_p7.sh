export GUILE_AUTO_COMPILE=0

for N in 50 100 200 400 600 800 1000
do
python make_dataset.py $N
bash load_dgraph.sh
cd time_check
python run_atomspace_50x50.py > atomspace_${N}.txt
python run_dgraph_50x50_p7.py > dgraph_p7_${N}.txt
cd ..
done
