from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
from tkinter import filedialog
import sys
import math
import random

import smtplib
from datetime import datetime


root = Tk()
root.title("Login Panel")
root.geometry('400x300')
root.iconbitmap('book.ico')



#============================================Admin Login Check======================================================
def admin_check():

    uname=un.get()
    password=pwd.get()
        
    global flag
    flag=0

    if(uname=="tejashatle" and password=="tejas345"):
        flag=flag+1
    else:
        flag=0

    connection = sqlite3.connect("Books")
    cursor = connection.cursor()
    sql="""SELECT * FROM ADMIN WHERE Username='%s' and Password='%s'""" %(uname,password)
    cursor.execute(sql)
    result = cursor.fetchall()

    if(uname=='' and password==''):
        messagebox.showinfo("Message","Entry fields are blank")
        
    else:
        if len(result) > 0:
            remove_all_window()
            Book()
        else:
            messagebox.showinfo("Message","Invalid Credentials.")

  
            

#===============================================Inserting Admin====================================================

def Admin_Insert():

    connection=sqlite3.connect("Books")
    cursor = connection.cursor()

    sql="""CREATE TABLE IF NOT EXISTS ADMIN(Name Varchar(30),Email Varchar(30),Username varchar(30),Password varchar(30)) """
    
    cursor.execute(sql)

    sqlquery="""INSERT INTO ADMIN(Name,Email,Username,Password) VALUES ('%s','%s','%s','%s') """ % ("Tejas Hatle","tejashatle3@gmail.com","tejashatle","tejas345")
    result=cursor.execute(sqlquery)
    connection.commit()

    

#############################==============Truncate Admin table=================#############################
def Clear_TableAdmin():
    connection = sqlite3.connect("Books")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Admin")
    result = cursor.fetchall()
    
     
    if len(result) > 0:
        sql=" DELETE FROM Admin WHERE Name='%s'"%("Tejas Hatle")
        cursor.execute(sql)
        connection.commit()
        
        #messagebox.showinfo("Message","Table Cleared Succesfully")
        #cursor.execute("SELECT * FROM BOOKS")
        #result = cursor.fetchall()
        #for k in result:
         #   print("printING RESULTS",k)


    else:
        messagebox.showinfo("Message","Admin Table is already empty....")            


            

            
#===========================================Show Username and Passord==============================================
def ShowPass():

    if (Checked.get()):
        ent2.config(show="")
    else:
        ent2.config(show="*")

#=========================================Close Login Window=====================================================
def close_main():
    
    result=messagebox.askyesno("Warning","Do you want to close the application ?")
    if(result==True):
        Clear_TableAdmin()
        root.destroy()
        
    else:
        messagebox.showinfo("Title","Go do your work....")

#==========================================Close Login Window======================================================
def remove_all_window():
    for widget in root.winfo_children():
        widget.grid_remove()
    root.destroy()




#===================================================Main Panel====================================================
def Book():
    global top
    top=Tk()
    top.title("Book Management System By Tejas Hatle")
    top.geometry("1350x750+0+0")
    top.iconbitmap('book.ico')



    
#===================================================Remove Previous Widgets from Frame============================   
    def Remove_Widgets():
        global frmR
        for widget in frmR.winfo_children():
            widget.destroy()




#===================================================Close The Whole Window===========================================
    def Close_Window():
        result=messagebox.askyesno("Warning","Do you want to close the application ?")
        if(result==True):
            Clear_TableAdmin()
            top.destroy()
            
        else:
            messagebox.showinfo("Title","Go do your work....")

        

#===================================================Add  Book========================================================
        
    def AddBook(Bid,Bname,Aname,Bprice):
        bid=Bid.get()
        bname=Bname.get()
        aname=Aname.get()
        bprice=Bprice.get()
   
        bcat=B_Category_Ent.get()
##        print(bid)
##        print(bname)
##        print(aname)
##        print(bprice)
##        print(bcat)


        connection=sqlite3.connect("Books")
        cursor = connection.cursor()

        sql="""CREATE TABLE IF NOT EXISTS Book(BID INT PRIMARY KEY ,BOOK_NAME  VARCHAR(100),AUTHOR_NAME VARCHAR(100),PRICE INT,BOOK_CATEGORY VARCHAR(20)) """
        
        cursor.execute(sql)

        sqlquery="""INSERT INTO Book (BID,BOOK_NAME,AUTHOR_NAME,PRICE,BOOK_CATEGORY)VALUES ('%d','%s','%s','%d','%s') """ % (bid,bname,aname,bprice,bcat)
        result=cursor.execute(sqlquery)
        connection.commit()

        if(result):
            messagebox.showinfo("Message","Successfully inserted one record")
        else:
            messagebox.showerror("Message","Something Went Wrong")


        Bid.set("")
        Bname.set("")
        Aname.set("")
        Bprice.set("")
        B_Category_Ent.set("")


#===================================================Show Book===================================================
    def ShowBook():
        global tv
        records=tv.get_children()
        for rows in records:
            tv.delete(rows)
        

        connection=sqlite3.connect("Books")
        cursor = connection.cursor()

        sql="""SELECT*FROM BOOK ORDER BY BID DESC"""
        result=cursor.execute(sql)

        for k in result:
            tv.insert("",0,text=k[0],values=(k[1],k[2],k[3],k[4]))

##            print(k[0],"\n")
##            print(k[1],"\n")
##            print(k[2],"\n")
##            print(k[3],"\n")
##            print(k[4],"\n")
        

#===================================================Show Admin===================================================
    def ShowAdmin():
        global tv2
        records=tv2.get_children()
        for rows in records:
            tv2.delete(rows)
        

        connection=sqlite3.connect("Books")
        cursor = connection.cursor()

        sql="""SELECT*FROM ADMIN ORDER BY Name DESC"""
        result=cursor.execute(sql)

        for k in result:
            tv2.insert("",0,text=k[0],values=(k[1],k[2],k[3]))

##            print(k[0],"\n")
##            print(k[1],"\n")
##            print(k[2],"\n")
##            print(k[3],"\n")
##            print(k[4],"\n")
        


#===============================================Display Value In EntryBox==========================================
    def DisplayValue(event):
        global tv
        entryIndex=tv.focus()
        records=tv.get_children()

        for rows in records:
            if rows==entryIndex:
                values=tv.item(rows)["values"]
                text=tv.item(rows)["text"]
                #print("values are",values)
                #print("text is",text)
                global v
                global w
                global x
                global y
                global z
                global e1
                Bid.set(text)
                Bname.set(values[0])
                Aname.set(values[1])
                Bprice.set(values[2])
                B_Category_Ent.set(values[3])


#===============================================Display Value In EntryBox==========================================
    def DisplayValue2(event):
        global tv2
        entryIndex=tv2.focus()
        records=tv2.get_children()

        for rows in records:
            if rows==entryIndex:
                values=tv2.item(rows)["values"]
                text=tv2.item(rows)["text"]
                #print("values are",values)
                #print("text is",text)
                global v
                global w
                global x
                global y
                global z
                global e1
                Aname.set(text)
                Aemail.set(values[0])
                Auname.set(values[1])
                Apwd.set(values[2])
                

                    

