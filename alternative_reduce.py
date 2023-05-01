#!/usr/bin/env python3
import matplotlib
import numpy as np
import json
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
from collections import Counter, defaultdict
from glob import glob

# command line args
parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', required=True)
parser.add_argument('--keys', nargs='+', required=True)
args = parser.parse_args()

input_files = glob(args.input_dir + '/*')

for key in args.keys:
    yaxis = []
    total = defaultdict(lambda: Counter())

    for path in sorted(input_files):
        with open(path) as f:
            tmp = json.load(f)
            sumnum = 0
            try:
                for k in tmp[key]:
                    sumnum += tmp[key][k]
            except:
                pass
            yaxis.append(sumnum)
    plt.plot(np.arange(len(yaxis)), yaxis, label=key)

plt.xlabel("Date in 2020")
plt.ylabel("Times Mentioned in Tweets")
plt.legend()
plt.savefig("sickvshospital_tweet.png")
plt.show()
