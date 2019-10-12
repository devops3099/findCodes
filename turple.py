import re
import pickle

#global tuple_3
#tuple_3 = {}
tuple_1 = {None:{None:[None]}}


def tryAddToTuple( palet, box, code, tuple_1 ):
    #print(' \n !!!!!!!!!!!!!!!!!!!!!!',palet,' -- ', box, ' -- ', code)
    isPaletFinded = False
    isBoxFinded = False
    lengthOfTuple_1 = len(tuple_1)
    if lengthOfTuple_1 == 0:
        if tuple_1[None]:
           # print('lengthOfTuple_1 = ', lengthOfTuple_1)
            tuple_1 = {palet: None}
            #print(' in1 ')
            tuple_1[palet] = {box:None}
            tuple_1[palet][box] = [code]
            tuple_1 = dict(palet={box:[code]})
            #print(' in2 ')
            #print('tuple === ', tuple_1)
        #continue
    if lengthOfTuple_1 > 0:# or lengthOfTuple_1 == 0:
        #print(' IN lengthOfTuple_1 = ', lengthOfTuple_1)
        for cyclePalet in tuple_1:
            if cyclePalet == palet:
                isPaletFinded = True
                for cycleBox in tuple_1[palet]:
                    if cycleBox == box:
                        #print('cycleBox ===== ', cycleBox)
                        isBoxFinded = True
                        tuple_1[cyclePalet][cycleBox] += [code]
                        break
                        
        if isPaletFinded == False and isBoxFinded == False:
            tuple_1[palet] = {box:[code]}
            #tuple_1[palet][box] += [code]
            
        if isBoxFinded == False and isPaletFinded == True:
            tuple_1[palet][box] = []
            tuple_1[palet][box] += [code]
    #print('!!!!!!!   lengthOfTuple_1 = ', len(tuple_1))

#==Sort-Codes-in-tuple_1===========================================================
def sortCodesInTuple_1(tuple_1):
        for i in tuple_1:
            for j in tuple_1[i]:
                tuple_1[i][j].sort(reverse=True)
        print('TUPLE_1 IS SORTED')

