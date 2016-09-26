# -*- coding: utf-8 -*-
# Copyright (c) 2016
#
# This script removes multiple lines from all files in a directory. 
# 
# Author:
# 	Xenia Bogomolec, indigomind@gmx.de, xenia.bogomolec@extern.polizei.niedersachsen.de 
#
#
###################################### CUSTOM DEFINED PARAMETERS ##################################

# path to the directory with lists
filePath = "/path/to/folder/with/lists"

# file name
fileName = "rockyou.txt"

###################################################################################################
############################################# FUNCTIONS ###########################################
###################################################################################################

import os, datetime

filePath.replace("\\", "/")
os.chdir(filePath)
newFile = "new_" + fileName
startTime = datetime.datetime.now()

def removeMulitpleLines():
	print "start looking for mulitple lines in %s" % (fileName)
	numberOfReadLines = 0
	mulitpleLines = 0
	newLines = wrapperDict(1)
	with open(fileName, "rb") as addressFile:
		for line in addressFile:
			try:
				if numberOfReadLines != 0 and numberOfReadLines % 100000 == 0:
					print "%d lines read in %s" % (numberOfReadLines, str(datetime.datetime.now() - startTime))
				numberOfReadLines += 1
				line = line.rstrip().replace("\r", "").replace("\n", "")
				if line not in newLines[line[0]]:
					newLines[line[0]].append(line)
				elif line != "": 
					mulitpleLines += 1
			# for initial characters without correspondent key in readLines
			except(IndexError):
				pass
			except(KeyError):
				if line not in newLines['other']:
					newLines['other'].append(line)
				else: 
					mulitpleLines += 1
			except(KeyboardInterrupt):
				computationTime = str(datetime.datetime.now() - startTime)
				print "\nInterrupted after reading line %s of file %s during %s" % (line, fileName, computationTime)
				writeFile(mulitpleLines, newFile.split(".")[0] + "_part.txt", newLines)
				return
		print "loop end", numberOfReadLines
	writeFile(mulitpleLines, newFile, newLines)

def writeFile(mulitpleLines, newFile, newLines):
	content = ""
	for item in newLines:
		for newLine in newLines[item]:
			content += newLine + "\n"
	file = open(newFile, 'w+')
	file.write(content)
	processTime = str(datetime.datetime.now() - startTime)
	print "\nRemoved %d mulitple lines from %s in %s." % (mulitpleLines, newFile, processTime)
	file.close()

def charChoice():
	charChoice = []
	for i in range(33, 127):
		hexValue = hex(i) if len(hex(i)) == 4 else hex(i)[:2] + "0" + hex(i)[2]
		hexValue = '\\' + hexValue[1:]
		charChoice.append(hexValue.decode('unicode_escape').encode('latin-1').decode('utf8'))
	# German umlauts ä, Ä, ö, Ö, ü, Ü and whitespace
	for char in ['\xe4', '\xc4', '\xf6', '\xd6', '\xfc', '\xdc', ' ']:
		charChoice.append(char)
	# ì, í, à, á, â, ã, ò, ó, ë, è, é, ê
	for char in ['\xec', '\xed', '\xe0', '\xe1', '\xe2', '\xe3', '\xf2', '\xf3', '\xeb', '\xe8', '\xe9', '\xea']:
		charChoice.append(char)
	# ¿, §, ž, š, ñ, Ñ, £....
	for char in ['\xbf', '\xa7', '\x9e', '\x9a', '\xf1', '\xd1', '\xa3', 'other']:
		charChoice.append(char)
	return charChoice

# acceleration of the process: make a dictionary of checked lines instead of a list
def simpleDict():
	simpleDict = {}
	for char in charChoice():
		simpleDict[char] = []
	return simpleDict

# for multi level dictionaries, only makes sense for low number of characters
def wrapperDict(depth):
	wrapperDicts = [simpleDict()] + [{} for i in range(depth - 1)]
	for i in range(depth - 1):
		for char in charChoice():
			wrapperDicts[i + 1][char] = wrapperDicts[i]
	return wrapperDicts[depth - 1]

removeMulitpleLines()


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