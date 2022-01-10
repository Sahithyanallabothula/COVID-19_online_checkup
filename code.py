from tkinter import*
window=Tk()
window.title("ONLINE CHECKUP FOR COVID-19")
def final():
    s.destroy()
def display():
    a1.destroy()
    global s
    s=Tk()
    s.title("RESULT")
    v1=v.get()
    b1=b.get()
    d1=d.get()
    e1=e.get()
    if(v1==1 and b1==1 and d1==1 and (e1==1 or 2) ):
        Label(s,text="Seek Immediate medical attentation.",font=("times",15,"bold")).pack()
        Label(s,text="You are a COVID-19 positive....",font=("times",15,"bold")).pack()
        Label(s,text="Thank you for taking test",font=("times",10,"bold")).pack()
    elif((v1==1 or 2) and (b1==1 or 2) and d1==1 and (e1==3)):
        Label(s,text="Please, be home quarantine yourself.",font=("times",15,"bold")).pack()
        Label(s,text="Still if you face any difficulties,you wiil be shifted to the government quarantine facilities...",font=("times",15,"bold")).pack()
        Label(s,text="Thank you for taking test",font=("times",10,"bold")).pack()
    elif(v1==1 and b1==2 and d1==2 and e1==3):
        Label(s,text="If you have symptom difficulty in breathing,seek medical attentation.",font=("times",15,"bold")).pack()
        Label(s,text="Other than that if have remaning symptoms,then,You have only mild symptoms.",font=("times",15,"bold")).pack()
        Label(s,text="COVID-19 affects different people in different ways.\nMost infected people will develop mid to moderate illness and recover without hospitalisation.",font=("times",15,"bold")).pack()
        Label(s,text="Thank you for taking test",font=("times",10,"bold")).pack()
    elif((v1==1 or 2) and b1==1 and d1==2 and e1==3):
        Label(s,text="Please ,be careful you have more chances of infection...",font=("times",15,"bold")).pack()
        Label(s,text="Please,be isolate yourself.",font=("times",15,"bold")).pack()
        Label(s,text="Still if you face any difficulties,take the test in isolation centres near by you.",font=("times",15,"bold")).pack()
        Label(s,text="Thank you for taking test",font=("times",10,"bold")).pack()
    elif(v1==2 and b1==2 and d1==2 and e1==3):
        Label(s,text="You have no symptoms of COVID-19...",font=("times",15,"bold")).pack()
        Label(s,text="Your infection risk is low.\nWe recommend that you stay at home to avoid any chance of exposure to the Novel Coronavirus.",font=("times",15,"bold")).pack()
        Label(s,text="Retake self-Assessment Test if you develop symptoms or come in contact with a\nCOVID-19 confirmed patient.",font=("times",15,"bold")).pack()
        Label(s,text="Thank you for taking test",font=("times",10,"bold")).pack()
    elif((v1==1 or 2) and (b1== 1 or 2) and d1==2 and (e1==1 or 2)):
        Label(s,text="We recommend that you ,go to isolation centre near by you and take test.",font=("times",15,"bold")).pack()
        Label(s,text="According to the result of test,please go ahead...",font=("times",15,"bold")).pack()
        Label(s,text="Thank you for taking test",font=("times",10,"bold")).pack()
    else:
        Label(s,text="Please enter all choices provided to you...",font=("times",15,"bold")).pack()
    Button(s,text="Exit",width=10,font=("times",15,"bold"),command=final).pack()
