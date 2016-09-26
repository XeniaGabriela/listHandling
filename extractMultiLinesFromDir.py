# -*- coding: utf-8 -*-
# Copyright (c) 2016
#
# This script extracts multiple lines from all files in a directory 
# 	and writes them with the location of their occurence in a file 
#   'file_assigned_multiple_lines.txt' in a the folder newFolder
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

import os, datetime

def checkMultiples():
	startTime = datetime.datetime.now()
	filePath.replace("\\", "/")
	os.chdir(filePath)
	if not os.path.exists(newFolder):
		os.makedirs(newFolder)
	readLines = []
	multipleLines = []
	assignedMultipleLines = []
	fileList = [item for item in os.listdir(".") if len(item.split(".")) > 1]

	print "\nCollecting multiple occurrences\n---------------------------------------------------------" 
	for fileName in fileList:
		fileReadStart = datetime.datetime.now()
		with open(fileName, "rb") as readFile:
			print "Parsing %s" % (fileName)
			for line in readFile:
				line = line.rstrip().replace("\r", "").replace("\n", "")
				if line not in readLines:
					readLines.append(line)
				elif line not in multipleLines: 
					multipleLines.append(line)
		fileParseTime = str(datetime.datetime.now() - fileReadStart)
		print "\t(Parsing time: %s)" % (fileParseTime)

	print "\nAssigning multiple occurrences to file\n---------------------------------------------------------" 
	for fileName in fileList:
		fileReadStart = datetime.datetime.now()
		with open(fileName, "rb") as readFile:
			print "Parsing %s" % (fileName)
			for line in readFile:
				line = line.rstrip().replace("\r", "").replace("\n", "")
				if line in multipleLines:
					assignedMultipleLines.append({'pwd':line, 'file': fileName})
		fileParseTime = str(datetime.datetime.now() - fileReadStart)
		print "\t(Parsing time: %s)" % (fileParseTime)		

	writeMultipleLines(assignedMultipleLines)
	print "\nFound %d multiple lines in %s\n." % (len(assignedMultipleLines), str(datetime.datetime.now() - startTime))

def writeMultipleLines(multipleLines):
	newFile = open(newFolder + "/" + "file_assigned_multiple_lines.txt", 'w+')
	newContent = ""
	sortedResults = sorted(multipleLines, key = lambda x: x['pwd'])
	sortedResults.reverse()
	for item in sortedResults:
		newContent += str(item['pwd']) + ": " + str(item['file']) + "\n"
	newFile.write(newContent)
	newFile.close()	

checkMultiples()


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