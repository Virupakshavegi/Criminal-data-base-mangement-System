from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('Virupakshas CRIMINAL DATABASE MANAGEMENT SYSTEM')
        
        # variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_crime_time=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar ()
        self.var_birthMark=StringVar()
        self.var_crime_type=StringVar()
        self.var_status=StringVar()
        self.var_nickname=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()

        
        
        label_title=Label(self.root,text='CRIMINAL DATABASE MANAGEMENT SYSTEM',font=('times new roman',40,'bold'),bg='blanched almond',fg='gold')
        label_title.place(x=0,y=0,width=1530,height=70)
        #AP Police logo
        #img_logo=Image.open('images/APpolice.png')
        #img_logo=img_logo.resize((60,60), Image.ANTIALIAS)
        #self.photo_logo=ImageTk.PhotoImage(img_logo)
        #self.logo=Label(self.root, image=self.photo_logo)
        #self.logo.place(x=80, y=5,width=60,height=60)
        # Img_Frame
        #img_frame=Frame(self.root, bd=2,relief=RIDGE, bg='white')
        #img_frame.place(x=0, y=70,width=1530, height=130)
        #img1=Image.open('images/mb.png')
        #img1=img1.resize((540,160), Image.ANTIALIAS)
        #self.photo1=ImageTk.PhotoImage (img1)
        #Any img_1=Label(img_frame, image=self.photo1)
        #self.img_1.place(x=0, y=0, width=540,height=160)


        # Main Frame of the Label
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=200,width=1500,height=560)
        
        #Upper frame of the label
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal details',font=('times new roman',14,'bold'),fg='chartreuse4')
        upper_frame.place(x=10,y=10,width=1480,height=270)
         
        #Entities
        #Case number
        Case_id=Label(upper_frame,text='Case ID:',font=('arial',11,'bold'),fg='cornflower blue',bg='white')
        Case_id.grid(row=0,column=0,padx=2,sticky=W)
        
        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)
        
        #Accused number
        criminalnumber=Label(upper_frame,text='Criminal Number:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        criminalnumber.grid(row=0,column=2,padx=2,pady=7,sticky=W)
        
        criminalnumbentry=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('arial',11,'bold'))
        criminalnumbentry.grid(row=0,column=3,padx=2,pady=7,sticky=W)
        
        #Criminal original name
        criminaloriginalname=Label(upper_frame,text='Criminal Name:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        criminaloriginalname.grid(row=1,column=0,padx=2,pady=7,sticky=W)
        
        
        criminaloriginalnamentry=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        criminaloriginalnamentry.grid(row=1,column=1,padx=2,pady=7,sticky=W)
        
        #Crime time
        crimetime=Label(upper_frame,text='Crime time:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        crimetime.grid(row=1,column=2,padx=2,pady=7,sticky=W)
        
        
        criminalnicknamentry=ttk.Entry(upper_frame,textvariable=self.var_crime_time,width=22,font=('arial',11,'bold'))
        criminalnicknamentry.grid(row=1,column=3,padx=2,pady=7,sticky=W)
        
        #Date of Arrest
        dateofarrest=Label(upper_frame,text='Arrest date:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        dateofarrest.grid(row=2,column=0,padx=2,pady=7,sticky=W)
        
        
        arrestdatentry=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=('arial',11,'bold'))
        arrestdatentry.grid(row=2,column=1,padx=2,pady=7,sticky=W)
        
        #Date of Crime
        crimedate=Label(upper_frame,text='Crime date:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        crimedate.grid(row=2,column=2,padx=2,pady=7,sticky=W)
        
        
        crimedatentry=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=('arial',11,'bold'))
        crimedatentry.grid(row=2,column=3,padx=2,pady=7,sticky=W)
        
        #Address
        address=Label(upper_frame,text='Place of crime:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        address.grid(row=3,column=0,padx=2,pady=7,sticky=W)
        
        
        address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        address.grid(row=3,column=1,padx=2,pady=7,sticky=W)
        
        #Age of criminal
        age=Label(upper_frame,text='Age of the criminal:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        age.grid(row=3,column=2,padx=2,pady=7,sticky=W)
        
        
        age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',11,'bold'))
        age.grid(row=3,column=3,padx=2,pady=7,sticky=W)
        
        #Occupation of the criminal
        profession=Label(upper_frame,text='Profession:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        profession.grid(row=4,column=0,padx=2,pady=7,sticky=W)
        
        
        profession=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=('arial',11,'bold'))
        profession.grid(row=4,column=1,padx=2,pady=7,sticky=W)
        
        #BirthMark
        birthmark=Label(upper_frame,text='BirthMark:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        birthmark.grid(row=4,column=2,padx=2,pady=7,sticky=W)
        
        
        birthmark=ttk.Entry(upper_frame,textvariable=self.var_birthMark,width=22,font=('arial',11,'bold'))
        birthmark.grid(row=4,column=3,padx=2,pady=7,sticky=W)
        
        #Type of crime
        crimetype=Label(upper_frame,text='Crime Category:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        crimetype.grid(row=0,column=4,padx=2,pady=7,sticky=W)
        
        
        crimetype=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=('arial',11,'bold'))
        crimetype.grid(row=0,column=5,padx=2,pady=7,sticky=W)
        
        #Current Status of crime
        status=Label(upper_frame,text='Current status of the crime:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        status.grid(row=1,column=4,padx=2,pady=7,sticky=W)
        
        
        status=ttk.Entry(upper_frame,textvariable=self.var_status,width=22,font=('arial',11,'bold'))
        status.grid(row=1,column=5,padx=2,pady=7,sticky=W)
        
         #Criminal nick name
        criminalnickname=Label(upper_frame,text='Criminal nickname:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        criminalnickname.grid(row=4,column=4,padx=2,pady=7,sticky=W)
        
        
        criminalnicknamentry=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=('arial',11,'bold'))
        criminalnicknamentry.grid(row=4,column=5,padx=2,pady=7,sticky=W)
        
        #Gender
        criminalgender=Label(upper_frame,text='Gender:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        criminalgender.grid(row=2,column=4,padx=2,pady=7,sticky=W)
        
        
        #criminalgender=ttk.Entry(upper_frame,textvariable=self.var_gender,width=22,font=('arial',11,'bold'))
        #criminalgender.grid(row=2,column=5,padx=2,pady=7,sticky=W)
        
        #Wanted
        
        
        #criminaltype=ttk.Entry(upper_frame,textvariable=self.var_wanted,width=22,font=('arial',11,'bold'))
        #criminaltype.grid(row=3,column=5,padx=2,pady=7,sticky=W)
        
        
        #ButtonsforGender
        #Gender
        criminalgender=Label(upper_frame,text='Gender:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        criminalgender.grid(row=2,column=4,padx=2,pady=7,sticky=W)
        
        radio_button_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_button_gender.place(x=870,y=80,width=190,height=30)
        
        male=Radiobutton(radio_button_gender,variable=self.var_gender,text='Male',value='male',font=('arial',9,'bold'),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        self.var_gender.set('male')
        
        female=Radiobutton(radio_button_gender,variable=self.var_gender,text='Female',value='female',font=('arial',9,'bold'),bg='white')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)
        
        #Button for criminal type
        criminaltype=Label(upper_frame,text='Most Wanted:',font=('arial',12,'bold'),fg='cornflower blue',bg='white')
        criminaltype.grid(row=3,column=4,padx=2,pady=7,sticky=W)
        
        radio_button_criminaltype=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_button_criminaltype.place(x=870,y=120,width=190,height=30)
        
        yes=Radiobutton(radio_button_criminaltype,variable=self.var_wanted,text='Yes',value='yes',font=('arial',9,'bold'),bg='white')
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        self.var_wanted.set('yes')
        
        no=Radiobutton(radio_button_criminaltype,variable=self.var_wanted,text='No',value='no',font=('arial',9,'bold'),bg='white')
        no.grid(row=0,column=1,pady=2,padx=5,sticky=W)
        
        #Buttons
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=620,height=45)
        
        #Insert button
        button_insert=Button(button_frame,command=self.add_data,text='Insert',font=("arial",13,"bold"),width=14,bg='red',fg='white')
        button_insert.grid(row=0, column=0, padx=3, pady=5)
        
        #Update button
        button_update=Button(button_frame,command=self.update_date,text='Update',font=("arial",13,"bold"),width=14,bg='red',fg='white')
        button_update.grid(row=0, column=1, padx=3, pady=5)
        
        #Delete button
        button_delete=Button(button_frame,command=self.delete_data,text='Delete',font=("arial",13,"bold"),width=14,bg='red',fg='white')
        button_delete.grid(row=0, column=2, padx=3, pady=5)
        
        #Clear button
        button_clear=Button(button_frame,command=self.clear_data,text='Clear',font=("arial",13,"bold"),width=14,bg='red',fg='white')
        button_clear.grid(row=0, column=3, padx=3, pady=5)
        
        
        
        #Lower frame of the label(which shows the DBMS table)
        lower_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal information table',font=('times new roman',11,'bold'),fg='chartreuse4')
        lower_frame.place(x=10,y=280,width=1480,height=270)
        
        search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,text='Search criminal record ',font=('times new roman',11,'bold'),fg='chartreuse4')
        search_frame.place(x=0,y=0,width=1470,height=80)#height=60
        
        
        search=Label(search_frame,font=("arial",11,"bold"),text="Search By:",bg="chartreuse1",fg="DarkCyan")
        search.grid(row=0,column=0,sticky=W,padx=2,pady=7)
        
        self.var_com_search=StringVar()
        combosearchbox=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("arial",11,"bold"),width=18,state='readonly')
        combosearchbox['value']=('Select Option','Case_id','criminalnumber')
        combosearchbox.current(0)
        combosearchbox.grid(row=0,column=1,sticky=W,padx=5)
        
        self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_search, width=18, font=("arial", 11, "bold"))
        search_txt.grid(row=0,column=2, sticky=W, padx=5)
        
        #Search button
        button_search=Button(search_frame,command=self.search_data,text='Search',font=("arial",13,"bold"),width=14,bg='dark magenta',fg='white')
        button_search.grid(row=0, column=3, padx=3, pady=5)
        
        #All button
        button_all=Button(search_frame,command=self.fetch_data,text='Show all',font=("arial",13,"bold"),width=14,bg='dark magenta',fg='white')
        button_all.grid(row=0, column=4, padx=3, pady=5)
        
        crimeagency=Label(search_frame,text='Virupakshas Crime agency:',font=('arial',25,'bold'),fg='red',bg='floral white')
        crimeagency.grid(row=0,column=5,padx=50,sticky=W,pady=0)
        
        
        #Table frame
        table_frame=Frame (lower_frame, bd=2, relief=RIDGE)
        table_frame.place (x=0, y=60,width=1470, height=170)
        
        # Scroll bar
        scroll_x=ttk. Scrollbar (table_frame, orient=HORIZONTAL)
        scroll_y=ttk. Scrollbar(table_frame, orient=VERTICAL)
        
        
        self.criminal_table=ttk. Treeview (table_frame, column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)
        
        
        self.criminal_table.heading ('1', text='CaseId')
        self.criminal_table.heading ("2", text="CrimeNumber")
        self.criminal_table.heading ("3", text="Criminal Name")
        self.criminal_table.heading ("4",text="Crime time")
        self.criminal_table.heading ("5", text="Arrest Date")
        self.criminal_table.heading ("6", text="Crime Date")
        self.criminal_table.heading ("7", text="Place of crime")
        self.criminal_table.heading ("8", text="Age of the criminal")
        self.criminal_table.heading ("9", text="Profession")
        self.criminal_table.heading ("10", text="BirthMark")
        self.criminal_table.heading ("11", text="Crime Category")
        self.criminal_table.heading("12", text="Current status")
        self.criminal_table.heading ("13", text="Gender")
        self.criminal_table.heading("14", text="Criminal Type")
        self.criminal_table.heading("15", text="Criminal nickname")
        
        
        self.criminal_table['show'] = 'headings'
        
        self.criminal_table.column ("1", width=100)
        self.criminal_table.column ("2", width=100)
        self.criminal_table.column ("3", width=100)
        self.criminal_table.column ("4", width=100)
        self.criminal_table.column ("5", width=100)
        self.criminal_table.column ("6", width=100)
        self.criminal_table.column ("7", width=100)
        self.criminal_table.column ("8", width=100)
        self.criminal_table.column ("9", width=100)
        self.criminal_table.column ("10", width=100)
        self.criminal_table.column ("11", width=100)
        self.criminal_table.column("12", width=100)
        self.criminal_table.column ("13", width=100)
        self.criminal_table.column("14", width=100)
        self.criminal_table.column("15", width=100)
        
        self.criminal_table.pack(fill=BOTH,expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

   # Add Function
    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root', password='Virupakshavegi123',database='crimemanagement')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                               self.var_case_id.get(),
                                                                                                               self.var_criminal_no.get(),
                                                                                                               self.var_name.get(),
                                                                                                               self.var_crime_time.get(),
                                                                                                               self.var_arrest_date.get(),
                                                                                                               self.var_date_of_crime.get(),
                                                                                                               self.var_address.get(),
                                                                                                               self.var_age.get(),
                                                                                                               self.var_occupation.get(),
                                                                                                               self.var_birthMark.get(),
                                                                                                               self.var_crime_type.get(),
                                                                                                               self.var_status.get(),
                                                                                                               self.var_nickname.get(),
                                                                                                               self.var_gender.get(),
                                                                                                               self.var_wanted.get()

                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has been added')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost', username='root', password='Virupakshavegi123',database='crimemanagement')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    
    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_crime_time.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthMark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_status.set(data[11])
        self.var_nickname.set(data[12])
        self.var_gender.set(data[13])
        self.var_wanted.set(data[14])

    #Update
    def update_date(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                update=messagebox.askyesno('update','Are you sure to update this criminal record')
                if update>0:
                    conn=mysql.connector.connect(host='localhost', username='root', password='Virupakshavegi123',database='crimemanagement')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update criminal set criminalnumber=%s,criminaloriginalname=%s,crimetime=%s,dateofarrest=%s,crimedate=%s,crime_address=%s,age=%s,profession=%s,birthmark=%s,crimetype=%s,status=%s,gender=%s,wanted=%s,criminal_nickname=%s where Case_id=%s',(
                                                                                                                                                                                                                                                                                   #self.var_case_id.get(),
                                                                                                                                                                                                                                                                                   self.var_criminal_no.get(),
                                                                                                                                                                                                                                                                                   self.var_name.get(),
                                                                                                                                                                                                                                                                                   self.var_crime_time.get(),
                                                                                                                                                                                                                                                                                   self.var_arrest_date.get(),
                                                                                                                                                                                                                                                                                   self.var_date_of_crime.get(),
                                                                                                                                                                                                                                                                                   self.var_address.get(),
                                                                                                                                                                                                                                                                                   self.var_age.get(),
                                                                                                                                                                                                                                                                                   self.var_occupation.get(),
                                                                                                                                                                                                                                                                                   self.var_birthMark.get(),
                                                                                                                                                                                                                                                                                   self.var_crime_type.get(),
                                                                                                                                                                                                                                                                                   self.var_status.get(),
                                                                                                                                                                                                                                                                                   self.var_nickname.get(),
                                                                                                                                                                                                                                                                                   self.var_gender.get(),
                                                                                                                                                                                                                                                                                   self.var_wanted.get(),
                                                                                                                                                                                                                                                                                   self.var_case_id.get(),
                    
                                                                                                                                                                                                                                                                                ))
                    
                else:
                    if not update:
                        return
                conn.commit()
                self.clear_data()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Succes','Criminal record updated successfully')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')


    #delete
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure to Delete this criminal record')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost', username='root', password='Virupakshavegi123',database='crimemanagement')
                    my_cursor=conn.cursor()
                    sql='delete from criminal where Case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Succes','Criminal record deleted successfully')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    #clear
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_crime_time.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthMark.set("")
        self.var_crime_type.set("")
        self.var_status.set("")
        self.var_nickname.set("")
        self.var_gender.set("")
        self.var_wanted.set("")


    #search
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root', password='Virupakshavegi123',database='crimemanagement')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminal where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'")) 
                rows=my_cursor.fetchall()
                if len(rows)!=0:

                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')



                




    




if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()