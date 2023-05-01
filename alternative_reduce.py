#!/usr/bin/env python3
import argparse
import json
from collections import Counter, defaultdict
from glob import glob

import matplotlib
import numpy as np
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main(args):
    input_files = glob(args.input_dir + '/*')
    for key in args.keys:
        yaxis = []
        total = defaultdict(lambda: Counter())

        for path in sorted(input_files):
            with open(path) as f:
                tmp = json.load(f)
                num = 0
                try:
                    for k in tmp[key]:
                        num += tmp[key][k]
                except:
                    pass
                yaxis.append(num)
        plt.plot(np.arrange(len(yaxis)), yaxis, label=key)

plt.xlabel("Date in 2020")
plt.ylabel("Times Mentioned in Tweets")
plt.legend()
plt.xticks([0, 60, 121, 182, 244, 305], ["Jan", "Mar", "May", "Jul", "Sept", "Nov"])
plt.savefig("sickvshospital_tweet.png")
