import subprocess
from subprocess import Popen, PIPE, STDOUT
import re
import sys
import os
subprocess.run(['clear'])
print('''
'||''|.                        '||  '||          
 ||   ||    ...     ...      .. ||   ||    ....  
 ||    || .|  '|. .|  '|.  .'  '||   ||  .|...|| 
 ||    || ||   || ||   ||  |.   ||   ||  ||      
.||...|'   '|..|'  '|..|'  '|..'||. .||.  '|...' 
                                                 
                                                 
''')                                                 
URL = input('Please enter the IP: ')
word = '/usr/share/wordlists/dirbuster/directory-list-2.3-small.txt'
nmap = subprocess.run(['nmap', '-sV', '-oN', 'out.txt', URL]) 
universal_newlines = True
stdout = subprocess.PIPE

path_to_file='/home/doodle/out.txt'
with open(path_to_file,'r') as file:
	lines = (file.readlines())
	for line in lines:
		match = re.search(r'(.*)(?=OpenSSH,*)(.*) ',line)
		if match:
			subprocess.run(['gobuster', 'dir', '-u', URL, '-w', word])
			print('done')

path_to_file='/home/doodle/out.txt'
with open(path_to_file,'r') as file:
	lines = (file.readlines())
	for line in lines:
		match = re.search(r'(.*)(?=Apache,*)(.*) ',line)
		if match:
			subprocess.run(['gobuster', 'dir', '-u', URL, '-w', word])
			print('done')
			
