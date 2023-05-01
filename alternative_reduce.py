#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import glob
from datetime import datetime

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

paths = glob.glob('outputs/geoTwitter*.country')
results = {}

for path in paths:
        date_str = os.path.splitext(os.path.basename(path))[0][10:18]
        date = datetime.strptime(date_str, '%y-%m-%d')
        with open(path) as f:
            try:
                data = json.load(f)
                for key in args.key.split(','):
                    if key in data:
                        if date not in results:
                            results[date] = defaultdict(int)
                        results[date][key] += sum(data[key].values())
            except json.decoder.JSONDecodeError:
                print(f"Skipping invalid JSON file: {path}")
results = dict(sorted(results.items()))
print("results=", results)
keys = set()

for date, data in results.items():
    keys.update(data.keys())
keys = list(keys)
for key in keys:
    x = [date.date() for date in results.keys()]
    y = [results[date][key] for date in results.keys()]
    plt.plot(x,y,label = key)


plt.xlabel("Date in 2020")
plt.ylabel("Times Mentioned in Tweets")
plt.title("Times a Hastag was mentioned in Tweets by day in 2020")
plt.legend()
plt.savefig("sickvhospital_tweet.png")
plt.show()
