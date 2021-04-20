#!/usr/bin/env python3

import sys, json, yaml

mode = sys.argv[1]

impls = yaml.safe_load(open("impls.yml"))

print("::set-output name=matrix::{\"IMPL\":%s}" % json.dumps(impls[mode]))
