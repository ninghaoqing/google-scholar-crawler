#!/usr/bin/python3
   
import re 
line = 'A B,C D - E  …  F'

temp=re.split(r'[\u2026],-',line)
print(temp)
print('\u2026')