list_1 =  [
'2||171200789522001018001ZLDMO6XOMNN7QLKJVWXK6O26NUM3PEH7MK7OZFYQJCSCD77V7247V36YE77VJS7HGYPRHE7NR765GSI4M6R73GDGQF53OJRMFGT2R2RAK2NE67T7T527SDZTQEJWCC7VA||01000000018713119349211524||01000000018723119000012158\n', 
'2||171200789522051018001RRZZD5U37KWDBN6HB5U5OI6YXEUOF27HQCZL3SGGHJKOZYQVRCKBUHLUJ3XMZPV2NZEWLZROZSQHT2IL7Y7JLCBPZFADZKGHF3RVUEPSSCCC4THYZZ6IXSYJMOQWUIFFI||01000000018713119349211524||01000000018723119000012158\n', 
'2||171200789522121018001YFPMCHJO7BQBDT2CT7CYQ2RMDYSEIQGTFVVBOHPXYKNMHAFCWYYOX2DYCBHQOHOLHQGLTKSBOT3OGDDSRLNXV75VNEM5MURHU6IMSFTGURJXEY3IAR62PFMAJPRM7JVSY||01000000018713119349211524||01000000018723119000012158\n', 
'2||171200789522131018001YT7AIRNGK3ZI4RSLQKMSOTETDMLNQCHQPGOBZFS6DCFFI4EVBC7LBPQU5T7UEM5XXJK4SD6ZJULGL5JDIIIQYU7LBHKDOXFIH64OED4DQ4HSAH5R3P5M47WNB6BFZUVRY||01000000018713119349211524||01000000018723119000012158\n',
'2||PLMXPO2JIURJH253ARQFLMMLUE2GO22ZI52LZOMHQKHSXQD6TKK6NY5Q||01000000018713119349211524||01000000018723119000012158\n', 
'1||1702001715922410180016MGZTKFQS762ONZ6FQXZTWOKAISCJ73IZCFM3J25O443WAAGZPTLLHSTQ6OAYRUNUIQ7UIYROUM6QSVZCEOAET4YR2GG4IDKSACIRMI7UGLR7PJQ55ER5JDA6XIFWHUEA||01000000018713119348900934||01000000018723119000012056\n', 
'1||170200171592301018001JA5OQ5SPB2ZPSDZTLNNE3LM344JDZKP3T7BFVOZXC5ZDA3WBFUXIL4XEGIBJ43K6SK3B77QIOSDD3AHBYUYGDPA5INW25PXTLMCZOGJEMZMLC7I4FFJTCRWV7FHRFCQMI||01000000018713119348900934||01000000018723119000012056\n', 
'1||1702001715925810180014KDW4SUA6ZELQRP3UXMQQNYUSAWSCGGZJXLFIEJUMJWDDHK2FNTHG66CFHOIVB5JEQKJL3ZYCBJRCUOWZ7B6ZNAHBZ6CYZL4CO6KFUAMY5UZUGQGRSRV2IX2SWJ6WY6XY||01000000018713119348900934||01000000018723119000012056\n', 
'1||1702001715919210180014ERLFVNVSHXQUEKJM2P3774POEWO24U5CLD3M3IPRUYZWII5UHB5LQGRKFLDF3K6BWBIKM4BJY7GXDDH4ERRXPR3CTG5A56HAH2CPBV4K2I4GC7G2SUGEB732HQSYMK2I||01000000018723119000012056\n',#||01000000018713119348900935\n', 
'1||170200171591941018001EPWWFWBGXAV35NA5WQAKXWXVPUOACMVRGAGVH2Y6R6S7VRRC4XE3HNNOHXEFLWWAYWV334WO5C5B6VDY5DIOPPBC3ZI4KJEPF3JDRW7KKZIVIL6QVNIVUS4UZORXNSOSA||01000000018713119348900935||01000000018723119000012056\n', 
'1||170200171592111018001Y52TELAYA6SB52FBD7D5EQMDEUNSRMNWHLC2SEC77VZZMH3CSC5FELXPXOEMDRBRNK5QE4WINO77JZSQVOB4UAGCUTHFVGVSGGO6M4E4LUOC7GUHY672JUM7VE6V25KJQ||01000000018713119348900935||01000000018723119000012056\n', 
'1||170200171592151018001PWTWLPVNA7N3RNBT7JOKN6GMGACRYU7YF4JYDZEJVIZDXLXVXW6JY3SAJNHZOXE5JGTAJDQJPMFOTV34PDT2VNPNT2FLE2AXFBYASZYHJMPDMH2SRKBD3GQ5YWI3JBYEQ||01000000018713119348900935||01000000018723119000012056\n', 
'4||170200169060741018001GTFCLPQWWHT4GVPDYXDG7BM2L43LJ5M5XGAR5AZJR6HBKI2QRQ735L35QKDQ6URJJGYIP6EYBP2TGW3UJLDN3EMVZDVETZ4UYYXGIWAL2WZSKHNIZVGRPHMCOLSX7KYKI||01000000018723119000012197\n',#||01000000018713119349627272\n', 
'4||170200169060781018001C5RLCU4HRPORHD6U2GBDIKE6OQVUL5XLMIQZ6O2KK7ERXJTLAAXGIDCENA6Q5J7M5DIWZ4OSSOBNFGCV5KMP3MWPHLKXDS7GX3QJ5JZIIJVMO3RSPIDDX2WMUANTQTCBA||01000000018713119349627272||01000000018723119000012197\n', 
'4||170200169060161018001SIEGOUPSRWG6SIGPFSAD342GRALOIYBC2LL2M5YPRKJKA4IGBWU7POH2P3LBDSYN3NHCHQCYK3QXNFBBO6DPOM2PPBFLPMNATAKFDEPFTDVDWITG4PW2T4NSGTT6LBL2Q||01000000018713119349627273||01000000018723119000012197\n', 
'4||170200169060221018001G5T7VWQ5M46EBJNUQKMRLZ2FQUYVPMRK4EOIAQ4XCSM5IT7CML2GIHTYIOCO57UXX7PCRL6F7ZJWDCNYSE6OYB4WTZAMD3IO5Y6GLQ4FTD62K2GPJA6VIVXZ4YEKCD4LY||01000000018713119349627273||01000000018723119000012197\n', 
'4||1702001690605010180013MD3DAUCRXUXZQYMFKRKSDPXOECPOP3DUB6X6K2CMOJ4P4G3ZBAEHOECP54GVPBYCJXFQACXAK3ZU2K2N7QIWG625YUM7OMOFHFZZ4RGX4EJVDTEQ7FHAREOVUZGKN7NA||01000000018713119349627273||01000000018723119000012197\n', 
'4||170200169060511018001NXJ2CRS3AEYKI7NMOQEDNDBQMUCZF4TGPX6QY5GZMX2WR6WLVKKGQG57KWXCCQT23W2UWSUV63RPTV727SB5PIOPZNH52NIJAQGD6LLP64RWGMF2VFF5UNI3FDD5X4M4A||01000000018713119349627273||01000000018723119000012197\n', 
]

