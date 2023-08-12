import tkinter as ttk
from tkinter import font
login_app = ttk.Tk()
login_app.title('Register Yourself')
login_app.geometry('600x400')
font_ = font.Font(size=20)

ttk.Label(login_app, 
          text='Enter your credentials',
          font=font_
).place(x=200,y=10)
uname = ttk.Variable(login_app)
pwd = ttk.Variable(login_app)
ttk.Label(login_app,text='username', font = font_).place(x=100,y=80)
ttk.Entry(login_app,font=font_,textvariable=uname).place(x=250,y=80)
ttk.Label(login_app,text='password', font = font_).place(x=100,y=130)
ttk.Entry(login_app,font=font_,show='#',textvariable=pwd).place(x=250,y=130)

def submit():
    op = ''
    with open('opr','r') as f:
        op = f.read()
    if len(op) > 0:
        userid = uname.get()
        password = pwd.get()
        p =open('ped').read()
        if userid == 'admin' and password == p:
            print('login successfully')
        else:
            print('login failed')   
ttk.Button(login_app,text='submit',font=font_,width=8,height=1).place(x=310,y=200)

def back():
    login_app.destroy()
    with open('opr','w') as f:
        f.write('')
    import app    

ttk.Button(
    login_app,text='<-Back', font =font_,
      width=6,height=1, command=back).place(x=20,y=340)

login_app.mainloop()