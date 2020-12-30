import bisect
import collections
import fractions
import heapq
import itertools
import math
import os
import pprint
import shutil
import sys
import urllib.request
from functools import lru_cache, reduce
from operator import mul

import requests


def mkdir(contest_id):
    path = os.path.dirname(os.path.abspath(__file__)) + "/problems/" + contest_id
    if not os.path.exists(path):
        os.mkdir(path)

def mkfile(contest_id, problem_id):
    path = os.path.dirname(os.path.abspath(__file__)) + "/problems/" + contest_id + "/" + problem_id + ".py"
    if not os.path.exists(path):
        f = open(path, 'w')
        f.write('')
        f.close()

def main():
    contest_url = "https://kenkoooo.com/atcoder/resources/contest-problem.json"
    res = requests.get(contest_url)
    for contest in res.json():
        mkdir(contest["contest_id"])
        #mkfile(contest["contest_id"], contest["problem_id"])


if __name__ == '__main__':
    main()