def symptoms():
    Register_window.destroy()
    global a1
    a=c.get()
    if(a==1):
        a1=Tk()
        a1.attributes("-fullscreen",True)
        a1.title("COVID SYMPTOMS")
        l1=Label(a1,text="Assess test",font="times 20").place(x=270,y=50)
        global v
        v=IntVar()
        Label(a1,text="Are you experiencing any of the following symptoms:\nCough,Fever,Difficulty in breathing",padx=25,font=("times",15,"bold")).place(x=150,y=120)
        Radiobutton(a1,text="Yes",padx=25,value=1,font=("times",10,"bold"),width=25,variable=v,fg="blue").place(x=200,y=180)
        Radiobutton(a1,text="No",padx=25,value=2,font=("times",10,"bold"),width=25,variable=v,fg="blue").place(x=350,y=180)
        global b
        b=IntVar()
        Label(a1,text="Have you ever had any of the following:\nDiabetes,Hyper tension,Lung disease,Heart disease",padx=25,font=("times",15,"bold")).place(x=150,y=220)
        Radiobutton(a1,text="Yes",padx=25,width=25,font=("times",10,"bold"),value=1,variable=b,fg="blue").place(x=200,y=300)
        Radiobutton(a1,text="No",padx=25,value=2,width=25,font=("times",10,"bold"),variable=b,fg="blue").place(x=350,y=300)
        global d
        d=IntVar()
        Label(a1,text="Have you travelled anywhere internationally in the last 28-45 days?",padx=25,font=("times",15,"bold")).place(x=150,y=350)
        Radiobutton(a1,text="Yes",padx=25,width=25,font=("times",10,"bold"),value=1,variable=d,fg="blue").place(x=200,y=400)
        Radiobutton(a1,text="No",padx=25,value=2,font=("times",10,"bold"),width=25,variable=d,fg="blue").place(x=350,y=400)
        global e
        e=IntVar()
        Label(a1,text="Which of the following apply to you?",padx=25,font=("times",15,"bold")).place(x=150,y=450)
        Radiobutton(a1,text="I have in contact with someone who has tested positive for COVID-19" ,width=50,font=("times",10,"bold"),padx=70,pady=15,value=1,variable=e,fg="blue").place(x=150,y=500)
        Radiobutton(a1,text="I am healthcare worker and I examined a COVID-19 confirmed case without protectivegear",padx=70,width=50,font=("times",10,"bold"),pady=15,value=2,variable=e,fg="blue").place(x=200,y=550)
        Radiobutton(a1,text="None of the above",padx=70,pady=15,width=50,font=("times",10,"bold"),value=3,variable=e,fg="blue").place(x=40,y=600)
        Button(a1,text="submit",width=10,font=("times",15,"bold"),command=display).place(x=300,y=650)
def register():
    window.destroy()
    global Register_window
    Register_window=Tk()
    Register_window.geometry("450x350")
    Register_window.title("Registration")
    l1=Label(Register_window,text="personal details",font="times 20")
    l1.grid(row=1,column=1,columnspan=2)
    l2=Label(Register_window,text="Full Name",font="times 20")
    l2.grid(row=2,column=1)
    name_text=StringVar()
    e2=Entry(Register_window,textvariable=name_text,width=25)
    e2.grid(row=2,column=2)
    l3=Label(Register_window,text="gender",font=("times", 20))
    l3.grid(row=3,column=1)
    gender_text=IntVar()
    e3=Radiobutton(Register_window,text="Male",indicatoron=0,variable=gender_text,value=1,font=("times",10))
    e3.grid(row=4,column=1,)
    e31=Radiobutton(Register_window,text="Female",indicatoron=0,variable=gender_text,value=2,font=("times",10))
    e31.grid(row=4,column=2,)
    global c
    c=IntVar()
    l4=Label(Register_window,text="Confirm Submission",font="times 20",padx=20)
    l4.grid(row=5,column=1)
    e4=Radiobutton(Register_window,text="Submit",padx=20,variable=c,indicatoron=0,value=1,command=symptoms)
    e4.grid(row=6,column=1)
    e41=Radiobutton(Register_window,text="Reset",indicatoron=0,padx=20,variable=c,value=2,command=symptoms)
    e41.grid(row=6,column=2)
l1=Label(window,text="Welcome this is an online checkup for COVID-19\nBy registering this ,\n you can protect yourself,your family and friends,and \n  help our country in the effort to fight COVID-19",font=("times",20,"bold"),justify=CENTER)
l1.grid(row=1,column=2,columnspan=2)
b1=Button(window,text="Register now",width=30,command=register,font=("times",10,"bold"))
b1.grid(row=2,column=2)
b2=Button(window,text="Exit",width=30,command=window.destroy,font=("times",10,"bold"))
b2.grid(row=2,column=3)
window.mainloop()

