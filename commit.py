#!/bin/python3

import sys

keyword=("alignas","alignof","and","and_eq","asm","atomic_cancel","atomic_commit","atomic_noexcept","auto","bitand","bitor","bool","break","case","catch","char","char16_t","char32_t","class","compl","concept","const","constexpr","const_cast","continue","co_await","co_return","co_yield","decltype","default","delete","do","double","dynamic_cast","else","enum","explicit","export","extern","false","float","for","friend","goto","if","import","inline","int","long","module","mutable","namespace","new","noexcept","not","not_eq","nullptr","operator","or","or_eq","private","protected","public","register","reinterpret_cast","requires","return","short","signed","sizeof","static","static_assert","static_cast","struct","switch","synchronized","template","this","thread_local","throw","true","try","typedef","typeid","typename","union","unsigned","using","virtual","void","volatile","wchar_t","while","xor","xor_eq")

punctuators=("[","]","(",")","{","}",",",";","#",":",'"',"!","'")

identifires=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

operators=("+","++","==","=",">>",">","<","<<","-","--")


keyworditp=list()
punctuatorsitp=list()
identifiresitp=list()
constantsitp=list()
operatorsitp=list()
stringitp=list()

def lexim(z):
    a=len(z)
    b=0
    c=str()
    list1=list()
    while(b<a):
        if(z[b]=='#' or z[b]=='<' or z[b]=='(' or z[b]=='{' or z[b]=='[' or z[b]=='>' or z[b]==')' or z[b]=='}' or z[b]==']' or z[b]==' 'or z[b]==';' or z[b]=='\n' or z[b]=='"' or z[b]=='\t' or z[b]=='+' or z[b]==',' or z[b]=='=' or z[b]==':' or z[b]=='/' or z[b]=='!'):
            if(c!=" " or c!=""):
                list1.append(c)
                list1.append(z[b])  
            c=""
            if(z[b]=='+'):
                list1=check_and_remove('+','+',list1)
            elif(z[b]=='<'):
                list1=check_and_remove('<','<',list1)
            elif(z[b]=='>'):
                list1=check_and_remove('>','>',list1)
            elif(z[b]=='-'):
                list1=check_and_remove('-','-',list1)
            elif(z[b]=='='):
                list1=check_and_remove('=','=',list1)
            elif(z[b]=='/'):
                list1.pop()
                if(list1[-2]=="/"):
                    list1.pop()
                    list1.pop()
                    while(z[b]!='\n'):
                        b=b+1
                else:
                    list1.append('/')
            elif(z[b]=='"'):
                b+=1
                c="\\"
                while(z[b]!='"'):
                    c=c+z[b]
                    b+=1
                list1.append(c)
                c=""
                list1.append(z[b])
                b+=1
        else:
            c=c+z[b]
        b+=1
    list1.remove(" ")
    return list1


def check_and_remove(c,p,listtc):
    listtc.pop()
    if(listtc[-2]==p):
        listtc.pop()
        listtc.pop()
        s=c+p
        listtc.append(s)
    else:
        listtc.append(c)
    return listtc


def find_keyword(z):
    if(z in keyword):
        keyworditp.append(z)


def find_punctuators(z):
    if(z in punctuators):
        punctuatorsitp.append(z)


def find_identifires(z):
    if(z[0] in identifires):
        identifiresitp.append(z)


def find_operators(z):
    if(z[0] in operators):
        operatorsitp.append(z)


def find_string(z):
    if(z[0:1]=='\\'):
        stringitp.append(z)


def find_constants(z):
    try:
        x=int(z)
        constantsitp.append(z)
    except:
        try:
            x=float(z)
            constantsitp.append(z)
        except:
            x=10



a=sys.argv[1]
f=open(a,"r")
b=f.read()
f.close()
lexims=lexim(b)
e=1
print(type(lexims[1]))
list2=list()
for word in lexims:
    if(word==" " or word == "" or word == "\n" or word == "\t"):
        continue
    else:
        list2.append(word)
        print(str(e) + " " + word,end=" ")
    e+=1
print("\n\n\n\n\n")
print(list2)
for word in list2:
    find_keyword(word)
for word in list2:
    find_punctuators(word)
for word in keyworditp:
    try:
        list2.remove(word)
    except:
        continue
for word in list2:
    find_identifires(word)
for word in list2:
    find_constants(word)
for word in punctuatorsitp:
    try:
        list2.remove(word)
    except:
        continue
for word in identifiresitp:
    try:
        list2.remove(word)
    except:
        continue
for word in constantsitp:
    try:
        list2.remove(word)
    except:
        continue
for word in list2:
    find_operators(word)
for word in operatorsitp:
    try:
        list2.remove(word)
    except:
        continue
for word in list2:
    find_string(word)
for word in stringitp:
    try:
        list2.remove(word)
    except:
        continue
print("\n\nKeywords - ")
print(keyworditp)
print("Number Of Keyword : "+str(len(keyworditp)))
print("\n\nPunctuators - ")
print(punctuatorsitp)
print("Number Of Punctuators : "+str(len(punctuatorsitp)))
print("\n\nIdentifires - ")
print(identifiresitp)
print("Number Of Identifires : "+str(len(identifiresitp)))
print("\n\nConstants - ")
print(constantsitp)
print("Number Of Constants : "+str(len(constantsitp)))
print("\n\nOperators - ")
print(operatorsitp)
print("Number Of Operators : "+str(len(operatorsitp)))
print("\n\nStrings - ")
print(stringitp)
print("Number Of Strings : "+str(len(stringitp)))
