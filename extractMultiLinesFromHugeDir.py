# -*- coding: utf-8 -*-
# Copyright (c) 2016
#
# This script removes multiple lines from all files in a directory with huge files
# 	and writes the results in cleaned files
#
# Author:
# 	Xenia Bogomolec, indigomind@gmx.de, xenia.bogomolec@extern.polizei.niedersachsen.de
#
#
###################################### CUSTOM DEFINED PARAMETERS ##################################

# path to the directory with the files to be checked
filePath = "/path/to/folder/with/lists"

# the maximum number of lines in a cleaned file 
# all these files will be compared to each other
# a high value might cause memory error
linesChunkSize = 1000000

# name of the folder for the divided files
workFolder = "distributed_files"

# name of the folder for the divided files
newFolder = "evaluations"

####################################################################################################
############################################# FUNCTIONS ############################################
#################################################################################################### 

import binascii, datetime, math, os, shutil

startTime = datetime.datetime.now()
filePath.replace("\\", "/")
os.chdir(filePath)

if not os.path.exists(newFolder):
	os.makedirs(newFolder)

if not os.path.exists(workFolder):
	os.makedirs(workFolder)

def cleanFiles():
	multiLines = []
	fileList = [item for item in os.listdir(".") if len(item.split(".")) > 1] 
	print "\n"
	for fileName in fileList:
		divideFile(fileName)
	os.chdir(workFolder) 
	distributedFiles = os.listdir(".")
	numberOfFiles = len(distributedFiles)
	steps = numberOfFiles*(numberOfFiles-1)/2
	print "\nComparing all files against each other in %d steps:" % (steps)
	for baseFileName in distributedFiles:
		print "\nbaseFile %s" % baseFileName
		baseIndex = distributedFiles.index(baseFileName)
		with open(baseFileName, "rb") as baseFile:
			baseFile = baseFile.readlines()
			for compareFileName in distributedFiles[baseIndex + 1:]:
				print "  compare with %s" % compareFileName
				with open(compareFileName, "rb") as compareFile:
					compareFile = compareFile.readlines()
					intersection = list(set(baseFile).intersection(compareFile))
					multiLines.extend(intersection)
	os.chdir(filePath)
	shutil.rmtree(filePath + "/" + workFolder)
	multiLines = sorted(list(set(multiLines)))
	writeMultiLines(multiLines, fileList)

	print "\nFOUND %d VARIOUS MULTIPLE ENTRIES. PROCESSING TIME: %s" % (len(multiLines), str(datetime.datetime.now() - startTime))

# divides file into manageable chunks
def divideFile(fileName):
	with open(fileName, "rb") as readFile:
		print "Dividing %s ..." % (fileName)
		newFileNo = 0
		while 1:
			contentLines = [] 
			for i in range(linesChunkSize):
				try:
					contentLines.append(readFile.next().rstrip())
				except:
					writePart(contentLines, newFileNo, fileName)
					return
			newFileNo = writePart(contentLines, newFileNo, fileName)	

# writes chunk to file
def writePart(contentLines, newFileNo, fileName):
	contentLines = set(contentLines)
	content = ""
	for line in contentLines:
		content += line + "\n"
	fileName = workFolder + "/" + fileName + "_" + str(newFileNo)
	file = open(fileName, 'w+')
	file.write(content)
	file.close()
	newFileNo += 1
	return newFileNo


# write multiple lines in separate file
def writeMultiLines(multiLines, fileList):
	content = "Multiple Lines of the Files \n-------------------------\n"
	for line in fileList:
		content += "\t" + line + "\n"
	content += "\n"
	for line in multiLines:
		content += line
	file = open(newFolder + "/multiple_lines.txt", 'w+')
	file.write(content)
	file.close()

cleanFiles()


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