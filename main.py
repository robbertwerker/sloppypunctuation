from tkinter import *
import re

def regex():
    ver1 = re.sub("\s+", " ", e1_value.get())
    ver2 = re.sub(r'^[^a-z]', r'', ver1)
    ver3 = re.sub(r'\s*([.,?!:])\s*', r'\1 ', ver2)
    ver4 = re.sub(r'(^|[.?!])\s*([a-zA-Z])', lambda pat: pat.group(0).upper(), ver3)
    print(e1_value.get())
    t1.insert(END,ver4)

window=Tk()

b1=Button(window,text="Execute",command=regex)
b1.grid(row=0, column=1)

b2=Button(window,text="Clear"   )
b2.grid(row=0, column=3)

e1_value=StringVar()
e1=Entry(window, width=50,textvariable=e1_value)
e1.grid(row=0,column=0)

t1=Text(window,height=1,width=50)
t1.grid(row=0,column=2)

window.mainloop()
