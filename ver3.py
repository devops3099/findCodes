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

global arrForZhazhda025
arrForZhazhda025 = {None:{None:[None]}}

global listForFindedResults
listForFindedResults = {}
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
        #outputOfDirCommand = check_output('ls', shell=True)
        outputOfDirCommand = check_output(['dir','/B'], shell=True)
        print('\n!!!!!', outputOfDirCommand)
        listOfDocFilesNames = []
        b = re.findall('\d{1,6}.doc\w?', str(outputOfDirCommand))
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
        #outputOfDirCommand = check_output('ls', shell=True)
        outputOfDirCommand = check_output(['dir','/B'], shell=True)
        print('\n!!!!!', outputOfDirCommand)
        listOfTXTFilesNames = []
        b = re.findall(r'\d{1,6}.txt', str(outputOfDirCommand))
        listOfTXTFilesNames += b
        print('\n List TXT Files = ',listOfTXTFilesNames)
        return listOfTXTFilesNames
#=====TXT================================
#get text from doc/docx file
def getTextFromTXTFile(filename):
        f = open(filename, 'r')
        txtFile = []
        txtStringg = ''
        for i in f:
                txtFile.append(i)
                txtStringg += i
        f.close()
        return txtStringg #txtFile
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
        print('БАЗА не сформирована или пустая!')#print('tuple_1 не сформирована или пустая!')
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
        print('БАЗА ОТСОРТИРОВАНА!')#print('TUPLE_1 IS SORTED')
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
            a_palet = 'noThirdColumn'
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
#=========================================================================
#=========================================================================
# "Открыть источник кодов" BUTTON
def openSourceFile():
        #global ccounter
        global fileForSource
        #global ccounter_fileOpen
        fileForSource = "0"
        fileForSource = fd.askopenfilename()
        if fileForSource == '':
                print("Файл не выбран!")
        else:
                global tuple_1
                tuple_1 = {None:{None:[None]}}
                print("__название файла: |", fileForSource,'|')#print("fileForSource = ", fileForSource)
                fsource = open(fileForSource, "r")
                tryAddToTuple(fsource)
                fsource.close()
                tuple_1.pop(None)
                #print(' key None has been deleted from tuple_1')
                try:
                        print("коды без палетов _{0}_ + без коробок : ", ( len(tuple_1['noThirdColumn']['onlyCodes'])))
                        print('Кол-во палетов и отдельных коробок ( + 1 [отдельные коды] ) - ', len(tuple_1))
                except KeyError:
                        print('Кол-во палетов и отдельных коробок - ', len(tuple_1))
                        print('кодов без палетов и коробок не найдено')
                        #listTuple_1_AllValuesAndKeys(tuple_1)                

#=========================================================================
#=========================================================================
#=========================================================================
# LOAD DATABASE "Load Database"
def openFileDB():
    #global ccounter
    global nameOfFileDB
    #global ccounter_fileOpen
    nameOfFileDB = "0"
    nameOfFileDB = fd.askopenfilename()
    if nameOfFileDB == '':
        print("|Файл с базой данных не выбран!|")
    else:
        print('|nameOfFileDB = {0}|'.format(nameOfFileDB))
        with open(nameOfFileDB, 'rb') as fLoadFromFile:
            data_new = pickle.load(fLoadFromFile)
        global tuple_1
        tuple_1 = data_new
        print('|{0} opened and saved to "CASH" len = {1}|'.format(nameOfFileDB,len(tuple_1)))

