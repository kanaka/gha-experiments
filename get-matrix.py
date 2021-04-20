#!/usr/bin/env python3

import json, yaml

impls = yaml.safe_load(open("impls.yml"))

print("::set-output name=linux::{\"IMPL\":%s}" % json.dumps(impls[linux]))
print("::set-output name=osx::{\"IMPL\":%s}" % json.dumps(impls[osx]))
