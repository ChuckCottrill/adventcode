#!python3

import os.path
import sys
import re

"""
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

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

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

two1nine => two,nine => 29
eightwothree => eight,three => 83
abcone2threexyz => one,three => 13
xtwone3four => two,four => 24
4nineeightseven2 => nine,2 => 42
zoneight234 => one,4 => 14
7pqrstsixteen => 7,six => 76
sum = 281
"""

digitmap = {
  # '0': 0,
  '1': 1,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  # 'zero': 0,
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9,
}
replacemap = {
  'oneight': 'one eight',
  'twone': 'two one',
  'threeight': 'three eight',
  'fiveight': 'five eight',
  'eightwo': 'eight two',
  'eighthree': 'eight three',
  'nineight': 'nine eight',
  # 'one': '1',
  # 'two': '2',
  # 'three': '3',
  # 'four': '4',
  # 'five': '5',
  # 'six': '6',
  # 'seven': '7',
  # 'eight': '8',
  # 'nine': '9'
}

def todigit (digit):
  if digit not in digitmap:
    raise Exception("unknown digit")
  return digitmap [digit]

def calibration0 (line):
  """ extract calibration digits """
  rex = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
  line = line.rstrip('\r\n').lower()
  # extract digits
  # digits = [ int(digit) for digit in re.findall (rex, line) ]
  # digits = [ todigit(digit) for digit in re.findall (rex, line) ]
  digits = [ digit for digit in re.findall (rex, line) ]
  print (f"{line}: {digits}")
  first = todigit(digits[0])
  last = todigit(digits[-1])
  #  print (f"first: {first} last: {last}")
  result = first * 10 + last
  print (f"{line} => {result}")
  return result

def calibration2 (line):
  """ extract calibration digits """
  rex = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
  line = line.rstrip('\r\n').lower()
  xline = line
  for key,val in replacemap.items():
    xline = xline.replace(key, val)
  # extract digits
  # digits = [ digit for digit in re.findall (rex, line) ]
  digits = [ digit for digit in re.findall (rex, xline) ]
  print (f"{line}: {digits}")
  first = todigit(digits[0])
  last = todigit(digits[-1])
  #  print (f"first: {first} last: {last}")
  result = first * 10 + last
  print (f"{line} => {result}")
  return result

def total (lines):
  lines = [ line.rstrip('\r\n') for line in lines ]
  calibrations = [ calibration2 (line) for line in lines ]
  s = sum (calibrations)
  print (f"sum: {s}")
  return s

def trebuchet (filename):
  """ read calibration lines from file """
  lines = []
  with open(filename) as f:
    lines = f.readlines() # read input line
  result = total (lines)
  print (f"total: {result}")
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

