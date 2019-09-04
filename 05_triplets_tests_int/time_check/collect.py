import glob
import re
import os

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('prefix', type=str)
args = parser.parse_args()



def collect(prefix):    
    f = glob.glob("%s_*.txt"%(prefix))
    d = {}
    for f in glob.glob("%s_*.txt"%(prefix)):
        m = re.search('%s_(\d+).txt'%(prefix), f)
        if (m == None):
            continue
        N = m.group(1)
        x = os.popen("cat %s |tail -1"%f).read().split()
        rez1 = x[1]
        d[int(N)] = rez1
    for N in sorted(d.keys()):
        print(N, d[N])
        
collect(args.prefix)
