import requests
import collections
import csv


contest_url = "https://kenkoooo.com/atcoder/resources/lang.json"
res = requests.get(contest_url)
d = collections.defaultdict(int)

for j in res.json():
    d[j["language"]] += j["count"]

with open("language_cnt.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sorted(d.items(), key=lambda x: x[1], reverse=True))
    f.close()
