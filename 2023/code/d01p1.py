#!python3

import os.path
import sys
import re

"""
--- Day 1: Trebuchet?! ---
see puzzle/d01/description

The calibration document consists of lines of text.
each line originally contained a specific calibration value that the Elves now need to recover.
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

example input:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

1abc2 = > 1,2 => 12
pqr3stu8vwx = > 3,8 => 38
a1b2c3d4e5f = > 1,5 => 15
treb7uchet = > 7,7 => 77
sum = 142
"""

debug = False

def calibration (line):
  """ extract calibration digits """
  line = line.rstrip('\r\n')
  rex = r'\d'
  # extract digits
  digits = [ digit for digit in re.findall (rex, line) ]
  first = int(digits[0])
  last = int(digits[-1])
  result = first * 10 + last
  if debug: print (f"{line} => {result}")
  return result

def total (lines):
  lines = [ line.rstrip('\r\n') for line in lines ]
  calibrations = [ calibration (line) for line in lines ]
  s = sum (calibrations)
  if debug: print (f"sum: {s}")
  return s

def trebuchet (filename):
  """ read calibration lines from file """
  lines = []
  with open(filename) as f:
    lines = f.readlines() # read input line
  result = total (lines)
  if debug: print (f"total: {result}")
  return result

def main (filename):
  print (f"filename: {filename}")
  if not os.path.isfile(filename):
    print(f"File {filename} does not exist.")
    return 0
  else:
    result = trebuchet (filename)
    print (f"trebuchet: {result}")
    return result

if __name__ == '__main__':
  for argv in sys.argv[1:]:
    main (argv)

