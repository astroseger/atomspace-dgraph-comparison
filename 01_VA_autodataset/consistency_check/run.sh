bash ../dgraph_req_1.sh  |grep name_of_reservation > dgrap_req_1_rez.txt
bash ../dgraph_req_2.sh  |grep name_of_reservation > dgrap_req_2_rez.txt
python run_atomspace.py
