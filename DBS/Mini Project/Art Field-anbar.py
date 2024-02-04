import mysql.connector as myconnect
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
from tkinter import messagebox
import random as rand
import csv

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#OWNER
#-------------------------------------------------------------------------------------------------
#O1. Paintings:

#P1. Display all paintings 
def displaypaintings():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        mycursor.execute('select * from paintings')
        myrecord=mycursor.fetchall()
        print('')
        print('-'*120)
        print('%10s'%'PCODE','%30s'%'PIECE','%20s'%'ARTIST','%15s'%'ACODE','%10s'%'PRICE','%10s'%'MAXVAL','%10s'%'STATUS')
        print('-'*120)
        for x in myrecord:
            print('%10s'%x[0],'%30s'%x[1],'%20s'%x[2],'%15s'%x[3],'%10s'%x[4],'%10s'%x[5],'%10s'%x[6])
        print(' ')
    except:
        print(' ')

#P2. Search by painting code
def searchbypcode():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        req_code =int(input("Enter the painting code:"))
        query ="select * from paintings where pcode = {} ".format(req_code)
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        if len(myrecord)==0:
            print('record not found')
        else:
            print('')
            print('-'*120)
            print('%10s'%'PCODE','%30s'%'PIECE','%20s'%'ARTIST','%15s'%'ACODE','%10s'%'PRICE','%10s'%'MAXVAL','%10s'%'STATUS')
            print('-'*120)
            for x in myrecord:
                print('%10s'%x[0],'%30s'%x[1],'%20s'%x[2],'%15s'%x[3],'%10s'%x[4],'%10s'%x[5],'%10s'%x[6])
            print(' ')
            print("Search successful.")
            print(' ')
    except Exception as e:
        print(' ')
        print("Record not found.", e)
        print(' ')
        
#P3. Search by painting name        
def searchbypainting():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        req_name=input("Enter the name of the painting:")
        query ="select * from paintings where piece = '{}' ".format(req_name)
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        if len(myrecord)==0:
            print('record not found')
        else:
            print('-'*120)
            print('%10s'%'PCODE','%30s'%'PIECE','%20s'%'ARTIST','%15s'%'ACODE','%10s'%'PRICE','%10s'%'MAXVAL','%10s'%'STATUS')
            print('-'*120)
            for x in myrecord:
                print('%10s'%x[0],'%30s'%x[1],'%20s'%x[2],'%15s'%x[3],'%10s'%x[4],'%10s'%x[5],'%10s'%x[6])
            print(' ')
            print("Search successful.")
            print(' ')
    except Exception as e:
        print(' ')
        print('Record is not found', e)
        print(' ')

#P4. Search by artist code
def searchbyacode():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        req_code =int(input("Enter the artist code :"))
        query ="select * from paintings where acode = {} ".format(req_code)
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        if len(myrecord)==0:
            print('record not found')
        else:
            print('')
            print('-'*120)
            print('%10s'%'PCODE','%30s'%'PIECE','%20s'%'ARTIST','%15s'%'ACODE','%10s'%'PRICE','%10s'%'MAXVAL','%10s'%'STATUS')
            print('-'*120)
            for x in myrecord:
                print('%10s'%x[0],'%30s'%x[1],'%20s'%x[2],'%15s'%x[3],'%10s'%x[4],'%10s'%x[5],'%10s'%x[6])
            print(' ')
            print("Search successful.")
            print(' ')
    except Exception as e:
        print(' ')
        print('Record is not found',e)
        print(' ')

#P5. Search by artist name
def searchbyartist():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        req_name=input("Enter the name of the artist:")
        query ="select * from paintings where artist = '{}'".format(req_name)
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        if len(myrecord)==0:
            print('record not found')
        else:
            print('-'*120)
            print('%10s'%'PCODE','%30s'%'PIECE','%20s'%'ARTIST','%15s'%'ACODE','%10s'%'PRICE','%10s'%'MAXVAL','%10s'%'STATUS')
            print('-'*120)
            for x in myrecord:
                print('%10s'%x[0],'%30s'%x[1],'%20s'%x[2],'%15s'%x[3],'%10s'%x[4],'%10s'%x[5],'%10s'%x[6])
            print(' ')
            print("Search successful.")
            print(' ')
    except Exception as e:
        print(' ')
        print('Record is not found', e)
        print(' ')

