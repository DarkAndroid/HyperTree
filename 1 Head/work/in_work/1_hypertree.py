

import os 


import requests

import urllib2
from bs4 import BeautifulSoup




listtree = open("prank_tre.ordN.coll",'r')



path3="Replacements.txt"
reps3 = open(path3, "w")



#for r in range(1,maxid+1):

cr=1

# while True: 

#     print cr
#     cr+=1

#     read = listtree.readline().strip()
#     if read=='':
#         break
    
#     sepread=read.split('	')
#     anc=sepread[0]
#     first=sepread[1].split(';')[0]
#     second=sepread[1].split(';')[1]

#     if sepread[1] == "13287;16549":
#     	break


while True: 

    print cr
    cr+=1
    

    read = listtree.readline().strip()
    if read=='':
        break
    
    sepread=read.split('	')
    anc=sepread[0]
    first=sepread[1].split(';')[0]
    second=sepread[1].split(';')[1]

    print sepread




    ancali = open("ASR.raxml.reduced.prank.anconly.fas",'r')



    pr=1
        
    ancgenome = ""

    #for n in range(10):
    while True:
        #print pr
        name = ancali.readline().strip()[1:]
        if name == "":
            # print "END"    
            break
        genome = ancali.readline().strip()
            
        #print name

        if name == anc:
            # print "Second"
            
            ancgenome=genome
            break

        pr=pr+1   


    #print ancgenome



    #### FIRST with Ancestor

    aligment2 = open("ASR.raxml.reduced.prank.anconly.fas",'r')
    aligment1 = open("RefAli.fa",'r')


    #print "%s." % first

    if "_" in first:
    	
    	pr=1
		
    	genome1 = ""

		#for n in range(10):
    	while True:
    	    #print pr
     	    name = aligment1.readline().strip()[1:]
     	    #print "-----%s.\r" % name,
    	    if name == "":
    	        # print "END"    
    	        break
    	    genome= aligment1.readline().strip()
		    
            #print name

            if name == first:
            	# print "First"
                genome1=genome
                break
            pr=pr+1
    
    else:

    	pr=1
		
    	genome1 = ""

		#for n in range(10):
    	while True:
    	    #print pr
     	    name = aligment2.readline().strip()[1:]
     	    #print "-----%s" % name
    	    if name == "":
    	        # print "END"    
    	        break
    	    genome= aligment2.readline().strip()
		    
            #print name

            if name == first:
            	# print "First"
                genome1=genome
                break

    	    pr=pr+1

    

    ################################################################################

    # print second

    aligment2 = open("ASR.raxml.reduced.prank.anconly.fas",'r')
    aligment1 = open("RefAli.fa",'r')


    if "_" in second:
    	
    	pr=1
		
    	genome2 = ""

		#for n in range(10):
    	while True:
    	    #print pr
     	    name = aligment1.readline().strip()[1:]
    	    if name == "":
    	        # print "END"    
    	        break
    	    genome= aligment1.readline().strip()
		    
            #print name

            if name == second:
            	# print "Second"
                genome2=genome
                break
            pr=pr+1
    
    else:

    	pr=1
		
    	genome2 = ""

		#for n in range(10):
    	while True:
    	    #print pr
     	    name = aligment2.readline().strip()[1:]
    	    if name == "":
    	        # print "END"    
    	        break
    	    genome= aligment2.readline().strip()
		    
            #print name

            if name == second:
            	# print "Second"
                genome2=genome
                break

    	    pr=pr+1   










    # print genome1[:20] 
    # print genome2[:20] 
    #reps3.write ("%s\n" % (read))


    length=len(ancgenome)




    if ancgenome == genome1:
        print "SKIP"

    else:

        #print genome1[:10] 
        #print genome2[:10] 

        

        if len(ancgenome) == len(genome1):
            print "EQUAL"
        else:
            print "MOTHERFUCKAAAAAAA"

        
        for cur in range(length):
            #print "%s %s" % (genome1[cur],genome2[cur])
            #print "%s\r" % cur,
            #print "%s" % cur
            if ancgenome[cur] != genome1[cur]:

                if len(ancgenome[cur:])!=1:

                    print "YEAH! %s %s" % (ancgenome[cur],genome1[cur])
                    reps3.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (anc,first,cur,ancgenome[cur-1],ancgenome[cur],ancgenome[cur+1],genome1[cur-1],genome1[cur],genome1[cur+1]))

                else:

                    print "YEAH! %s %s" % (ancgenome[cur],genome1[cur])
                    reps3.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (anc,first,cur,ancgenome[cur-1],ancgenome[cur],ancgenome[0],genome1[cur-1],genome1[cur],genome1[0]))



    if ancgenome == genome2:
    	print "SKIP"

    else:

        #print genome1[:10] 
        #print genome2[:10] 


        if len(ancgenome) == len(genome2):
            print "EQUAL"
        else:
            print "MOTHERFUCKAAAAAAA"

        
        for cur in range(length):
	        #print "%s %s" % (genome1[cur],genome2[cur])
            #print "%s\r" % cur,
	        #print "%s" % cur
            if ancgenome[cur] != genome2[cur]:

                if len(ancgenome[cur:])!=1:

                    print "YEAH! %s %s" % (ancgenome[cur],genome2[cur])
                    reps3.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (anc,second,cur,ancgenome[cur-1],ancgenome[cur],ancgenome[cur+1],genome2[cur-1],genome2[cur],genome2[cur+1]))

                else:

                    print "YEAH! %s %s" % (ancgenome[cur],genome2[cur])
                    reps3.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (anc,second,cur,ancgenome[cur-1],ancgenome[cur],ancgenome[0],genome2[cur-1],genome2[cur],genome2[0]))