#======================================================Update Book=============================================
    def UpdateBook():
        a=Bid.get()
        b=Bname.get()
        c=Aname.get()
        d=Bprice.get()
        e=B_Category_Ent.get()

        
        connection=sqlite3.connect("Books")
        cursor = connection.cursor()

        sql="""Update Book set BID='%d',BOOK_NAME='%s',AUTHOR_NAME='%s',PRICE='%d',BOOK_CATEGORY='%s' where BID='%d'"""%(a,b,c,d,e,a)
        
        result=cursor.execute(sql)
        connection.commit()

        if(result):
            messagebox.showinfo("Message","Successfully Updated Record.")
            ShowBook()
            
                
        else:
            messagebox.showerror("Error","Unable to Update record...")

        Bid.set(" ")
        Bname.set(" ")
        Aname.set(" ")
        Bprice.set(" ")
        B_Category_Ent.set(" ")

#=============================================Delete Selected Book============================================
    def DeleteBook():

        global tv
        entryIndex=tv.focus()
        records=tv.get_children()

        if records == None :
            #print(records)
            messagebox.showerror("Error","Unable to delete record...")
        else:
            for rows in records:
                if rows==entryIndex:
                    values=tv.item(rows)["values"]
                    text=tv.item(rows)["text"]
                    connection = sqlite3.connect("Books")
                    cursor = connection.cursor()
                    resultfordel=messagebox.askyesno("Warning","Are you sure you want to delete selecetd record?")
                    if(resultfordel==True):
                        sql="""Delete from Book where BID = '%d' and Book_Name='%s' """ % (text,values[0])
                        result=cursor.execute(sql)
                        connection.commit()

                    
                        if(result):
                            messagebox.showinfo("Error","Successfully Deleted Record.")
                            tv.delete(entryIndex)
                            Bid.set(" ")
                            Bname.set(" ")
                            Aname.set(" ")
                            Bprice.set(" ")
                            B_Category_Ent.set(" ")
                        else:
                            messagebox.showerror("Error","Unable to delete record...")
                    else:
                        messagebox.shoinfo("Title","Think before you do...")
                        
                         

#=============================================Delete Selected Admin============================================
    def DeleteAdmin():

        global tv2
        entryIndex=tv2.focus()
        records=tv2.get_children()

        if records == None :
            #print(records)
            messagebox.showerror("Error","Unable to delete record...")
        else:
            for rows in records:
                if rows==entryIndex:
                    values=tv2.item(rows)["values"]
                    text=tv2.item(rows)["text"]
                    connection = sqlite3.connect("Books")
                    cursor = connection.cursor()
                    result=messagebox.askyesno("Warning","Are you sure you want to delete selected record ?")
                    if(result==True):
                        sql="""Delete from ADMIN where NAME = '%s' and EMAIL='%s' """ % (text,values[0])
                        result=cursor.execute(sql)
                        connection.commit()

                    
                        if(result):
                            messagebox.showinfo("Error","Successfully Deleted Record.")
                            tv2.delete(entryIndex)
                            Aname.set(" ")
                            Aemail.set(" ")
                            Auname.set(" ")
                            Apwd.set(" ")
                            
                        else:
                            messagebox.showerror("Error","Unable to delete record...")
                    else:
                        messagebox.shoinfo("Title","Think before you do...")
                        


#=======================================================Search Book=====================================================

    def SearchBook(Bsearch):
        item=Bsearch.get()
        selection=B_Search_Cmb.get()

##
## result=cursor.execute(sql)
##
##        for k in result:
##            tv.insert("",0,text=k[0],values=(k[1],k[2],k[3],k[4]))
##


        
        connection=sqlite3.connect("Books")
        cursor = connection.cursor()

        global tv
        records=tv.get_children()
        for rows in records:
            tv.delete(rows)
        if(selection=="By ID"):
##            global tv
##            records=tv.get_children()
##            for rows in records:
##                tv.delete(rows)
##                
            sql="""SELECT * FROM BOOK WHERE BID='%s' """ %(item)
            result=cursor.execute(sql)
            
            for k in result:
                tv.insert("",0,text=k[0],values=(k[1],k[2],k[3],k[4]))
                Bsearch.set("")
                B_Search_Cmb.set("")
            
            connection.commit()
        elif(selection=="By Book Name"):
           
                
            sql="""SELECT * FROM BOOK WHERE BOOK_NAME='%s' """ %(item)
            result=cursor.execute(sql)
            
            for k in result:
                tv.insert("",0,text=k[0],values=(k[1],k[2],k[3],k[4]))
                Bsearch.set("")
                B_Search_Cmb.set("")
            
            connection.commit()
        elif(selection=="By Author Name"):
            
                
            sql="""SELECT * FROM BOOK WHERE AUTHOR_NAME='%s' """ %(item)
            result=cursor.execute(sql)
            
            for k in result:
                tv.insert("",0,text=k[0],values=(k[1],k[2],k[3],k[4]))
                Bsearch.set("")
                B_Search_Cmb.set("")
            
            connection.commit()

        elif(selection=="By Book Category"):
            
                
            sql="""SELECT * FROM BOOK WHERE BOOK_CATEGORY='%s' """ %(item)
            result=cursor.execute(sql)
            
            for k in result:
                tv.insert("",0,text=k[0],values=(k[1],k[2],k[3],k[4]))
                Bsearch.set("")
                B_Search_Cmb.set("")
            
            connection.commit()

        else:
            print("Invalid Selection")

#==============================================================Show Issuer=============================================

    def ShowIssuer():
        global tv3
        records=tv3.get_children()
        for rows in records:
            tv3.delete(rows)
       
        connection=sqlite3.connect("Books")
        cursor = connection.cursor()

        sql="SELECT * FROM Issuer "
        result=cursor.execute(sql)
        

        for k in result:
            tv3.insert("",0,text=k[0],values=(k[1],k[3],k[4],k[5],k[7],k[8]))


        
#=============================================Delete Selected Issuer============================================
    def DeleteIssuer():

        global tv3
        entryIndex=tv3.focus()
        records=tv3.get_children()

        if records == None :
            #print(records)
            messagebox.showerror("Error","Unable to delete record...")
        else:
            for rows in records:
                if rows==entryIndex:
                    values=tv3.item(rows)["values"]
                    #print(values)
                    text=tv3.item(rows)["text"]
                    #print(text)
                    connection = sqlite3.connect("Books")
                    cursor = connection.cursor()
                    result=messagebox.askyesno("Warning","Are you sure you want to delete selected record ?")
                    if(result==True):
                        sql="""Delete from Issuer where Iname = '%s' and Irollno='%s' """ % (text,values[5])
                        result=cursor.execute(sql)
                        connection.commit()

                    
                        if(result):
                            messagebox.showinfo("Error","Successfully Deleted Record.")
                            
                            tv3.delete(entryIndex)
                            Iname.set(" ")
                            Icontact.set(" ")
                            Iemail.set(" ")
                            I_Book_Cmb.set(" ")
                            Idate.set(" ")
                            Rdate.set(" ")
                            I_Stream_Cmb.set(" ")
                            I_Class_Cmb.set(" ")
                            Irollno.set(" ")
                            ShowIssuer()
                            
                        else:
                            messagebox.showerror("Error","Unable to delete record...")
                    else:
                        messagebox.shoinfo("Title","Think before you do...")
                        


        

        
