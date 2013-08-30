import os.path
import sys

print "Irc Log parser for use in limechat"


for fileName in os.listdir(str(raw_input("Enter path: "))):
	print fileName
	if os.path.isfile(fileName):
		curFile = open(fileName)
		print(curFile.readline())
		curFile.close()
	else :
		print("%s is a directory" % fileName)