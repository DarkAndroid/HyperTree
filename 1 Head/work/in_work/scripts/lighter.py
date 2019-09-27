

import os 


import requests

import urllib2
from bs4 import BeautifulSoup




src = open("refgenes.gb.gff",'r')


path3="refgenes.gb.gff.Truncated"
reps3 = open(path3, "w")



#for r in range(1,maxid+1):

while True: 

    read = src.readline().strip()
    if read=='':
        break
    
    sep=read.split("	")
     
    if  sep[2]!="STS" and sep[2]!="CDS" and sep[2]!="gene" and sep[2]!="exon" and sep[2]!="region": #and sep[2]!="STS"
        print sep[2]+" "+sep[3]+" "+sep[4]

    # if sep[3]!="-" and sep[4]!="-":

        reps3.write ("%s	%s	%s	%s	%s	%s	%s	%s\n" % (sep[0],sep[1],sep[2],sep[3],sep[4],sep[5],sep[6],sep[7]))


