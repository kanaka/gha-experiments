#!/usr/bin/env python3

import json
import re
import sys
import yaml

RE_IGNORE = re.compile(r'(^LICENSE$|^README.md$|^docs/|^process/)')
RE_IMPL = re.compile(r'^impls/(?!lib|tests)([^/]*)/')

def impl_text(impl):
    s = "IMPL=%s" % impl['IMPL']
    for k, v in impl.items():
        if k == 'IMPL': continue
        s += " %s=%s" % (k, v)
    return s

all_changes = sys.argv[1:]
# code changes that are not just to docs
code_changes = set([c for c in all_changes if not RE_IGNORE.search(c)])
# actual changes to implementations
impl_changes = set([c for c in all_changes if RE_IMPL.search(c)])
# names of changed implementations
changed_impls = set([RE_IMPL.search(c).groups()[0] for c in impl_changes])

# If we have non-implementation code changes then we will add all
# implementations to the test matrix
do_full = (len(code_changes) != len(impl_changes))

print("code_changes: %s (%d)" % (code_changes, len(code_changes)))
print("impl_changes: %s (%d)" % (impl_changes, len(impl_changes)))
print("changed_impls: %s (%d)" % (changed_impls, len(changed_impls)))
print("do_full: %s" % do_full)

# Load the full implementation description file
all_impls = yaml.safe_load(open("impls.yml"))

# Accumulate and output linux and macos implementations separately
linux_impls = []
macos_impls = []
for impl in all_impls['IMPL']:
    if do_full or impl['IMPL'] in changed_impls:
        if 'OS' in impl and impl['OS'] == 'macos':
            macos_impls.append(impl_text(impl))
        else:
            linux_impls.append(impl_text(impl))

print("::set-output name=linux::{\"IMPL\":%s}" % json.dumps(linux_impls))
print("::set-output name=macos::{\"IMPL\":%s}" % json.dumps(macos_impls))
