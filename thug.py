import schemas
import pre
import inLine
import after
# import pprint


def man(func = None):
	# if func is given then it prints just the info regarding that func
	# if not then everything will be printed

	defsList = {

	}

	if func is None:
		print ('empty')

	else:
		print ('not empty')

	# print(all)



def test(text):
	print(text)



def justGbot(input, output, schema):
	# input is a single file

	with open(input, 'rb') as csvfile:
		# lines = 


