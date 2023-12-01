#!python3

import os.path
import sys
import re

"""
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

input:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

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
"""

# 1abc2 = > 1,2 => 12
# pqr3stu8vwx = > 3,8 => 38
# a1b2c3d4e5f = > 1,5 => 15
# treb7uchet = > 7,7 => 77
# sum = 142

# two1nine => 29
# eightwothree => 83
# abcone2threexyz => 13
# xtwone3four => 24
# 4nineeightseven2 => 42
# zoneight234 => 14
# 7pqrstsixteen => 76
# sum = 281

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
  'nine': 9
}

def todigit (digit):
  if digit not in digitmap:
    throw
  return digitmap [digit]

def calibration (line):
  """ extract calibration digits """
  rex = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
  line = line.rstrip('\r\n')
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

def total (lines):
  calibrations = [ calibration (line.rstrip('\r\n')) for line in lines ]
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