#P6. Add a new painting
def addpainting():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='vrushali',database='artgallery')
        mycursor=mydb.cursor()
        n=int(input('How many records would you like to add?: '))
        for i in range(n):
            print('-'*40)
            print('Enter the details for record',str(i+1))
            print('-'*40)
            pcode=int(input('Enter the painting code:'))
            query="select * from paintings where pcode = " + str(pcode)
            mycursor.execute(query)
            myrecord = mycursor.fetchall()
            if mycursor.rowcount>0:
                print('__'*50)
                print("Sorry, record already exists.")
                print('__'*50)
                continue
            else:
                piece=input('Enter the name of the painting:')
                artist=input('Enter the name of the artist:')
                acode=int(input('Enter the artist code:'))
                price=int(input('Enter the price of the painting:'))
                maxval=int(input('Enter the maximum price of the painting:'))
                status=input('Enter the status of the painting (SOLD/AVAILABLE):')
                q2="INSERT INTO PAINTINGS VALUES({},'{}','{}',{},{},{},'{}')".format(pcode,piece,artist,acode,price,maxval,status)
                mycursor.execute(q2)
                mydb.commit()
            with open('masterpaintings.csv', 'a') as CSVfile:
                CSVobj= csv.writer(CSVfile, delimiter=',')
                line= [pcode,piece,artist,acode,price,maxval,status]
                CSVobj.writerow(line)
            print(' ')
            print('Record was added')
            print(' ')
    except Exception as e:
        print(' ')
        print('Record was not added',e)
        print(' ')
        
#P7. Delete a painting
def deletepainting():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        req_code =int(input("Enter the painting code to be deleted:"))
        query="select * from paintings where pcode = " + str(req_code)
        mycursor.execute(query)
        myrecord = mycursor.fetchall() 
        if mycursor.rowcount<=0:
            print('__'*50)
            print("Sorry, no such record exists.")
            print('__'*50)
        else:
            print('-'*120)
            print('%10s'%'PCODE','%30s'%'PIECE','%20s'%'ARTIST','%15s'%'ACODE','%10s'%'PRICE','%10s'%'MAXVAL','%10s'%'STATUS')
            print('-'*120)
            for x in myrecord:
                print('%10s'%x[0],'%30s'%x[1],'%20s'%x[2],'%15s'%x[3],'%10s'%x[4],'%10s'%x[5],'%10s'%x[6])
            print(' ')
            sure = input("Are you sure you want to delete this record? (Y/N) : ")
            if sure=="y" or sure=="Y":
                query=" Delete from paintings where pcode = {} ".format(req_code)
                mycursor.execute(query)
                mydb.commit()
                print(' ')
                print("Record was deleted.")
                print(' ')
            else:
                print(' ')
                print("Record was not deleted.")
                print(' ')
    except Exception as e:
        print(e)
            
#P8. Update the details of a painting
def updatepainting():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='vrushali',database='artgallery')
        mycursor=mydb.cursor()
        req_code =int(input("Enter the painting code: "))
        query="select * from paintings where pcode = " + str(req_code)
        mycursor.execute(query)
        myrecord = mycursor.fetchall()
        if mycursor.rowcount<=0:
            print('__'*50)
            print("Sorry, no such record exists.")
            print('__'*50)
        else:
            print('Enter 1 to change the name of the painting.')
            print('Enter 2 to change the name of the artist.')
            print('Enter 3 to change the artist code.')
            print('Enter 4 to change the price of the painting.')
            print('Enter 5 to change the maximum price of the painting.')
            print('Enter 6 to change the status of the painting.')
            update=input('Please enter your choice: (1/2/3/4/5/6)')
            if update=='1':
                piece=input('Enter the new name of the painting:')
                query="update PAINTINGS set PIECE='{}' where PCODE={}".format(name, req_code)
            elif update=='2':
                artist=input('Enter the new name of the artist:')
                query="update PAINTINGS set ARTIST='{}' where PCODE={}".format(artist, req_code)
            elif update=='3':
                acode=int(input('Enter the new artist code:'))
                query="update PAINTINGS set ACODE='{}' where PCODE={}".format(acode, req_code)
            elif update=='4':
                price=int(input('Enter the new price of the painting:'))
                query="update PAINTINGS set PRICE='{}' where PCODE={}".format(price, req_code)
            elif update=='5':
                maxval=int(input('Enter the new maximum price of the painting:'))
                query="update PAINTINGS set MAXVAL='{}' where PCODE={}".format(maxval, req_code)
            elif update=='6':
                status=input('Enter the new status of the painting (SOLD/AVAILABLE):')
                query="update PAINTINGS set STATUS='{}' where PCODE={}".format(status, req_code)
            mycursor.execute(query)
            mydb.commit()
            print(' ')
            print('Record updated.')
            print(' ')
    except Exception as e:
        print(e)
        
