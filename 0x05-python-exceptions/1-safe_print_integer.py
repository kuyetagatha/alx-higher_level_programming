#!/usr/bin/python3

def safe_print_integer(value):
try:
prnt("{:d}".format(value))
return (True)
except (TypeError, ValueError):
return (False)
