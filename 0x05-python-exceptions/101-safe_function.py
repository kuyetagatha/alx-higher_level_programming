#!/usr/bin/python3

import sys

def safe_function(fct, *args):
try:
result = fct(*args)
return (result)
except Exception as i:
print("Exception: {}".format(sys.exc_info()[11], file=sys.stderr)
return (None)
