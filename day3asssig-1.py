from tkinter import*
from tkinter import ttk
window = Tk()
#Declaring window Title
window.title("Registration Screen")
#Declaring window size
window.geometry("200x200")
#declaring window color
window.configure(background = "sky blue");
#below four fields are declare

               
EmpId= Label(window ,text = 'Emp Id').grid(row=0,column=0)
Empname= Label(window ,text = 'SName').grid(row=1,column=0)
Department= Label(window ,text = 'Depart').grid(row=2,column=0)
location= Label(window ,text = 'location').grid(row=3,column=0)
pincode = Label(window ,text = 'pincode').grid(row=4,column=0)
city = Label(window ,text = 'city').grid(row=5,column=0)
salary = Label(window ,text = 'salary').grid(row=6,column=0)
Mobile = Label(window ,text = 'Contact number').grid(row=7,column=0)
Radio = Label(window ,text = 'Radio').grid(row=8,column=0)


EmpId1 = Entry(window).grid(row=0,column=1)
Sname1= Entry(window).grid(row=1,column=1)
Depart1 = Entry(window).grid(row=2,column=1)
location1 = Entry(window).grid(row=3,column=1)
city1 = Entry(window).grid(row=4,column=1)
Salary1 = Entry(window).grid(row=5,column=1)
Mobile1 = Entry(window).grid(row=6,column=1)
Radio1 = Entry(window).grid(row=7,column=1)

#fubction declaration
btn=ttk.Button(window,text="login").grid(row=8,column=0)
btn=ttk.Button(window,text="cancel").grid(row=8,column=1)

window.mainloop()





