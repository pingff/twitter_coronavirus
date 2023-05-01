#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', required=True)
parser.add_argument('--keys', nargs='+', required=True)
args = parser.parse_args()

# imports
import json
from collections import Counter, defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from glob import glob

input = glob(args.input_dir + '/*')

for key in args.keys:
    yaxis = []
    total = defaultdict(lambda: Counter())
    
    for path in sorted(input):
        with open(path) as f:
            tmp = json.load(f)
            sumnum = 0
            try:
                for k in tmp[key]:
                    sumnum += tmp[key][k]
            except KeyError:
                pass
            yaxis.append(sumnum)

    plt.plot(np.arange(len(yaxis)), yaxis, label=key)

plt.xlabel("Date in 2020")
plt.ylabel("Times Mentioned in Tweets")
plt.title("Times a Hastag was mentioned in Tweets by day in 2020")
plt.legend()
plt.xticks([0, 60, 121, 182, 244, 305], ["Jan", "Mar", "May", "Jul", "Sept", "Nov"])
plt.savefig("sickvhospital_tweet.png")