#==============================================================Add Issuer Record=======================================

    def AddIssuer(Iname,Icontact,Iemail,Ibook,Idate,Rdate,Irollno):
        iname=Iname.get()
        icontact=Icontact.get()
        iemail=Iemail.get()
        ibook=I_Book_Cmb.get()
        idate=Idate.get()
        rdate=Rdate.get()
        istream=I_Stream_Cmb.get()
        iclass=I_Class_Cmb.get()
        irollno=Irollno.get()

        


        #========Contact length===========
        contactlen=len(str(icontact))
        #print("contact is",contactlen)
        
        if(iname==" " or icontact==0 or icontact==" " or iemail==" " or ibook==" " or idate==" " or rdate==" " or irollno==0 or irollno==" "):
            messagebox.showerror("Warning","Fields are blank..")

        elif(contactlen != 10):
            messagebox.showerror("Warning","Contact number should consist of 10 digits..")
            
        else:    
            try:
                #print(filename)
                connection=sqlite3.connect("Books")#=================================================                print(filename)print(iname)print(icontact)print(iemail)print(ibook)print(idate)print(rdate)print(istream)print(iclass)print(irollno)
                cursor = connection.cursor()

                    
                

                sql="""CREATE TABLE IF NOT EXISTS Issuer(Iname Varchar(40),Icontact Bigint,Iemail VARCHAR(50),Ibook VARCHAR(40),Idate Date,Rdate Date,Istream Varchar(40),Iclass Varchar(40),Irollno Int PRIMARY KEY ,Imagepath Varchar(300)) """
        
                cursor.execute(sql)

                sqlquery="""INSERT INTO Issuer (Iname,Icontact,Iemail,Ibook,Idate,Rdate,Istream,Iclass,Irollno,Imagepath)VALUES ('%s','%d','%s','%s','%s','%s','%s','%s','%d','%s') """ % (iname,icontact,iemail,ibook,idate,rdate,istream,iclass,irollno,filename)
                result=cursor.execute(sqlquery)
                connection.commit()

                if(result):
                    messagebox.showinfo("Message","Successfully inserted one record")
                    Iname.set(" ")
                    Icontact.set(" ")
                    Iemail.set(" ")
                    I_Book_Cmb.set(" ")
                    Idate.set(" ")
                    Rdate.set(" ")
                    I_Stream_Cmb.set(" ")
                    I_Class_Cmb.set(" ")
                    Irollno.set(" ")
                    ShowIssuer()
                else:
                    messagebox.showerror("Message","Something Went Wrong")

                

                
            except:
                ShowIssuer()
                messagebox.showerror("Warning","Issuer image is not selecetd..")
            
                
        
        
#==============================================================Add Issuer Photo========================================
    def AddPhoto():
        global filename
        filename=filedialog.askopenfilename(initialdir="F:/book/Book.ico",title="Select a file",filetypes=(("png files","*.png"),("jpg files","*.jpg"),("All files","*.*")))
        #print(filename)


        try:
            image=Image.open((filename))
            image=image.resize((230,230),Image.ANTIALIAS)
            Iimage=ImageTk.PhotoImage(image)#Image.open(frmR.filename)
            global Artwork
            Artwork=Label(frmR,image=Iimage,height=230,width=250)
            Artwork.photo=Iimage
            Artwork.place(x=730,y=70)
            return filename
        except AttributeError:
            print("Query Completed..")

#==================================================

    def SearchIssuer(Isearch):
        isearch=Isearch.get()
        iselection=I_Search_Cmb.get()

        connection=sqlite3.connect("Books")
        cursor = connection.cursor()

        global tv3
        records=tv3.get_children()
        for rows in records:
            tv3.delete(rows)
        if(iselection=="By Issuer Name"):
                
            sql="""SELECT * FROM Issuer WHERE Iname='%s' """ %(isearch)
            result=cursor.execute(sql)
            
            for k in result:
                tv3.insert("",0,text=k[0],values=(k[1],k[3],k[4],k[5],k[7],k[8]))
                Isearch.set("")
                I_Search_Cmb.set("")
            
            connection.commit()
        elif(iselection=="By Book Name"):
           
                
            sql="""SELECT * FROM Issuer WHERE Ibook='%s' """ %(isearch)
            result=cursor.execute(sql)
            
            for k in result:
                tv3.insert("",0,text=k[0],values=(k[1],k[3],k[4],k[5],k[7],k[8]))
                Isearch.set("")
                I_Search_Cmb.set("")
            
            connection.commit()
        elif(iselection=="By Roll No"):
           
                
            sql="""SELECT * FROM Issuer WHERE Irollno='%s' """ %(isearch)
            result=cursor.execute(sql)
            
            for k in result:
                tv3.insert("",0,text=k[0],values=(k[1],k[3],k[4],k[5],k[7],k[8]))
                Isearch.set("")
                I_Search_Cmb.set("")
            
            connection.commit()
        
        elif(iselection=="By Stream"):
           
                
            sql="""SELECT * FROM Issuer WHERE Istream='%s' """ %(isearch)
            result=cursor.execute(sql)
            
            for k in result:
                tv3.insert("",0,text=k[0],values=(k[1],k[3],k[4],k[5],k[7],k[8]))
                Isearch.set("")
                I_Search_Cmb.set("")
            
            connection.commit()
        elif(iselection=="By Class"):
           
                
            sql="""SELECT * FROM Issuer WHERE Iclass='%s' """ %(isearch)
            result=cursor.execute(sql)
            
            for k in result:
                tv3.insert("",0,text=k[0],values=(k[1],k[3],k[4],k[5],k[7],k[8]))
                Isearch.set("")
                I_Search_Cmb.set("")
            
            connection.commit()
            
        

        else:
            print("Invalid Selection")

#==========================================Send Mail===================================================

    def SendEmail():
        Issuername=Iname.get()
        Bname=I_Book_Cmb.get()
        TO=Iemail.get()
        idate=Idate.get()
        rdate=Rdate.get()
        cdate=str(datetime.date(datetime.now()))
        
        #print(Issuername)
        #print(Bname)
        #print(TO)
        
        
        SUBJECT="Reminder"
        TEXT="Dear,"+Issuername+". \n\nThis email is just to remind you that you have not returned the Book "+Bname+" taken on "+idate+".It\'s returning date was "+rdate+" and today is "+cdate+"."

        gmail_sender='tejashatle3@gmail.com'
        gmail_passwd='Tejashatle123'
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender,gmail_passwd)
        BODY='\r\n'.join(['TO:%s'%TO,'From:%s'%gmail_sender,'SUBJECT:%s'%SUBJECT,'',TEXT])
        try:
            server.sendmail(gmail_sender,[TO],BODY)
            messagebox.showinfo("Message","Email sent")
        except:
            messagebox.showerror("Message","Something went wrong..") 
            server.quit()



        
#===============================================Display Value In EntryBox(FOR ISSUER)==========================================
    def DisplayValue3(event):
        global tv3
        entryIndex=tv3.focus()
        records=tv3.get_children()
        global Browse
        Browse.configure(state="disabled")
        connection=sqlite3.connect("Books")
        cursor = connection.cursor()


        for rows in records:
            if rows==entryIndex:
                values=tv3.item(rows)["values"]
                #print("values",values)
                text=tv3.item(rows)["text"]
                #print("text",text)
                #print("values are",values)
                #print("text is",text)
                rdate=values[3]
                #rdate=datetime.date.strptime(rdate,"%d/%m/%Y")
                cdate=str(datetime.date(datetime.now()))
                #print("rdate is",rdate)
                #print("date is",cdate)
                if(cdate>rdate):
                    SendMail.configure(state="normal")
                    #print("Current date is bigger...")
                else:
                    #print("current is Smaller..")
                    SendMail.configure(state="disabled")
                    
                
                global v
                global w
                global x
                global y
                global z
                global e1
