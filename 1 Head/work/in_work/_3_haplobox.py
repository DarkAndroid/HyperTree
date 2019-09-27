

import os 







listtree = open("prank_tre.ordN.coll.pathS",'r')




# path4="hyperlist.csv"
# reps4 = open(path4, "w")





# folder="FilledN"
# files=os.listdir(folder)
# prepath=(folder+"/")








# for f in files:

#     fi=f[:-4].split("__")
#     print fi
#     reps4.write("%s;%s\n" % (fi[0],fi[1]))



# reps4.close()






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
        continue





    path3="Haplo/%s_%s.csv" % (cr,hread[0])
    reps3 = open(path3, "w")


    


    for pair in range(len(sepread)-1):

 
        first=sepread[pair]
        second=sepread[pair+1]

        # print first
        # print second


        path4="FilledN/%s__%s.csv" % (first,second)
        reps4 = open(path4, "r")


        while True: 



            readP = reps4.readline().strip()
            if readP=='':
                break
    
            #print readP
            reps3.write("%s\n" % (readP))


    cr+=1