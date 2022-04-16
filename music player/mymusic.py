import os
import time
from tkinter import messagebox
from tkinter import*
from tkinter import filedialog
from tkinter import ttk
from mutagen.mp3 import MP3
from pygame import mixer

root=Tk()
root.resizable(0,0)
root.geometry("700x700+400+0")
root.title("DARK KNIGHT")
path=os.path.dirname(os.path.realpath("mymusic"))
global n
n=0
cn1=Canvas(root,bg="gray5",width=1366,height=768)
cn1.place(x=0,y=0)

playlist=[]
mixer.init()


img1=PhotoImage(file=("{}/z2.png".format(path)))
img2=PhotoImage(file=("{}/z4.png".format(path)))
img3=PhotoImage(file=("{}/z5.png".format(path)))

img4=PhotoImage(file=("{}/jokkk.png".format(path)))
cn1.create_image(120,380,image=img4,anchor=CENTER)

imgg2=img2.subsample(2,6)

cn1.create_image(350,610,image=img1,anchor=CENTER)
cn1.create_image(95,610,image=img3,anchor=CENTER)
cn1.create_image(595,610,image=img3,anchor=CENTER)
cn1.create_image(350,20,image=imgg2,anchor=CENTER)
cn1.create_text(350,70,text="WELCOME TO  DARK KNIGHT ",angle=0,anchor=CENTER,font=("Algerian",20),fill="chartreuse2")
cn1.create_line(699,0,699,700,fill="white",width=1)
cn1.create_line(250,90,450,90,fill="green",width=1)
def opene():
    pass
def change():
    pass
def fav():
    pass
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0,activebackground="gray20",activeforeground="green2",bg="black",fg="yellow",font="Corbel")

filemenu.add_command(label="Open",command=opene)
filemenu.add_separator()
filemenu.add_command(label="Edit",command=change)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
menubar.add_cascade(label="File",menu=filemenu)

fav=Menu(menubar,tearoff=0,activebackground="gray20",activeforeground="green2",bg="black",fg="yellow",font="Corbel")
fav.add_command(label="Favourite Songs",command=fav)
menubar.add_cascade(label="Favourite",menu=fav)
root.config(menu=menubar)
pnimg=PhotoImage(file=("{}/pause1.png".format(path)))
pnimg1=pnimg.subsample(18,18)
i=0
v=0
def playm():
    global paused
    global v
    if paused==True:
        v=1
        mixer.music.unpause()
        pause_bu=Button(cn1,image=pnimg1,command=pause,bg="black")
        pause_bu.place(x=305,y=110)
        fr1=Frame(cn1,bg="gray5",width=10,height=62)
        fr1.place(x=304,y=110)
        fr2=Frame(cn1,bg="gray5",width=10,height=62)
        fr2.place(x=360,y=110)
        fr3=Frame(cn1,bg="gray5",width=50,height=10)
        fr3.place(x=310,y=110)
        fr4=Frame(cn1,bg="gray5",width=70,height=10)
        fr4.place(x=305,y=165)
        
    else:
        try:
           global pause_but
           i=1
           stop()
           time.sleep(1)
           song=listbox.curselection()
           s_song=int(song[0])
           play_it=playlist[s_song]
           mixer.music.load(play_it)
           mixer.music.play()
           pause_but=Button(cn1,image=pnimg1,command=pause,bg="black")
           pause_but.place(x=305,y=110)
           fr1=Frame(cn1,bg="gray5",width=10,height=62)
           fr1.place(x=304,y=110)
           fr2=Frame(cn1,bg="gray5",width=10,height=62)
           fr2.place(x=360,y=110)
           fr3=Frame(cn1,bg="gray5",width=50,height=10)
           fr3.place(x=310,y=110)
           fr4=Frame(cn1,bg="gray5",width=70,height=10)
           fr4.place(x=305,y=165)
        except:
              if i==0:
                 messagebox.showwarning("File Error","Please Add a File")
################################################################################    another song play error


playPhoto= PhotoImage(file='{}/playzz1.png'.format(path))
play1=playPhoto.subsample(4,4)
playBtn =Button(cn1, image=play1,command=playm,bg="black")
playBtn.place(x=305,y=110)
fr1=Frame(cn1,bg="gray5",width=10,height=62)
fr1.place(x=304,y=110)
fr2=Frame(cn1,bg="gray5",width=10,height=62)
fr2.place(x=360,y=110)
fr3=Frame(cn1,bg="gray5",width=50,height=10)
fr3.place(x=310,y=110)
fr4=Frame(cn1,bg="gray5",width=70,height=10)
fr4.place(x=305,y=165)
paused=False

volimg11=PhotoImage(file="{}/mutegg.png".format(path))
volimg111=volimg11.subsample(20,20)
def mute():
    mixer.music.set_volume(0)
    try:
        scale.set(0)
    except:
        print()