# lil code len = 56 / 68 / 
# big code len = 150
# palet = 26
# box = 26

#!!!WRONG STRINGS = 
#                   1)//Выгрузка документа: Товарно-транспортная накладная ЕГАИС (КТ-2000) АЛОО-439 от 19.07.2019 14:36:10
#                       len = 17
#                   2)//По № строки (вар. 3) | ['По', 'строки', 'вар', '3']  
#                       len = 4
#                   3){//№ строки ||        код        ||   алк. продукция   ||справка Б} 
#                       {['строки', 'код', 'алк', 'продукция', 'справка', 'Б']} 
#                       len=6
#                   4)//Строка: 1||0001509000006371466||Напиток слабоалкогольный газированный  "Джин-тоник классический (Gin-tonic classic) 7,2% об.".Объемн||FB-000002461115618
#                       len = 18 || 9

new_list = []

#f = open('forTurple.txt', 'r')
f = open('commonUpdated.txt', 'r')
#f = open('2.txt', 'r')

for i in list_1:
    new_list.append(i)

print('\nFILE OPENED AND COPIED TO CACHE...')
# ______working code for adding to tuples!!
#for lister in list_1:
for lister in f:
    #CHECK IF LIST FULL( 4 ) number code box palet;;; if list ( 3 ): palet = 'noThirdColumn'
    ff = re.findall(r'\w+', lister)
    #print('ff from first func = ', ff)
    #print('all in ff ======', ff[1], ' -- ', ff[2])
    if len(ff) == 4:
        #print('ff = \n', len(ff))
        a_code = ff[1]
        a_box = ff[2]
        a_palet = ff[3]
        tryAddToTuple( a_palet, a_box, a_code, tuple_1)
        #print('len(tuple_1) --------------=', len(tuple_1))
        
    if len(ff) == 3:
        #print('ff = \n', len(ff))
        a_code = ff[1]
        a_box = ff[2]
        a_palet = 'noThirdColumn'
        tryAddToTuple( a_palet, a_box, a_code, tuple_1)



tuple_1.pop(None)
print(' key None has been deleted from tuple_1')
        #print('len(tuple_1) sSSSSSSSSSSSec --------------=', len(tuple_1))
        #palet = ff[3]
    # if len(ff) < 2:
        # continue
 


# _-_-_-_-_-_-working code for adding to tuples!!            

print("END!!")
f.close()
#print('\ntuple_1 =\n', tuple_1)

# for i in tuple_1:
    # print('\n\n1111st level =\n__', tuple_1[i])
    # for j in tuple_1[i]:
        # print('22222 level =\n_____', tuple_1[i][j])


# # _______START_______ COUNT ALL LENGTH
# ss = 0

# for i in tuple_1:
    # #print('\n\ni =',i)
    
    # for j in tuple_1[i]:
        # #print('\n__j =', j)
        # #print('\t_____value = ', tuple_1[i][j])
        # ss += len(tuple_1[i][j])
        # #print("LENGTH = ", ss)

# print("LENGTH = ", ss)
# # END_-_-_-_-_-_ COUNT ALL LENGTH


# # _______START_______find in list_1
# gg = 0
# for i in list_1:
    # dd = re.findall(r'\w+', i)
    
    # if len(dd) == 4:
        # ddd = dd[3]
        # gg += len(tuple_1[ddd])
# print('\n\nD = ', gg)
# # END_-_-_-_-_-_ find in list_1



# # _______START_______check find by 2 paletes
# print('new count =', len(tuple_1['01000000018723119000012065']))
# ee = 0
# for i in tuple_1['01000000018723119000012065']:
    # ee += len(tuple_1['01000000018723119000012065'][i])
# print(ee)

# print('new count =', len(tuple_1['01000000018723119000012206']))

# ee = 0
# for i in tuple_1['01000000018723119000012206']:
    # ee += len(tuple_1['01000000018723119000012206'][i])
# print(ee)
# # END_-_-_-_-_-_ check find by 2 paletes


