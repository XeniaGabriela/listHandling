# -*- coding: utf-8 -*-
# Copyright (c) 2016
#
# This script checks the distribution of initial characters of lines from all files in a directory
# 	and writes them into a new file newFolder + "/initial_character_distribution.txt"
#
# Author:
# 	Xenia Bogomolec, indigomind@gmx.de, xenia.bogomolec@extern.polizei.niedersachsen.de
#
#
###################################### CUSTOM DEFINED PARAMETERS ##################################

# path to the directory with lists
filePath = "/path/to/folder/with/lists"

# folder for the new file
newFolder = "evaluations"


###################################################################################################
############################################# FUNCTIONS ###########################################
###################################################################################################

import os, datetime, binascii

def checkfiles():
	startTime = datetime.datetime.now()
	filePath.replace("\\", "/")
	os.chdir(filePath)
	if not os.path.exists(newFolder):
		os.makedirs(newFolder)
	readLines = charDict()
	fileList = [item for item in os.listdir(".") if len(item.split(".")) > 1] 

	for fileName in fileList:
		fileReadStart = datetime.datetime.now()
		with open(fileName, "rb") as readFile:
			# print "\n%s: Reading %s" % (datetime.datetime.now(), fileName)
			# lines = readFile.readlines()
			print "%s: Parsing %s" % (datetime.datetime.now(), fileName)
			for line in readFile:
				line = line.rstrip()
				try:
					readLines[line[0]] += 1
				# for initial characters without correspondent key in readLines
				except(IndexError):
					pass
				except(KeyError):
					readLines['other'] += 1
				except(KeyboardInterrupt):
					print "Interrupted after reading line %s of file %s" % (line, fileName)
					return					

		print "\t(Parsing time: %s)" % (str(datetime.datetime.now() - fileReadStart))

	writeDistribution(readLines, fileList)
	print "\nTotal parsing time: %s \n" % (str(datetime.datetime.now() - startTime))



# just a test for acceleration of the process
def charDict():
	dictionary = {}
	for i in range(33, 127):
		hexValue = hex(i) if len(hex(i)) == 4 else hex(i)[:2] + "0" + hex(i)[2]
		hexValue = '\\' + hexValue[1:]
		char = hexValue.decode('unicode_escape').encode('latin-1').decode('utf8')
		dictionary[char] = 0
	# German umlauts ä, Ä, ö, Ö, ü, Ü and whitespace
	for char in ['\xe4', '\xc4', '\xf6', '\xd6', '\xfc', '\xdc', ' ']:
		dictionary[char] = 0
	# ì, í, à, á, â, ã, ò, ó, ë, è, é, ê
	for char in ['\xec', '\xed', '\xe0', '\xe1', '\xe2', '\xe3', '\xf2', '\xf3', '\xeb', '\xe8', '\xe9', '\xea']:
		dictionary[char] = 0
	# ¿, §, ž, š, ñ, Ñ, £....
	for char in ['\xbf', '\xa7', '\x9e', '\x9a', '\xf1', '\xd1', '\xa3', 'other']:
		dictionary[char] = 0
	return dictionary

def writeDistribution(readLines, fileList):
	newFile = open(newFolder + "/initial_character_distribution.txt", 'w+')
	newContent = "Character Distribution of the Files \n-------------------------\n"
	for line in fileList:
		newContent += "\t" + line + "\n"
	newContent += "\n\n" 
	sortedResults = sorted(readLines.items(), key = lambda x: x[1])
	sortedResults.reverse()
	for item in sortedResults:
		newContent += str(item[0]) + ": " + str(item[1]) + "\n"
	newFile.write(newContent)
	newFile.close()		


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