#Iname,Icontact,Iemail,Ibook,Idate,Rdate,Irollno
                sql="SELECT * FROM Issuer WHERE Iname='%s'" %(text)
                result=cursor.execute(sql)
                

                for k in result:
                    Iname.set(k[0])
                    Icontact.set(k[1])
                    Iemail.set(k[2])
                    I_Book_Cmb.set(k[3])
                    Idate.set(k[4])
                    Rdate.set(k[5])
                    I_Stream_Cmb.set(k[6])
                    I_Class_Cmb.set(k[7])
                    Irollno.set(k[8])
                    filenm=k[9]
                    try:
                        image=Image.open((filenm))
                        image=image.resize((230,230),Image.ANTIALIAS)
                        Iimage=ImageTk.PhotoImage(image)#Image.open(frmR.filename)
                        global Artwork
                        Artwork=Label(frmR,image=Iimage,height=230,width=250)
                        Artwork.photo=Iimage
                        Artwork.place(x=730,y=70)
                    except:
                        messagebox.showerror("Warning","Something Went Wrong...")    
                
        #print("Emailisin",email)
#===============================================Update Issuer=================================================
    
    def UpdateIssuer():
        iname=Iname.get()
        icontact=Icontact.get()
        iemail=Iemail.get()
        ibook=I_Book_Cmb.get()
        idate=Idate.get()
        rdate=Rdate.get()
        istream=I_Stream_Cmb.get()
        iclass=I_Class_Cmb.get()
        irollno=Irollno.get()
##        global filename
##        print("filename is",filename)
        

        #========Contact length===========
        contactlen=len(str(icontact))
        #print("contact is",contactlen)
        
        if(iname==" " or icontact==0 or icontact==" " or iemail==" " or ibook==" " or idate==" " or rdate==" " or irollno==0 or irollno==" "):
            messagebox.showerror("Warning","Fields are blank..")

        elif(contactlen != 10):
            messagebox.showerror("Warning","Contact number should consist of 10 digits..")
            
        else:
            result=messagebox.askyesno("Warning","Do you want to update Image ?")
            if(result==True):
                AddPhoto()
                global filename
                #print("FilenameinADDHOTO",filename)
            else:
                connection=sqlite3.connect("Books")
                cursor = connection.cursor()

                sqlpath="Select * from Issuer"
                resultpath=cursor.execute(sqlpath)
                for path in resultpath:
                    filename=path[9]

                #print("Filenam is",filename)

                        
            connection=sqlite3.connect("Books")#========================================iname,icontact,iemail,ibook,idate,rdate,istream,iclass,irollno,filename,iname
            cursor = connection.cursor()

            
            sql="""Update Issuer set Iname='%s',Icontact='%d',Iemail='%s',Ibook='%s',Idate='%s',Rdate='%s',Istream='%s',Iclass='%s',Irollno='%d',Imagepath='%s' where Irollno='%d' """%(iname,icontact,iemail,ibook,idate,rdate,istream,iclass,irollno,filename,irollno)
    
            result=cursor.execute(sql)
            connection.commit()

            if(result):
                messagebox.showinfo("Message","Successfully Updated Record.")
                ShowIssuer()
                
                    
            else:
                messagebox.showerror("Error","Unable to Update record...")

            Iname.set(" ")
            Icontact.set(" ")
            Iemail.set(" ")
            I_Book_Cmb.set(" ")
            Idate.set(" ")
            Rdate.set(" ")
            I_Stream_Cmb.set(" ")
            I_Class_Cmb.set(" ")
            Irollno.set(" ")
##            except NameError:
##                messagebox.showerror("Warning","Issuer image is not selecetd..")
##                            
##                


        
                    
                    
        
#====================================Add Book Panel============================================================                
                    
    def Add_New_Book():

        Remove_Widgets()
        #print("flag is",flag)
        main_lbl=Label(frmR,text="New Book Entry",font=('Times New Roman', 20,'bold'),bg="#b3daff")
        main_lbl.place(x=430,y=20)

        global tv
        tv=ttk.Treeview(frmR,selectmode="extended",height=15,columns=("Id","Book name","Author name","price","book category"))
    

        global Bid
        global Bname
        global Aname
        global Bprice
        global Bcategory
        global Bsearch
        
        Bid=IntVar()
        Bname=StringVar()
        Aname=StringVar()
        Bprice=IntVar()
        Bcategory=StringVar()
        Bsearch=StringVar()
        
        B_ID_Lbl=Label(frmR,text="Enter Book ID",height=1,width=15,font=('Verdana', 10,'bold'))
        B_ID_Lbl.place(x=15,y=70)#grid(row=0,column=0)

        B_ID_Ent=Entry(frmR,textvariable=Bid,bd=3,width=25) 
        B_ID_Ent.place(x=165,y=70)#grid(row=0,column=1)



        B_Name_Lbl=Label(frmR,text="Enter Book Name",height=1,width=15,font=('Verdana', 10,'bold'))
        B_Name_Lbl.place(x=350,y=70)#grid(row=1,column=0)

        B_Name_Ent=Entry(frmR,textvariable=Bname,bd=3,width=25)
        B_Name_Ent.place(x=500,y=70)#grid(row=1,column=1)

        

        A_Name_Lbl=Label(frmR,text="Enter Author Name",height=1,width=15,font=('Verdana', 10,'bold'))
        A_Name_Lbl.place(x=685,y=70)#grid(row=2,column=0)

        A_Name_Ent=Entry(frmR,textvariable=Aname,bd=3,width=25)
        A_Name_Ent.place(x=835,y=70)#grid(row=2,column=1)


        
        B_Price_Lbl=Label(frmR,text="Enter Book Price",height=1,width=17,font=('Verdana', 10,'bold'))
        B_Price_Lbl.place(x=165,y=120)#grid(row=2,column=0)

        B_Price_Ent=Entry(frmR,textvariable=Bprice,bd=3,width=25)
        B_Price_Ent.place(x=350,y=120)#grid(row=2,column=1)


        
        B_Category_Lbl=Label(frmR,text="Enter Book Category",height=1,width=17,font=('Verdana', 10,'bold'))
        B_Category_Lbl.place(x=520,y=120)#grid(row=2,column=0)


        global B_Category_Ent
        B_Category_Ent=ttk.Combobox(frmR,values=["Science Fiction","satire","drama","Action and Adventure","Romance","mystery","horror","self help","guide","travel","children's","religious","science","history","math","anthologies","poetry","encyclopedia","dictionaries","comics","art","cookbooks","diaries","prayer books","series","trilogies","biographies","autobiographies","fantasy"])
        B_Category_Ent.place(x=690,y=120)#grid(row=2,column=1)


        AddBookBtn=Button(frmR,text="Add Book",width=15,height=2,bg="#80c1ff",font=('Verdana',10,'bold'),command= lambda: AddBook(Bid,Bname,Aname,Bprice))
        AddBookBtn.place(x=15,y=180)

        ShowBookBtn=Button(frmR,text="Show Book",width=15,height=2,bg="#80c1ff",font=('Verdana',10,'bold'),command= ShowBook)
        ShowBookBtn.place(x=230,y=180)

        UpdateBookBtn=Button(frmR,text="Update Book",width=15,height=2,bg="#80c1ff",font=('Verdana',10,'bold'),command= UpdateBook)
        UpdateBookBtn.place(x=430,y=180)

        DeleteBookBtn=Button(frmR,text="Delete Book",width=15,height=2,bg="#80c1ff",font=('Verdana',10,'bold'),command= DeleteBook)
        DeleteBookBtn.place(x=630,y=180)


        searchlbl=Label(frmR,text="Select Search Choice",height=1,width=17,font=('Verdana', 10,'bold'))
        searchlbl.place(x=15,y=250)

        global B_Search_Cmb
        B_Search_Cmb=ttk.Combobox(frmR,values=["By ID","By Book Name","By Author Name","By Book Category"])
        B_Search_Cmb.place(x=200,y=250)#grid(row=2,column=1)

        B_Search_Ent=Entry(frmR,textvariable=Bsearch,bd=3,width=25)
        B_Search_Ent.place(x=370,y=250)#grid(row=2,column=1)
        
        SearchBookBtn=Button(frmR,text="Search Book",width=15,height=1,bg="#80c1ff",font=('Verdana',10,'bold'),command= lambda: SearchBook(Bsearch))
        SearchBookBtn.place(x=550,y=250)
        
        lbl=Label(frmR,text="Database",font=('Times New Roman', 20,'bold'),bg="#b3daff")
        lbl.place(x=430,y=300)

        
        tv.place(x=15,y=350)
        tv.heading("#0",text="ID")
        tv.column("#0",minwidth=0,width=150, stretch=NO)
        tv.heading("#1",text="Book Name")
        tv.column("#1",minwidth=0,width=150, stretch=NO)
        tv.heading("#2",text="Author Name")
        tv.column("#2",minwidth=0,width=150, stretch=NO)
        tv.heading("#3",text="Book Price")
        tv.column("#3",minwidth=0,width=150, stretch=NO)
        tv.heading("#4",text="Book Category")
        tv.column("#4",minwidth=0,width=150, stretch=NO)

        scrollv=Scrollbar(frmR,orient="vertical",command=tv.yview)
        scrollv.place(x=1000,y=350)
        tv.configure(yscrollcommand=scrollv.set)
        tv.bind('<Button-1>', DisplayValue)

