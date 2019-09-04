import time
import os


N = 5

def run(prefix):
    print("run dgraph_req_50x50%s"%prefix)
    t1 = time.time()
    for i in range(N):
        t11 = time.time()
        os.system("cd ..; curl localhost:8080/query -XPOST --data-binary @dgraph_req_50x50%s.txt >/dev/null 2>/dev/null"%prefix)
        print(time.time() - t11)
    rez = (time.time() - t1) / N
    print("rez ", (time.time() - t1) / N)
    
run("")

