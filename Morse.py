#Import all necessary libraries
from Tkinter import *
import Tkinter
import tkMessageBox
import serial;
import time;
import tkMessageBox
import tkFont
from PIL import ImageTk,Image


Morse=[[0,0,0,0,5],[0,0,0,3,1],[0,1,3,3,3],[0,1,3,1,3],[0,0,1,3,3],\
	[0,0,0,0,3],[0,3,3,1,3],[0,0,1,1,3],[0,3,3,3,3],[0,0,0,3,3],\
	[0,3,1,1,1],[0,0,1,3,1],[0,3,1,3,3],[0,0,0,1,1],[0,0,0,1,3],\
	[0,0,1,1,1],[0,3,1,1,3],[0,1,1,3,1],[0,0,3,1,3],[0,0,3,3,3],\
	[0,0,0,0,1],[0,0,3,3,1],[0,3,3,3,1],[0,0,3,1,1],[0,1,3,3,1],\
	[0,1,3,1,1],[0,1,1,3,3],[1,1,1,1,1],[3,1,1,1,1],[3,3,1,1,1],\
	[3,3,3,1,1],[3,3,3,3,1],[3,3,3,3,3],[1,3,3,3,3],[1,1,3,3,3],\
	[1,1,1,3,3],[1,1,1,1,3]]

Alpha=[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n',\
	'o','p','q','r','s','t','u','v','w','x','y','z','0','1','2',\
	'3','4','5','6','7','8','9']


def process():
    string=Entry.get(E1)
    com=Entry.get(E2)

    print "The set of characters you want to code is:", string, "."

    output=[]
    for n in range(0,len(string)):
        i=0
        while i!=99:
            if Alpha[i]==string[n]:
                output.append(Morse[i]);
                i=99;
            else:
                i=i+1;

    print output
    ArduinoSerial=serial.Serial(com,9600);
    time.sleep(2)
    print ArduinoSerial.readline
    for k in range(0,len(output)):
        for m in range(0,len(output[k])):
            data=output[k][m];
            if data==1:
                ArduinoSerial.write('1');
                #time.sleep(3);
            elif data==3:
                ArduinoSerial.write('3');
                #time.sleep(1);
            elif data==5:
                ArduinoSerial.write('5');
                #time.sleep(7);
            elif data==0:
                ArduinoSerial.write('0');
            print data;
    print ArduinoSerial.readline;




top = Tk()
top.title("String to Morse")
F1=Frame(top)
F1=Frame(top,width=400,height=450)
F1.place(height=7000, width=4000, x=100, y=100)
F1.config()

F1.grid(columnspan=10,rowspan=10)
F1.grid_rowconfigure(0,weight=1)
F1.grid_columnconfigure(0,weight=1)

photo=PhotoImage(file="marinha.gif")
label = Label(top,image = photo)
label.image = photo # Needs to be in the same dir
label.grid(row=0,column=0,columnspan=20,rowspan=20)

L1 = Label(top, text="Stream").grid(row=1,column=0)
L2 = Label(top, text="COM").grid(row=2,column=0)
E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
B=Button(top, text ="Morse Me !", command=proces).grid(row=3,column=1)

top.mainloop() #forces the window to be kept open until the user closes it.