#======================================
###ttt = open('2.txt', 'r')
##ttt = open('3.txt', 'r')
##
##listfor2txt = []
##for i in ttt:
##    asd = re.findall(r'\w+', i)
##    print('i =', asd[0])
##    #if len(asd) > 20:
##    #listfor2txt += asd
##    listfor2txt.append(asd[0])
##    print('LIST FOR @TXT = ',listfor2txt)
##
##tuple_2 = {}
##
###sorted(tuple_1, key=lambda iindex: student[2])
##
##sorted_tuple_1 = {'1':{'2':[]}}
##
##
##for i in tuple_1:
##   for j in tuple_1[i]:
##            sorted_tuple_1[i] = sorted(tuple_1[i], reverse=True)
##            sorted_tuple_1[i][j] += [sorted(tuple_1[i][j], reverse=True)]
##
###print("tuple_1['01000000018723119000012065'] = ", tuple_1['01000000018723119000012065'])
##
##ee = 0
##for i in listfor2txt:
##    #print('tuple_1[i] =', tuple_1[i])
##    for j in tuple_1[i]:
##        #print('\j = ', j)
##        ee += len(tuple_1[i][j])
##
##print('new ee = ', ee)
##ttt.close
###======================================
##
##ee = 0
##for i in tuple_1:
##    print('\n_____i = ', i)
##    #print('\\tuple_1[i] = ', tuple_1[i])
##    ee += 1
##    for j in tuple_1[i]:
##        print('_____j = ', j)
##    if ee > 6:
##        break
##
##
##f.close()

# finds all in tuple_1[palet]
# for i in hh:
	# sdf = re.findall(r'\w+', str(hh[i]))
	# for j in sdf:
		# kk.write(j + '\n')


#count boxes in palets
##for i in tuple_1:
##	print('\n\n', i, ' --- ',len(tuple_1[i]))
##	for j in tuple_1[i]:
##		if len(str(j)) < 8: continue
##		print('___', j, ' --- ', len(tuple_1[i][j]), '\n', tuple_1[i][j])
        #print("_________", tuple_1[i][j])



count = 0
countPal = 0
for i in tuple_1:
	countPal += len(tuple_1[i])
	for j in tuple_1[i]:
		count += len(tuple_1[i][j])

def listTuple_1_AllValuesAndKeys():
    for i in tuple_1:
        print('\n', i, ' - ', len(tuple_1[i]))
        for j in tuple_1[i]:
            print(' ____', j ,'___', len(tuple_1[i][j]))
            for k in tuple_1[i][j]:
                print('=========', k)



def forPrintToResultFilePalet( palet, box ):
    f_ForPrintToResultFile = open('result.txt', 'w')
    if box == '0':
        gg = tuple_1[palet]
        for i in tuple_1[palet]:
            for j in tuple_1[palet][i]:
                strForWrite = '1' + '||' + j + '||' + i + '||' + palet + '\n'
                f_ForPrintToResultFile.write(strForWrite)
        return 0

    gg = tuple_1[palet][box]
    for i in gg:
        strForWrite = '1' + '||' + i + '||' + box + '||' + palet + '\n'
        f_ForPrintToResultFile.write(strForWrite)
    f_ForPrintToResultFile.close()

def forPrintToResultFileBox( palet, box ):
    f_ForPrintToResultFile = open('resultTRY.txt', 'w')
    if palet == '0':
        #palet = 'noThirdColumn'
        #gg = tuple_1[palet]
        for pal in tuple_1:
            try:
                listCodes = tuple_1[pal][box]
            except KeyError:
                print("ERROR: No such BOX=({}) in PALET=({})".format(box, pal))
                continue
            for j in tuple_1[pal][box]:
                strForWrite = '1' + '||' + j + '||' + box + '||' + pal + '\n'
                f_ForPrintToResultFile.write(strForWrite)
        f_ForPrintToResultFile.close()
        return 0

    try:
        gg = tuple_1[palet][box]
    except KeyError:
        print("ERROR: No such BOX=({}) in PALET=({})".format(box, palet))
        return 0
    for i in gg:
        strForWrite = '1' + '||' + i + '||' + box + '||' + palet + '\n'
        f_ForPrintToResultFile.write(strForWrite)
    f_ForPrintToResultFile.close()
#listTuple_1_AllValuesAndKeys()

fileForParseBoxesOrPaletes = open('44.txt', 'r')

for i in fileForParseBoxesOrPaletes:
    ffpbop = re.findall(r'\w+', i)
    #print(ffpbop)
    forPrintToResultFileBox( ffpbop[0], '0' )



#data = {11028522: 2, 46042277: 17, 398612226: 1033}
sortCodesInTuple_1(tuple_1)
  
# Сохраняем словарь в файл

  
# Читаем словарь из файла
with open('tuple_1.pickle', 'rb') as fLoadFromFile:
   data_new = pickle.load(fLoadFromFile)

fileForParseBoxesOrPaletes.close()  
# Проверяем, что получился действительно словарь, а не строка
#print(data_new[46042277])
  
# Получили результат '17'

##try:
##    print('!!!!!!!!!!!!!!!!!!!!!!!\n', tuple_1['01000000018723119000012056'])
##except KeyError:
##    print('NO SUCH KEY')