#==============================================================Add New Issuer======================================================        
    def Add_New_Issuer():

        Remove_Widgets()
        main_lbl=Label(frmR,text="New Issuer Entry",font=('Times New Roman', 20,'bold'),bg="#b3daff")
        main_lbl.place(x=430,y=20)

        global tv3
        tv3=ttk.Treeview(frmR,selectmode="extended",height=13,columns=("Issuer Name","Contact","Book Name","Book Issued Date","Issuer Class","Book Returning Date"))
    

        global Iname
        global Icontact
        global Iemail
        global Ibook
        global Idate
        global Rdate
        global Irollno

        Iname=StringVar()
        Icontact=IntVar()
        Iemail=StringVar()
        Ibook=StringVar()
        Idate=StringVar()
        Rdate=StringVar()
        Irollno=IntVar()
        Isearch=StringVar()

        
        I_Name_Lbl=Label(frmR,text="Enter Issuer Name",height=1,width=15,font=('Verdana', 10,'bold'))
        I_Name_Lbl.place(x=15,y=70)#grid(row=0,column=0)

        I_Name_Ent=Entry(frmR,textvariable=Iname,bd=3,width=25) 
        I_Name_Ent.place(x=165,y=70)#grid(row=0,column=1)



        I_Contact_Lbl=Label(frmR,text="Enter Issuer Contact",height=1,width=18,font=('Verdana', 10,'bold'))
        I_Contact_Lbl.place(x=350,y=70)#grid(row=1,column=0)

        I_Contact_Ent=Entry(frmR,textvariable=Icontact,bd=3,width=25)
        I_Contact_Ent.place(x=530,y=70)#grid(row=1,column=1)

        
        I_Email_Lbl=Label(frmR,text="Enter Issuer Email",height=1,width=15,font=('Verdana', 10,'bold'))
        I_Email_Lbl.place(x=15,y=110)#grid(row=0,column=0)

        I_Email_Ent=Entry(frmR,textvariable=Iemail,bd=3,width=25) 
        I_Email_Ent.place(x=165,y=110)#grid(row=0,column=1)



        I_Book_Lbl=Label(frmR,text="Enter Issued Book",height=1,width=18,font=('Verdana', 10,'bold'))
        I_Book_Lbl.place(x=350,y=110)#grid(row=1,column=0)

        booklist=[]
        connection=sqlite3.connect("Books")
        cursor = connection.cursor()

        sql="""SELECT BOOK_NAME FROM BOOK """ 
        result=cursor.execute(sql)
        for k in result.fetchall():
            booklist.append(k[0])
            

        
        global I_Book_Cmb
        I_Book_Cmb=ttk.Combobox(frmR,width=23,values=booklist)
        I_Book_Cmb.place(x=530,y=110)#grid(row=2,column=1)

