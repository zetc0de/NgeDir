#!/usr/bin/env python3
#
#=============================
# 31 Agustus 2018
# Author : @zetc0de
# NgeSec | https://ngesec.id
#=============================

import sys
import requests

CRED = '\033[91m'
CGREEN = '\033[32m'
CCLEAR = '\033[0m'

print("""%s
         _  __         ___  _    
        / |/ /__ ____ / _ \(_)___
       /    / _ `/ -_) // / / __/
      /_/|_/\_, /\__/____/_/_/   
           /___/ %s _______v1 %s                
""" %(CGREEN,CRED,CCLEAR)) 


if len(sys.argv) != 3:
    print("%s [%s+%s] Usage     : ./ngedir.py list.txt checklist.txt %s" %(CGREEN,CRED,CGREEN,CCLEAR))
    print("%s [%s+%s] Author    : @zetc0de %s" %(CGREEN,CRED,CGREEN,CCLEAR))
    print("%s [%s+%s] Version   : v1 Made with <3 %s\n" %(CGREEN,CRED,CGREEN,CCLEAR))
    sys.exit()


lists = sys.argv[1]
target = open(lists,'r')
target = target.read().split('\n')

cek = sys.argv[2]
ceks = open(cek,'r')
ceks = ceks.read().split('\n') 

def hasil(r):
    if r.status_code in [200,301] and "html" not in r.text : print(r.url,CGREEN + ' [FOUND]' + CCLEAR)
    else: print(r.url,CRED + ' [NOT FOUND]' + CCLEAR)

def checking(i,j):
        r = requests.get('http://'+i+'/'+j)
        hasil(r)
def checking2(i,j):
        r = requests.get(i+'/'+j)
        hasil(r)
print("============================================")
for i in target:
    if i != '':
        for j in ceks:
             if j != '':
                if 'http' not in i:
                    checking(i,j)
                else: 
                    checking2(i,j)


#for i in target:
#    if i != '':
#        for j in ceks:   
#            if j != '':
#                if 'http' not in i:
#                    #i = 'http://'+i+'/'+j
#                    r = requests.get('http://'+i+'/'+j)
                    #print(r.url,' :',r.status_code)
#                    if r.status_code == 200:
#                        print(r.url,' [VULNERABLE]')
#                    else: print(r.url,' [NOT VULNERABLE]')



