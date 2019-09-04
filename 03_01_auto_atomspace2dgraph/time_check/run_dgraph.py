import time
import os

N = 5
t1 = time.time()
for i in range(N):
    t11 = time.time()
    os.system("bash ../dgraph_req_1.sh >/dev/null 2>/dev/null")
    print(time.time() - t11)
rez = (time.time() - t1) / N
print("reqs1 ", (time.time() - t1) / N)


