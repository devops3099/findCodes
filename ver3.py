# !/usr/bin/python3
#coding: UTF-8
from tkinter import *
from tkinter import filedialog as fd
import re
import datetime
import pickle
import docx
from subprocess import check_output


global ccounter
ccounter = 0

#comment1

#global ccounter_fileOpen
#ccounter_fileOpen = 0
# ccounter += 1
global list_arr
list_arr = []       #only NAMES

#===Dictionary-for-changing======================================================================
global tuple_1
tuple_1 = {None:{None:[None]}}

global tuple_forDeleting
tuple_forDeleting = {None:{None:[None]}}

#=========================================================================
# SAVE ONLY CODES FROM TXT FILES
def saveOnlyCodesFromFiles(filename):
	nameForSaveToTxt = re.findall(r'\w+', filename)
	nameForSaveToTxt = str(nameForSaveToTxt[0])
	f = open(filename, 'r')
	listSource = []
	#save to list from file
	for i in f:
		ii = re.findall(r'\w+', i)
		#print('!!!!!!!\n', ii)
		for j in ii:
			#print('__________!!!!!!!\n', j)
			if len(j) > 15:
				listSource.append(j)

	listSource.sort()
		
	fs = open(nameForSaveToTxt + '.txt', 'w')
	for i in listSource:
		ii = str(i)
		ii2 = re.findall(r'\w+', ii)
		#if len(i) > 20:
		for j in ii2:
			iii = '\t' + j + '\n' #new code!
			#iii = ii + '\n'
			fs.write(iii)          
	fs.close()
	f.close()
	print('Opened ',filename, ' and saved to ', nameForSaveToTxt)
	print('__READY________!!!!!!!\n')

def commandForButton_saveOnlyCodes():
	saveOnlyCodesFromFiles(filename)

#=========================================================================
#=========================================================================
#Find names of all doc/docx files
#=====DOC================================
def outputOfDirCommandDOCFilesFunc():
	outputOfDirCommand = check_output(['dir','/B'], shell=True)
	print('\n!!!!!', outputOfDirCommand)
	listOfDocFilesNames = []
	b = re.findall(r'\d{1,6}.doc\w?', str(a))
	listOfDocFilesNames += b
	print('\n List DOC/DOCX Files = ',listOfDocFilesNames)
	return listOfDocFilesNames

