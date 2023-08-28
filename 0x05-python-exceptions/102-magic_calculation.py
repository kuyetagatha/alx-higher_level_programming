#!/usr/bin/python3

def magic_calculation(a, b):
result = 0
for i range(1, 3):
try:
if i > a:
raise Exceptin('Too far')
else:
result += a ** b/i
except Exception:
result = b + a
break
return (result)
