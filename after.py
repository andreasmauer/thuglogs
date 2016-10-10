






















# internal tools
def _toCSV(self, fileName):

	with open(fileName, 'wt') as csvfile:

	    csvwriter = csv.writer(csvfile, delimiter=',')

	    for key in self.output:
	    	self.dates.append(key)


	    self.dates.sort()
	    # print self.dates

	    # print the date-headers
	    headers = ['']
	    for key in self.dates:
	    	headers.append(key)

	    csvwriter.writerow(headers)

	    # print the lines 
	    
	    for key in self.filters:
	    	toLine = [key]
	    	for date in self.dates:
	    		
	    		if key not in self.output[date]:
	    			toLine.append(0)
	    		else:
	    			toLine.append(self.output[date][key])
	    	csvwriter.writerow(toLine)