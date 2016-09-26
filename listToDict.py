# -*- coding: utf-8 -*-
# Copyright (c) 2016
#
# This script converts a list of two '\t'-separated  terms into a dictionary
# 
# Author:
# 	Xenia Bogomolec, indigomind@gmx.de, xenia.bogomolec@extern.polizei.niedersachsen.de 
#
#
###################################### CUSTOM DEFINED PARAMETERS ##################################

import os

filePath = "C:/Users/path/to/file"
fileName = "listfile.txt"
newFile = "new_file.py"
dict_name = "myDictionary"
 
os.chdir(filePath)
newLines = []

with open(fileName, "rb") as addressFile:
	lines = addressFile.readlines()
	for line in lines:
		lineParts = line.split("\t")
		if line not in newLines:
			newLines.append("\t'" + lineParts[0].strip() + "': '" + lineParts[1].replace("\r\n", "") + "',\n")
content = dict_name + " = {\n"
for newLine in newLines:
	content += newLine
content += "}\n"
file = open(newFile, 'w+')
file.write(content)
file.close()


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