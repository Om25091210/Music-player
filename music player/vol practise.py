from tkinter import*

root=Tk()
var=DoubleVar()
scale=Scale(root,variable=var)
scale.pack(anchor=CENTER)
def get_vol():
    display="Value = "+str(var.get())
    label.config(text=display)
button=Button(root,text="display volume",command=get_vol)
button.pack(anchor=CENTER)
label=Label(root)
label.pack()
root.mainloop()
