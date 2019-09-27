

import os 


import requests

import urllib2
from bs4 import BeautifulSoup




src = open("Replacements.txt",'r')


path3="ReplacementsNOgaps.txt"
reps3 = open(path3, "w")



#for r in range(1,maxid+1):

while True: 

    read = src.readline().strip()
    if read=='':
        break
    
    sep=read.split(";")

    if sep[4]!="-" and sep[7]!="-":

        reps3.write ("%s\n" % (read))


