export GUILE_AUTO_COMPILE=0

for N in 400 600 800
do
python make_dataset.py $N
bash load_dgraph.sh
cd time_check
python run_dgraph_50x50_p8.py > dgraph_p8_${N}.txt
python run_dgraph_50x50_p9.py > dgraph_p9_${N}.txt
cd ..
done
