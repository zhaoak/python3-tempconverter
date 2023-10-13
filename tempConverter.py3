#!/usr/bin/env python3

# for grabbing args from shell
import sys

# check for adequate number of args
if len(sys.argv) != 3:
    print('Usage: python3 tempConverter.py3 [outputTempScale] [temperature] \noutputTempScale should be C for celsius, K for Kelvin, or F for Farenheit (case insensitive)')
    quit()

# load args into dictionary
args = { 'outputTempScale': sys.argv[1], 'inputTemp': sys.argv[2] }

# check if args are properly formatted and of correct types
if sys.argv[1].upper() != 'C' and sys.argv[1].upper() != 'F' and sys.argv[1].upper() != 'K':
    print('Usage: python3 tempConverter.py3 [outputTempScale] [temperature] \noutputTempScale should be C for celsius, K for Kelvin, or F for Farenheit (case insensitive)')
    quit()

try:
    args['inputTemp'] = float(args['inputTemp'])
except ValueError:
    print('Usage: python3 tempConverter.py3 [outputTempScale] [temperature] \ntemperature must be a number')
    quit()

# functions from converting from scale to scale
def celsiusToFarenheit(temp):
    return 9 / 5 * temp + 32

def kelvinToFarenheit(temp):
    return 9 / 5 * (temp - 273) + 32

def farenheitToCelsius(temp):
    return (5 / 9 * (temp - 32))

def celsiusToKelvin(temp):
    return temp + 273

def kelvinToCelsius(temp):
    return (temp - 273)

def farenheitToKelvin(temp):
    return (5 / 9 * (temp - 32) + 273)

# convert and print output values
match args['outputTempScale'].upper():
    case 'C':
        print(str(args['inputTemp']) + ' Farenheit -> Celsius: ' + str(farenheitToCelsius(args['inputTemp'])) + ' C')
        print(str(args['inputTemp']) + ' Kelvin -> Celsius: ' + str(kelvinToCelsius(args['inputTemp'])) + ' C') 
    case 'F':
        print(str(args['inputTemp']) + ' Farenheit -> Celsius: ' + str(farenheitToCelsius(args['inputTemp'])) + ' C')
        print(str(args['inputTemp']) + ' Kelvin -> Celsius: ' + str(kelvinToCelsius(args['inputTemp'])) + ' C') 
