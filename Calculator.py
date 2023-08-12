from tkinter import *

root = Tk()
root.geometry("470x450")
root.title("Calculator")
root.config(bg='black')

def click(number):
    entry.insert(END, number)

def clear():
    entry.delete(0, END)

def result():
    expression=entry.get()
    res=eval(expression)
    ans=round(res, 1)
    entry.delete(0, END)
    entry.insert(0, ans)

value = StringVar()

entry = Entry(root, textvariable=value, justify='center', bd=6, font=('ariel',30))
entry.grid(row=0,columnspan=4,padx=10, pady=10)


btn7 = Button(root, text="7", font=('arial', 25 ,'bold'), bd=5, height=1, width=3, command=lambda:click('7'))
btn7.grid(row=1,column=0, padx=5, pady=10)

btn8 = Button(root, text="8", font=('arial', 25, 'bold'), bd=5,height=1, width=3, command=lambda:click('8'))
btn8.grid(row=1,column=1, padx=5, pady=10)

btn9 = Button(root, text="9", font=('arial', 25 ,'bold'), bd=5,height=1, width=3, command=lambda:click('9'))
btn9.grid(row=1,column=2, padx=5, pady=10)

btn_add = Button(root, text="+", font=('arial', 25, 'bold'), bd=5,height=1, width=3, command=lambda:click('+'))
btn_add.grid(row=1,column=3, padx=5, pady=10)


btn4 = Button(root, text="4", font=('arial', 25 ,'bold'), bd=5,height=1, width=3, command=lambda:click('4'))
btn4.grid(row=2,column=0, padx=5, pady=10)

btn5 = Button(root, text="5", font=('arial', 25, 'bold'), bd=5,height=1, width=3, command=lambda:click('5'))
btn5.grid(row=2,column=1, padx=5, pady=10)

btn6 = Button(root, text="6", font=('arial', 25 ,'bold'), bd=5,height=1, width=3, command=lambda:click('6'))
btn6.grid(row=2,column=2, padx=5, pady=10)

btn_sub = Button(root, text="-", font=('arial', 25, 'bold'), bd=5,height=1, width=3, command=lambda:click('-'))
btn_sub.grid(row=2,column=3, padx=5, pady=10)


btn1 = Button(root, text="1", font=('arial', 25 ,'bold'), bd=5,height=1, width=3, command=lambda:click('1'))
btn1.grid(row=3,column=0, padx=5, pady=10)

btn2 = Button(root, text="2", font=('arial', 25, 'bold'), bd=5,height=1, width=3, command=lambda:click('2'))
btn2.grid(row=3,column=1, padx=5, pady=10)

btn3 = Button(root, text="3", font=('arial', 25 ,'bold'), bd=5,height=1, width=3, command=lambda:click('3'))
btn3.grid(row=3,column=2, padx=5, pady=10)

btn_mul = Button(root, text="*", font=('arial', 25, 'bold'), bd=5,height=1, width=3, command=lambda:click('*'))
btn_mul.grid(row=3,column=3, padx=5, pady=10)


btnC = Button(root, text="0", font=('arial', 25 ,'bold'), bd=5,height=1, width=3, command=lambda:click('0'))
btnC.grid(row=4,column=0, padx=5, pady=10)

btn0 = Button(root, text="C", font=('arial', 25, 'bold'), bd=5, bg='#3697f5', height=1, width=3,command=clear)
btn0.grid(row=4,column=1, padx=5, pady=10)

btn_equ=Button(root,text="=", font=('arial', 25 ,'bold'), bd=5, bg='#fe9037', height=1, width=3, command=result)
btn_equ.grid(row=4,column=2, padx=5, pady=10)

btn_div = Button(root, text="/", font=('arial', 25, 'bold'), bd=5, height=1, width=3, command=lambda:click('/'))
btn_div.grid(row=4,column=3, padx=5, pady=10)

root.mainloop()