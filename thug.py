import schemas
import pre
import inLine
import after
import os
import csv
# import pprint

inPath  = os.getcwd() + '/inputs'
outPath = os.getcwd() + '/outputs'

def man(func = None):
	# if func is given then it prints just the info regarding that func
	# if not then everything will be printed

	print('>>> FORMAT <<<')
	print('')
	print('>loop')
	print('core used for ...')


def filter(input, output, what):
	with open(input, 'rb') as csvfile:
		lines = csv.reader(csvfile)

def test(text):
	print(text)


def learn(input, newline='', delimiter='', quoterchar=''):
	with open(input, 'rb') as csvfile:




def justGbot(input, output, schema):
	# input is a single file

	with open(input, 'rb') as csvfile:
		# lines = 
		pass

def loop(input, output, schema, pre, inLine, after):
	# core def, it will be used a lot

	sch = schemas.Schema(schema)

	for filename in os.listdir(inPath + input):
		if '.DS_Store' not in filename:
			print ('looping: ' + filename)
			with open(inPath + input + filename, newline=sch.newline) as csvfile:
				lines = csv.reader(csvfile, delimiter=sch.delimiter, quotechar=sch.quotechar)
				for line in lines:
					result = sch.schematize(line)
					print (result['URI'])

					



