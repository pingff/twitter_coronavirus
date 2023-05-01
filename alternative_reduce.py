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


for key in args.keys:
    yaxis = []
    total = defaultdict(lambda: Counter())

    for path in sorted(glob(args.input_dir + '/*')):
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
plt.title("Times a Hastag was mentioned in Tweets by day in 2020")
plt.legend()
plt.xticks([0, 60, 121, 182, 244, 305], ["Jan", "Mar", "May", "Jul", "Sept", "Nov"])
plt.savefig("sickvshospital_tweet.png")
plt.show()
