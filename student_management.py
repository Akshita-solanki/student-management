
#importing libraries
from tkinter import *  
import sqlite3

#start is for the first window
start = Tk()
start.config(background="#373838")
start.geometry("500x500")

#fuction is for attendance - shows list of students and updates attendance if their name is checked using check button
def attendance():
    #att is window for attendance
    att=Tk()
    att.title("Attendance")
    att.geometry("350x450")  
    att.config(background="#373838")
    ckbtn_var=IntVar()
    ckbtn_var=0
    #connecting and using "attendance_e.db" for updating and checking attendance
    con=sqlite3.connect("attendance_e.db")
    #table name for attendance is atn
    tablee="""create table atn(name text,number_of_days integer)"""
    #con.execute(tablee)

    #namee() function increases the no of days by one where the name is "check-ed" in the list 
    def namee(n):
        updatee ="""update atn
                    set number_of_days= number_of_days+1
                    
                    where name='{}' """.format(n)
                    
        con.execute(updatee)
        con.commit()  
    
    #show() is used to show the updated table in another window-display
    def show():
        my_con = con.cursor()
        my_con.execute("SELECT * FROM atn")
        i=0
        #display window to show the updated table
        display=Tk()
        display.config(background="#373838")
        display.title("data")
        display.geometry("500x500")
        for student in my_con: 
            for j in range(len(student)):
                #print(student[j],end=" ")
                e = Entry(display, width=10,fg="#373838", bg="#34ebc6") 
                e.grid(row=i, column=j) 
                e.insert(END, student[j])
            i=i+1
    #defining the widgets for the att window and placing them in position
    chkbtn1 = Checkbutton(att, fg="#373838", bg="#34ebc6",text = "Akansha", height = 2, width = 10,command=lambda:namee("Akansha")).place(x = 50,y = 50)
    chkbtn2 = Checkbutton(att, fg="#373838", bg="#34ebc6",text = "Akash", height = 2, width = 10,command=lambda:namee("Akash")).place(x = 50,y = 80)
    chkbtn3 = Checkbutton(att, fg="#373838", bg="#34ebc6",text = "Becky", height = 2, width = 10,command=lambda:namee("Becky")).place(x = 50,y = 110)
    chkbtn4 = Checkbutton(att, fg="#373838", bg="#34ebc6",text = "jessica", height = 2, width = 10,command=lambda:namee("jessica")).place(x = 50,y = 140)
    chkbtn5 = Checkbutton(att, fg="#373838", bg="#34ebc6",text = "lexi", height = 2, width = 10,command=lambda:namee("lexi")).place(x = 50,y = 170)
    chkbtn6 = Checkbutton(att, fg="#373838", bg="#34ebc6",text = "Ben", height = 2, width = 10,command=lambda:namee("Ben")).place(x = 50,y = 200)
    chkbtn7 = Checkbutton(att, fg="#373838", bg="#34ebc6",text = "James", height = 2, width = 10,command=lambda:namee("James")).place(x = 50,y = 240)
    chkbtn8 = Checkbutton(att, fg="#373838", bg="#34ebc6",text = "Sophia", height = 2, width = 10,command=lambda:namee("Sophia")).place(x = 50,y = 270)
    chkbtn9 = Checkbutton(att, fg="#373838", bg="#34ebc6",text = "Michael", height = 2, width = 10,command=lambda:namee("Michael")).place(x = 50,y = 300)
    chkbtn10 = Checkbutton(att,fg="#373838", bg="#34ebc6", text = "Daniel", height = 2, width = 10,command=lambda:namee("Daniel")).place(x = 50,y = 330)

    button1=Button(att,text="updated list",command=show,fg="#373838", bg="#34ebc6").place(x = 100,y = 380)

    att.mainloop()
#attendance()ends here 


#function for register student data- stores the data enterd in database when "submitted" and displays the table when cliked show data
def student_data():
    #top is the window for the student data
    top = Tk()
    top.config(background="#373838")
    top.geometry("500x500")
    top.title("Student Data")

    cb_var1=StringVar()  
    cb_var2=StringVar()  
    #connecting to database student_data
    conn=sqlite3.connect("student_dataa.db")
    c=conn.cursor()
    #creating tabel students
    table="""create table students(name text,reg_no integer,department text,gender text)"""
    conn.execute(table)


    #delete() is used to delete the entry field when "enter another field" is cliked to take in next set of data
    def delete():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        c1.deselect()
        c2.deselect()

    #genderr returns the male or female 
    def genderr(gen):
        global ge
        ge=gen
    #submit () is used to update the values of made changes to data base
    def submitt():
        conn.execute("insert into students (name,reg_no,department,gender ) values( '{}', '{}', '{}', '{}')".format(e1.get(),e2.get(),e3.get(),ge))
        conn.commit()

    # display() is used to display the table with updated data
    def display():
        my_conn = conn.cursor()
        my_conn.execute("SELECT * FROM students")
        i=0
        #display window to show the updated table
        showw=Tk()
        showw.config(background="#373838")
        showw.title("data")
        showw.geometry("500x500")
        for student in my_conn: 
            for j in range(len(student)):
                
                e = Entry(showw, width=10,fg="#373838", bg="#34ebc6") 
                e.grid(row=i, column=j) 
                e.insert(END, student[j])
            i=i+1
                
    #defining the widgets for the top window and placing them in position
    name = Label(top, text = "Name",fg="#373838", bg="#34ebc6").place(x = 30,y = 50)  
    rn = Label(top, text = "Registration no.",fg="#373838", bg="#34ebc6").place(x = 30, y = 90)  
    dep = Label(top, text = "Department",fg="#373838", bg="#34ebc6").place(x = 30, y = 130) 
    gender=Label(top,text="Gender",fg="#373838", bg="#34ebc6").place(x=30,y=170)
    e1 = Entry(top,fg="#373838", bg="#34ebc6")
    e1.place(x = 140, y = 50) 

    e2 = Entry(top,fg="#373838", bg="#34ebc6")
    e2.place(x = 140, y = 90)  
    e3 = Entry(top,fg="#373838", bg="#34ebc6")
    e3.place(x = 140, y = 130)
    c1=Checkbutton(top,fg="#373838", bg="#34ebc6",text="Male",command=lambda:genderr("Male")).place(x = 140,y =170)

    c2=Checkbutton(top,fg="#373838", bg="#34ebc6",text="Female",command=lambda:genderr("Female")).place(x = 220,y =170)

    button=Button(top,text="Submit",command=submitt,fg="#373838", bg="#34ebc6",height=2,width=10).place(x = 30,y = 240)
    button1=Button(top,text="Show data",command=display,fg="#373838", bg="#34ebc6",height=2,width=10).place(x = 130,y = 240)
    button2=Button(top,text="fill another entry ",command=delete,fg="#373838", bg="#34ebc6",height=2,width=15).place(x = 230,y = 240)

    top.mainloop()

#defining the widgets for the start window and placing them in position
# the respective function is called based on the button clicked by the user
button_1=Button(start,text="Add student data ",fg="#373838", bg="#34ebc6",command=student_data,height=4,width=15).place(x = 100, y = 200)
button_2=Button(start,text="Attendance ",fg="#373838", bg="#34ebc6",command=attendance,height=4,width=15).place(x = 300, y = 200)

start.mainloop()