import tkinter as ttk
from tkinter import font
app = ttk.Tk()
app.title('attendence system ')
app.geometry('400x400')
font_ = font.Font(size=20)

ttk.Label(app, 
          text='Fcae Recognition based Attendence System',
          font=font_
).pack()

def register():
    app.destroy()
    import login_admin
    with open('opr','w') as f:
        f.write('Register')

def attendence():
    print('Attendence')
def clear_data():
     app.destroy()
     with open('opr','w') as f:
        f.write('clear')
     import login_admin

ttk.Button(
    app, text='Register', command=register, font=font_,
    height = 2,width = 15,bg = 'green'
    ).pack(expand=True)
ttk.Button(
    app, text='Attendence', command=attendence, font=font_,
    height = 2,width=15,bg='#0033ff'
    ).pack(expand=True)
ttk.Button(
    app, text='clear_data', command=clear_data, font=font_,
    height = 2,width=15,bg = 'violet'
    ).pack(expand=True)
app.mainloop()