#=========================================================================
#=========================================================================
def findInTuple_1FromTextField():
    #ccounter = 0
    global arrForZhazhda025
    #all_list = []       #ALL FILE list
    if len(tuple_1) < 2:
        #return 'Tuple_1 is empty!'
        print('_____LEN tuple_1 = ',len(tuple_1))
    else:
        print('1111 LEN tuple_1 = ',len(tuple_1))

    #del all_list[:]

    gTFF = re.findall(r'\w+', getTextFromField())
    print('\n__________________\nGTFF = \n_________________', '\n____________________')
    for i in gTFF:
            print('i = ', i)
    print('__________________', '\n__________________')

    arrForZhazhda025 = {None:{None:[None]}}
    #del arrForZhazhda025[:]
    #"""
    funcForFillarrForZhazhda025(gTFF, arrForZhazhda025)
    
    #print('len(arrForZhazhda025) = ', len(arrForZhazhda025))

    currentDate = datetime.datetime.now()
    fullDate = str(currentDate.year) + str(currentDate.month) + str(currentDate.day) + " " + str(currentDate.hour) + "-" + str(currentDate.minute) + "-" + str(currentDate.second)

    fileForResult = getTextForResultFile()
    if fileForResult != '':
        fResult = open(fileForResult + " " + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")
    else:
        fileForResult = 'result'
        fResult = open(fileForResult + " " + str(len(arrForZhazhda025)) + " " + fullDate + '.txt', "w")

    #valueForFirstColumn = getTextForFirstColumn()

    #print("valueForFirstColumn = ", valueForFirstColumn)
    #arrForZhazhda025.pop(None)
    #print('LEN arrForZhazhda025 = \n', len(arrForZhazhda025))
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

#=========================================================================
#=========================================================================
#deleteCodesFromTuple_1('noThirdColumn', '01000000018723119000012056', '1702001715919210180014ERLFVNVSHXQUEKJM2P3774POEWO24U5CLD3M3IPRUYZWII5UHB5LQGRKFLDF3K6BWBIKM4BJY7GXDDH4ERRXPR3CTG5A56HAH2CPBV4K2I4GC7G2SUGEB732HQSYMK2I', tuple_1)
def deleteCodesFromTuple_1(pal, box, code, listFromDelete):
        listFromDelete[pal][box].remove(code)
def deleteBoxesFromTuple_1(pal, box, listFromDelete):
        if len(listFromDelete[pal][box]) == 0:
                del listFromDelete[pal][box]
def deletePalsFromTuple_1(pal, listFromDelete):
        if len(listFromDelete[pal]) == 0:
                del listFromDelete[pal]
#=========================================================================
#=========================================================================
#=========================================================================
def getFirstColumnForSearchSIRIUS( firstColumn ):
        textForFirstColumn = firstColumn.get(1.0, END)
        if textForFirstColumn:
                #print('|textForFirstColumn = ', textForFirstColumn, '|')
                return textForFirstColumn[:-1]

def getTextForSearchingSIRIUS( forSearching ):
        textForSearching = forSearching.get(1.0, END)
        if textForSearching:
                #print('|BOX/PAL: ', textForSearching[:-1], '|')#print('textForSearching = ', textForSearching)
                return textForSearching

def listTuple_1_AllValuesAndKeys(arrForZhazhda025):
    for i in arrForZhazhda025:
        print('\n', i, ' - ', len(arrForZhazhda025[i]))
        for j in arrForZhazhda025[i]:
            print(' ____', j ,'___', len(arrForZhazhda025[i][j]))
            for k in arrForZhazhda025[i][j]:
                print('=========', k)

def forCycleAllSearchFieldSIRIUS(varGTFF, varTextSiriusFind, arrZhazhda,dictDelete):
        varGTFF = re.findall(r'\w+', getTextForSearchingSIRIUS( varTextSiriusFind ))
        funcForFillarrForZhazhda025(varGTFF, dictDelete )

'''
01000000018713119349211524
01000000018713119348900934
01000000018723119000012056
01000000018713119348900935
01000000018713119349627272
'''
def SAVE_TO_FILE_FromFindedList(ffileOPened, ListALL):
        #print('\n\n LIST ALL\n++++++++++++++++++\n', ListALL)
        #listTuple_1_AllValuesAndKeys(ListALL)
        if ffileOPened:
                if ListALL:
                        countResultArr = 0
                        for kkey in ListALL:
                                countResultArr = 0
                                for i in ListALL[kkey]:
                                        for j in ListALL[kkey][i]:
                                                for h in ListALL[kkey][i][j]:
                                                        countResultArr += 1
                                                        #iii = '\t' + h + '\n' #new code!
                                                        if i == 'noThirdColumn':
                                                                iii = str(kkey) + '||' + h + '||' + j + '\n'
                                                        else:
                                                                iii = str(kkey) + '||' + h + '||' + j + '||' + i + '\n'
                                                        ffileOPened.write(iii)
                                print("|", str(kkey), " ВСЕГО : ", countResultArr, ' ', len(ListALL[kkey]), '|')
                                #print("\nВСЕГО :", countResultArr, ' ', len(ListALL[kkey]))
                                
                                listTuple_1_AllValuesAndKeys(ListALL)
                                print('________________________________')
                else:
                        print('|СПИСОК НАЙДЕННОГО ПУСТ|')
                ffileOPened.close()
        else:
                print('|Файл для сохранения не открыт|')
        


def copyToListForFindedResultsSIRIUS(whatToCopy, varTextSiriusX):
        global listForFindedResults
        #listForFindedResults = {}
        whatFirstColumn = getFirstColumnForSearchSIRIUS( varTextSiriusX )
        listForFindedResults[whatFirstColumn] = whatToCopy

#_______________________________________________________________________________________________________
#_______________________________________________________________________________________________________
# main for NEW find SIRIUS# main for NEW find SIRIUS# main for NEW find SIRIUS# main for NEW find SIRIUS
def findInTuple_1FromTextFieldSiriusNew():
        global listForFindedResults
        global arrForZhazhda025
        if len(tuple_1) < 2:
                print('_____LEN tuple_1 = ',len(tuple_1))
        else:
                print('1111 LEN tuple_1 = ',len(tuple_1))

        global dictForDelete
        arrForZhazhda025 = {None:{None:[None]}}
        dictForDelete = {None:{None:[None]}}
        listForFindedResults = {}
        
        gTFF = []#FOR 
        #ARRZHAZHDA LIST FOR FINDED CODES + PALS + BOXES (ARRFORZHAZHDA025))!!!!!!!!!!!!!!!!
        #ARRZHAZHDA LIST FOR FINDED CODES + PALS + BOXES (ARRFORZHAZHDA025))!!!!!!!!!!!!!!!!
        forCycleAllSearchFieldSIRIUS(gTFF, textSirius1Find, arrForZhazhda025, dictForDelete)
        copyToListForFindedResultsSIRIUS(arrForZhazhda025, textSirius1)
        
        forCycleAllSearchFieldSIRIUS(gTFF, textSirius2Find, arrForZhazhda025, dictForDelete)
        copyToListForFindedResultsSIRIUS(arrForZhazhda025, textSirius2)

        forCycleAllSearchFieldSIRIUS(gTFF, textSirius3Find, arrForZhazhda025, dictForDelete)
        copyToListForFindedResultsSIRIUS(arrForZhazhda025, textSirius3)

        forCycleAllSearchFieldSIRIUS(gTFF, textSirius4Find, arrForZhazhda025, dictForDelete)
        copyToListForFindedResultsSIRIUS(arrForZhazhda025, textSirius4)

        forCycleAllSearchFieldSIRIUS(gTFF, textSirius5Find, arrForZhazhda025, dictForDelete)
        copyToListForFindedResultsSIRIUS(arrForZhazhda025, textSirius5)
		
        forCycleAllSearchFieldSIRIUS(gTFF, textSirius6Find, arrForZhazhda025, dictForDelete)
        copyToListForFindedResultsSIRIUS(arrForZhazhda025, textSirius6)
		
        forCycleAllSearchFieldSIRIUS(gTFF, textSirius7Find, arrForZhazhda025, dictForDelete)
        copyToListForFindedResultsSIRIUS(arrForZhazhda025, textSirius7)
		
        forCycleAllSearchFieldSIRIUS(gTFF, textSirius8Find, arrForZhazhda025, dictForDelete)
        copyToListForFindedResultsSIRIUS(arrForZhazhda025, textSirius8)
        
        print('len(arrForZhazhda025) = ', len(arrForZhazhda025))
        print('len(listForFindedResults) = ', len(listForFindedResults))
        ddddd = len(dictForDelete)
        print('|len(dictForDelete) = ', len(dictForDelete), '|')
        currentDate = datetime.datetime.now()
        fullDate = str(currentDate.year) + "_" + str(currentDate.month) + "_" + str(currentDate.day) + " " + str(currentDate.hour) + "-" + str(currentDate.minute) + "-" + str(currentDate.second)

        fileForResult = getTextForResultFile()
        if fileForResult != '':
                fResult = open(fileForResult + " " + str(len(listForFindedResults)) + " " + fullDate + '.txt', "w")
                SAVE_TO_FILE_FromFindedList(fResult, listForFindedResults)
        else:
                fileForResult = 'result'
                fResult = open(fileForResult + " " + str(len(listForFindedResults)) + " " + fullDate + '.txt', "w")
                SAVE_TO_FILE_FromFindedList(fResult, listForFindedResults)

##        arrForZhazhda025.pop(None)
##        dictForDelete.pop(None)
        print('LEN arrForZhazhda025 = \n', len(arrForZhazhda025))
        #print('arrForZhazhda025 = \n', arrForZhazhda025)
        
##        SAVE_TO_FILE_FromFindedList(fResult, listForFindedResults)
#=========================================================================

def funcForFillarrForZhazhda025(listGTFF, arrDelete):#arrZhazhda list for finded CODES + PALS + BOXES (arrForZhazhda025)
        global arrForZhazhda025
        global dictForDelete
        arrForZhazhda025 = {None:{None:[None]}}
        if listGTFF:
                for i in listGTFF:
                        strForCurrent = ''
                        if i in tuple_1:# if palet is finded
                                for h in tuple_1[i]:
                                        for g in tuple_1[str(i)][str(h)]:
                                                functionForTryAddToTuple( i, h , g, arrForZhazhda025 )
                                                functionForTryAddToTuple( i, h , g, arrDelete )
                                                #arrZhazhda.append(tuple_1[i])
                                                strForCurrent = i + ' is finded! '
                        else:
                                for j in tuple_1:
                                        if i in tuple_1[j]:
                                                for g in tuple_1[j][i]:
                                                        functionForTryAddToTuple( j, i , g, arrForZhazhda025 )
                                                        functionForTryAddToTuple( j, i , g, arrDelete )
                                        else:
                                                strForCurrent = 'No such {} box or palet'.format(i)
                        r = 'noThirdColumn'
                        for g in tuple_1[r]:
                                if g == i:
                                        for cc in tuple_1[r][g]:
                                                functionForTryAddToTuple( r, g , cc, arrForZhazhda025 )
                                                functionForTryAddToTuple( r, g , cc, arrDelete )
                                        #arrZhazhda.append(tuple_1[i])
                                        strForCurrent = i + ' is finded! '
        arrForZhazhda025.pop(None)
##        dictForDelete.pop(None)
                                                
        # if strForCurrent != '':
            # print(strForCurrent)
#+++++++++++++++++++++++++++++++++++++++++++++++++++
# save text for name result file
def getTextForResultFile():
    rr = nameForResultFile.get(1.0, END)
    return rr[:-1]
#+++++++++++++++++++++++++++++++++++++++++++++++++++
# save text for SIRIUS number strings and values for searching
def getTextForSIRIUSstring(numberOfString):
        nOS = numberOfString.get(1.0, END)
        if nOS:
                print(nOS[:-1])
                return nOS[:-1]
        
def getTextForSIRIUSFind(searchString):
        tSOF = searchString.get(1.0, END)
        if tSoF:
                print(tSOF[:-1])
                return tSOF[:-1]

##def getAllTextForSearchSIRIUStest():
##        textForFirstColumn1 = textSirius1.get(1.0, END)
##        textForSearching1 = textSirius1Find.get(1.0, END)
##        textForFirstColumn2 = textSirius2.get(1.0, END)
##        textForSearching2 = textSirius2Find.get(1.0, END)
##        textForFirstColumn3 = textSirius3.get(1.0, END)
##        textForSearching3 = textSirius3Find.get(1.0, END)
##        textForFirstColumn4 = textSirius4.get(1.0, END)
##        textForSearching4 = textSirius4Find.get(1.0, END)
##        textForFirstColumn5 = textSirius5.get(1.0, END)
##        textForSearching5 = textSirius5Find.get(1.0, END)


'''
getAllTextForSearchSIRIUS(textForFirstColumn1, textForSearching1)
getAllTextForSearchSIRIUS(textForFirstColumn2, textForSearching2)
getAllTextForSearchSIRIUS(textForFirstColumn3, textForSearching3)
getAllTextForSearchSIRIUS(textForFirstColumn4, textForSearching4)
getAllTextForSearchSIRIUS(textForFirstColumn5, textForSearching5)
'''
def commandSiriusString():
    getTextForSIRIUSstring(textSirius1)

def commandSiriusFind():
    getTextForSIRIUSFind(textSirius1Find)
#+++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++
# Сделать пездато! (поиск по папке среди *.doc => вывод только КОДЫ
def justDoIt():
    print('in development')
#+++++++++++++++++++++++++++++++++++++++++++++++++++

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
text.grid(rowspan=8, columnspan=3)
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

textSiriusLabel6 = Label(root, text='№ Строки:')
textSiriusLabel6.grid(row=5, column=2, sticky=E)
textSirius6 = Text(width=3, height=1, background = "old lace", foreground = "black")
textSirius6.grid(row=5, column=3, columnspan=1, sticky=W)
textSirius6Find = Text(width=30, height=1, background = "old lace", foreground = "black")
textSirius6Find.grid(row=5, column=4)
textSiriusFindLabel6 = Label(root, text='<-№ box/palet')
textSiriusFindLabel6.grid(row=5, column=5, sticky=W)

textSiriusLabel7 = Label(root, text='№ Строки:')
textSiriusLabel7.grid(row=6, column=2, sticky=E)
textSirius7 = Text(width=3, height=1, background = "old lace", foreground = "black")
textSirius7.grid(row=6, column=3, columnspan=1, sticky=W)
textSirius7Find = Text(width=30, height=1, background = "old lace", foreground = "black")
textSirius7Find.grid(row=6, column=4)
textSiriusFindLabel7 = Label(root, text='<-№ box/palet')
textSiriusFindLabel7.grid(row=6, column=5, sticky=W)

textSiriusLabel8 = Label(root, text='№ Строки:')
textSiriusLabel8.grid(row=7, column=2, sticky=E)
textSirius8 = Text(width=3, height=1, background = "old lace", foreground = "black")
textSirius8.grid(row=7, column=3, columnspan=1, sticky=W)
textSirius8Find = Text(width=30, height=1, background = "old lace", foreground = "black")
textSirius8Find.grid(row=7, column=4)
textSiriusFindLabel8 = Label(root, text='<-№ box/palet')
textSiriusFindLabel8.grid(row=7, column=5, sticky=W)
#==================================

##text1 = Label(root, text='Число 1ый столбец:')
##text1.grid(row=6, column=0, sticky=E)
#numForFirstColumn = Text(width=3, height=1, background = "old lace", foreground = "black")
#numForFirstColumn.grid(row=6, column=1, sticky=W)



logInfotext1 = Label(root, text='forDelete:')
logInfotext1.grid(row=8, column=0, sticky=E)
logInfo = Label(text='werwer', width=30, height=1, background = "red", foreground = "black")
logInfo.grid(row=8, column=1, sticky=W)


text2 = Label(root, text='Название файла:')
text2.grid(row=9, column=0, sticky=E)
nameForResultFile = Text(width=30, height=1, background = "old lace", foreground = "black")
nameForResultFile.grid(row=9, column=1, sticky=W)

#entryText = Entry(width=25, height=1)
#entryText.grid(columnspan=3)

b1 = Button(text="Открыть источник кодов", command=openSourceFile)
b1.grid(row=10, sticky=E)

# b3 = Button(text="сделать пездато!", command=justDoIt)
# b3.grid(row=8, column=2, sticky=W)

#====NEW=BUTTONS=ADD=DEL=LOAD=SAVE=================================================================================
bLoadDB = Button(text="Load Database", command=openFileDB)
bLoadDB.grid(row=13, column=1, sticky=W)

bSaveDB = Button(text="___Save To Database___", command=saveCurrentTuple_1ToFileDB)
bSaveDB.grid(row=11, column=2, sticky=W)

bAddToDB = Button(text="___Add To Database___", command=justDoIt)
bAddToDB.grid(row=12, column=2, sticky=W)

bFindInTuple = Button(text="ПОИСК КОДОВ", command=findInTuple_1FromTextField)
bFindInTuple.grid(row=13, column=4, sticky=W)

##bFindInTupleSirius = Button(text="Find for SIRIUS", command=findInTuple_1FromTextFieldSirius)
##bFindInTupleSirius.grid(row=14, column=4, sticky=W)


bDelFromDB = Button(text="Delete Finded Codes From Database", command=justDoIt)
bDelFromDB.grid(row=10, column=1, sticky=W)



#====================#====================#====================
bTryNewButtonsNumber = Button(text="ПОИСК СИРИУС", command=findInTuple_1FromTextFieldSiriusNew)
bTryNewButtonsNumber.grid(row=12, column=4, sticky=W)

bTryNewButtonsSearch = Button(text="bTryNewButtons SEARCH \n(tuple_1)", command=commandSiriusFind)
bTryNewButtonsSearch.grid(row=11, column=4, sticky=W)
#====================#====================#====================


root.mainloop()
