import re
str= """Sam is 15 years old, and Anu is 27 years old.
Avi is 67 years old, and his grandfather, Ram is 102"""
name=re.findall('[A-Z][a-z]*',str)
age=re.findall('[0-9]+',str)
for i in range (len(name)):
	voe=age[i]
	print(name[i],"age is",voe)
