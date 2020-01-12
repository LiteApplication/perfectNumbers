#!/usr/bin/python3

import os
import sys
import time

import number
import performances
try:
    input = raw_input
except:
    pass

log = performances.logger(debug=True, show_ram_time=True)
d = log.debug
p = log.log
if len(sys.argv) == 1:
    go = True
    while go:
        try:
            MIN = int(input("MIN = "))
            MAX = int(input("MAX = "))
            go = False
        except:
            p("Error, please enter an integer :")
    del(go)
elif len(sys.argv) < 3:
    d("Not enough args")
    p("SYNTAXE :")
    p("  main.py <min (!= 0)> <max (> min)>")
    p("Search all perfect number in the range. ")
    exit(1)
else:
    d("Parsing args...")
    try:
        MIN = int(sys.argv[1])
        MAX = int(sys.argv[2])
    except Exception as e:
        p("Error while parsing args : " + str(e))
        exit(1)


if MIN == 0:
    p("Error : MIN cannot be equal to 0, please start from 1.")
    exit(1)
if MAX <= MIN:
    p("Error : MAX value must be higher than MIN")
    exit(1)
d("Argument parsed :")
d("MIN = " + str(MIN))
d("MAX = " + str(MAX))
p("Result will be write in result.txt")
if os.path.exists("result.txt") and MIN < 6:
    os.remove("result.txt")
result = open("result.txt", "a")
c = 1
for i in range(MIN, MAX+1):
    if c >= 1:
        c = 0
        log.progress(str(int(i/MAX*100)) + "% processing " + str(i))
    if number.check_perfect(i):
        result.write(str(i)+"\n")
        p("Found " + str(i))
    c += 1