#=====DOC================================
#get text from doc/docx file
def getTextFromDocFile(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
#=======DOC==============================
def openTakeTextFromDOCFile(listWithNamesOfDOCFiles):
	for i in listWithNamesOfDOCFiles:
		print('\n\tName of file = ', i)
		print(getTextFromDocFile(i))
		#return getTextFromDocFile(i)
# USAGE
#   openTakeTextFromDOCFile(outputOfDirCommandDOCFilesFunc())

#====TXT=================================
def outputOfDirCommandTXTFilesFunc():
	outputOfDirCommand = check_output(['dir','/B'], shell=True)
	print('\n!!!!!', outputOfDirCommand)
	listOfTXTFilesNames = []
	b = re.findall(r'\d{1,6}.txt', str(a))
	listOfDocFilesNames += b
	print('\n List TXT Files = ',listOfTXTFilesNames)
	return listOfTXTFilesNames
#=====TXT================================
#get text from doc/docx file
def getTextFromTXTFile(filename):
	f = open(filename, 'r')
	txtFile = f
	f.close()
	return txtFile
#========TXT=============================
def openTakeTextFromTXTFile(listForNamesOfTXTFiles):
	for i in listForNamesOfTXTFiles:
		print('\n\tName of file = ', i)
		print(getTextFromTXTFile(i))
		#return getTextFromTXTFile(i)
# USAGE
#   openTakeTextFromTXTFile(outputOfDirCommandTXTFilesFunc())
#=====================================


#=========================================================================
#=========================================================================
#global all_list
global all_source_list
all_source_list = []#ALL FILE source

global all_from_FileDB
all_from_FileDB = {}#ALL FILE source


def insertText():
    file_name = fd.askopenfilename()
    f = open(file_name, 'r')
    s = f.read()
    text.insert(1.0, s)
    f.close()

# "Save To Database" 
def saveCurrentTuple_1ToFileDB():
    file_name = fd.asksaveasfilename(filetypes=(("DataBase files", "*.pickle"),
                                                ("All files", "*.*") ))
    lenTuple_1 = len(tuple_1)
    if lenTuple_1 > 0:
        funcForSaveCurrentTuple_1ToFileDB(tuple_1, file_name)    
    else:
        print('tuple_1 не сформирована или пустая!')
    # f = open(file_name, 'w')
    # s = text.get(1.0, END)
    # f.write(s)
    # f.close()

def funcForSaveCurrentTuple_1ToFileDB(tuple_1, name):    
    with open(name, 'wb') as fSsaveToFile:
        pickle.dump(tuple_1, fSsaveToFile)


#=========================================================================
def sortCodesInTuple_1(tuple_1):
        for i in tuple_1:
            for j in tuple_1[i]:
                tuple_1[i][j].sort(reverse=True)
        print('TUPLE_1 IS SORTED')
#=========================================================================

#==Function-for-=tryAddToTuple( palet, box, code, tuple_1 )======================================================================
# f = file || FileDB.pickle
def tryAddToTuple(f):
    for lister in f:
        #CHECK IF LIST FULL( 4 ) number code box palet;;; if list ( 3 ): palet = 'noThirdColumn'
        ff = re.findall(r'\w+', lister)
        if len(ff) == 4 and ff[2] != 'вар':
            #print('ff = \n', len(ff))
            a_code = ff[1]
            a_box = ff[2]
            a_palet = ff[3]
            functionForTryAddToTuple( a_palet, a_box, a_code, tuple_1)
            #print('len(tuple_1) --------------=', len(tuple_1))

        if len(ff) == 3:
            #print('ff = \n', len(ff))
            a_code = ff[1]
            a_box = ff[2]
            a_palet = 'noThirdColumn'
            functionForTryAddToTuple( a_palet, a_box, a_code, tuple_1)

        if len(ff) == 2:
            #print('ff = \n', len(ff))
            a_code = ff[1]
            a_box = 'onlyCodes'
            a_palet = 'noSecondColumn'
            functionForTryAddToTuple( a_palet, a_box, a_code, tuple_1)

def functionForTryAddToTuple( palet, box, code, x ):
    #print(' \n !!!!!!!!!!!!!!!!!!!!!!',palet,' -- ', box, ' -- ', code)
    isPaletFinded = False
    isBoxFinded = False
    lengthOfTuple_1 = len(x)
    if lengthOfTuple_1 == 0:
        if x[None]:
           # print('lengthOfTuple_1 = ', lengthOfTuple_1)
            x = {palet: None}
            #print(' in1 ')
            x[palet] = {box:None}
            x[palet][box] = [code]
            x = dict(palet={box:[code]})
            #print(' in2 ')
            #print('tuple === ', tuple_1)
        #continue
    if lengthOfTuple_1 > 0:# or lengthOfTuple_1 == 0:
        #print(' IN lengthOfTuple_1 = ', lengthOfTuple_1)
        for cyclePalet in x:
            if cyclePalet == palet:
                isPaletFinded = True
                for cycleBox in x[palet]:
                    if cycleBox == box:
                        #print('cycleBox ===== ', cycleBox)
                        isBoxFinded = True
                        x[cyclePalet][cycleBox] += [code]
                        break

        if isPaletFinded == False and isBoxFinded == False:
            x[palet] = {box:[code]}
            #tuple_1[palet][box] += [code]

        if isBoxFinded == False and isPaletFinded == True:
            x[palet][box] = []
            x[palet][box] += [code]
    #print('!!!!!!!   lengthOfTuple_1 = ', len(tuple_1))
            
#==Sort-Codes-in-tuple_1===========================================================
def sortCodesInTuple_1(tuple_1):
        for i in tuple_1:
            for j in tuple_1[i]:
                tuple_1[i][j].sort(reverse=True)
        print('TUPLE_1 IS SORTED')
            
#=========================================================================

listForFindedCodesToDelFromTuple_1 = []
# list for finded codes to delete from tuple_1 // methods: add, clear, 
def addToListForFindedCodesToDeleteFromTuple_1(valueForAddTo,listForFindedCodesToDelFromTuple_1):
    listForFindedCodesToDelFromTuple_1.append(valueForAddTo)

def delListForFindedCodesToDeleteFromTuple_1(valueForAddTo,listForFindedCodesToDelFromTuple_1):    
    listForFindedCodesToDelFromTuple_1.clear()


#=========================================================================
# "Открыть источник кодов" BUTTON
def openSourceFile():
    #global ccounter
    global fileForSource
    tuple_1 = {None:{None:[None]}}
    #global ccounter_fileOpen
    fileForSource = "0"
    fileForSource = fd.askopenfilename()
    if fileForSource == '':
        print("Файл не выбран!")
    else:
        print("fileForSource = ", fileForSource)
        #del all_source_list[:]
        fsource = open(fileForSource, "r")
        #all_source_list = fsource.read()
        #all_source_list = re.findall(r'\w+', all_source_list)
        #print("fsource.read() = ", fsource.read())
        #print(" !!!!!!!!!!!!!!!!!!!!!!!")
        print("all_source_list = ", all_source_list)
        #del all_source_list[:]
        tryAddToTuple(fsource)
#        for i in fsource:
#            #ccounter_fileOpen += 1 #--------------------------------------------
#            all_source_list.append(i)
#        #print("all_source_list = \n", all_source_list)

        print('Added to tuple_1 ')
        print('len(tuple_1) - ', len(tuple_1))
        fsource.close()
        
        tuple_1.pop(None)
        print(' key None has been deleted from tuple_1')
        print('len(tuple_1) - ', len(tuple_1))

# LOAD DATABASE "Load Database"
def openFileDB():
    #global ccounter
    global nameOfFileDB
    #global ccounter_fileOpen
    nameOfFileDB = "0"
    nameOfFileDB = fd.askopenfilename()
    if nameOfFileDB == '':
        print("Файл с базой данных не выбран!")
    else:
        print("nameOfFileDB = ", nameOfFileDB)
        #del all_from_FileDB[:]
        
        with open(nameOfFileDB, 'rb') as fLoadFromFile:
            data_new = pickle.load(fLoadFromFile)
        global tuple_1
        tuple_1 = data_new
        print(nameOfFileDB, ' opened and saved to "Tuple_1" len = ', len(tuple_1))

def findInTuple_1FromTextField():
    #ccounter = 0
    #all_list = []       #ALL FILE list
    if len(tuple_1) < 2:
        #return 'Tuple_1 is empty!'
        print('_____LEN tuple_1 = ',len(tuple_1))
    else:
        print('1111 LEN tuple_1 = ',len(tuple_1))
        
    #del all_list[:]

    gTFF = re.findall(r'\w+', getTextFromField())

    arrForZhazhda025 = {None:{None:[None]}}
    #del arrForZhazhda025[:]
    #"""
    for i in gTFF:
        strForCurrent = ''
        if i in tuple_1:# if palet is finded
            boxList = []
            
            for box in tuple_1[i]:
                boxList.append(i)
            
            for h in tuple_1[i]:
                for g in tuple_1[str(i)][str(h)]:
                    functionForTryAddToTuple( i, h , g, arrForZhazhda025 )
            #arrForZhazhda025.append(tuple_1[i])
            strForCurrent = i + ' is finded! '
        else:
            for j in tuple_1:
                if i in tuple_1[j]:
                    for g in tuple_1[j][i]:
                        functionForTryAddToTuple( j, i , g, arrForZhazhda025 )
                    #arrForZhazhda025.append(tuple_1[i])
                    strForCurrent = i + ' is finded! '
                    break
                else:
                    strForCurrent = 'No such {} box or palet'.format(i)
        # if strForCurrent != '':
            # print(strForCurrent)
    print('len(arrForZhazhda025) = ', len(arrForZhazhda025))
    
    currentDate = datetime.datetime.now()
    fullDate = str(currentDate.year) + str(currentDate.month) + str(currentDate.day) + " " + str(currentDate.hour) + "-" + str(currentDate.minute) + "-" + str(currentDate.second)

    fileForResult = getTextForResultFile()
    if fileForResult != '':
        fResult = open(fileForResult + " " + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")
    else:
        fileForResult = 'result'
        fResult = open(fileForResult + " " + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")

    valueForFirstColumn = getTextForFirstColumn()

    #print("valueForFirstColumn = ", valueForFirstColumn)
    arrForZhazhda025.pop(None)
    print('LEN arrForZhazhda025 = \n', len(arrForZhazhda025))
    #print('arrForZhazhda025 = \n', arrForZhazhda025)
    countResultArr = 0
    for i in arrForZhazhda025:
        for j in arrForZhazhda025[i]:
            for h in arrForZhazhda025[i][j]:
                countResultArr += 1
                #ii = str(i)
                #rtrt = re.findall(r'\w+', ii)
                iii = '\t' + h + '\n' #new code!
                #iii = valueForFirstColumn[:-1] + '||' + h + '||' + j + '||' + i + '\n'
                fResult.write(iii)
    #"""

    print("\nВСЕГО :", countResultArr, ' ', len(arrForZhazhda025))

    fResult.close()        

def findInTuple_1FromTextFieldSirius():
    #ccounter = 0
    #all_list = []       #ALL FILE list
    if len(tuple_1) < 2:
        #return 'Tuple_1 is empty!'
        print('_____LEN tuple_1 = ',len(tuple_1))
    else:
        print('1111 LEN tuple_1 = ',len(tuple_1))
        
    #del all_list[:]

    gTFF = re.findall(r'\w+', getTextFromField())

    arrForZhazhda025 = {None:{None:[None]}}
    #del arrForZhazhda025[:]
    #"""
    for i in gTFF:
        strForCurrent = ''
        if i in tuple_1:# if palet is finded
            boxList = []
            
            for box in tuple_1[i]:
                boxList.append(i)
            
            for h in tuple_1[i]:
                for g in tuple_1[str(i)][str(h)]:
                    functionForTryAddToTuple( i, h , g, arrForZhazhda025 )
            #arrForZhazhda025.append(tuple_1[i])
            strForCurrent = i + ' is finded! '
        else:
            for j in tuple_1:
                if i in tuple_1[j]:
                    for g in tuple_1[j][i]:
                        functionForTryAddToTuple( j, i , g, arrForZhazhda025 )
                    #arrForZhazhda025.append(tuple_1[i])
                    strForCurrent = i + ' is finded! '
                    break
                else:
                    strForCurrent = 'No such {} box or palet'.format(i)
        # if strForCurrent != '':
            # print(strForCurrent)
    print('len(arrForZhazhda025) = ', len(arrForZhazhda025))
    
    currentDate = datetime.datetime.now()
    fullDate = str(currentDate.year) + str(currentDate.month) + str(currentDate.day) + " " + str(currentDate.hour) + "-" + str(currentDate.minute) + "-" + str(currentDate.second)

    fileForResult = getTextForResultFile()
    if fileForResult != '':
        fResult = open(fileForResult + " " + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")
    else:
        fileForResult = 'result'
        fResult = open(fileForResult + " " + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")

    valueForFirstColumn = getTextForFirstColumn()

    #print("valueForFirstColumn = ", valueForFirstColumn)
    arrForZhazhda025.pop(None)
    print('LEN arrForZhazhda025 = \n', len(arrForZhazhda025))
    #print('arrForZhazhda025 = \n', arrForZhazhda025)
    countResultArr = 0
    for i in arrForZhazhda025:
        for j in arrForZhazhda025[i]:
            for h in arrForZhazhda025[i][j]:
                countResultArr += 1
                #ii = str(i)
                #rtrt = re.findall(r'\w+', ii)
                #iii = '\t' + h + '\n' #new code!
                iii = valueForFirstColumn[:-1] + '||' + h + '||' + j + '||' + i + '\n'
                fResult.write(iii)
    #"""

    print("\nВСЕГО :", countResultArr, ' ', len(arrForZhazhda025))

    fResult.close()        

def findInTuple_1FromTextFieldSiriusNew():
    #ccounter = 0
    #all_list = []       #ALL FILE list
    if len(tuple_1) < 2:
        #return 'Tuple_1 is empty!'
        print('_____LEN tuple_1 = ',len(tuple_1))
    else:
        print('1111 LEN tuple_1 = ',len(tuple_1))

    #del all_list[:]
    
    gTFF = re.findall(r'\w+', getTextFromField())

    arrForZhazhda025 = {None:{None:[None]}}
    #del arrForZhazhda025[:]
    #"""
    for i in gTFF:
        strForCurrent = ''
		# if palet is finded
        if i in tuple_1:
            boxList = []
            
            for box in tuple_1[i]:
                boxList.append(i)
            
            for h in tuple_1[i]:
                for g in tuple_1[str(i)][str(h)]:
                    functionForTryAddToTuple( i, h , g, arrForZhazhda025 )
            #arrForZhazhda025.append(tuple_1[i])
            strForCurrent = i + ' is finded! '
        else:
            for j in tuple_1:
                if i in tuple_1[j]:
                    for g in tuple_1[j][i]:
                        functionForTryAddToTuple( j, i , g, arrForZhazhda025 )
                        #arrForZhazhda025.append(tuple_1[i])
                        strForCurrent = i + ' is finded! '
                        break
                    else:
                        strForCurrent = 'No such {} box or palet'.format(i)
    # if strForCurrent != '':
    # print(strForCurrent)
    #print('len(arrForZhazhda025) = ', len(arrForZhazhda025))

        currentDate = datetime.datetime.now()
        fullDate = str(currentDate.year) + str(currentDate.month) + str(currentDate.day) + " " + str(currentDate.hour) + "-" + str(currentDate.minute) + "-" + str(currentDate.second)
        
        fileForResult = getTextForResultFile()
        if fileForResult != '':
            fResult = open(fileForResult + " " + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")
        else:
            fileForResult = 'result'
            fResult = open(fileForResult + " " + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")

    valueForFirstColumn = getTextForFirstColumn()

    #print("valueForFirstColumn = ", valueForFirstColumn)
    arrForZhazhda025.pop(None)
    print('LEN arrForZhazhda025 = \n', len(arrForZhazhda025))
    #print('arrForZhazhda025 = \n', arrForZhazhda025)
    countResultArr = 0
    for i in arrForZhazhda025:
        for j in arrForZhazhda025[i]:
            for h in arrForZhazhda025[i][j]:
                countResultArr += 1
                #ii = str(i)
                #rtrt = re.findall(r'\w+', ii)
                #iii = '\t' + h + '\n' #new code!
                iii = valueForFirstColumn[:-1] + '||' + h + '||' + j + '||' + i + '\n'
                fResult.write(iii)
    #"""

    print("\nВСЕГО :", countResultArr, ' ', len(arrForZhazhda025))

    fResult.close()


def openListFile():
    global fileForList
    #fileForList = "0"
    fileForList = fd.askopenfilename()
#+++++++++++++++++++++++++++++++++++++++++++++++++++
# Сделать пездато! (поиск по 1источнику из файла списка => вывод только КОДЫ
def justDoIt():
    #"""
    #fileForSource = "1.txt"
    #fileForList = "2.txt"
    #fileForResult = "result.txt"
    #"""
    fileForResult = "result"

    flist = open(fileForList, "r")      #list
    #fResult = open(fileForResult, "w")

    all_list = []       #ALL FILE list

    del all_list[:]

    for i in flist:
        if re.search(r'\w[а-я]', i):
            list_arr.append(i)
            all_list.append(i)
        if re.search(r'\d{5,}', i):
            all_list.append(i)

    #save source file to array 'all_source_list'

    zhazhda = "Жажда 025\n"
    zhazhda_bool = False
    #fff = 0
    arrForZhazhda025 = []

    #"""
    for i in all_list:
        #if i == zhazhda:
            #zhazhda_bool = True
        for j in all_source_list:
            pat_str = str(i)
            pat2_str = str(j)
            listRoad = re.findall(r'\w+', pat_str)  # from list
            crossRoad = re.findall(r'\w+', pat2_str)# from source
            for k in crossRoad:
                    kk = str(k)
                    for ii in listRoad:
                        iii = str(ii)
                        if iii == kk and crossRoad[1] != "1" and crossRoad[1] != "2" and crossRoad[1] != "документа" and crossRoad[1] != "4" and crossRoad[1] != "5":#and iii != "05": #and zhazhda_bool == True
                            #print("\n\nEEEEEEEEEEEEEEe i = ", iii, "\nCROSSROAD = ", crossRoad[1])
                            #"""new code!!
                            #str_crossRoad = "||" + crossRoad[1] + "||" + crossRoad[2]
                            #arrForZhazhda025.append(str_crossRoad)
                            #"""#end new code!!
                            arrForZhazhda025.append(crossRoad[1])#paste old code
                            #print(crossRoad[1])
    #zhazhda_bool = False
    currentDate = datetime.datetime.now()
    fullDate = str(currentDate.year) + "-" + str(currentDate.month) + "-" + str(currentDate.day) + " " + str(currentDate.hour) + "-" + str(currentDate.minute) + "-" + str(currentDate.second)
    fResult = open(fileForResult + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")

    for i in arrForZhazhda025:
        ii = str(i)
        iii = '\t' + ii + '\n' #new code!
        #iii = '2' + ii + '\n'
        fResult.write(iii)
    #"""

    print("\nВСЕГО :", len(arrForZhazhda025))
    #print("\n all Source list = \n", all_list)
    #if tumblerSourceFileOpened == True or len(all_source_list) > 0:
        #fsource.close()
        #tumblerSourceFileOpened == False
    flist.close()
    fResult.close()
#+++++++++++++++++++++++++++++++++++++++++++++++++++

# Сделать пездато! с коробками (поиск по 1источнику из файла списка => вывод только КОДЫ + КОРОБКИ
def justDoItBoxes():

    fileForResult = "result"

    flist = open(fileForList, "r")      #list
    #fResult = open(fileForResult, "w")

    all_list = []       #ALL FILE list

    del all_list[:]

    for i in flist:
        if re.search(r'\w[а-я]', i):
            list_arr.append(i)
            all_list.append(i)
        if re.search(r'\d{5,}', i):
            all_list.append(i)

    #save source file to array 'all_source_list'

    zhazhda = "Жажда 025\n"
    zhazhda_bool = False
    #fff = 0
    arrForZhazhda025 = []

    #"""
    for i in all_list:
        #if i == zhazhda:
            #zhazhda_bool = True
        for j in all_source_list:
            pat_str = str(i)
            pat2_str = str(j)
            listRoad = re.findall(r'\w+', pat_str)  # from list
            crossRoad = re.findall(r'\w+', pat2_str)# from source
            for k in crossRoad:
                    kk = str(k)
                    for ii in listRoad:
                        iii = str(ii)
                        if iii == kk and crossRoad[1] != "1" and crossRoad[1] != "2" and crossRoad[1] != "документа" and crossRoad[1] != "4" and crossRoad[1] != "5":#and iii != "05": #and zhazhda_bool == True
                            #print("\n\nEEEEEEEEEEEEEEe i = ", iii, "\nCROSSROAD = ", crossRoad[1])
                            #"""new code!!
                            str_crossRoad = "||" + crossRoad[1] + "||" + crossRoad[2]
                            arrForZhazhda025.append(str_crossRoad)
                            #"""#end new code!!
                            #arrForZhazhda025.append(crossRoad[1])#paste old code
                            #print(crossRoad[1])
    #zhazhda_bool = False
    currentDate = datetime.datetime.now()
    fullDate = str(currentDate.year) + "-" + str(currentDate.month) + "-" + str(currentDate.day) + " " + str(currentDate.hour) + "-" + str(currentDate.minute) + "-" + str(currentDate.second)
    fResult = open(fileForResult + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")

    valueForFirstColumn = getTextForFirstColumn()
    for i in arrForZhazhda025:
        ii = str(i)
        #iii = '\t' + ii + '\n' #new code!
        iii = valueForFirstColumn[:-1] + ii + '\n'
        fResult.write(iii)
    #"""

    print("\nВСЕГО :", len(arrForZhazhda025))
    #print("\n all Source list = \n", all_list)
    #if tumblerSourceFileOpened == True or len(all_source_list) > 0:
        #fsource.close()
        #tumblerSourceFileOpened == False
    flist.close()
    fResult.close()
#+++++++++++++++++++++++++++++++++++++++++++++++++++

# Сделать пездато! с коробками и паллетами (поиск по 1источнику из файла списка => вывод только КОДЫ + КОРОБКИ + ПАЛЛЕТЫ
def justDoItPalettes():
    #"""
    #fileForSource = "1.txt"
    #fileForList = "2.txt"
    #fileForResult = "result.txt"
    #"""
    fileForResult = "result"

    flist = open(fileForList, "r")      #list
    #fResult = open(fileForResult, "w")

    all_list = []       #ALL FILE list

    del all_list[:]

    for i in flist:
        if re.search(r'\w[а-я]', i):
            list_arr.append(i)
            all_list.append(i)
        if re.search(r'\d{5,}', i):
            all_list.append(i)

    #save source file to array 'all_source_list'

    zhazhda = "Жажда 025\n"
    zhazhda_bool = False
    #fff = 0
    arrForZhazhda025 = []

    #"""
    for i in all_list:
        #if i == zhazhda:
            #zhazhda_bool = True
        for j in all_source_list:
            pat_str = str(i)
            pat2_str = str(j)
            listRoad = re.findall(r'\w+', pat_str)  # from list
            crossRoad = re.findall(r'\w+', pat2_str)# from source
            for k in crossRoad:
                    kk = str(k)
                    for ii in listRoad:
                        iii = str(ii)
                        if iii == kk and crossRoad[1] != "1" and crossRoad[1] != "2" and crossRoad[1] != "документа" and crossRoad[1] != "4" and crossRoad[1] != "5":#and iii != "05": #and zhazhda_bool == True
                            str_crossRoad = "||" + crossRoad[1] + "||" + crossRoad[2] + "||" + crossRoad[3]
                            arrForZhazhda025.append(str_crossRoad)
                            #"""#end new code!!
                            #arrForZhazhda025.append(crossRoad[1])#paste old code
                            #print(crossRoad[1])
    #zhazhda_bool = False
    currentDate = datetime.datetime.now()
    fullDate = str(currentDate.year) + "-" + str(currentDate.month) + "-" + str(currentDate.day) + " " + str(currentDate.hour) + "-" + str(currentDate.minute) + "-" + str(currentDate.second)
    fResult = open(fileForResult + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")

    valueForFirstColumn = getTextForFirstColumn()
    for i in arrForZhazhda025:
        ii = str(i)
        #iii = '\t' + ii + '\n' #new code!
        iii = valueForFirstColumn[:-1] + ii + '\n'
        fResult.write(iii)
    #"""

    print("\nВСЕГО :", len(arrForZhazhda025))
    #print("\n all Source list = \n", all_list)
    #if tumblerSourceFileOpened == True or len(all_source_list) > 0:
        #fsource.close()
        #tumblerSourceFileOpened == False
    flist.close()
    fResult.close()
#+++++++++++++++++++++++++++++++++++++++++++++++++++
# Поиск по тексту! с коробками + паллеты (поиск по 1источнику из текста => вывод КОДЫ + КОРОБКИ + ПАЛЛЕТЫ
def justDoItFromGetText_BoxesPalettes():

    global ccounter

    all_list = []       #ALL FILE list

    del all_list[:]

    gTFF = re.findall(r'\w+', getTextFromField())

    arrForZhazhda025 = []

    for i in gTFF:
        for j in all_source_list:
            ccounter += 1 #--------------------------------------------
            pat2_str = str(j)
            crossRoad = re.findall(r'\w+', pat2_str)# from source

            if len(crossRoad) < 3: continue
            if len(crossRoad) == 3:
                if i == crossRoad[2]:# or i == crossRoad[3]:
                    str_crossRoad = "||" + crossRoad[1] + "||" + crossRoad[2] + "||" + crossRoad[3]
                    #str_crossRoad = crossRoad[1]
                    arrForZhazhda025.append(str_crossRoad)
            if len(crossRoad) > 3:
                if i == crossRoad[2] or i == crossRoad[3]:
                    str_crossRoad = "||" + crossRoad[1] + "||" + crossRoad[2] + "||" + crossRoad[3]
                    #str_crossRoad = crossRoad[1]
                    arrForZhazhda025.append(str_crossRoad)


    #zhazhda_bool = False

    currentDate = datetime.datetime.now()
    fullDate = str(currentDate.year) + str(currentDate.month) + str(currentDate.day) + " " + str(currentDate.hour) + "-" + str(currentDate.minute) + "-" + str(currentDate.second)

    fileForResult = getTextForResultFile()
    if fileForResult != '':
        fResult = open(fileForResult + " " + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")
    else:
        fileForResult = 'result'
        fResult = open(fileForResult + " " + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")

    valueForFirstColumn = getTextForFirstColumn()

    print("valueForFirstColumn = ", valueForFirstColumn)
    for i in arrForZhazhda025:
        #ccounter += 1 #--------------------------------------------
        ii = str(i)
        #iii = '\t' + ii + '\n' #new code!
        iii = valueForFirstColumn[:-1] + ii + '\n'
        fResult.write(iii)
    #"""

    print("\nВСЕГО :", len(arrForZhazhda025))
    #print("ccounter = ", ccounter, "\ncounter_fileOpen = ", ccounter_fileOpen)
    #print("ccounter = ", ccounter, "\ncounter_fileOpen = ", ccounter_fileOpen)
    fResult.close()
#+++++++++++++++++++++++++++++++++++++++++++++++++++
# Поиск по тексту!КОДЫ(поиск по 1источнику из текста => вывод КОДЫ
def justDoItFromGetText_Codes():
    #ccounter = 0
    all_list = []       #ALL FILE list

    del all_list[:]

    gTFF = re.findall(r'\w+', getTextFromField())

    arrForZhazhda025 = []
    del arrForZhazhda025[:]
    #"""
    for i in gTFF:
        for j in all_source_list:
            pat2_str = str(j)
            crossRoad = re.findall(r'\w+', pat2_str)# from source
            if len(crossRoad) < 3: continue
            if len(crossRoad) == 3:
                if i == crossRoad[2]:# or i == crossRoad[3]:
                    #str_crossRoad = "||" + crossRoad[1] + "||" + crossRoad[2] + "||" + crossRoad[3]
                    str_crossRoad = crossRoad[1]
                    arrForZhazhda025.append(str_crossRoad)
            if len(crossRoad) > 3:
                if i == crossRoad[2] or i == crossRoad[3]:
                    #str_crossRoad = "||" + crossRoad[1] + "||" + crossRoad[2] + "||" + crossRoad[3]
                    str_crossRoad = crossRoad[1]
                    arrForZhazhda025.append(str_crossRoad)
    #zhazhda_bool = False
    currentDate = datetime.datetime.now()
    fullDate = str(currentDate.year) + str(currentDate.month) + str(currentDate.day) + " " + str(currentDate.hour) + "-" + str(currentDate.minute) + "-" + str(currentDate.second)

    fileForResult = getTextForResultFile()
    if fileForResult != '':
        fResult = open(fileForResult + " " + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")
    else:
        fileForResult = 'result'
        fResult = open(fileForResult + " " + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")

    valueForFirstColumn = getTextForFirstColumn()

    #print("valueForFirstColumn = ", valueForFirstColumn)
    for i in arrForZhazhda025:
        ii = str(i)
        iii = '\t' + ii + '\n' #new code!
        #iii = valueForFirstColumn[:-1] + ii + '\n'
        fResult.write(iii)
    #"""

    print("\nВСЕГО :", len(arrForZhazhda025))

    fResult.close()
#+++++++++++++++++++++++++++++++++++++++++++++++++++
# Поиск по тексту! с коробками  (поиск по 1источнику из текста => вывод КОДЫ + КОРОБКИ
def justDoItFromGetText_Codes_Boxes():

    all_list = []       #ALL FILE list

    del all_list[:]

    gTFF = re.findall(r'\w+', getTextFromField())
    #gTFF.sort(reverse=True)
    print("\ngTFF = \n", gTFF)

    arrForZhazhda025 = []

    #"""
    for i in gTFF:
        for j in all_source_list:
            pat2_str = str(j)
            crossRoad = re.findall(r'\w+', pat2_str)# from source
            if len(crossRoad) < 3: continue
            if len(crossRoad) == 3:
                if i == crossRoad[2]:# or i == crossRoad[3]:
                    str_crossRoad = "||" + crossRoad[1] + "||" + crossRoad[2]
                    #str_crossRoad = crossRoad[1]
                    arrForZhazhda025.append(str_crossRoad)
            if len(crossRoad) > 3:
                if i == crossRoad[2] or i == crossRoad[3]:
                    str_crossRoad = "||" + crossRoad[1] + "||" + crossRoad[2]
                    #str_crossRoad = crossRoad[1]
                    arrForZhazhda025.append(str_crossRoad)


    lengthOf_arrForZhazhda025 = str(len(arrForZhazhda025))
    openResultFileAndSave( arrForZhazhda025, lengthOf_arrForZhazhda025 )

    print("\nВСЕГО :", lengthOf_arrForZhazhda025)

    #fResult.close()
#+++++++++++++++++++++++++++++++++++++++++++++++++++
# save text from field
def getTextFromField():
    ss = text.get(1.0, END)
    print("ss =\n", ss)
    return ss
    #return '01000000207610119002020672'
#+++++++++++++++++++++++++++++++++++++++++++++++++++
#count current date
def dateCounter():
    currentDate = datetime.datetime.now()
    fullDate = str(currentDate.year) + str(currentDate.month) + str(currentDate.day) + " " + str(currentDate.hour) + "-" + str(currentDate.minute) + "-" + str(currentDate.second)
    print("fullDate = ", fullDate)
    return fullDate
#+++++++++++++++++++++++++++++++++++++++++++++++++++
# save text for column ( name 1st table column )
def getTextForFirstColumn():
    ff = numForFirstColumn.get(1.0, END)
    print("ff = ", ff)
    if ff == '' or ff == '\n':
        ff = '1\n'
    return ff
#+++++++++++++++++++++++++++++++++++++++++++++++++++
# save text for name result file
def getTextForResultFile():
    rr = nameForResultFile.get(1.0, END)
    return rr[:-1]
#+++++++++++++++++++++++++++++++++++++++++++++++++++
# save text for SIRIUS number strings and values for searching
def getTextForSIRIUSstring(numberOfString):
    nOS = numberOfString.get(1.0, END)
    print(nOS[:-1])
    return nOS[:-1]

def getTextForSIRIUSFind(searchString):
    tSOF = searchString.get(1.0, END)
    print(tSOF[:-1])
    return tSOF[:-1]

def commandSiriusString():
    getTextForSIRIUSstring(textSirius1)

def commandSiriusFind():
    getTextForSIRIUSFind(textSirius1Find)
#+++++++++++++++++++++++++++++++++++++++++++++++++++
#name for RESULT file + save RESULT file
def openResultFileAndSave( arrayWithStrings, lenArray ):
    fileForResult = getTextForResultFile()

    if fileForResult != '':
        fResult = open(fileForResult + " " + lenArray + " " + dateCounter() + '.txt', "w")
    else:
        fileForResult = 'result'
        fResult = open(fileForResult + " " + lenArray + " " + dateCounter() + '.txt', "w")

    valueForFirstColumn = getTextForFirstColumn()

    #iii = ''

    for i in arrayWithStrings:
        ii = str(i)
        #iii = '\t' + ii + '\n' #new code!
        iii = valueForFirstColumn[:-1] + ii + '\n'
        fResult.write(iii)

    fResult.close()
#+++++++++++++++++++++++++++++++++++++++++++++++++++

root = Tk()

mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход")

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь")
helpmenu.add_command(label="О программе")

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

text = Text(width=50, height=15, background = "old lace", foreground = "black")
#text.grid(columnspan=3)
text.grid(rowspan=5, columnspan=3)
#text.grid(row=0, column=0)

#column for number of boxes/pals for SIRIUS===================
textSiriusLabel1 = Label(root, text='№ Строки:')
textSiriusLabel1.grid(row=0, column=2, sticky=E)
textSirius1 = Text(width=3, height=1, background = "old lace", foreground = "black")
textSirius1.grid(row=0, column=3, columnspan=1, sticky=W)
textSirius1Find = Text(width=30, height=1, background = "old lace", foreground = "black")
textSirius1Find.grid(row=0, column=4)
textSiriusFindLabel1 = Label(root, text='<-№ box/palet')
textSiriusFindLabel1.grid(row=0, column=5, sticky=W)

textSiriusLabel2 = Label(root, text='№ Строки:')
textSiriusLabel2.grid(row=1, column=2, sticky=E)
textSirius2 = Text(width=3, height=1, background = "old lace", foreground = "black")
textSirius2.grid(row=1, column=3, columnspan=1, sticky=W)
textSirius2Find = Text(width=30, height=1, background = "old lace", foreground = "black")
textSirius2Find.grid(row=1, column=4)
textSiriusFindLabel2 = Label(root, text='<-№ box/palet')
textSiriusFindLabel2.grid(row=1, column=5, sticky=W)

textSiriusLabel3 = Label(root, text='№ Строки:')
textSiriusLabel3.grid(row=2, column=2, sticky=E)
textSirius3 = Text(width=3, height=1, background = "old lace", foreground = "black")
textSirius3.grid(row=2, column=3, columnspan=1, sticky=W)
textSirius3Find = Text(width=30, height=1, background = "old lace", foreground = "black")
textSirius3Find.grid(row=2, column=4)
textSiriusFindLabel3 = Label(root, text='<-№ box/palet')
textSiriusFindLabel3.grid(row=2, column=5, sticky=W)

textSiriusLabel4 = Label(root, text='№ Строки:')
textSiriusLabel4.grid(row=3, column=2, sticky=E)
textSirius4 = Text(width=3, height=1, background = "old lace", foreground = "black")
textSirius4.grid(row=3, column=3, columnspan=1, sticky=W)
textSirius4Find = Text(width=30, height=1, background = "old lace", foreground = "black")
textSirius4Find.grid(row=3, column=4)
textSiriusFindLabel4 = Label(root, text='<-№ box/palet')
textSiriusFindLabel4.grid(row=3, column=5, sticky=W)

textSiriusLabel5 = Label(root, text='№ Строки:')
textSiriusLabel5.grid(row=4, column=2, sticky=E)
textSirius5 = Text(width=3, height=1, background = "old lace", foreground = "black")
textSirius5.grid(row=4, column=3, columnspan=1, sticky=W)
textSirius5Find = Text(width=30, height=1, background = "old lace", foreground = "black")
textSirius5Find.grid(row=4, column=4)
textSiriusFindLabel5 = Label(root, text='<-№ box/palet')
textSiriusFindLabel5.grid(row=4, column=5, sticky=W)

#==================================

text1 = Label(root, text='Число 1ый столбец:')
text1.grid(row=6, column=0, sticky=E)
numForFirstColumn = Text(width=3, height=1, background = "old lace", foreground = "black")
numForFirstColumn.grid(row=6, column=1, sticky=W)

text2 = Label(root, text='Название файла:')
text2.grid(row=7, column=0, sticky=E)
nameForResultFile = Text(width=30, height=1, background = "old lace", foreground = "black")
nameForResultFile.grid(row=7, column=1, sticky=W)

#entryText = Entry(width=25, height=1)
#entryText.grid(columnspan=3)

b1 = Button(text="Открыть источник кодов", command=openSourceFile)
b1.grid(row=8, sticky=E)

# b2 = Button(text="Окрыть список номеров", command=openListFile)
# b2.grid(row=8, column=1, sticky=W)

# b3 = Button(text="сделать пездато!", command=justDoIt)
# b3.grid(row=8, column=2, sticky=W)

# b4 = Button(text="сделать пездато! с коробками", command=justDoItBoxes)
# b4.grid(row=10, column=1, sticky=W)

# b5 = Button(text="сделать пездато! с палетами", command=justDoItPalettes)
# b5.grid(row=10, column=2, sticky=W)

# b6 = Button(text="Поиск по тексту ( коды )", command=justDoItFromGetText_Codes)
# b6.grid(row=11, column=1, sticky=W)

# b7 = Button(text="Поиск по тексту ( +коробки )", command=justDoItFromGetText_Codes_Boxes)
# b7.grid(row=11, column=2, sticky=W)

# b8 = Button(text="Поиск по тексту ( коробки + палетты )", command=justDoItFromGetText_BoxesPalettes)
# b8.grid(row=11, column=4, sticky=W)

#====NEW=BUTTONS=ADD=DEL=LOAD=SAVE=================================================================================
bLoadDB = Button(text="Load Database", command=openFileDB)
bLoadDB.grid(row=13, column=1, sticky=W)

bSaveDB = Button(text="___Save To Database___", command=saveCurrentTuple_1ToFileDB)
bSaveDB.grid(row=11, column=2, sticky=W)

bAddToDB = Button(text="___Add To Database___", command=justDoItFromGetText_BoxesPalettes)
bAddToDB.grid(row=12, column=2, sticky=W)

bFindInTuple = Button(text="Find in Database \n(tuple_1)", command=findInTuple_1FromTextField)
bFindInTuple.grid(row=13, column=4, sticky=W)

bFindInTupleSirius = Button(text="Find for SIRIUS", command=findInTuple_1FromTextFieldSirius)
bFindInTupleSirius.grid(row=14, column=4, sticky=W)


bDelFromDB = Button(text="Delete Finded Codes From Database", command=justDoItFromGetText_BoxesPalettes)
bDelFromDB.grid(row=10, column=1, sticky=W)



#====================#====================#====================
bTryNewButtonsNumber = Button(text="bTryNewButtons number string \n(tuple_1)", command=commandSiriusString)
bTryNewButtonsNumber.grid(row=12, column=4, sticky=W)

bTryNewButtonsSearch = Button(text="bTryNewButtons SEARCH \n(tuple_1)", command=commandSiriusFind)
bTryNewButtonsSearch.grid(row=11, column=4, sticky=W)
#====================#====================#====================

root.mainloop()