#P9. Finding the profit
def profit():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        req_code =int(input("Enter the painting code: "))
        query="select * from paintings where pcode = " + str(req_code)
        mycursor.execute(query)
        myrecord = mycursor.fetchall()
        for x in myrecord:
            if x[0]==req_code:
                if x[6]=='SOLD':
                    profit= int(x[5])- int(x[4])
                    print('The profit we made on this painting was:', profit)
                else:
                    print('This painting has not been sold yet')
    except Exception as e:
        print('Sorry, no such record exists.')
        print(e)
        
#-------------------------------------------------------------------------------------------------
#O2. Buyers

#B1. Display all buyers
def displaybuyers():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="anbar",database="artgallery")
    mycursor=mydb.cursor()
    try:
        mycursor.execute("select * from BUYERS")
        myrecords=mycursor.fetchall()
        print('-'*120)
        print('%10s'%'BCODE','%30s'%'NAME','%20s'%'PIECE','%15s'%'PCODE','%10s'%'PRICE','%10s'%'DATE')
        print('-'*120)
        for row in myrecords:
            print('%10s' % row[0],'%30s'%row[1],'%20s'%row[2],'%15s'%row[3],'%10s'%row[4],'%10s'%row[5])
    except:
        print("Sorry, unable to display")

#B2. Search by buyer code
def searchbybcode():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        req_code =int(input("Enter the buyer code:"))
        query ="select * from buyers where bcode = {} ".format(req_code)
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        if len(myrecord)==0:
            print('record not found')
        else:
            print('')
            print('-'*120)
            print('%10s'%'BCODE','%30s'%'NAME','%20s'%'PIECE','%15s'%'PCODE','%10s'%'PRICE','%10s'%'DATE')
            print('-'*120)
            for x in myrecord:
                print('%10s'%x[0],'%30s'%x[1],'%20s'%x[2],'%15s'%x[3],'%10s'%x[4],'%10s'%x[5])
            print(' ')
            print("Search successful.")
            print(' ')
    except Exception as e:
        print(' ')
        print("Record not found.", e)
        print(' ')

#B3. Search by BUYER name        
def searchbybname():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        req_name=input("Enter the name of the buyer:")
        query ="select * from buyers where name = '{}' ".format(req_name)
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        if len(myrecord)==0:
            print('record not found')
        else:
            print('-'*120)
            print('%10s'%'BCODE','%30s'%'NAME','%20s'%'PIECE','%15s'%'PCODE','%10s'%'PRICE','%10s'%'DATE')
            print('-'*120)
            for x in myrecord:
                print('%10s'%x[0],'%30s'%x[1],'%20s'%x[2],'%15s'%x[3],'%10s'%x[4],'%10s'%x[5])
            print(' ')
            print("Search successful.")
            print(' ')
    except Exception as e:
        print(' ')
        print('Record is not found', e)
        print(' ')

#B4. Search by painting code
def searchbybpcode():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        req_code =int(input("Enter the painting code :"))
        query ="select * from buyers where pcode = {} ".format(req_code)
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        if len(myrecord)==0:
            print('record not found')
        else:
            print('')
            print('-'*120)
            print('%10s'%'BCODE','%30s'%'NAME','%20s'%'PIECE','%15s'%'PCODE','%10s'%'PRICE','%10s'%'DATE')
            print('-'*120)
            for x in myrecord:
                print('%10s'%x[0],'%30s'%x[1],'%20s'%x[2],'%15s'%x[3],'%10s'%x[4],'%10s'%x[5])
            print(' ')
            print("Search successful.")
            print(' ')
    except Exception as e:
        print(' ')
        print('Record is not found',e)
        print(' ')

