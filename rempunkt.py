
import codecs
#import csv

def RemovePunctuation(str):
    set = {"-",",",".","?","!",":",";","[","]","(",")","*","!","@",'"', "'",'\n','\r'," ",'…','0','1','2','3','4','5','6','7','8','9','»','«','>','¿','·'}
    str1 = "" #new string where we put only letters
    for i in str:
        if i not in set:
            str1 = str1 + i
    str1 = str1.lower()#all lower to count letters no metter lower or higher case
    return str1

def CountLetters(str):
    dic = {}
    str1 = RemovePunctuation(str)
    for i in str1:
        if i == 'ď':
            dic['d'] = dic['d'] + 1
        elif i in dic:
            dic[i] = dic[i] +1
        else:
            dic[i]=1
    SortVal(dic)
    return dic

def procent(x,y):
    procent = (x/y)*100%
    return procent

def SortVal(dic):
    sorted_values = sorted(dic.values(),reverse=True)
    sorted_dic = {}
    for i in sorted_values:
        for k in dic.keys():
            if dic[k] == i:
                sorted_dic[k] = dic[k]
                break
    print(sorted_dic)
    return sorted_dic

#def CreateCsv(dic,str):
    #with open('language.csv','w',newline='') as file:
        #writer = csv.writer(file)
        #writer.writerow(["Language", "Letter", "Amount"])
        #for (key,value) in dic.items():
            #writer.writerow([str,value, key])
    #return 'language.csv'

str = input("""Enter a language code
     EN for english
     DE for german
     ES for spanish
     VI for vietnamese
     LT for lithuanian
     EL for greek""")

str = str.upper()
str = str + ".txt"
if (str == "EN.txt" or str == "DE.txt" or str == "VI.txt" or str == "ES.txt" or str == "LT.txt"or str == "EL.txt"):
    f = codecs.open(str,"r", 'utf8')
else:
    print("""Choose a correct language code:
    EN for english
    DE for german
    ES for spanish
    VI for vietnamese
    LT for lithuanian
    EL for greek""")

st = ""
for line in f:
    if (len(line)> 5): #excluding romes numbering I,II t/m XXVII
        line.strip().split(':')
        st = st + line

dic = CountLetters(st)

#CreateCsv(dic,st)
