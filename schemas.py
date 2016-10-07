class kfz():

	def __init__(self):

		# self.path = os.getcwd() + '/user-logs/'
		self.headers = False
		self.encoding = 'utf8'
		self.delimiter = ' '
		self.quotechar = '"'


	def schematize(self, line):
	
		result = {}	

		result['host'] = line[0]
		result['ip'] = line[1].replace('(', '').replace(')', '')
		result['httpMethod'] = line[7].split(' ')[0]
		result['URI'] = line[7].split(' ')[1]
		result['httpVersion'] = line[7].split(' ')[2]
		result['httpResponse'] = line[8]
		result['referral'] = line[11]
		result['userAgent'] = line[12]
		
		# make a proper date object
		tempDate = line[5].replace('[', '').split(':')[0]
		tempDate = tempDate.split('/')
		tempDate = datetime.date(int(tempDate[2]), monthToInt(tempDate[1]), int(tempDate[0]))
		result['date'] = tempDate
		result['dateStr'] = str(tempDate)

		return result

def monthToInt(self, month):

	result = {
		'Jan': 1,
		'Feb': 2,
		'Mar': 3,
		'Apr': 4,
		'May': 5,
		'Jun': 6,
		'Jul': 7,
		'Aug': 8,
		'Sep': 9,
		'Oct': 10,
		'Nov': 11,
		'Dec': 12
	}

	return result[month]