#B5. Search by painting name
def searchbybpname():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        req_name=input("Enter the name of the painting:")
        query ="select * from buyers where piece = '{}'".format(req_name)
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        if len(myrecord)==0:
            print('record not found')
        else:
            print('-'*120)
            print('%10s'%'BCODE','%30s'%'NAME','%20s'%'PIECE','%15s'%'PCODE','%10s'%'PRICE','%10s'%'DATE')
            print('-'*120)
            for x in myrecord:
                print('%10s'%x[0],'%30s'%x[1],'%20s'%x[2],'%15s'%x[3],'%10s'%x[4],'%10s'%x[5])
            print(' ')
            print("Search successful.")
            print(' ')
    except Exception as e:
        print(' ')
        print('Record is not found', e)
        print(' ')
        
#B6. Add a new buyer
def addbuyer():
    import mysql.connector
    mydb= mysql.connector.connect(host="localhost", user="root", passwd="vrushali", database="artgallery")
    mycursor=mydb.cursor()
    myrecord = mycursor.fetchall()
    n= int(input('Enter the number of records you wish to add:'))
    try:
        for i in range(n):
            print('Enter the details for record',str(i+1))
            print('-'*40)
            bcode=int(input('Enter the buyer code:'))
            query="select * from buyers where bcode = " + str(bcode)
            mycursor.execute(query)
            myrecord = mycursor.fetchall()
            if mycursor.rowcount>0:
                print('__'*50)
                print("Sorry, record already exists.")
                print('__'*50)
                continue
            else:
                bcode=int(input('Enter the buyer code:'))
                name= input('Enter the name of the buyer:')
                piece= input('Enter the name of the painting:')
                pcode= int(input('Enter the painting code:'))
                price= int(input('Enter the price of the painting:'))
                date= input('Enter the date on which the piece was bought (YYYY-MM-DD format ONLY):')
                q2= "INSERT INTO BUYERS values({}, '{}', '{}', {}, {}, '{}')".format(bcode, name, piece, pcode, price, date)
                #mycursor.execute(q1)
                mycursor.execute(q2)
                with open('masterbuyers.csv', 'a') as CSVfile:
                    CSVobj= csv.writer(CSVfile, delimiter=',')
                    line= [bcode, name, piece, pcode, price, date]
                    CSVobj.writerow(line)
                mydb.commit()
            print(' ')
            print('Record was added')
            print(' ')
    except:
        print(' ')
        print('Record was not added.')
        print(' ')
        
#B7. Delete a buyer
def deletebuyer():
    import mysql.connector
    from mysql.connector import Error
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="anbar",database="artgallery")
    mycursor=mydb.cursor()
    try:
        reqno=int(input("Enter the buyer code to be deleted: "))
        query="select * from BUYERS where bcode="+str(reqno)
        mycursor.execute(query)
        myrecords=mycursor.fetchall()
        if mycursor.rowcount<=0:
            print('__'*50)
            print("Sorry, no such record exists.")
            print('__'*50)
        else:
            print('-'*120)
            print('%10s'%'BCODE','%30s'%'NAME','%20s'%'PIECE','%15s'%'PCODE','%10s'%'PRICE','%10s'%'DATE')
            print('-'*120)
            for row in myrecords:
                print('%10s' % row[0],'%30s'%row[1],'%20s'%row[2],'%15s'%row[3],'%10s'%row[4],'%10s'%row[5])
            sure=input("Are you sure you want to delete? (Y/N):")
            if sure=="y" or sure=="Y":
                query="Delete from BUYERS where bcode={}".format(reqno)
                mycursor.execute(query)
                mydb.commit()
                print(' ')
                print("Record was deleted.")
                print(' ')
            else:
                print(' ')
                print("Record was not deleted.")
                print(' ')
    except Error as e:
        print(e)

