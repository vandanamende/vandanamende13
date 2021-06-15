from tkinter import*
from tkinter import ttk
window = Tk()
#Declaring window Title
window.title("Registration Screen")
#Declaring window size
window.geometry("300x300")
#declaring window color
window.configure(background = "green");
#below four fields are declared

Firstname = Label(window ,text = 'First Name').grid(row=0,column=0)
Lastname = Label(window ,text = 'Last Name').grid(row=1,column=0)
Email = Label(window ,text = 'Email Id').grid(row=2,column=0)
Mobile = Label(window ,text = 'Contact number').grid(row=3,column=0)

Firstname1 = Entry(window).grid(row=0,column=1)
Lastname1= Entry(window).grid(row=1,column=1)
Email1 = Entry(window).grid(row=2,column=1)
Mobile1 = Entry(window).grid(row=3,column=1)

#fubction declaration
btn=ttk.Button(window,text="submit").grid(row=4,column=0)
window.mainloop()





