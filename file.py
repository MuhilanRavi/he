import tkinter
from tkinter import *
from tkinter import messagebox
w1=tkinter.Tk()
w1.geometry("400x400")
w1.title("imagecon")

def next2():
    f3=Frame(f1,width=400,height=400,bg="red").place(x=0,y=0)
def next1():
    messagebox.showinfo("saved","login successfully")
    f2=Frame(f1,width=400,height=400,bg="red").place(x=0,y=0)
def login():
        global f1
        b3=Button
        f1=Frame(w1,width=400,height=400,bg="white").place(x=0,y=0)
        l2=Label(w1,text="login form",font=("italic",20,"bold italic"),bg="white",fg="black").place(x=120,y=50)
        l3=Label(f1,text="username:",font=("times news roman",10,"bold italic"),bg="white",fg="black").place(x=120,y=115)
        l4=Label(f1,text="password:",font=("times news roman",10,"bold italic"),bg="white",fg="black").place(x=120,y=200)
        b2=Button(f1,text="next1",font=("italic",15,"bold"),bg="white",command="next1").place(x=150,y=280)
        
        e1=Entry(f1).place(x=125,y=155)
        e2=Entry(f1,show="*").place(x=125,y=240)
        b1=Button(f1,text="login",font=("italic",15,"bold"),bg="white",command=login).place(x=150,y=280)
        l5=Label(f1,text="do not have acc",font=("italic",15,"bold"),bg="white",command="next1").place(x=150,y=280)
        b3=Button(f1,text="sign in",font=("italic",15,"bold"),bg="white",command="next1").place(x=150,y=280)
        
w1.configure(background="white")
l1=Label(w1,text="it software",font=("italic",30,"bold italic"),fg="black").place(x=100,y=100)
b1=Button(w1,text="get started",font=("italic",15,"bold"),bg="white",command=login).place(x=150,y=280)



