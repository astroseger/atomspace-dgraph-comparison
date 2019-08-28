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
        N = re.search('(\d+)', f).group(0)
        x = os.popen("cat %s |grep req"%f).read().split()
        rez1 = x[1]
        rez2 = x[3]
        d[int(N)] = (rez1, rez2)
    for N in sorted(d.keys()):
        print(N, *d[N])
        
collect(args.prefix)