##        I_Book_Ent=Entry(frmR,textvariable=Ibook,bd=3,width=25)
##        I_Book_Ent.place(x=530,y=110)#grid(row=1,column=1)


        I_Idate_Lbl=Label(frmR,text="Enter Issued Date",height=1,width=15,font=('Verdana', 10,'bold'))
        I_Idate_Lbl.place(x=15,y=150)#grid(row=0,column=0)

        I_Idate_Ent=Entry(frmR,textvariable=Idate,bd=3,width=25) 
        I_Idate_Ent.place(x=165,y=150)#grid(row=0,column=1)



        I_Rdate_Lbl=Label(frmR,text="Enter Returning Date",height=1,width=18,font=('Verdana', 10,'bold'))
        I_Rdate_Lbl.place(x=350,y=150)#grid(row=1,column=0)

        I_Rdate_Ent=Entry(frmR,textvariable=Rdate,bd=3,width=25)
        I_Rdate_Ent.place(x=530,y=150)#grid(row=1,column=1)


        I_Stream_Lbl=Label(frmR,text="Select Stream",height=1,width=15,font=('Verdana', 10,'bold'))
        I_Stream_Lbl.place(x=15,y=190)#grid(row=0,column=0)

        global I_Stream_Cmb
        I_Stream_Cmb=ttk.Combobox(frmR,width=23,values=["BMS","BMM","BIOTECH","CS","IT"])
        I_Stream_Cmb.place(x=165,y=190)#grid(row=2,column=1)


        I_Class_Lbl=Label(frmR,text="Select Class",height=1,width=18,font=('Verdana', 10,'bold'))
        I_Class_Lbl.place(x=350,y=190)#grid(row=0,column=0)

        global I_Class_Cmb
        I_Class_Cmb=ttk.Combobox(frmR,width=23,values=["FY","SY","TY"])
        I_Class_Cmb.place(x=530,y=190)#grid(row=2,column=1)

        
        I_Rollno_Lbl=Label(frmR,text="Enter Issuer Roll No.",height=1,width=16,font=('Verdana', 10,'bold'))
        I_Rollno_Lbl.place(x=15,y=230)#grid(row=0,column=0)
        
        I_Rollno_Ent=Entry(frmR,textvariable=Irollno,bd=3,width=25) 
        I_Rollno_Ent.place(x=168,y=230)#grid(row=0,column=1)

        I_ChooseImg_Lbl=Label(frmR,text="Choose Image",height=1,width=18,font=('Verdana', 10,'bold'))
        I_ChooseImg_Lbl.place(x=350,y=230)#grid(row=0,column=0)
        
        tv3.place(x=15,y=370)
        tv3.heading("#0",text="Issuer Name")
        tv3.column("#0",minwidth=0,width=150, stretch=NO)
        tv3.heading("#1",text="Contact")
        tv3.column("#1",minwidth=0,width=150, stretch=NO)
        tv3.heading("#2",text="Book Name")
        tv3.column("#2",minwidth=0,width=130, stretch=NO)
        tv3.heading("#3",text="Book IDate")
        tv3.column("#3",minwidth=0,width=130, stretch=NO)
        tv3.heading("#4",text="Book RDate")
        tv3.column("#4",minwidth=0,width=150, stretch=NO)
        tv3.heading("#5",text="Issuer Class")
        tv3.column("#5",minwidth=0,width=130, stretch=NO)
        tv3.heading("#6",text="Issuer ROLLNO")
        tv3.column("#6",minwidth=0,width=120, stretch=NO)



        scrollv3=Scrollbar(frmR,orient="vertical",command=tv3.yview)
        scrollv3.place(x=990,y=370)
        tv3.configure(yscrollcommand=scrollv3.set)
        tv3.bind('<Button-1>', DisplayValue3)
        

        global Browse
        Browse=Button(frmR,text="Browse",width=17,height=1,bg="#80c1ff",font=('Verdana',10,'bold'),command= lambda : AddPhoto())
        Browse.place(x=530,y=230)


        IssuerSubmit=Button(frmR,text="Submit",width=15,height=2,bg="#80c1ff",font=('Verdana',10,'bold'),command= lambda : AddIssuer(Iname,Icontact,Iemail,Ibook,Idate,Rdate,Irollno))
        IssuerSubmit.place(x=15,y=270)
        
        ShowIssuerBtn=Button(frmR,text="Show",width=15,height=2,bg="#80c1ff",font=('Verdana',10,'bold'),command= ShowIssuer)
        ShowIssuerBtn.place(x=190,y=270)

        UpdateIssuerBtn=Button(frmR,text="Update",width=15,height=2,bg="#80c1ff",font=('Verdana',10,'bold'),command= UpdateIssuer)
        UpdateIssuerBtn.place(x=370,y=270)
        
        DeleteIssuerBtn=Button(frmR,text="Delete",width=15,height=2,bg="#80c1ff",font=('Verdana',10,'bold'),command= DeleteIssuer)
        DeleteIssuerBtn.place(x=546,y=270)

        searchlbl2=Label(frmR,text="Select Search Choice",height=1,width=17,font=('Verdana', 10,'bold'))
        searchlbl2.place(x=15,y=330)

        global I_Search_Cmb
        I_Search_Cmb=ttk.Combobox(frmR,values=["By Issuer Name","By Book Name","By Roll No","By Stream","By Class"])
        I_Search_Cmb.place(x=200,y=330)#grid(row=2,column=1)

        I_Search_Ent=Entry(frmR,textvariable=Isearch,bd=3,width=25)
        I_Search_Ent.place(x=370,y=330)#grid(row=2,column=1)
        
        ISearchBookBtn=Button(frmR,text="Search Issuer",width=15,height=1,bg="#80c1ff",font=('Verdana',10,'bold'),command= lambda: SearchIssuer(Isearch))
        ISearchBookBtn.place(x=548,y=330)
        
        global SendMail
        SendMail=Button(frmR,text="Send Mail",width=27,height=1,bg="#80c1ff",font=('Verdana',10,'bold'),command= lambda: SendEmail())
        SendMail.place(x=730,y=330)
        
        

        ShowIssuer()
        

        #print(path)



        
#=========================================================Add Admin in DB===========================================================            
    def AddAdmin(Aname,Aemail,Auname,Apwd):
        aname=Aname.get()
        aemail=Aemail.get()
        auname=Auname.get()
        apwd=Apwd.get()
   
      

        connection=sqlite3.connect("Books")
        cursor = connection.cursor()


        sqlquery="""INSERT INTO ADMIN(Name,Email,Username,Password) VALUES ('%s','%s','%s','%s') """ %  (aname,aemail,auname,apwd)
        result=cursor.execute(sqlquery)
        connection.commit()

        if(result):
            messagebox.showinfo("Message","Successfully inserted one record")
        else:
            messagebox.showerror("Message","Something Went Wrong")


        Aname.set("")
        Aemail.set("")
        Auname.set("")
        Apwd.set("")
       
#======================================================Update Book=============================================
    def UpdateAdmin():
        aname=Aname.get()
        aemail=Aemail.get()
        auname=Auname.get()
        apwd=Apwd.get()
   

        
        connection=sqlite3.connect("Books")
        cursor = connection.cursor()

        sql="""Update Admin set Name='%s',Email='%s',Username='%s',Password='%s' where Name='%s'"""%(aname,aemail,auname,apwd,aname)
        
        result=cursor.execute(sql)
        connection.commit()

        if(result):
            messagebox.showinfo("Message","Successfully Updated Record.")
            ShowAdmin()
            
                
        else:
            messagebox.showerror("Error","Unable to Update record...")

        Aname.set(" ")
        Aemail.set(" ")
        Auname.set(" ")
        Apwd.set(" ")
        
        

