#!/usr/bin/env python3

# for grabbing args from shell
import sys

# helper function for checking if number
# def is_number(value):
#     if value is None:
#         return False
#     try:
#

# check for adequate number of args
if len(sys.argv) != 3:
    print('Usage: python3 tempConverter.py3 [outputTempScale] [temperature] \noutputTempScale should be C for celsius, K for Kelvin, or F for Farenheit (case insensitive)')
    quit()

# load args into dictionary
args = { 'outputTempScale': sys.argv[1], 'inputTemp': sys.argv[2] }

# check if args are properly formatted
if str(sys.argv[1]).upper() != 'C' and str(sys.argv[1]).upper() != 'F' and str(sys.argv[1]).upper() != 'K':
    print('Usage: python3 tempConverter.py3 [outputTempScale] [temperature] \noutputTempScale should be C for celsius, K for Kelvin, or F for Farenheit (case insensitive)')
    quit()
try:
    args['inputTemp'] = float(args['inputTemp'])
except ValueError:
    print('Usage: python3 tempConverter.py3 [outputTempScale] [temperature] \ntemperature must be a number')
    quit()