vol_but=Button(cn1,image=volimg111,bg="black",command=mute)
vol_but.place(x=590,y=150)
fe=Frame(cn1,bg="gray5",width=10,height=50)
fe.place(x=590,y=150)
fe1=Frame(cn1,bg="gray5",width=8,height=45)
fe1.place(x=638,y=150)
fe2=Frame(cn1,bg="gray5",width=50,height=10)
fe2.place(x=600,y=150)
fe2=Frame(cn1,bg="gray5",width=50,height=10)
fe2.place(x=600,y=190)
def setvol():
    global scale
    def set_vol(var):
        volume=float(var)/100
        mixer.music.set_volume(volume)
        
    var=DoubleVar()
    scale=Scale(cn1,variable=var,orient=HORIZONTAL,activebackground="black",command=set_vol)
    scale.place(x=590,y=90)
    scale.config(bg="black",fg="red",font=("Algerian",20))
    scale.set(70)
    mixer.music.set_volume(0.7)
    def des():
        scale.destroy()
        vol_but=Button(cn1,image=volimg22,bg="black",command=setvol)
        vol_but.place(x=648,y=153)

        frr1=Frame(cn1,bg="gray5",width=8,height=38)
        frr1.place(x=647,y=160)
        frr2=Frame(cn1,bg="gray5",width=51,height=12)
        frr2.place(x=647,y=149)
        frr2=Frame(cn1,bg="gray5",width=54,height=8)
        frr2.place(x=645,y=190)
        frr2=Frame(cn1,bg="gray5",width=8,height=38)
        frr2.place(x=690,y=160)
    vol_but=Button(cn1,image=volimg22,bg="black",command=des)
    vol_but.place(x=648,y=153)

    frr1=Frame(cn1,bg="gray5",width=8,height=38)
    frr1.place(x=647,y=160)
    frr2=Frame(cn1,bg="gray5",width=51,height=12)
    frr2.place(x=647,y=149)
    frr2=Frame(cn1,bg="gray5",width=54,height=8)
    frr2.place(x=645,y=190)
    frr2=Frame(cn1,bg="gray5",width=8,height=38)
    frr2.place(x=690,y=160)

volimg=PhotoImage(file="{}/volbutimg.png".format(path))
volimg1=volimg.subsample(11,11)
volimg22=volimg.subsample(13,13)
vol_but=Button(cn1,image=volimg1,bg="black",command=setvol)
vol_but.place(x=645,y=150)

frr1=Frame(cn1,bg="gray5",width=10,height=62)
frr1.place(x=645,y=150)
frr2=Frame(cn1,bg="gray5",width=51,height=20)
frr2.place(x=647,y=147)
frr2=Frame(cn1,bg="gray5",width=54,height=10)
frr2.place(x=645,y=190)
frr2=Frame(cn1,bg="gray5",width=8,height=62)
frr2.place(x=690,y=150)
def pause():
    global paused
    mixer.music.pause()    
    pause_but.destroy()
    paused=True
    if v==1:
       playBtn =Button(cn1,image=play1,command=playm,bg="black")
       playBtn.place(x=305,y=110)
       fr1=Frame(cn1,bg="gray5",width=10,height=62)
       fr1.place(x=304,y=110)
       fr2=Frame(cn1,bg="gray5",width=10,height=62)
       fr2.place(x=360,y=110)
       fr3=Frame(cn1,bg="gray5",width=50,height=10)
       fr3.place(x=310,y=110)
       fr4=Frame(cn1,bg="gray5",width=70,height=10)
       fr4.place(x=305,y=165) 
def unpause():
    mixer.music.unpause()
    pause=True
def stop():
    mixer.music.stop()
def go(event):
    try:
       pause_but.destroy()
       pause_bu.destroy()
####################################################################################################error
    except:
        print("0")
    stop()
    song=listbox.curselection()
    s_song=int(song[0])
    print(song)
    print(s_song)
    
listbox = Listbox(cn1,width=65,bg="black",fg="white",highlightcolor="gray5",selectbackground="gray23",cursor="hand2",font=("Corbel",19))
listbox.place(x=300,y=200)
listbox.bind("<Double-1>",go)
def browse():
    global file_path
    file_path=filedialog.askopenfilename()
    addd(file_path)
    try:
       mixer.music.queue(file_path)
    except:
        print()
def addd(file):
    global n
    file_name=os.path.basename(file)
    listbox.insert(n,file_name)
    playlist.insert(n,file_path)
    n=n+1
    
        
igm=PhotoImage(file="{}/add.png".format(path))
igmm=igm.subsample(4,4)
but_add=Button(cn1,image=igmm,command=browse,bg="black")
but_add.place(x=255,y=310)
 
def dele():
    try:
       song=listbox.curselection()
       s_song=int(song[0]) 
       listbox.delete(s_song)
    except:
        messagebox.showwarning("FILE ERROR!","Please Select a file")
    
igm1=PhotoImage(file="{}/del1.png".format(path))
igmm1=igm1.subsample(9,9)
but_del=Button(cn1,image=igmm1,command=dele,bg="gray5")
but_del.place(x=255,y=372)
def close():
    stop()
    messagebox.showinfo("COME SOON!","""HOPE YOU ENJOYED!!.
Made By::- Code__Z:""")
    root.destroy()
    
root.protocol("WM_DELETE_WINDOW",close)

root.mainloop()