#B8. Update the details of a buyer
def updatebuyer():
    import mysql.connector
    from mysql.connector import Error
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="vrushali",database="artgallery")
    mycursor=mydb.cursor()
    try:
        reqno =input("Enter the buyer code:")
        query="select * from buyers where BCODE="+str(reqno)
        mycursor.execute(query)
        myrecord = mycursor.fetchall()
        if mycursor.rowcount<=0:
            print('__'*50)
            print("Sorry, no such record exists.")
            print('__'*50)
        else:
            print('Enter 1 to change the name of the buyer.')
            print('Enter 2 to change the name of the painting.')
            print('Enter 3 to change the painting code.')
            print('Enter 4 to change the price of the painting.')
            print('Enter 5 to change the date.')
            update=input('Please enter your choice: (1/2/3/4/5/6)')
            if update=='1':
                name= input('Enter the new name of the buyer:')
                query="update BUYERS set NAME='{}' where BCODE={}".format(name, reqno)
            elif update=='2':
                piece= input('Enter the new name of the painting:')
                query="update BUYERS set PIECE='{}' where BCODE={}".format(piece, reqno)
            elif update=='3':
                pcode= int(input('Enter the new painting code:'))
                query="update BUYERS set PCODE={} where BCODE={}".format(pcode, reqno)
            elif update=='4':
                price=int(input('Enter the new price of the painting:'))
                query="update BUYERS set PRICE={} where BCODE={}".format(price, reqno)
            elif update=='5':
                date= input('Enter the new date on which the piece was bought (YYYY-MM-DD format ONLY):')
                query="update BUYERS set DATE='{}' where BCODE={}".format(date, reqno)
                        #query="update BUYERS set NAME='"+name+"',PIECE="+str(piece) + " where rno="+str(reqno)
            mycursor.execute(query)
            mydb.commit()
            print("Record updated")
    except Error as e:
        print(e)

#-------------------------------------------------------------------------------------------------

#import mysql.connector as myconnect

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#O3. Info

#I1. Add info
def addinfo():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        n=int(input('How many records would you like to add?: '))
        for i in range(n):
            print('-'*40)
            print('Enter the details for record',str(i+1))
            print('-'*40)
            pcode=int(input('Enter the painting code:'))
            piece=input('Enter the name of the painting:')
            artist=input('Enter the name of the artist:')
            acode=int(input('Enter the artist code:'))
            year=int(input('Enter the year of the painting:'))
            price=int(input('Enter the price of the painting:'))
            status=input('Enter the status of the painting (SOLD/AVAILABLE):')
            q2="INSERT INTO INFO VALUES({},'{}','{}',{},{},{},'{}')".format(pcode,piece,artist,acode,year,price,status)
            mycursor.execute(q2)
            mydb.commit()
            print(' ')
            print('Record was added')
            print(' ')
    except Exception as e:
        print(' ')
        print('Record was not added',e)
        print(' ')

#I2. Delete info
def deleteinfo():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        req_code =int(input("Enter the painting code to be deleted:"))
        query="select * from info where pcode = " + str(req_code)
        mycursor.execute(query)
        myrecord = mycursor.fetchall() 
        if mycursor.rowcount<=0:
            print('__'*50)
            print("Sorry, no such record exists.")
            print('__'*50)
        else:
            print('-'*120)
            print('%10s'%'PCODE','%30s'%'PIECE','%20s'%'ARTIST','%15s'%'ACODE','%10s'%'PRICE','%10s'%'MAXVAL','%10s'%'STATUS')
            print('-'*120)
            for x in myrecord:
                print('%10s'%x[0],'%30s'%x[1],'%20s'%x[2],'%15s'%x[3],'%10s'%x[4],'%10s'%x[5],'%10s'%x[6])
            print(' ')
            sure = input("Are you sure you want to delete this record? (Y/N) : ")
            if sure=="y" or sure=="Y":
                query=" Delete from info where pcode = {} ".format(req_code)
                mycursor.execute(query)
                mydb.commit()
                print(' ')
                print("Record was deleted.")
                print(' ')
            else:
                print(' ')
                print("Record was not deleted.")
                print(' ')
    except Exception as e:
        print(e)
            