#=====================================================Add New Admin================================================================        
    def Add_New_Admin():

        Remove_Widgets()
        main_lbl3=Label(frmR,text="New Admin Entry",font=('Times New Roman', 20,'bold'),bg="#b3daff")
        main_lbl3.place(x=430,y=20)

        global tv2
        tv2=ttk.Treeview(frmR,selectmode="extended",height=15,columns=("Admin name","Admin Email","Username","Password"))
    
        global Aname
        global Aemail
        global Auname
        global Apwd
        
        
        Aname=StringVar()
        Aemail=StringVar()
        Auname=StringVar()
        Apwd=StringVar()

        
        A_Name_Lbl=Label(frmR,text="Enter Admin Name",height=1,width=15,font=('Verdana', 10,'bold'))
        A_Name_Lbl.place(x=15,y=70)#grid(row=0,column=0)

        A_Name_Ent=Entry(frmR,textvariable=Aname,bd=3,width=25) 
        A_Name_Ent.place(x=165,y=70)#grid(row=0,column=1)



        A_Email_Lbl=Label(frmR,text="Enter Admin Email",height=1,width=15,font=('Verdana', 10,'bold'))
        A_Email_Lbl.place(x=350,y=70)#grid(row=1,column=0)

        A_Email_Ent=Entry(frmR,textvariable=Aemail,bd=3,width=25)
        A_Email_Ent.place(x=500,y=70)#grid(row=1,column=1)

        

        A_UName_Lbl=Label(frmR,text="Enter Admin Username",height=1,width=18,font=('Verdana', 10,'bold'))
        A_UName_Lbl.place(x=685,y=70)#grid(row=2,column=0)

        A_UName_Ent=Entry(frmR,textvariable=Auname,bd=3,width=25)
        A_UName_Ent.place(x=860,y=70)#grid(row=2,column=1)


        
        A_Pwd_Lbl=Label(frmR,text="Enter Admin Password",height=1,width=18,font=('Verdana', 10,'bold'))
        A_Pwd_Lbl.place(x=165,y=120)#grid(row=2,column=0)

        A_Pwd_Ent=Entry(frmR,textvariable=Apwd,bd=3,width=25)
        A_Pwd_Ent.place(x=350,y=120)#grid(row=2,column=1)

        AddAdminBtn=Button(frmR,text="Add Admin",width=15,height=2,bg="#80c1ff",font=('Verdana',10,'bold'),command= lambda: AddAdmin(Aname,Aemail,Auname,Apwd))
        AddAdminBtn.place(x=15,y=180)

        ShowAdminBtn=Button(frmR,text="Show Admins",width=15,height=2,bg="#80c1ff",font=('Verdana',10,'bold'),command= lambda: ShowAdmin())
        ShowAdminBtn.place(x=230,y=180)

        UpdateAdminBtn=Button(frmR,text="Update Admin",width=15,height=2,bg="#80c1ff",font=('Verdana',10,'bold'),command= lambda: UpdateAdmin())
        UpdateAdminBtn.place(x=430,y=180)
        
        DeleteAdminBtn=Button(frmR,text="Delete Admin",width=15,height=2,bg="#80c1ff",font=('Verdana',10,'bold'),command= lambda: DeleteAdmin())
        DeleteAdminBtn.place(x=600,y=180)

        lbl=Label(frmR,text="Database",font=('Times New Roman', 20,'bold'),bg="#b3daff")
        lbl.place(x=430,y=300)

        
        tv2.place(x=90,y=350)
        tv2.heading("#0",text="Admin Name")
        tv2.column("#0",minwidth=0,width=150, stretch=NO)
        tv2.heading("#1",text="Admin Email")
        tv2.column("#1",minwidth=0,width=150, stretch=NO)
        tv2.heading("#2",text="Username")
        tv2.column("#2",minwidth=0,width=150, stretch=NO)
        tv2.heading("#3",text="Password")
        tv2.column("#3",minwidth=0,width=150, stretch=NO)

        scrollv2=Scrollbar(frmR,orient="vertical",command=tv2.yview)
        scrollv2.place(x=900,y=350)
        ShowAdmin()
        tv2.configure(yscrollcommand=scrollv2.set)
        tv2.bind('<Button-1>', DisplayValue2)
        




        
#======================================================================================================================================
        
#==============================================================Right Side Frame========================================================        

#======================================================================================================================================
    frmL=Frame(top,height=750,width=250)
    frmL.grid(row=0,column=0)
    canv = Canvas(frmL, width=280, height=750,bg='#80c1ff')
    canv.grid(row=0, column=1)

    img = ImageTk.PhotoImage(Image.open("F:/book/book2.png"))  # PIL solution
    canv.create_image(20, 20, anchor=NW, image=img)

    navbtn1=Button(frmL,text="ADD BOOK",width=35,height=2,bg="aqua",command=Add_New_Book)
    navbtn1.place(x=18,y=250)
    navbtn2=Button(frmL,text="ADD ISSUER",width=35,height=2,bg="aqua",command=Add_New_Issuer)
    navbtn2.place(x=18,y=300)
    navbtn3=Button(frmL,text="ADD ADMIN",width=35,height=2,bg="aqua",command=Add_New_Admin)
    navbtn3.place(x=18,y=350)
    
    
    navbtn5=Button(frmL,text="CLOSE",width=35,height=2,bg="aqua",command=Close_Window)
    navbtn5.place(x=18,y=400)

    global frmR
    frmR=Frame(top,height=750,width=1100,bg="#b3daff")
    frmR.grid(row=0,column=1)


    main_lbl=Label(frmR,text="About Us",font=('Times New Roman', 20,'bold'),bg="#b3daff")
    main_lbl.place(x=430,y=30)

    abtus=Label(frmR,text="This Software is developed by Tejas Hatle who is Computer Science Student and doing his Degree from Bhavan's College situated in Andheri (West).This is just a Demo software to work with Books Management.This software can be used to store data of books and their respective Issuer.Also we can store the data of Admins.Software can be used to send Gmail to issuer if they do not return their books before returning date.",height=7,width=86,wraplength=1000,font=('Verdana', 13,'bold'),fg="black")
    abtus.place(x=15,y=70)


    #print("Flag Is",flag)
    if(flag==1):
        navbtn3.configure(state="normal")
    else:
        navbtn3.configure(state="disabled")
    top.mainloop()
    

##f1=Frame(root,bg='dodger blue')
##f1.grid(row=1,column=1)
##canv = Canvas(f1, width=280, height=250,background='red')
##canv.grid(row=2, column=3)
##
##img = ImageTk.PhotoImage(Image.open("book2.png"))  # PIL solution
##canv.create_image(20, 20, anchor=NW, image=img)

#================================================Forget  Password=================================================

