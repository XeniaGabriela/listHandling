# -*- coding: utf-8 -*-
# Copyright (c) 2016
#
# This script removes multiple lines from all files in a directory 
# 	and writes the results in assigned files in a folder 'cleanedFiles'
#
# Author:
# 	Xenia Bogomolec, indigomind@gmx.de
#
#
###################################### CUSTOM DEFINED PARAMETERS ##################################

filePath = "/path/to/folder/with/lists"


###################################################################################################
############################################# FUNCTIONS ###########################################
###################################################################################################

import os, datetime, binascii

doubleLines = []

def checkfiles():
	startTime = datetime.datetime.now()
	filePath.replace("\\", "/")
	os.chdir(filePath)
	readLines = charDict()
	numberOfReadLines = 0
	fileList = [item for item in os.listdir(".") if len(item.split(".")) > 1]
	for fileName in fileList:
		fileReadStart = datetime.datetime.now()
		with open(fileName, "rb") as readFile:
			newContent = ""
			print "\nParsing %s" % (fileName)
			lines = readFile.readlines()
			numberOfReadLines += len(lines)
			for line in lines:
				line = line.rstrip()
				try:
					if line not in readLines[line[0]]:
						readLines[line[0]].append(line)
						newContent += line + "\n"
					else:
						doubleLines.append({'pwd':line, 'file': fileName})
				# for initial characters without correspondent key in readLines
				except(IndexError):
					pass
				except(KeyError):
					if line not in readLines['other']:
						readLines['other'].append(line)
					else: 
						doubleLines.append({'pwd':line, 'file': fileName})
				except(KeyboardInterrupt):
					print "Interrupted after reading line # %d of file %s" % (lines.index(line), fileName)
					computationTime = str(datetime.datetime.now() - startTime)
					print "\nFound %d double lines in %d read lines during %s." % (len(doubleLines), numberOfReadLines, computationTime)
					return

		if not os.path.exists("cleanedFiles"):
			os.makedirs("cleanedFiles")
		cleanedFile = open("cleanedFiles/" + fileName.split(".")[0] + "_cleaned.txt", 'w+')
		cleanedFile.write(newContent)
		cleanedFile.close()				
		fileParseTime = str(datetime.datetime.now() - fileReadStart)
		print "(Parsing time: %s)" % (fileParseTime)

	computationTime = str(datetime.datetime.now() - startTime)
	print "\nFound %d double lines in %d read lines during %s\n." % (len(doubleLines), numberOfReadLines, computationTime)
    
# just a test for acceleration of the process
def charDict():
	dictionary = {}
	for i in range(33, 127):
		hexValue = hex(i) if len(hex(i)) == 4 else hex(i)[:2] + "0" + hex(i)[2]
		hexValue = '\\' + hexValue[1:]
		char = hexValue.decode('unicode_escape').encode('latin-1').decode('utf8')
		dictionary[char] = []
	# German umlauts ä, Ä, ö, Ö, ü, Ü and whitespace
	for char in ['\xe4', '\xc4', '\xf6', '\xd6', '\xfc', '\xdc', ' ']:
		dictionary[char] = []
	# ì, í, à, á, â, ã, ò, ó, ë, è, é, ê
	for char in ['\xec', '\xed', '\xe0', '\xe1', '\xe2', '\xe3', '\xf2', '\xf3', '\xeb', '\xe8', '\xe9', '\xea']:
		dictionary[char] = []
	# ¿, §, ž, š, ñ, Ñ, £....
	for char in ['\xbf', '\xa7', '\x9e', '\x9a', '\xf1', '\xd1', '\xa3']:
		dictionary[char] = []
	dictionary['other'] = []
	return dictionary
	
checkfiles()


#
#
#                          m    m      \           /      m    m   
#                      m            m   \    n    /   m            m
#                       m              m \  OOO  / m              m
#                         m              m\/ Ö \/m              m
#                            m             mÖÖÖm            m
#                                 m    m    ÖÖÖ    m    m
#                                    m   m   Ö   m   m
#                           m               /Ö\              m
#                       m              |   / Ö \   |             m
#                     m               m   !  Ö  !   m              m
#                      m          m   /   !  Ö  !   \   m          m
#                         m  m            !  Ö  !           m  m
#                                        /   Ö   \
#                                            Ö
#                                            Ö
#                                            Ö
#                                            Ö
#                                            Ö
#
#