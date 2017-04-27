
while True:
    print ("********************************************************************")
    print("welcome")
    print ("********************************************************************")
    method=input('1.input\n2.find and modify\n3.rinking\n4.quit\n')
    if method=='1':
        num=input("input student's number:")
        name=input("input student's name:")
        score=input("input student's score:")
        list_1=[num,name,score]
        strcontent=str(list_1)
        stufile=open("stuData.txt","a")
        stufile.write(strcontent)
        stufile.write("\n")
        stufile.close()
        
    elif method=='2':
        findNum=input("input student's number:")
        stufile=open('stuData.txt','r')
        isFind=False
        while True:
            inputString=stufile.readline()
            if inputString=='':
                break
            stuArr1=inputString.split("'",1)
            stuArr2=stuArr1[1].split("'",1)
            num=str(stuArr2[0])
            
            if findNum==num:
                tmpstr1=inputString.split("'",1)
                tmpstr2=tmpstr1[1].split("'",1)
                print("number="+tmpstr2[0]);
                tmpstr3=tmpstr2[1].split(",'",1)
                tmpstr4=tmpstr3[0].split("'",1)
                tmpstr5=tmpstr4[1].split("'",1)
                print("name="+tmpstr5[0]);
                tmpstr6=tmpstr5[1].split("'",1)
                tmpstr7=tmpstr6[1].split("'",1)
                print("score="+tmpstr7[0])
                print('Is your information right?')
                option=input('choose:\nyes or no\n')
                if option=='yes':
                    break
                elif option=='no':
                    rigname=input('input your right name:\n')
                    rigscore=input('input your right score:\n')
                    list_2=[tmpstr2[0],tmpstr5[0],tmpstr7[0]]

                    stufile= open('stuData.txt').readlines()
                    fp= open('stuData1.txt','w') 
                    for list_2 in stufile:  
                       fp.write(list_2.replace(tmpstr5[0],rigname).replace(tmpstr7[0],rigscore))
                    fp.close()

                    import os
                    os.remove('stuData.txt')
                    os.rename('stuData1.txt','stuData.txt')
                    print('Now your information has been modified,please confirm it again.\n')
                    isFind=True
                    break
        if isFind==False:
            print('not found!')
            
    elif method=='3':
        stufile=open('stuData.txt','r')
        database=[]
        while True:
            a=stufile.readline()
            if a=='':
                break
            else:
                tmpstr1=a.split("'",1)
                tmpstr2=tmpstr1[1].split("'",1)
                tmpstr3=tmpstr2[1].split(",'",1)
                tmpstr4=tmpstr3[0].split("'",1)
                tmpstr5=tmpstr4[1].split("'",1)
                tmpstr6=tmpstr5[1].split("'",1)
                tmpstr7=tmpstr6[1].split("'",1)
                list_3=[tmpstr2[0],tmpstr5[0],tmpstr7[0]]
                database.append(list_3)				
        stufile.close()
        option=input("1.rank with number\n2.rank with score\n")
        n =len(database)
        i=0
        m=0
        if option=='1':
            while i<n-1 :
                while m <n-1:
                    if int(database[m][0])> int(database[m+1][0]):
                        database[m],database[m+1]=database[m+1],database[m]
                    m=m+1 
                i=i+1
                m=0
            for line in database:
                print(line)
        elif option=='2':        
            while i<n-1 :
                while m <n-1:
                    if int(database[m][2])< int(database[m+1][2]):
                        database[m],database[m+1]=database[m+1],database[m]
                    m=m+1
                i=i+1
                m=0
            for line in database:        
                print(line)        
    else:
        quit()
 

                                
                  

                
         
        