def forget_password():
    global top2
    top2=Tk()
    top2.title("Forget Password")
    top2.geometry('500x200')

   
    #=================================================Send OTP========================================================

    def send_otp():

        global TO    
        TO=Emailent1.get()
        
        print(TO)

        connection = sqlite3.connect("Books")
        cursor = connection.cursor()
        sql="""SELECT * FROM ADMIN WHERE Email='%s'""" %(TO)
        cursor.execute(sql)
        result = cursor.fetchall()
        print("results are",result)

        if(result):
            global OTP
            OTP=random.randrange(100000,999999)
            OTP=str(OTP)
            print(OTP)

            SUBJECT="Update Password "
            TEXT="Dear,"+TO+"\n\nYour OTP(One Time Password) is "+OTP+"."

            gmail_sender='tejashatle3@gmail.com'
            gmail_passwd='Tejashatle123'
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.login(gmail_sender,gmail_passwd)
            BODY='\r\n'.join(['TO:%s'%TO,'From:%s'%gmail_sender,'SUBJECT:%s'%SUBJECT,'',TEXT])
            try:
                server.sendmail(gmail_sender,[TO],BODY)
                messagebox.showinfo("Message","Email sent")
                top2.destroy()
                top4=Tk()

                top4.title("Verify OTP")
                top4.geometry('400x200')

                
                            
               


                def Verify_OTP():

                    Otp=OTPent1.get()
                    print("Otp is",Otp)

                    print("OTP is",OTP)

                    if(Otp==OTP):

                        top4.destroy()
                        top5=Tk()
                        top5.geometry('450x300')
                        top5.title('Update Password')

                        def Update_Password():

                            Upass=Emailent1pass.get()
                            ReUpass=Emailent2pass.get()

                            if(Upass==ReUpass):
                                
                                print(Upass)
                                print(TO)


                                connection=sqlite3.connect("Books")
                                cursor = connection.cursor()

                                sql="""Update Admin set Password='%s' where Email='%s'"""%(Upass,TO)
                                
                                result=cursor.execute(sql)
                                connection.commit()

                                if(result):
                                    lbldisplay.configure(text="")
                                    lbldisplay2.configure(text="Password Updated successfully,\nClose the Update Password Window to login.")
                                    
        
                                else:
                                    lbldisplay2.configure(text="")
                                    lbldisplay.configure(text="Something went wrong...")

                            else:
                                lbldisplay2.configure(text="")
                                lbldisplay.configure(text="Both the passwords do not match...")

                            



                        def close_update_password():
                            top5.destroy()

                            
                            
                        frpass=Frame(top5,bg='#80c1ff',relief='raised')
                        frpass.place(relwidth=1,relheight=1)
                        lblpass=Label(frpass,text="Update Password Panel",font=('Verdana', 20,'bold'),fg="white",bg='#80c1ff' ).grid(row=0,column=1,columnspan=2 ,padx=(40,0),pady=(10,0))
                        #lbl.grid(row=1,column=1)

                        global upass
                        upass=StringVar()
                        global reupass
                        reupass=StringVar()
                        
                        #ShowAdmin()
                        lbl1pass=Label(frpass,text="Enter Your New Password",height=3,width=25,font=('Verdana', 10,'bold'),bg='#80c1ff' ).grid(row=1,column=1)
                        global Emailent1pass
                        Emailent1pass=Entry(frpass,textvariable=upass,bd=6,width=30)
                        Emailent1pass.grid(row=1,column=2)

                        lbl2pass=Label(frpass,text="Re-Enter Your New Password",height=3,width=25,font=('Verdana', 10,'bold'),bg='#80c1ff' ).grid(row=2,column=1)
                        global Emailent2pass
                        Emailent2pass=Entry(frpass,textvariable=reupass,bd=6,width=30)
                        Emailent2pass.grid(row=2,column=2)

                        global lbldisplay
                        lbldisplay=Label(frpass,text="",fg="red",font=('Verdana', 10,'bold'),bg='#80c1ff')
                        lbldisplay.grid(row=3,column=1,columnspan=2)
                        
                        global lbldisplay2
                        lbldisplay2=Label(frpass,text="",fg="green",font=('Verdana', 10,'bold'),bg='#80c1ff')
                        lbldisplay2.grid(row=4,column=1,columnspan=2)
                        
                        btn1pass=Button(frpass,text="Update Password",command= lambda: Update_Password(),width=15,bd=3,bg="white",fg="black",relief="raised").grid(row=9,column=1)
                        btn2pass=Button(frpass,text="Close",command= lambda: close_update_password(),width=15,bd=3,bg="white",fg="black").grid(row=9,column=2)

                        top5.mainloop()
                    else:
                        messagebox.showerror("Warning","OTP do not matches...")


                frp=Frame(top4,bg='#80c1ff',relief='raised')
                frp.place(relwidth=1,relheight=1)
                lbl=Label(frp,text="Verify OTP",font=('Verdana', 20,'bold'),fg="white",bg='#80c1ff' ).grid(row=0,column=1,columnspan=2 ,padx=(40,0),pady=(10,0))
                #lbl.grid(row=1,column=1)

                global otp
                otp=IntVar()
                
                #ShowAdmin()
                lblOTP=Label(frp,text="Enter OTP",height=3,width=15,font=('Verdana', 10,'bold'),bg='#80c1ff' ).grid(row=1,column=1)
                global OTPent1
                OTPent1=Entry(frp,textvariable=otp,bd=6,width=30)
                OTPent1.grid(row=1,column=2)
                
                OTPbtn1=Button(frp,text="Verify OTP",command= lambda: Verify_OTP(),width=15,bd=3,bg="white",fg="black",relief="raised").grid(row=4,column=1)
                OTPbtn2=Button(frp,text="Close",width=15,bd=3,bg="white",fg="black").grid(row=4,column=2)

                top4.mainloop()
            except:
                messagebox.showerror("Message","Something went wrong..") 
                server.quit()

        else:
            messagebox.showerror("Warning","Given email is not in the records....")
        

    #=================================================close_forget_password=================================================

    def close_forget_password():
        top2.destroy()

    
    fr=Frame(top2,bg='#80c1ff',relief='raised')
    fr.place(relwidth=1,relheight=1)
    lbl=Label(fr,text="Forget Password Panel",font=('Verdana', 20,'bold'),fg="white",bg='#80c1ff' ).grid(row=0,column=1,columnspan=2 ,padx=(40,0),pady=(10,0))
    #lbl.grid(row=1,column=1)

    global emailid
    emailid=StringVar()
    
    #ShowAdmin()
    lbl1=Label(fr,text="Enter Your Registered Email",height=3,width=25,font=('Verdana', 10,'bold'),bg='#80c1ff' ).grid(row=1,column=1)
    global Emailent1
    Emailent1=Entry(fr,textvariable=emailid,bd=6,width=30)
    Emailent1.grid(row=1,column=2)
    
    btn1=Button(fr,text="Send OTP",command= lambda: send_otp(),width=15,bd=3,bg="white",fg="black",relief="raised").grid(row=4,column=1)
    btn2=Button(fr,text="Close",command= lambda: close_forget_password(),width=15,bd=3,bg="white",fg="black").grid(row=4,column=2)

    
    top2.mainloop()

  


#===========================================================Login Panel Code================================================================
f2=Frame(root,bg='#80c1ff',relief='raised')
f2.place(relwidth=1,relheight=1)
lbl=Label(f2,text="Login Panel",font=('Verdana', 20,'bold'),fg="white",bg='#80c1ff' ).grid(row=0,column=1,columnspan=2 ,padx=(40,0),pady=(10,0))
#lbl.grid(row=1,column=1)

global un
global pwd
global Checked
un=StringVar()
pwd=StringVar()
Checked=IntVar()
Admin_Insert()
#ShowAdmin()
label=Label(f2, text="Admin Panel",font=('Verdana', 20,'bold'),fg="white",bg='#80c1ff' ).grid(row=0,column=1,columnspan=2 ,padx=(40,0),pady=(10,0))
lbl1=Label(f2,text="Enter User Name",height=3,width=20,font=('Verdana', 10,'bold'),bg='#80c1ff' ).grid(row=1,column=1)
global ent1
ent1=Entry(f2,textvariable=un,bd=6,width=30).grid(row=1,column=2)
lbl2=Label(f2,text="Enter Password",height=3,width=20,font=('Verdana', 10,'bold'),bg='#80c1ff' ).grid(row=2,column=1)
ent2=Entry(f2,textvariable=pwd,show="*",bd=6,width=30)
ent2.grid(row=2,column=2)

chk=Checkbutton(f2,text="show Password.", variable=Checked,bg='#80c1ff' ,command=ShowPass,width=10,bd=6,font=('Verdana', 10,'bold'))
chk.grid(row=3,column=2)    
btn1=Button(f2,text="Submit",command= lambda: admin_check(),width=15,bd=3,bg="white",fg="black",relief="raised").grid(row=4,column=1)
btn2=Button(f2,text="Close",command= lambda: close_main(),width=15,bd=3,bg="white",fg="black").grid(row=4,column=2)

btn3=Button(f2,text="Forget Password",command= lambda: forget_password(),width=42,bd=3,bg="white",fg="black").grid(row=5,column=1,columnspan=2,pady=10)



mainloop()
