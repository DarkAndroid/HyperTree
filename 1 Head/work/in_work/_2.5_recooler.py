

import os 







# listtree = open("ReplacementsNOgaps.txt",'r')



# path3="ReplacementsTrueNOgaps.txt"
# reps3 = open(path3, "w")

folder="FilledN"
files=os.listdir(folder)
prepath=(folder+"/")
# prepath=("%s/" % (sys.argv[1]))
# pgen_path = sys.argv[2]


for f in files:
    print f

    listtreeIn = open(prepath+f,'r')

    listtreeOut = open("Filled5/"+f,'w')


    #reps3.write("first;second;position;pos_ref_in_ali;pos_ref_gb;left_from_neighbor;nuc_from;right_from_neighbor;left_to_neighbor;nuc_to;right_to_neighbor;nuc_ref_in_ali;nuc_ref_gb;shift_from_last_ref_pos;gene_info\n")





    first=f[:-4].split("__")[0]
    second=f[:-4].split("__")[1]





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













    cr=1


    while True: 

        print cr
        cr+=1
	    

        read1 = listtreeIn.readline().strip()
        if read1=='':
            break
	    
        s1=read1.split(';')

	    #print s1

        listtreeOut.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (s1[0],s1[1],s1[2]   ,s1[4],      genome1[int(s1[2])-2:int(s1[2])+3],     genome2[int(s1[2])-2:int(s1[2])+3],     s1[11],s1[12],s1[14]))