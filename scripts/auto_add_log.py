#!/user/bin/python3 

'''
automatically add progress log to README.md  
'''

from datetime import datetime
x  = datetime.now()
formated_date = '/'.join([str(i) for i in [x.day, x.month, x.year]])
print(formated_date)

import subprocess

for i in subprocess.Popen(["ls", "-lt", "python_solutions"], stdout=subprocess.PIPE).stdout:
	for line in str(i).split("\n"):
		print(line)


