

import os 







listtree = open("prank_tre.ordN.coll",'r')




path4="hyperlist.csv"
reps4 = open(path4, "w")





files=os.listdir("Neighbors_full")

for f in files:

    fi=f[:-4].split("__")
    print fi
    reps4.write("%s;%s\n" % (fi[0],fi[1]))







# files=os.listdir("Neighbors_prolong")

# for f in files:

#     fi=f[:-4].split("__")
#     print fi
#     reps4.write("%s;%s\n" % (fi[0],fi[1]))



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

    print cr
    
    


    skip=False

    read = listtree.readline().strip()
    if read=='':
        break
    
    sepread=read.split('	')
    anc=sepread[0]
    first=sepread[1].split(';')[0]
    second=sepread[1].split(';')[1]

    print sepread




    

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


    path3="Neighbors_full/%s__%s.csv" % (first,second)
    reps3 = open(path3, "w")







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

                if cur==0:

                    print "YEAH! %s %s" % (ancgenome[cur],genome1[cur])
                    reps3.write("%s;%s;%s;%s;%s\n" % (anc,first,cur,ancgenome[length-2:length]+ancgenome[0:3],genome1[length-2:length+1]+genome1[0:3]))


                if cur==1:

                    print "YEAH! %s %s" % (ancgenome[cur],genome1[cur])
                    reps3.write("%s;%s;%s;%s;%s\n" % (anc,first,cur,ancgenome[length-1:length]+ancgenome[0:4],genome1[length-1:length+1]+genome1[0:4]))



                if len(ancgenome[cur:])==1:

                    print "YEAH! %s %s" % (ancgenome[cur],genome1[cur])
                    reps3.write("%s;%s;%s;%s;%s\n" % (anc,first,cur,ancgenome[length-3:length]+ancgenome[0:2],genome1[length-3:length+1]+genome1[0:2]))


                if len(ancgenome[cur:])==2:


                    print "YEAH! %s %s" % (ancgenome[cur],genome1[cur])
                    reps3.write("%s;%s;%s;%s;%s\n" % (anc,first,cur,ancgenome[length-4:length]+ancgenome[0:1],genome1[length-4:length+1]+genome1[0:1]))


                else:


                    print "YEAH! %s %s" % (ancgenome[cur],genome1[cur])
                    reps3.write("%s;%s;%s;%s;%s\n" % (anc,first,cur,ancgenome[cur-2:cur+3],genome1[cur-2:cur+3]))



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

                if cur==0:

                    print "YEAH! %s %s" % (ancgenome[cur],genome2[cur])
                    reps3.write("%s;%s;%s;%s;%s\n" % (anc,first,cur,ancgenome[length-2:length]+ancgenome[0:3],genome2[length-2:length+1]+genome2[0:3]))


                if cur==1:

                    print "YEAH! %s %s" % (ancgenome[cur],genome2[cur])
                    reps3.write("%s;%s;%s;%s;%s\n" % (anc,first,cur,ancgenome[length-1:length]+ancgenome[0:4],genome2[length-1:length+1]+genome2[0:4]))



                if len(ancgenome[cur:])==1:

                    print "YEAH! %s %s" % (ancgenome[cur],genome2[cur])
                    reps3.write("%s;%s;%s;%s;%s\n" % (anc,first,cur,ancgenome[length-3:length]+ancgenome[0:2],genome2[length-3:length+1]+genome2[0:2]))


                if len(ancgenome[cur:])==2:


                    print "YEAH! %s %s" % (ancgenome[cur],genome2[cur])
                    reps3.write("%s;%s;%s;%s;%s\n" % (anc,first,cur,ancgenome[length-4:length]+ancgenome[0:1],genome2[length-4:length+1]+genome2[0:1]))


                else:


                    print "YEAH! %s %s" % (ancgenome[cur],genome2[cur])
                    reps3.write("%s;%s;%s;%s;%s\n" % (anc,first,cur,ancgenome[cur-2:cur+3],genome2[cur-2:cur+3]))


    cr+=1