#I3. Update info
def updateinfo():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='vrushali',database='artgallery')
        mycursor=mydb.cursor()
        req_code =int(input("Enter the painting code: "))
        query="select * from info where pcode = " + str(req_code)
        mycursor.execute(query)
        myrecord = mycursor.fetchall()
        if mycursor.rowcount<=0:
            print('__'*50)
            print("Sorry, no such record exists.")
            print('__'*50)
        else:
            print('Enter 1 to change the name of the painting.')
            print('Enter 2 to change the name of the artist.')
            print('Enter 3 to change the artist code.')
            print('Enter 4 to change the year of the painting.')
            print('Enter 5 to change the price of the painting.')
            print('Enter 6 to change the status of the painting.')
            update=input('Please enter your choice: (1/2/3/4/5/6)')
            if update=='1':
                piece=input('Enter the new name of the painting:')
                query="update INFO set PIECE='{}' where PCODE={}".format(name, req_code)
            elif update=='2':
                artist=input('Enter the new name of the artist:')
                query="update INFO set ARTIST='{}' where PCODE={}".format(artist, req_code)
            elif update=='3':
                acode=int(input('Enter the new artist code:'))
                query="update INFO set ACODE='{}' where PCODE={}".format(acode, req_code)
            elif update=='4':
                year=int(input('Enter the new year of the painting:'))
                query="update INFO set MAXVAL='{}' where PCODE={}".format(maxval, req_code)
            elif update=='5':
                price=int(input('Enter the new price of the painting:'))
                query="update INFO set PRICE='{}' where PCODE={}".format(price, req_code)
            elif update=='6':
                status=input('Enter the new status of the painting (SOLD/AVAILABLE):')
                query="update INFO set STATUS='{}' where PCODE={}".format(status, req_code)
            mycursor.execute(query)
            mydb.commit()
            print(' ')
            print('Record updated.')
            print(' ')
    except Exception as e:
        print(e)
    
#VISITOR

#V1. Display all paintings
def displayinfo():
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        mycursor.execute('select * from info')
        myrecord=mycursor.fetchall()
        print('')
        print('-'*120)
        print('%10s'%'PCODE','%30s'%'PIECE','%20s'%'ARTIST','%15s'%'ACODE','%10s'%'YEAR','%10s'%'PRICE','%10s'%'STATUS')
        print('-'*120)
        for x in myrecord:
            print('%10s'%x[0],'%30s'%x[1],'%20s'%x[2],'%15s'%x[3],'%10s'%x[4],'%10s'%x[5],'%10s'%x[6])
        print(' ')
    except:
        print(' ')
        
#V2. Search by painting name
def searchinfobypainting():
    
    list1=['morning sun', 'the son of man', 'the scream', 'years of glory', 'the power of letter', 'lilacs in a window', 'my dress hangs there', 'me and my doll', 'convergence']
    list2=['SUN.jpg', 'MAN.jpg', 'SCREAM.jpg', 'GLORY.jpg', 'POWER.jpg', 'LILACS.jpg', 'DRESS.jpg', 'DOLL.jpg', 'CONE.jpg'] 
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        req_name=input("Enter the name of the painting:")
        query ="select * from info where piece = '{}' ".format(req_name)
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        if len(myrecord)==0:
            print('record not found')
        else:
            print('-'*120)
            print('%10s'%'PCODE','%17s'%'PIECE','%20s'%'ARTIST','%15s'%'ACODE','%10s'%'YEAR','%10s'%'PRICE','%10s'%'STATUS')
            print('-'*120)
            for x in myrecord:
                print('%10s'%x[0],'%20s'%x[1],'%20s'%x[2],'%9s'%x[3],'%11s'%x[4],'%10s'%x[5],'%13s'%x[6])
            print("Search successful")
                
            if req_name.lower() in list1:
                index= list1.index(req_name.lower())
                picture= list2[index]
                from PIL import Image
                img = Image.open(picture)
                img.show()
    except Exception as e:
        print('Record is not found',e)

#V3. Search by artist name
def searchinfobyartist():
    
    list1=['edward hopper', 'rene magritte', 'edvard munch', 'abdul qader al rais', 'mary cassatt', 'frida kahlo', 'jackson pollock']
    list2=['EDW.jpg', 'REN.jpg', 'EDV.jpg','ABD.jpg', 'MAR.jpg', 'FRI.jpg', 'JAC.jpg']
    try:
        mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
        mycursor=mydb.cursor()
        req_name=input("Enter the name of the artist:")
        query ="select * from info where artist = '{}'".format(req_name)
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        if len(myrecord)==0:
            print('record not found')
        else:
            print('-'*120)
            print('%10s'%'PCODE','%30s'%'PIECE','%20s'%'ARTIST','%15s'%'ACODE','%10s'%'YEAR','%10s'%'PRICE','%10s'%'STATUS')
            print('-'*120)
            for x in myrecord:
                print('%10s'%x[0],'%30s'%x[1],'%20s'%x[2],'%15s'%x[3],'%10s'%x[4],'%10s'%x[5],'%10s'%x[6])
            print("Search successful")
            if req_name.lower() in list1:
                index= list1.index(req_name.lower())
                picture= list2[index]
                from PIL import Image
                img = Image.open(picture)
                img.show()
                
    except Exception as e:
        print('Record is not found',e)

