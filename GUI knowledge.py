from tkinter import *
from tkinter import ttk #theme of ttk
from tkinter import messagebox

GUI = Tk()#นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล')#นี่คือชื่อโปรแกรม
GUI.geometry('500x400')#นี่คือขนาดโปรแกรม

L1 = Label (GUI, text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=100,y=100)
####################
def button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=300)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=button2)
B2.pack(ipadx=20,ipady=20)
####################
def button3():
    text = 'Python101, Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.พ.',text)

FB2 =Frame(GUI) #คล้ายกระดาน
FB2.place(x=150,y=150)
B3 = ttk.Button(GUI,text='สัปดาห์เรียนวิชาอะไร',command=button3)
B3.pack(ipadx=20,ipady=20)
 



GUI.mainloop()
