import os
import re

path = '/Users/clinton/Documents/dev/regextest'
files = os.listdir(path)

for file in files:
	new_filename = re.sub(r'(.*)-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}.[m][d])',r'<1>', file)
	new_filename += '.md'
	os.rename(file, new_filename)	
