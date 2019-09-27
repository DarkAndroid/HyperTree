

import os 







listtree = open("iqtree_tre.ordN.coll.pathS",'r')




path4="hyperlist.csv"
reps4 = open(path4, "w")





files=os.listdir("Neighbors")

for f in files:

    fi=f[:-4].split("__")
    print fi
    reps4.write("%s;%s\n" % (fi[0],fi[1]))



reps4.close()






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

    skip=False

    print cr
    cr+=1
    

    read = listtree.readline().strip()
    if read=='':
        break
    
    #print read
    hread=read.split('	')
    print hread

    try:
        sepread=hread[1].split('__')
    except:
        print "NO HAPLO"


    
    for pair in range(len(sepread)-1):

 
        first=sepread[pair]
        second=sepread[pair+1]


        hlist = open("hyperlist.csv",'r')


        while True: 

            lread = hlist.readline().strip()
            if lread=='':  
                break
            if lread==first+";"+second:  
                skip=True
                break


        if skip:
            break

        reps4 = open(path4, "a")
        reps4.write("%s;%s\n" % (first,second))
        reps4.close()


        print "%s  %s" % (first,second)


        path3="Neighbors/%s__%s.csv" % (first,second)
        reps3 = open(path3, "w")


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
                #print "--%s--%s--%s" % (name,first,name==first)
                if name == "":
                    print "END"    
                    break
                genome= aligment1.readline().strip()
    		    
                #print name

                if name == first:
                    #print "First1"
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
                    #print "First2"
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
                    #print "Second1"
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
                    #print "Second2"
                    genome2=genome
                    break

                pr=pr+1   










        # print genome1[:20] 
        # print genome2[:20] 
        #reps3.write ("%s\n" % (read))


        length=len(genome1)




        if genome1 == genome2:
            print "SKIP"

        else:

            #print genome1[:10] 
            #print genome2[:10] 

            

            if len(genome1) == len(genome2):
                print "EQUAL"
            else:
                print "MOTHERFUCKAAAAAAA"

            
            for cur in range(length):
                #print "%s %s" % (genome1[cur],genome2[cur])
                #print "%s\r" % cur,
                #print "%s" % cur
                if genome1[cur] != genome2[cur] and genome1[cur]!="-" and genome2[cur]!="-" and genome1[cur]!="N" and genome2[cur]!="N":

                    if len(genome1[cur:])!=1:

                        print "YEAH! %s %s" % (genome1[cur],genome2[cur])
                        reps3.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (first,second,cur,genome1[cur-1],genome1[cur],genome1[cur+1],genome2[cur-1],genome2[cur],genome2[cur+1]))

                    else:

                        print "YEAH! %s %s" % (genome1[cur],genome2[cur])
                        reps3.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (first,second,cur,genome1[cur-1],genome1[cur],genome1[0],genome2[cur-1],genome2[cur],genome2[0]))