#import csv
#V4. Bid for a painting
def bidding():
    import random as rand
    choice='Y'
    while choice=='Y' or choice=='y':
        try:
            mydb=myconnect.connect(host='localhost',user='root',passwd='anbar',database='artgallery')
            mycursor=mydb.cursor()
            req_name=input("Enter the painting name you wish to bid for:")
            query ="select * from paintings where PIECE = '{}' ".format(req_name)
            mycursor.execute(query)
            myrecord=mycursor.fetchall()
            status= myrecord[0][6]
            price=myrecord[0][4]
            maxval= myrecord[0][5]
            
            if status=='SOLD':
                print(' ')
                print('Sorry, this painting is sold. You cannot bid for it.')
                print(' ')
            else:
                print('The starting bid is:', price)
                print(' ')
                bid1= rand.randint(price, maxval)
                bid2= rand.randint(price, maxval)
                bid3= rand.randint(price, maxval)
                bid= int(input('Enter your bid:'))
                print(' ')
                bidlist=[bid1, bid2, bid3, bid]
                print('The bids are:')
                print(' ')
                print('Bidder 1:', bid1)
                print('Bidder 2:',bid2)
                print('Bidder 3:',bid3)
                print('Your bid:', bid)
                print(' ')
                
                if bid==max(bidlist):
                    print('Congrats! You win.')
                    print(' ')
                    query1 ="update PAINTINGS set STATUS='SOLD' WHERE PIECE = '{}' ".format(req_name)
                    query2 ="update INFO set STATUS='SOLD' WHERE PIECE = '{}' ".format(req_name)
                    mycursor.execute(query1)
                    mycursor.execute(query2)
                    query3="select count(*) from BUYERS"
                    mycursor.execute(query3)
                    bcod=mycursor.fetchone()
                    bcode=int(bcod[0])+101
                    name=input('Enter your name:')
                    phone=int(input('Enter your phone no.:'))
                    accno=int(input('Enter your bank account no.:'))
                    query4="select PCODE from paintings where PIECE='{}' ".format(req_name)
                    mycursor.execute(query4)
                    pcode= mycursor.fetchone()
                    query="insert into BUYERS (BCODE, NAME, PIECE, PCODE, PRICE, PHONENO, ACCNO) values({},'{}','{}',{}, {}, {}, {})".format(bcode, name, req_name, pcode[0], bid, phone, accno)
                    mycursor.execute(query)
                    query5='update BUYERS set DATE=curdate() where BCODE={}'.format(bcode)
                    mycursor.execute(query5)
                    query6 ="select * from BUYERS where BCODE={} ".format(bcode)
                    mycursor.execute(query6)
                    myrecord=mycursor.fetchall()
                    for x in myrecord:
                        date=x[5]
                        with open('masterbuyers.csv', 'a') as CSVfile:
                            CSVobj= csv.writer(CSVfile, delimiter=',')
                            line= [bcode, name, req_name, pcode, price, date]
                            CSVobj.writerow(line)
                    mydb.commit()
                    if bid>maxval:
                        charity= bid-maxval
                        print('Since your bid exceeds our maximum value, the remaining money goes to our favorite charity Red Crescent which helps the needy in UAE')
                        print('You have donated', charity, 'dirhams!')
                        print('Thank you!')
                        print(' ')
                else:
                    print("Sorry. You didn't win.")
                    print(' ')
            choice= input('Would you like to try again? (Y/N)')
        except Exception as e:
            print('Record is not found',e)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#MENUS
  
from tkinter import *
from tkinter import messagebox
  
def Ok():
    try:
        uname = e1.get()
        password = e2.get()
        if(uname == "" and password == "") :
            messagebox.showinfo("", "Blank Not allowed")
        elif(uname in ["mehreenart", "anbarart", "vrushaliart"] and password == "artfi3ld"):
            messagebox.showinfo("","Login Success")
            #root.destroy()
            omenu()
        else :
            messagebox.showinfo("","Incorrect Username and Password")
    except Exception as e:
        print(e)
 
def password():
    root = Tk()
    root.title("Login")
    root.geometry("300x200")
    global e1
    global e2
    Label(root, text="Username").place(x=10, y=10)
    Label(root, text="Password").place(x=10, y=40)
    e1 = Entry(root)
    e1.place(x=140, y=10)
    e2 = Entry(root)
    e2.place(x=140, y=40)
    e2.config(show="*")
    Button(root, text="Login", command=Ok ,height = 3, width = 13).place(x=10, y=100)
    root.mainloop()  
  
def omenu():
    ch='Y'
    while ch=='Y' or ch=='y':
        print(' ')
        print('Enter P to manage records of paintings.')
        print('Enter B to manage records of buyers.')
        print('Enter I to manage records of info.')
        print(' ')
        answer= input('Enter your choice (P/B/I):')
        print(' ')
        if answer=='p' or answer=='P':
            print('Enter 1 to display all records.')
            print('Enter 2 to search records based on painting code.')
            print('Enter 3 to search records based on painting name.')
            print('Enter 4 to search records based on artist code.')
            print('Enter 5 to search records based on artist name.')
            print('Enter 6 to add a new record.')
            print('Enter 7 to delete a record.')
            print('Enter 8 to update a record.')
            print('Enter 9 to find the profit of a painting.')
            print(' ')
            service=int(input('Enter your choice (1/2/3/4/5/6/7/8/9):'))
            if service==1:
                displaypaintings()
                print(' ')
            elif service==2:
                searchbybcode()
                print(' ')
            elif service==3:
                searchbypainting()
                print(' ')
            elif service==4:
                searchbyacode()
                print(' ')
            elif service==5:
                searchbyartist()
                print(' ')
            elif service==6:
                addpainting()
                print(' ')
            elif service==7:
                deletepainting()
                print(' ')
            elif service==8:
                updatepainting()
                print(' ')
            elif service==9:
                profit()
                print(' ')
        elif answer=='b' or answer=='B':
            print('Enter 1 to display all records')
            print('Enter 2 to search records based on buyer code')
            print('Enter 3 to search records based on buyer name')
            print('Enter 4 to search records based on painting code')
            print('Enter 5 to search records based on painting name')
            print('Enter 6 to add a new record.')
            print('Enter 7 to delete a record.')
            print('Enter 8 to update a record.')
            print(' ')
            service=int(input('Enter your choice (1/2/3/4/5/6/7/8):'))
            if service==1:
                displaybuyers()
                print(' ')
            elif service==2:
                searchbybcode()
            elif service==3:
                searchbybname()
            elif service==4:
                searchbybpcode()
            elif service==5:
                searchbybpname()
            elif service==6:
                addbuyer()
                print(' ')
            elif service==7:
                deletebuyer()
                print(' ')
            elif service==8:
                updatebuyer()
                print(' ')
        elif answer=='I' or answer=='i':
            print('PLEASE CONFIRM WITH OTHER OWNERS BEFORE CHANGING THIS TABLE.')
            print('Enter 1 to add a new record.')
            print('Enter 2 to delete a record.')
            print('Enter 3 to update a record.')
            service=int(input('Enter your choice (1/2/3):'))
            if service==1:
                addinfo()
                print(' ')
            elif service==2:
                deleteinfo()
                print(' ')
            elif service==3:
                updateinfo()
                print(' ')
        ch=input('Would you like to use another service? (Y/N):')
    print('Thank you for visiting Art Field!')

       
def vmenu():
    ch='Y'
    while ch=='Y' or ch=='y':
        print(' ')
        print('Enter 1 to display the records.')
        print('Enter 2 to search records based on painting name.')
        print('Enter 3 to search records based on artist name.')
        print('Enter 4 to bid on a painting.')
        print(' ')
        service=int(input('Enter your choice (1/2/3/4):'))
        if service==1:
            displayinfo()
            print(' ')
        elif service==2:
            searchinfobypainting()
            print(' ')
        elif service==3:
            searchinfobyartist()
            print(' ')
        elif service==4:
            bidding()
            print(' ')
        ch=input('Would you like to use another service? (Y/N):')
        print(' ')

        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#MAIN CODE
        
def maincode():
    print('Welcome to Art Field!')
    print(' ')
    print('Are you visiting or are you an owner?')
    ans= input('Enter V for visitor or O for owner:')
    print(' ')
    
    if ans=='O' or ans=='o':
        password()
    elif ans=='V' or ans=='v':
        print('Welcome to Art Field!')
        vmenu()
    
maincode()


        